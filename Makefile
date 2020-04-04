.PHONY: help

install-reqs: ## Installs the main dependencies
	scripts/install_reqs.sh

run: ## Run the main Django application and make it available on local network
	python manage.py runserver 0.0.0.0:8000

update: ## Update all outdated pip dependencies and updates requirements.txt file
	scripts/pip_update.sh

black-check: ## Show in console what would be changed by Black formatter
	black --check . --target-version py37 --skip-string-normalization  --exclude "pinode-env/*"

black: ## Runs Black formatter
	black . --target-version py37 --skip-string-normalization  --exclude "pinode-env/*"

test: ## Some info text
	echo "test"

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help