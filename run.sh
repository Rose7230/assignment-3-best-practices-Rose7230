#!/bin/bash
# runs the fire data script

# This script demonstrates:
# 1. A successful run of print_fires.py
# 2. An error from a missing file
# 3. An error from invalid column indexes


# Successful run with valid file and column indexes
python print_fires.py \
  --country "Saudi Arabia" \
  --country_column 0 \
  --fires_column 1 \
  --file_name Agrofood_co2_emission.csv


# Error: file does not exist
python print_fires.py \
  --country "Saudi Arabia" \
  --country_column 0 \
  --fires_column 1 \
  --file_name missing_file.csv


# Error: invalid column indexes
python print_fires.py \
  --country "Saudi Arabia" \
  --country_column 99 \
  --fires_column 150 \
  --file_name Agrofood_co2_emission.csv

  