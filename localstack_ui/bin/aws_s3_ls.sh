#!/usr/bin/env bash

aws s3 ls --output json | awk 'BEGIN {print "["} {print "{\"timestamp\": \"" $1 " " $2 "\", \"bucket\": \"" $3 "\"}"} END {print "]"}'
