#!/usr/bin/env bash

aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --output json
