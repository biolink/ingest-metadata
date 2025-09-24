## This is included by the main Makefile.

# Create a new Ingest Metadata Specification YAML from template
# Usage: make new-metadata INFORES=infores:ctd
new-metadata:
ifndef INFORES
	$(error INFORES is required. Usage: make new-metadata INFORES=infores:example")
endif
	$(RUN) python $(SRC)/scripts/create_metadata.py --infores "$(INFORES)"

# Validate all RIG files against the schema
validate-metadata:
	@echo "Validating Ingest Metadata Specification files against schema..."
	@for ingest_spec in $(SRC)/docs/metadata/*.yaml; do \
		if [ -f "$$ingest_spec" ]; then \
			echo "Validating $$ingest_spec"; \
			$(RUN) linkml-validate --schema $(SOURCE_SCHEMA_PATH) "$$ingest_spec"; \
		fi; \
	done
	@echo "✓ All Ingest Metadata Specification files validated successfully"
