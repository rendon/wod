#!/usr/bin/env bash

cd /home/rendon/projects/wod/

export PYENV_ROOT="/home/rendon/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

uvicorn main:app --reload --reload-include *.json
