#!/usr/bin/env bash
sample=${1:-100}
./s.py $sample | ./filter.sh | column -t -s' '
