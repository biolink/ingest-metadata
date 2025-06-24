# Auto generated from ingest_metadata.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-06-24T14:40:15
# Schema: ingest_metadata
#
# id: https://w3id.org/biolink/ingest-metadata
# description: Metadata about a data ingest process and its products.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
TRANSLATOR = CurieNamespace('translator', 'https://w3id.org/translator/')
DEFAULT_ = BIOLINK


# Types

# Class references



@dataclass(repr=False)
class IngestMetadata(YAMLRoot):
    """
    Metadata about a specific data ingest process and its outputs
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["IngestMetadata"]
    class_class_curie: ClassVar[str] = "biolink:IngestMetadata"
    class_name: ClassVar[str] = "IngestMetadata"
    class_model_uri: ClassVar[URIRef] = BIOLINK.IngestMetadata

    title: str = None
    creation_date: Union[str, XSDDate] = None
    ingest_code_url: Union[str, URIorCURIE] = None
    source_infores_id: Union[str, URIorCURIE] = None
    source_data_version: str = None
    target_title: str = None
    target_type: str = None
    target_data_version: str = None
    target_creation_date: Union[str, XSDDate] = None
    target_license: str = None
    target_data_format: str = None
    created_by: Optional[Union[str, list[str]]] = empty_list()
    ingest_guide_url: Optional[Union[str, URIorCURIE]] = None
    source_license: Optional[str] = None
    source_publication_date: Optional[Union[str, XSDDate]] = None
    source_download_date: Optional[Union[str, XSDDate]] = None
    source_access_urls: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    source_data_formats: Optional[Union[str, list[str]]] = empty_list()
    source_data_files: Optional[Union[str, list[str]]] = empty_list()
    target_data_model: Optional[str] = None
    target_data_model_version: Optional[str] = None
    node_normalizer: Optional[str] = None
    node_normalizer_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.creation_date):
            self.MissingRequiredField("creation_date")
        if not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self._is_empty(self.ingest_code_url):
            self.MissingRequiredField("ingest_code_url")
        if not isinstance(self.ingest_code_url, URIorCURIE):
            self.ingest_code_url = URIorCURIE(self.ingest_code_url)

        if self._is_empty(self.source_infores_id):
            self.MissingRequiredField("source_infores_id")
        if not isinstance(self.source_infores_id, URIorCURIE):
            self.source_infores_id = URIorCURIE(self.source_infores_id)

        if self._is_empty(self.source_data_version):
            self.MissingRequiredField("source_data_version")
        if not isinstance(self.source_data_version, str):
            self.source_data_version = str(self.source_data_version)

        if self._is_empty(self.target_title):
            self.MissingRequiredField("target_title")
        if not isinstance(self.target_title, str):
            self.target_title = str(self.target_title)

        if self._is_empty(self.target_type):
            self.MissingRequiredField("target_type")
        if not isinstance(self.target_type, str):
            self.target_type = str(self.target_type)

        if self._is_empty(self.target_data_version):
            self.MissingRequiredField("target_data_version")
        if not isinstance(self.target_data_version, str):
            self.target_data_version = str(self.target_data_version)

        if self._is_empty(self.target_creation_date):
            self.MissingRequiredField("target_creation_date")
        if not isinstance(self.target_creation_date, XSDDate):
            self.target_creation_date = XSDDate(self.target_creation_date)

        if self._is_empty(self.target_license):
            self.MissingRequiredField("target_license")
        if not isinstance(self.target_license, str):
            self.target_license = str(self.target_license)

        if self._is_empty(self.target_data_format):
            self.MissingRequiredField("target_data_format")
        if not isinstance(self.target_data_format, str):
            self.target_data_format = str(self.target_data_format)

        if not isinstance(self.created_by, list):
            self.created_by = [self.created_by] if self.created_by is not None else []
        self.created_by = [v if isinstance(v, str) else str(v) for v in self.created_by]

        if self.ingest_guide_url is not None and not isinstance(self.ingest_guide_url, URIorCURIE):
            self.ingest_guide_url = URIorCURIE(self.ingest_guide_url)

        if self.source_license is not None and not isinstance(self.source_license, str):
            self.source_license = str(self.source_license)

        if self.source_publication_date is not None and not isinstance(self.source_publication_date, XSDDate):
            self.source_publication_date = XSDDate(self.source_publication_date)

        if self.source_download_date is not None and not isinstance(self.source_download_date, XSDDate):
            self.source_download_date = XSDDate(self.source_download_date)

        if not isinstance(self.source_access_urls, list):
            self.source_access_urls = [self.source_access_urls] if self.source_access_urls is not None else []
        self.source_access_urls = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.source_access_urls]

        if not isinstance(self.source_data_formats, list):
            self.source_data_formats = [self.source_data_formats] if self.source_data_formats is not None else []
        self.source_data_formats = [v if isinstance(v, str) else str(v) for v in self.source_data_formats]

        if not isinstance(self.source_data_files, list):
            self.source_data_files = [self.source_data_files] if self.source_data_files is not None else []
        self.source_data_files = [v if isinstance(v, str) else str(v) for v in self.source_data_files]

        if self.target_data_model is not None and not isinstance(self.target_data_model, str):
            self.target_data_model = str(self.target_data_model)

        if self.target_data_model_version is not None and not isinstance(self.target_data_model_version, str):
            self.target_data_model_version = str(self.target_data_model_version)

        if self.node_normalizer is not None and not isinstance(self.node_normalizer, str):
            self.node_normalizer = str(self.node_normalizer)

        if self.node_normalizer_version is not None and not isinstance(self.node_normalizer_version, str):
            self.node_normalizer_version = str(self.node_normalizer_version)

        super().__post_init__(**kwargs)


# Enumerations
class TargetGraphType(EnumDefinitionImpl):
    """
    Level of processing or modeling applied to the target knowledge graph
    """
    SourceKG = PermissibleValue(
        text="SourceKG",
        description="A raw source KG parsed from a source without Biolink modeling")
    BiolinkKG = PermissibleValue(
        text="BiolinkKG",
        description="A KG transformed to use Biolink classes and predicates")
    NormalizedKG = PermissibleValue(
        text="NormalizedKG",
        description="A KG that has undergone Biolink modeling and node normalization")

    _defn = EnumDefinition(
        name="TargetGraphType",
        description="Level of processing or modeling applied to the target knowledge graph",
    )

# Slots
class slots:
    pass

slots.title = Slot(uri=BIOLINK.title, name="title", curie=BIOLINK.curie('title'),
                   model_uri=BIOLINK.title, domain=None, range=str)

slots.created_by = Slot(uri=BIOLINK.created_by, name="created_by", curie=BIOLINK.curie('created_by'),
                   model_uri=BIOLINK.created_by, domain=None, range=Optional[Union[str, list[str]]])

slots.creation_date = Slot(uri=BIOLINK.creation_date, name="creation_date", curie=BIOLINK.curie('creation_date'),
                   model_uri=BIOLINK.creation_date, domain=None, range=Union[str, XSDDate])

slots.ingest_code_url = Slot(uri=BIOLINK.ingest_code_url, name="ingest_code_url", curie=BIOLINK.curie('ingest_code_url'),
                   model_uri=BIOLINK.ingest_code_url, domain=None, range=Union[str, URIorCURIE])

slots.ingest_guide_url = Slot(uri=BIOLINK.ingest_guide_url, name="ingest_guide_url", curie=BIOLINK.curie('ingest_guide_url'),
                   model_uri=BIOLINK.ingest_guide_url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.source_infores_id = Slot(uri=BIOLINK.source_infores_id, name="source_infores_id", curie=BIOLINK.curie('source_infores_id'),
                   model_uri=BIOLINK.source_infores_id, domain=None, range=Union[str, URIorCURIE])

slots.source_license = Slot(uri=BIOLINK.source_license, name="source_license", curie=BIOLINK.curie('source_license'),
                   model_uri=BIOLINK.source_license, domain=None, range=Optional[str])

slots.source_data_version = Slot(uri=BIOLINK.source_data_version, name="source_data_version", curie=BIOLINK.curie('source_data_version'),
                   model_uri=BIOLINK.source_data_version, domain=None, range=str)

slots.source_publication_date = Slot(uri=BIOLINK.source_publication_date, name="source_publication_date", curie=BIOLINK.curie('source_publication_date'),
                   model_uri=BIOLINK.source_publication_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.source_download_date = Slot(uri=BIOLINK.source_download_date, name="source_download_date", curie=BIOLINK.curie('source_download_date'),
                   model_uri=BIOLINK.source_download_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.source_access_urls = Slot(uri=BIOLINK.source_access_urls, name="source_access_urls", curie=BIOLINK.curie('source_access_urls'),
                   model_uri=BIOLINK.source_access_urls, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.source_data_formats = Slot(uri=BIOLINK.source_data_formats, name="source_data_formats", curie=BIOLINK.curie('source_data_formats'),
                   model_uri=BIOLINK.source_data_formats, domain=None, range=Optional[Union[str, list[str]]])

slots.source_data_files = Slot(uri=BIOLINK.source_data_files, name="source_data_files", curie=BIOLINK.curie('source_data_files'),
                   model_uri=BIOLINK.source_data_files, domain=None, range=Optional[Union[str, list[str]]])

slots.target_title = Slot(uri=BIOLINK.target_title, name="target_title", curie=BIOLINK.curie('target_title'),
                   model_uri=BIOLINK.target_title, domain=None, range=str)

slots.target_type = Slot(uri=BIOLINK.target_type, name="target_type", curie=BIOLINK.curie('target_type'),
                   model_uri=BIOLINK.target_type, domain=None, range=str,
                   pattern=re.compile(r'^(Source-KG|Biolink KG|Normalized KG)$'))

slots.target_data_version = Slot(uri=BIOLINK.target_data_version, name="target_data_version", curie=BIOLINK.curie('target_data_version'),
                   model_uri=BIOLINK.target_data_version, domain=None, range=str)

slots.target_creation_date = Slot(uri=BIOLINK.target_creation_date, name="target_creation_date", curie=BIOLINK.curie('target_creation_date'),
                   model_uri=BIOLINK.target_creation_date, domain=None, range=Union[str, XSDDate])

slots.target_license = Slot(uri=BIOLINK.target_license, name="target_license", curie=BIOLINK.curie('target_license'),
                   model_uri=BIOLINK.target_license, domain=None, range=str)

slots.target_data_format = Slot(uri=BIOLINK.target_data_format, name="target_data_format", curie=BIOLINK.curie('target_data_format'),
                   model_uri=BIOLINK.target_data_format, domain=None, range=str)

slots.target_data_model = Slot(uri=BIOLINK.target_data_model, name="target_data_model", curie=BIOLINK.curie('target_data_model'),
                   model_uri=BIOLINK.target_data_model, domain=None, range=Optional[str])

slots.target_data_model_version = Slot(uri=BIOLINK.target_data_model_version, name="target_data_model_version", curie=BIOLINK.curie('target_data_model_version'),
                   model_uri=BIOLINK.target_data_model_version, domain=None, range=Optional[str])

slots.node_normalizer = Slot(uri=BIOLINK.node_normalizer, name="node_normalizer", curie=BIOLINK.curie('node_normalizer'),
                   model_uri=BIOLINK.node_normalizer, domain=None, range=Optional[str])

slots.node_normalizer_version = Slot(uri=BIOLINK.node_normalizer_version, name="node_normalizer_version", curie=BIOLINK.curie('node_normalizer_version'),
                   model_uri=BIOLINK.node_normalizer_version, domain=None, range=Optional[str])