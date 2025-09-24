## This is imported by the main justfile.

INFORES:= ""

# Create a new Ingest Metadata Specification YAML from template
# Usage: just INFORES=infores:ctd new-metadata
new-metadata:
    @if [[ -z "{{INFORES}}" ]]; then \
        echo "INFORES is required. Usage: just INFORES=infores:example new-metadata"; \
    else \
       {{run}} python {{src}}/scripts/create_metadata.py --infores "{{INFORES}}"; \
    fi

# Validate all Ingest Metadata Specification files against the schema
validate-metadata:
    @echo "Validating Ingest Metadata Specification files against schema..."
    @for ingest_spec in {{src}}/docs/metadata/*.yaml; do \
        if [ -f "$ingest_spec" ]; then \
            echo "Validating $ingest_spec"; \
            {{run}} linkml-validate --schema {{source_schema_path}} "$ingest_spec"; \
        fi; \
    done
    @echo "✓ All Ingest Metadata Specification files validated (with any errors as indicated)"
