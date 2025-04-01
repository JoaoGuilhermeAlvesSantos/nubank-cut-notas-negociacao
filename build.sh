#!/bin/bash -e

function cmd_venv() {
    if [ -d ".venv" ]; then
        source .venv/bin/activate
    else
        python3 -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
    fi
}

function cmd_run() {
    params="$@"
    if [ -z "$params" ]; then
        params="main.py"
    fi
    source .venv/bin/activate
    python $params
}


cd "$(dirname "$0")"
_cmd="${1?"cmd is required"}"
shift
"cmd_${_cmd}" "$@"
