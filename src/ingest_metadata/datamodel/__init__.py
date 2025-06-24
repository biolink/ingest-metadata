from pathlib import Path
from .ingest_metadata import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "ingest_metadata.yaml"
