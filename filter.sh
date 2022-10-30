#!/usr/bin/env bash
perl -ne 'print if s/^(.*\D1\/\d+\s+1\/.*)$/\1/g'
