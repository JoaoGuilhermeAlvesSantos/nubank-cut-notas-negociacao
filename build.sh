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

function cmd_create-target() {
    mkdir target
}
function cmd_run() {
    if [ ! -d "target" ]; then
        echo "Directory 'target' does not exist."
        exit 1
    fi

    if [ -z "$(ls -A "target")" ]; then
        echo "Directory 'target' is empty."
        exit
    fi

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
