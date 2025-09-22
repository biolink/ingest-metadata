# Auto generated from ingest_metadata.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-09-22T11:00:29
# Schema: kgx_ingest_metadata_schema
#
# id: https://w3id.org/biolink/kgx/ingest-metadata-schema
# description: A schema for describing metadata about a specific execution of a source ingest to produce a specific KGX-format graph.
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

from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = "0.1.0"

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = BIOLINK


# Types

# Class references



@dataclass(repr=False)
class IngestMetadataFile(YAMLRoot):
    """
    Information about a particular ingest performed to produce a KGX graph, describing source data, ingest process,
    and details of the resulting KGX graph.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["IngestMetadataFile"]
    class_class_curie: ClassVar[str] = "biolink:IngestMetadataFile"
    class_name: ClassVar[str] = "IngestMetadataFile"
    class_model_uri: ClassVar[URIRef] = BIOLINK.IngestMetadataFile

    file_name: str = None
    file_creation_date: Union[str, XSDDate] = None
    ingest_code_url: Union[str, URIorCURIE] = None
    ingest_code_version: str = None
    source_infores_id: Union[str, URIorCURIE] = None
    source_data_version: str = None
    source_access_date: Union[str, XSDDate] = None
    target_name: str = None
    target_creation_date: Union[str, XSDDate] = None
    target_format: str = None
    target_model: str = None
    target_data_model_version: str = None
    file_created_by: Optional[Union[str, list[str]]] = empty_list()
    source_access_urls: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    source_file_names: Optional[Union[str, list[str]]] = empty_list()
    target_model_url: Optional[str] = None
    node_normalizer: Optional[str] = None
    node_normalizer_version: Optional[str] = None
    node_normalizer_url: Optional[str] = None
    total_edge_count: Optional[int] = None
    total_node_count: Optional[int] = None
    orphan_node_count: Optional[int] = None
    node_categories: Optional[Union[str, list[str]]] = empty_list()
    edge_predicates: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.file_creation_date):
            self.MissingRequiredField("file_creation_date")
        if not isinstance(self.file_creation_date, XSDDate):
            self.file_creation_date = XSDDate(self.file_creation_date)

        if self._is_empty(self.ingest_code_url):
            self.MissingRequiredField("ingest_code_url")
        if not isinstance(self.ingest_code_url, URIorCURIE):
            self.ingest_code_url = URIorCURIE(self.ingest_code_url)

        if self._is_empty(self.ingest_code_version):
            self.MissingRequiredField("ingest_code_version")
        if not isinstance(self.ingest_code_version, str):
            self.ingest_code_version = str(self.ingest_code_version)

        if self._is_empty(self.source_infores_id):
            self.MissingRequiredField("source_infores_id")
        if not isinstance(self.source_infores_id, URIorCURIE):
            self.source_infores_id = URIorCURIE(self.source_infores_id)

        if self._is_empty(self.source_data_version):
            self.MissingRequiredField("source_data_version")
        if not isinstance(self.source_data_version, str):
            self.source_data_version = str(self.source_data_version)

        if self._is_empty(self.source_access_date):
            self.MissingRequiredField("source_access_date")
        if not isinstance(self.source_access_date, XSDDate):
            self.source_access_date = XSDDate(self.source_access_date)

        if self._is_empty(self.target_name):
            self.MissingRequiredField("target_name")
        if not isinstance(self.target_name, str):
            self.target_name = str(self.target_name)

        if self._is_empty(self.target_creation_date):
            self.MissingRequiredField("target_creation_date")
        if not isinstance(self.target_creation_date, XSDDate):
            self.target_creation_date = XSDDate(self.target_creation_date)

        if self._is_empty(self.target_format):
            self.MissingRequiredField("target_format")
        if not isinstance(self.target_format, str):
            self.target_format = str(self.target_format)

        if self._is_empty(self.target_model):
            self.MissingRequiredField("target_model")
        if not isinstance(self.target_model, str):
            self.target_model = str(self.target_model)

        if self._is_empty(self.target_data_model_version):
            self.MissingRequiredField("target_data_model_version")
        if not isinstance(self.target_data_model_version, str):
            self.target_data_model_version = str(self.target_data_model_version)

        if not isinstance(self.file_created_by, list):
            self.file_created_by = [self.file_created_by] if self.file_created_by is not None else []
        self.file_created_by = [v if isinstance(v, str) else str(v) for v in self.file_created_by]

        if not isinstance(self.source_access_urls, list):
            self.source_access_urls = [self.source_access_urls] if self.source_access_urls is not None else []
        self.source_access_urls = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.source_access_urls]

        if not isinstance(self.source_file_names, list):
            self.source_file_names = [self.source_file_names] if self.source_file_names is not None else []
        self.source_file_names = [v if isinstance(v, str) else str(v) for v in self.source_file_names]

        if self.target_model_url is not None and not isinstance(self.target_model_url, str):
            self.target_model_url = str(self.target_model_url)

        if self.node_normalizer is not None and not isinstance(self.node_normalizer, str):
            self.node_normalizer = str(self.node_normalizer)

        if self.node_normalizer_version is not None and not isinstance(self.node_normalizer_version, str):
            self.node_normalizer_version = str(self.node_normalizer_version)

        if self.node_normalizer_url is not None and not isinstance(self.node_normalizer_url, str):
            self.node_normalizer_url = str(self.node_normalizer_url)

        if self.total_edge_count is not None and not isinstance(self.total_edge_count, int):
            self.total_edge_count = int(self.total_edge_count)

        if self.total_node_count is not None and not isinstance(self.total_node_count, int):
            self.total_node_count = int(self.total_node_count)

        if self.orphan_node_count is not None and not isinstance(self.orphan_node_count, int):
            self.orphan_node_count = int(self.orphan_node_count)

        if not isinstance(self.node_categories, list):
            self.node_categories = [self.node_categories] if self.node_categories is not None else []
        self.node_categories = [v if isinstance(v, str) else str(v) for v in self.node_categories]

        if not isinstance(self.edge_predicates, list):
            self.edge_predicates = [self.edge_predicates] if self.edge_predicates is not None else []
        self.edge_predicates = [v if isinstance(v, str) else str(v) for v in self.edge_predicates]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.ingestMetadataFile__file_name = Slot(uri=BIOLINK.file_name, name="ingestMetadataFile__file_name", curie=BIOLINK.curie('file_name'),
                   model_uri=BIOLINK.ingestMetadataFile__file_name, domain=None, range=str)

slots.ingestMetadataFile__file_created_by = Slot(uri=BIOLINK.file_created_by, name="ingestMetadataFile__file_created_by", curie=BIOLINK.curie('file_created_by'),
                   model_uri=BIOLINK.ingestMetadataFile__file_created_by, domain=None, range=Optional[Union[str, list[str]]])

slots.ingestMetadataFile__file_creation_date = Slot(uri=BIOLINK.file_creation_date, name="ingestMetadataFile__file_creation_date", curie=BIOLINK.curie('file_creation_date'),
                   model_uri=BIOLINK.ingestMetadataFile__file_creation_date, domain=None, range=Union[str, XSDDate])

slots.ingestMetadataFile__ingest_code_url = Slot(uri=BIOLINK.ingest_code_url, name="ingestMetadataFile__ingest_code_url", curie=BIOLINK.curie('ingest_code_url'),
                   model_uri=BIOLINK.ingestMetadataFile__ingest_code_url, domain=None, range=Union[str, URIorCURIE])

slots.ingestMetadataFile__ingest_code_version = Slot(uri=BIOLINK.ingest_code_version, name="ingestMetadataFile__ingest_code_version", curie=BIOLINK.curie('ingest_code_version'),
                   model_uri=BIOLINK.ingestMetadataFile__ingest_code_version, domain=None, range=str)

slots.ingestMetadataFile__source_infores_id = Slot(uri=BIOLINK.source_infores_id, name="ingestMetadataFile__source_infores_id", curie=BIOLINK.curie('source_infores_id'),
                   model_uri=BIOLINK.ingestMetadataFile__source_infores_id, domain=None, range=Union[str, URIorCURIE])

slots.ingestMetadataFile__source_data_version = Slot(uri=BIOLINK.source_data_version, name="ingestMetadataFile__source_data_version", curie=BIOLINK.curie('source_data_version'),
                   model_uri=BIOLINK.ingestMetadataFile__source_data_version, domain=None, range=str)

slots.ingestMetadataFile__source_access_date = Slot(uri=BIOLINK.source_access_date, name="ingestMetadataFile__source_access_date", curie=BIOLINK.curie('source_access_date'),
                   model_uri=BIOLINK.ingestMetadataFile__source_access_date, domain=None, range=Union[str, XSDDate])

slots.ingestMetadataFile__source_access_urls = Slot(uri=BIOLINK.source_access_urls, name="ingestMetadataFile__source_access_urls", curie=BIOLINK.curie('source_access_urls'),
                   model_uri=BIOLINK.ingestMetadataFile__source_access_urls, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.ingestMetadataFile__source_file_names = Slot(uri=BIOLINK.source_file_names, name="ingestMetadataFile__source_file_names", curie=BIOLINK.curie('source_file_names'),
                   model_uri=BIOLINK.ingestMetadataFile__source_file_names, domain=None, range=Optional[Union[str, list[str]]])

slots.ingestMetadataFile__target_name = Slot(uri=BIOLINK.target_name, name="ingestMetadataFile__target_name", curie=BIOLINK.curie('target_name'),
                   model_uri=BIOLINK.ingestMetadataFile__target_name, domain=None, range=str)

slots.ingestMetadataFile__target_creation_date = Slot(uri=BIOLINK.target_creation_date, name="ingestMetadataFile__target_creation_date", curie=BIOLINK.curie('target_creation_date'),
                   model_uri=BIOLINK.ingestMetadataFile__target_creation_date, domain=None, range=Union[str, XSDDate])

slots.ingestMetadataFile__target_format = Slot(uri=BIOLINK.target_format, name="ingestMetadataFile__target_format", curie=BIOLINK.curie('target_format'),
                   model_uri=BIOLINK.ingestMetadataFile__target_format, domain=None, range=str)

slots.ingestMetadataFile__target_model = Slot(uri=BIOLINK.target_model, name="ingestMetadataFile__target_model", curie=BIOLINK.curie('target_model'),
                   model_uri=BIOLINK.ingestMetadataFile__target_model, domain=None, range=str)

slots.ingestMetadataFile__target_model_url = Slot(uri=BIOLINK.target_model_url, name="ingestMetadataFile__target_model_url", curie=BIOLINK.curie('target_model_url'),
                   model_uri=BIOLINK.ingestMetadataFile__target_model_url, domain=None, range=Optional[str])

slots.ingestMetadataFile__target_data_model_version = Slot(uri=BIOLINK.target_data_model_version, name="ingestMetadataFile__target_data_model_version", curie=BIOLINK.curie('target_data_model_version'),
                   model_uri=BIOLINK.ingestMetadataFile__target_data_model_version, domain=None, range=str)

slots.ingestMetadataFile__node_normalizer = Slot(uri=BIOLINK.node_normalizer, name="ingestMetadataFile__node_normalizer", curie=BIOLINK.curie('node_normalizer'),
                   model_uri=BIOLINK.ingestMetadataFile__node_normalizer, domain=None, range=Optional[str])

slots.ingestMetadataFile__node_normalizer_version = Slot(uri=BIOLINK.node_normalizer_version, name="ingestMetadataFile__node_normalizer_version", curie=BIOLINK.curie('node_normalizer_version'),
                   model_uri=BIOLINK.ingestMetadataFile__node_normalizer_version, domain=None, range=Optional[str])

slots.ingestMetadataFile__node_normalizer_url = Slot(uri=BIOLINK.node_normalizer_url, name="ingestMetadataFile__node_normalizer_url", curie=BIOLINK.curie('node_normalizer_url'),
                   model_uri=BIOLINK.ingestMetadataFile__node_normalizer_url, domain=None, range=Optional[str])

slots.ingestMetadataFile__total_edge_count = Slot(uri=BIOLINK.total_edge_count, name="ingestMetadataFile__total_edge_count", curie=BIOLINK.curie('total_edge_count'),
                   model_uri=BIOLINK.ingestMetadataFile__total_edge_count, domain=None, range=Optional[int])

slots.ingestMetadataFile__total_node_count = Slot(uri=BIOLINK.total_node_count, name="ingestMetadataFile__total_node_count", curie=BIOLINK.curie('total_node_count'),
                   model_uri=BIOLINK.ingestMetadataFile__total_node_count, domain=None, range=Optional[int])

slots.ingestMetadataFile__orphan_node_count = Slot(uri=BIOLINK.orphan_node_count, name="ingestMetadataFile__orphan_node_count", curie=BIOLINK.curie('orphan_node_count'),
                   model_uri=BIOLINK.ingestMetadataFile__orphan_node_count, domain=None, range=Optional[int])

slots.ingestMetadataFile__node_categories = Slot(uri=BIOLINK.node_categories, name="ingestMetadataFile__node_categories", curie=BIOLINK.curie('node_categories'),
                   model_uri=BIOLINK.ingestMetadataFile__node_categories, domain=None, range=Optional[Union[str, list[str]]])

slots.ingestMetadataFile__edge_predicates = Slot(uri=BIOLINK.edge_predicates, name="ingestMetadataFile__edge_predicates", curie=BIOLINK.curie('edge_predicates'),
                   model_uri=BIOLINK.ingestMetadataFile__edge_predicates, domain=None, range=Optional[Union[str, list[str]]])
