#!/usr/bin/env bash

# Run aws s3 ls and format the output as JSON
aws s3 ls --output json | awk 'BEGIN {print "["} {if (NR > 1) {print ","} print "{\"timestamp\": \"" $1 " " $2 "\", \"bucket\": \"" $3 "\"}"} END {print "]"}'

