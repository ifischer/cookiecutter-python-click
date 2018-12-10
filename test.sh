#!/bin/bash
set -e
if [ $# -eq 0 ]; then
    dir=$(mktemp -d)
else
    dir="${1}"
fi
echo "Using directory: ${dir}"
# Test cookiecutter template - create project and run Docker test
cookiecutter --no-input --config-file ./sample_config -o ${dir} .
cd ${dir}/foobar_project
make docker-build docker-test
make virtualenv-create virtualenv-test
echo "TEST SUCCESSFUL"
echo "Go to '${dir}' to play around with generated project"
