generate-example:  ## Generate code from cookiecutter template
	cookiecutter --overwrite-if-exists --no-input --config-file ./sample_config .
	cd example_project && \
		make docker-build docker-test && \
		make virtualenv-create virtualenv-test && \
		echo "TEST SUCCESSFUL"

clean:
	rm -rf example_project/.venv
	rm -rf example_project/example_project.egg-info
	rm -rf example_project/.pytest_cache
	find example_project -name "*.pyc" -exec rm {} \;

