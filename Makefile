.PHONY: help

run: ## Run the main Django application
	python manage.py runserver

update: ## Update all outdated pip dependencies and updates requirements.txt file
	scripts/pip_update

test: ## Some info text
	echo "test"

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help