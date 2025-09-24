#!/usr/bin/env python3
"""
Script to create a new Ingest Metadata Specification (metadata) from the template.
"""

from os import makedirs, path, sep
import sys
from pathlib import Path
import yaml
from datetime import datetime
import click

METADATA_FILE_DIRECTORY = Path(__file__).parent.parent / "docs" / "metadata"

def load_template(template_path):
    """Load the metadata template from the YAML file."""
    with open(template_path, 'r') as f:
        return yaml.safe_load(f)


def create_metadata(infores_id, output_file, output_path, template_path):
    """
    Create a new Ingest Metadata Specification from the template, with user-specified values.

    :param infores_id: Associated with the primary knowledge source
    :param output_file: file name of the metadata file
    :param output_path: full path to the metadata file
    :param template_path: full path to the template file
    :return: None
    """
    # Load template
    template = load_template(template_path)
    
    # Update template with user values
    template['file_name'] = output_file
    template['source_infores_id'] = infores_id
    template['file_creation_date'] = datetime.now().strftime('%Y-%m-%d')

    # Write the new metadata file
    with open(output_path, 'w') as f:
        yaml.dump(template, f, default_flow_style=False, sort_keys=False, indent=2)
    
    click.echo(f"Created new Ingest Metadata file: {output_file}")
    click.echo(f"  InfoRes ID: {infores_id}")
    click.echo(f"\nNext steps:")
    click.echo(f"1. Edit {output_path} to fill in the template sections")
    click.echo(f"2. See src{sep}docs{sep}files{sep}example-metadata.md for detailed guidance")


@click.command()
@click.option(
    '--infores', 
    required=True,
    help='InfoRes identifier for the data source (e.g., infores:ctd)'
)
@click.option(
    '--output',
    help='Output filename for the new metadata (default: based on infores ID)'
)
@click.option(
    '--template',
    default=f"src{sep}docs{sep}files{sep}ingest_metadata_template.yaml",
    help=f"Path to the metadata template file (default: src{sep}docs{sep}files{sep}metadata_template.yaml)"
)
def main(infores, output, template):
    """Create a new Ingest Metadata file from the template.
    
    Examples:
    
    \b
    create_metadata.py --infores "infores:ctd"
    create_metadata.py --infores "infores:pharmgkb" --output "my_own_pharmgkb_metadata.yaml"
    """
    
    # Validate infores format
    if not infores.startswith('infores:'):
        click.echo("Error: InfoRes ID must start with 'infores:'", err=True)
        sys.exit(1)

    # Generate output filename if not provided
    if not output:
        # Extract a source file name from infores ID and create the output filename
        source_name = infores.replace('infores:', '').replace(':', '_')
        output = f"{source_name}_metadata.yaml"

    # Sanity check: ensure the Ingest Metadata file directory exists
    makedirs(path.dirname(METADATA_FILE_DIRECTORY), exist_ok=True)
    output_path = f"{METADATA_FILE_DIRECTORY}{sep}{output}"
    
    # Check if template exists
    if not path.exists(template):
        click.echo(f"Error: Template file not found: {template}", err=True)
        sys.exit(1)
    
    # Check if an output file already exists
    if path.exists(output_path):
        if not click.confirm(f"File {output_path} already exists. Overwrite?"):
            click.echo("Aborted.")
            sys.exit(0)
    
    try:
        create_metadata(infores, output, output_path, template)
    except Exception as e:
        click.echo(f"Error creating Ingest Metadata Specification: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()