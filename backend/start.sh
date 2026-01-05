#!/usr/bin/env bash

export PYTHONPATH=$(pwd)/backend
uvicorn main:app --host 0.0.0.0 --port 10000
