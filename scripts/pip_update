#!/bin/bash

# Updates all outdated pip dependencies and updates requirements.txt file
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

echo "Packages updated. Please now execute 'pip freeze > requirements.txt'"
