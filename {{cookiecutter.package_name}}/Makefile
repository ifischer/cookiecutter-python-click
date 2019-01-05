.PHONY: help
.DEFAULT_GOAL := help
CONTAINER  = {{ cookiecutter.docker_container_name }}
VIRTUALENV_DIR = {{ cookiecutter.virtualenv_dir }}

help:
	# Print help by extracting ##-comments per target
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

docker-clean:
	docker stop --rm $(CONTAINER)

docker-build:  ## Build Docker container
	docker build -t $(CONTAINER) .

docker-run:  ## Run Docker container
	docker run -v $$(pwd):/code $(CONTAINER)

docker-shell:  ## Run Docker shell
	docker run -v $$(pwd):/code -it --rm $(CONTAINER) bash

docker-test:
	docker run --rm -i -t $(CONTAINER) pytest


virtualenv-create:  ## Create virtualenv
	virtualenv --python=$$(which python{{cookiecutter.python_version}}) $(VIRTUALENV_DIR)
	$(VIRTUALENV_DIR)/bin/pip3 install -r requirements.txt
	$(VIRTUALENV_DIR)/bin/pip3 install -r requirements-dev.txt
	$(VIRTUALENV_DIR)/bin/pip3 install -e .
	@echo "Activate virtualenv:\n. $(VIRTUALENV_DIR)/bin/activate"

virtualenv-test:
	$(VIRTUALENV_DIR)/bin/pytest


lint:  ## Run linter (Flake8, isort)
	$(DOCKERCMD) pytest --flake8
	$(DOCKERCMD) pytest --isort
