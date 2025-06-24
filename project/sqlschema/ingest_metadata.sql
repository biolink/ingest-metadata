-- # Class: "IngestMetadata" Description: "Metadata about a specific data ingest process and its outputs"
--     * Slot: id Description: 
--     * Slot: title Description: Human-readable name for this metadata object
--     * Slot: creation_date Description: Date the ingest metadata was created
--     * Slot: ingest_code_url Description: URL of the code used for the ingest (tagged release or branch)
--     * Slot: ingest_guide_url Description: URL of the RIG (Reference Ingest Guide)
--     * Slot: source_infores_id Description: Infores identifier of the ingested source
--     * Slot: source_license Description: License or terms of use for the source
--     * Slot: source_data_version Description: Version of the ingested source data
--     * Slot: source_publication_date Description: Date the source data was published
--     * Slot: source_download_date Description: Date the source data was downloaded
--     * Slot: target_title Description: Human-readable name of the output dataset/graph
--     * Slot: target_type Description: Level of processing applied to the output (e.g. Source-KG, Biolink KG, Normalized KG)
--     * Slot: target_data_version Description: Version of the output dataset/graph
--     * Slot: target_creation_date Description: Date the output was created
--     * Slot: target_license Description: License or terms of use for the output
--     * Slot: target_data_format Description: Format of the output graph (KGX)
--     * Slot: target_data_model Description: Data model used (Biolink Model)
--     * Slot: target_data_model_version Description: Version of the data model used
--     * Slot: node_normalizer Description: Name of the node normalizer used
--     * Slot: node_normalizer_version Description: Version of the node normalizer used
-- # Class: "IngestMetadata_created_by" Description: ""
--     * Slot: IngestMetadata_id Description: Autocreated FK slot
--     * Slot: created_by Description: One or more creators of this ingest metadata file
-- # Class: "IngestMetadata_source_access_urls" Description: ""
--     * Slot: IngestMetadata_id Description: Autocreated FK slot
--     * Slot: source_access_urls Description: URLs from which the source data was accessed
-- # Class: "IngestMetadata_source_data_formats" Description: ""
--     * Slot: IngestMetadata_id Description: Autocreated FK slot
--     * Slot: source_data_formats Description: Formats of source data files or payloads
-- # Class: "IngestMetadata_source_data_files" Description: ""
--     * Slot: IngestMetadata_id Description: Autocreated FK slot
--     * Slot: source_data_files Description: List of source file names ingested

CREATE TABLE "IngestMetadata" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	creation_date DATE NOT NULL, 
	ingest_code_url TEXT NOT NULL, 
	ingest_guide_url TEXT, 
	source_infores_id TEXT NOT NULL, 
	source_license TEXT, 
	source_data_version TEXT NOT NULL, 
	source_publication_date DATE, 
	source_download_date DATE, 
	target_title TEXT NOT NULL, 
	target_type TEXT NOT NULL, 
	target_data_version TEXT NOT NULL, 
	target_creation_date DATE NOT NULL, 
	target_license TEXT NOT NULL, 
	target_data_format TEXT NOT NULL, 
	target_data_model TEXT, 
	target_data_model_version TEXT, 
	node_normalizer TEXT, 
	node_normalizer_version TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "IngestMetadata_created_by" (
	"IngestMetadata_id" INTEGER, 
	created_by TEXT, 
	PRIMARY KEY ("IngestMetadata_id", created_by), 
	FOREIGN KEY("IngestMetadata_id") REFERENCES "IngestMetadata" (id)
);
CREATE TABLE "IngestMetadata_source_access_urls" (
	"IngestMetadata_id" INTEGER, 
	source_access_urls TEXT, 
	PRIMARY KEY ("IngestMetadata_id", source_access_urls), 
	FOREIGN KEY("IngestMetadata_id") REFERENCES "IngestMetadata" (id)
);
CREATE TABLE "IngestMetadata_source_data_formats" (
	"IngestMetadata_id" INTEGER, 
	source_data_formats TEXT, 
	PRIMARY KEY ("IngestMetadata_id", source_data_formats), 
	FOREIGN KEY("IngestMetadata_id") REFERENCES "IngestMetadata" (id)
);
CREATE TABLE "IngestMetadata_source_data_files" (
	"IngestMetadata_id" INTEGER, 
	source_data_files TEXT, 
	PRIMARY KEY ("IngestMetadata_id", source_data_files), 
	FOREIGN KEY("IngestMetadata_id") REFERENCES "IngestMetadata" (id)
);