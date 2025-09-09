#!/usr/bin/env bash
# simple-interest.sh - compute simple interest
# Usage: ./simple-interest.sh <principal> <rate> <time>

if [ $# -ne 3 ]; then
  echo "Usage: $0 <principal> <annual_rate_percent> <time_years>"
  exit 1
fi

P=$1
R=$2
T=$3

# Calculate simple interest: (P * R * T) / 100
SI=$(awk "BEGIN { printf \"%.2f\", ($P * $R * $T) / 100 }")

echo "Simple Interest for principal=${P}, rate=${R}%, time=${T} years is: ${SI}"
