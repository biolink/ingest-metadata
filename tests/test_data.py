"""Data test."""
import os

from linkml_runtime.loaders import yaml_loader
from src.ingest_metadata.datamodel.ingest_metadata import IngestMetadata

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
test_data_path = os.path.join(os.path.dirname(__file__), 'test_ingest_metadata.yaml')

def test_data():
    """Date test."""
    obj = yaml_loader.load(test_data_path, target_class=IngestMetadata)
    assert obj
    assert isinstance(obj, IngestMetadata)
    assert obj.title == "Test Ingest Metadata"
    assert obj.source_data_version == "1.0.0"
    assert obj.target_title == "Test Output Dataset"