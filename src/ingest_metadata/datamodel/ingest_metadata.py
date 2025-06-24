# Auto generated from ingest_metadata.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-06-24T14:30:43
# Schema: ingest-metadata
#
# id: https://w3id.org/biolink/ingest-metadata
# description: Schema hosting relevant metadata for a data transformation conformant to the Biolink Model
# license: MIT

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
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
INGEST_METADATA = CurieNamespace('ingest_metadata', 'https://w3id.org/biolink/ingest-metadata/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = INGEST_METADATA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class IngestMetadataId(NamedThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = INGEST_METADATA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IngestMetadata(NamedThing):
    """
    Represents a IngestMetadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INGEST_METADATA["IngestMetadata"]
    class_class_curie: ClassVar[str] = "ingest_metadata:IngestMetadata"
    class_name: ClassVar[str] = "IngestMetadata"
    class_model_uri: ClassVar[URIRef] = INGEST_METADATA.IngestMetadata

    id: Union[str, IngestMetadataId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IngestMetadataId):
            self.id = IngestMetadataId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IngestMetadataCollection(YAMLRoot):
    """
    A holder for IngestMetadata objects
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INGEST_METADATA["IngestMetadataCollection"]
    class_class_curie: ClassVar[str] = "ingest_metadata:IngestMetadataCollection"
    class_name: ClassVar[str] = "IngestMetadataCollection"
    class_model_uri: ClassVar[URIRef] = INGEST_METADATA.IngestMetadataCollection

    entries: Optional[Union[dict[Union[str, IngestMetadataId], Union[dict, IngestMetadata]], list[Union[dict, IngestMetadata]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=IngestMetadata, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=INGEST_METADATA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=INGEST_METADATA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=INGEST_METADATA.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=INGEST_METADATA.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=INGEST_METADATA.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=INGEST_METADATA.age_in_years, name="age_in_years", curie=INGEST_METADATA.curie('age_in_years'),
                   model_uri=INGEST_METADATA.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=INGEST_METADATA.vital_status, name="vital_status", curie=INGEST_METADATA.curie('vital_status'),
                   model_uri=INGEST_METADATA.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.ingestMetadataCollection__entries = Slot(uri=INGEST_METADATA.entries, name="ingestMetadataCollection__entries", curie=INGEST_METADATA.curie('entries'),
                   model_uri=INGEST_METADATA.ingestMetadataCollection__entries, domain=None, range=Optional[Union[dict[Union[str, IngestMetadataId], Union[dict, IngestMetadata]], list[Union[dict, IngestMetadata]]]])

slots.IngestMetadata_primary_email = Slot(uri=SCHEMA.email, name="IngestMetadata_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=INGEST_METADATA.IngestMetadata_primary_email, domain=IngestMetadata, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))