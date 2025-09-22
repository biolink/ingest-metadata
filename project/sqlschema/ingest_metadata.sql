-- # Class: IngestMetadataFile Description: Information about a particular ingest performed to produce a KGX graph, describing source data, ingest process, and details of the resulting KGX graph.
--     * Slot: id
--     * Slot: file_name Description: An informative, human-readable name for this metadata file/object. e.g. "2025-08-18 Translator CTD Ingest Metadata"
--     * Slot: file_creation_date Description: When this metadata file was created.
--     * Slot: ingest_code_url Description: URL of the specific official release or tagged branch of the ingest code executed to perform the ingest.
--     * Slot: ingest_code_version Description: The version of the ingest code executed to perform the ingest.
--     * Slot: source_infores_id Description: Infores identifier of the ingested source.
--     * Slot: source_data_version Description: Version of the source data ingested - using source's own conventions, or make one up (e.g. use the date) if not provided by source.
--     * Slot: source_access_date Description: Date the source data was accessed/downloaded into the system that performed the ingest.
--     * Slot: target_name Description: A unique human readable name of the target data set/graph produced by this ingest. e.g. "2025-08-18 Translator CTD Ingest Graph"
--     * Slot: target_creation_date Description: Date the target data set/graph was created.
--     * Slot: target_format Description: Format in which the KGX graph is serialized (e.g., "KGX-jsonlines").
--     * Slot: target_model Description: Name/identifier of the data model used to structure the KGX graph data.
--     * Slot: target_model_url Description: A URL providing information about the data model used to structure the KGX graph data. e.g. "https://biolink.github.io/biolink-model/"
--     * Slot: target_data_model_version Description: Version of the target data model used to structure the KGX graph data. e.g. "4.2.6-rc5"
--     * Slot: node_normalizer Description: Name/identifier of the algorithm/tool used to perform node normalization on the ingested data. e.g. "Babel"
--     * Slot: node_normalizer_version Description: Version of the node normalization tool/algorithm.
--     * Slot: node_normalizer_url Description: URL(s) pointing to source code and/or information about the node normalization tool used. e.g. "https://github.com/TranslatorSRI/NodeNormalization"
--     * Slot: total_edge_count Description: Count of total edges in the graph.
--     * Slot: total_node_count Description: Count of total nodes in the graph.
--     * Slot: orphan_node_count Description: Count of nodes in the graph that do not participate in an edge.
-- # Class: IngestMetadataFile_file_created_by
--     * Slot: IngestMetadataFile_id Description: Autocreated FK slot
--     * Slot: file_created_by Description: The agent(s) (person if hand-authored, software tool if created programmatically) that created this ingest metadata file.
-- # Class: IngestMetadataFile_source_access_urls
--     * Slot: IngestMetadataFile_id Description: Autocreated FK slot
--     * Slot: source_access_urls Description: URLs where source data was accessed / downloaded / queried to be brought into the system performing the ingest.
-- # Class: IngestMetadataFile_source_file_names
--     * Slot: IngestMetadataFile_id Description: Autocreated FK slot
--     * Slot: source_file_names Description: File names from which content used to produce the output KGX graph was retrieved.
-- # Class: IngestMetadataFile_node_categories
--     * Slot: IngestMetadataFile_id Description: Autocreated FK slot
--     * Slot: node_categories Description: List of all Biolink categories used for nodes in the graph.
-- # Class: IngestMetadataFile_edge_predicates
--     * Slot: IngestMetadataFile_id Description: Autocreated FK slot
--     * Slot: edge_predicates Description: List of all Biolink predicates used in the graph.

CREATE TABLE "IngestMetadataFile" (
	id INTEGER NOT NULL,
	file_name TEXT NOT NULL,
	file_creation_date DATE NOT NULL,
	ingest_code_url TEXT NOT NULL,
	ingest_code_version TEXT NOT NULL,
	source_infores_id TEXT NOT NULL,
	source_data_version TEXT NOT NULL,
	source_access_date DATE NOT NULL,
	target_name TEXT NOT NULL,
	target_creation_date DATE NOT NULL,
	target_format TEXT NOT NULL,
	target_model TEXT NOT NULL,
	target_model_url TEXT,
	target_data_model_version TEXT NOT NULL,
	node_normalizer TEXT,
	node_normalizer_version TEXT,
	node_normalizer_url TEXT,
	total_edge_count INTEGER,
	total_node_count INTEGER,
	orphan_node_count INTEGER,
	PRIMARY KEY (id)
);CREATE INDEX "ix_IngestMetadataFile_id" ON "IngestMetadataFile" (id);
CREATE TABLE "IngestMetadataFile_file_created_by" (
	"IngestMetadataFile_id" INTEGER,
	file_created_by TEXT,
	PRIMARY KEY ("IngestMetadataFile_id", file_created_by),
	FOREIGN KEY("IngestMetadataFile_id") REFERENCES "IngestMetadataFile" (id)
);CREATE INDEX "ix_IngestMetadataFile_file_created_by_IngestMetadataFile_id" ON "IngestMetadataFile_file_created_by" ("IngestMetadataFile_id");CREATE INDEX "ix_IngestMetadataFile_file_created_by_file_created_by" ON "IngestMetadataFile_file_created_by" (file_created_by);
CREATE TABLE "IngestMetadataFile_source_access_urls" (
	"IngestMetadataFile_id" INTEGER,
	source_access_urls TEXT,
	PRIMARY KEY ("IngestMetadataFile_id", source_access_urls),
	FOREIGN KEY("IngestMetadataFile_id") REFERENCES "IngestMetadataFile" (id)
);CREATE INDEX "ix_IngestMetadataFile_source_access_urls_IngestMetadataFile_id" ON "IngestMetadataFile_source_access_urls" ("IngestMetadataFile_id");CREATE INDEX "ix_IngestMetadataFile_source_access_urls_source_access_urls" ON "IngestMetadataFile_source_access_urls" (source_access_urls);
CREATE TABLE "IngestMetadataFile_source_file_names" (
	"IngestMetadataFile_id" INTEGER,
	source_file_names TEXT,
	PRIMARY KEY ("IngestMetadataFile_id", source_file_names),
	FOREIGN KEY("IngestMetadataFile_id") REFERENCES "IngestMetadataFile" (id)
);CREATE INDEX "ix_IngestMetadataFile_source_file_names_source_file_names" ON "IngestMetadataFile_source_file_names" (source_file_names);CREATE INDEX "ix_IngestMetadataFile_source_file_names_IngestMetadataFile_id" ON "IngestMetadataFile_source_file_names" ("IngestMetadataFile_id");
CREATE TABLE "IngestMetadataFile_node_categories" (
	"IngestMetadataFile_id" INTEGER,
	node_categories TEXT,
	PRIMARY KEY ("IngestMetadataFile_id", node_categories),
	FOREIGN KEY("IngestMetadataFile_id") REFERENCES "IngestMetadataFile" (id)
);CREATE INDEX "ix_IngestMetadataFile_node_categories_IngestMetadataFile_id" ON "IngestMetadataFile_node_categories" ("IngestMetadataFile_id");CREATE INDEX "ix_IngestMetadataFile_node_categories_node_categories" ON "IngestMetadataFile_node_categories" (node_categories);
CREATE TABLE "IngestMetadataFile_edge_predicates" (
	"IngestMetadataFile_id" INTEGER,
	edge_predicates TEXT,
	PRIMARY KEY ("IngestMetadataFile_id", edge_predicates),
	FOREIGN KEY("IngestMetadataFile_id") REFERENCES "IngestMetadataFile" (id)
);CREATE INDEX "ix_IngestMetadataFile_edge_predicates_IngestMetadataFile_id" ON "IngestMetadataFile_edge_predicates" ("IngestMetadataFile_id");CREATE INDEX "ix_IngestMetadataFile_edge_predicates_edge_predicates" ON "IngestMetadataFile_edge_predicates" (edge_predicates);
