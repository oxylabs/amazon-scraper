# Makefile for running Amazon scraper


.PHONY: install
install:
	pip install poetry==1.8.2
	poetry install


.PHONY: scrape
scrape:
	@if [ -z "$(URL)" ]; then \
		echo 'Error: A URL of an Amazon page is required. Use make scrape URL="<amazon_page_url>"'; \
		exit 1; \
	else \
		poetry run python -m amazon_scraper --url="$(URL)"; \
	fi
