[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

## Changes Made

Implemented get_column function to read CSV files and find matching data.

Added improvements:
- Named argument for result_column with default value of 1
- Updated print_fires.py to use named arguments  
- Created run.sh script to run the demo

## AI Usage Documentation

This assignment was completed with assistance from Claude AI for:
- CSV file parsing logic and implementation
- Fixing broken function calls and parameter handling
- Data structure analysis for column indexing
- Comment style improvements for natural language
- Git workflow guidance and repository management

Claude AI. *Conversational AI Assistant*. Anthropic, 2025. https://claude.ai.


## Assignment 4: Testing (v3.0.0)

This version adds statistical helper functions to `my_utils.py`:

- `mean(values)`
- `median(values)`
- `std(values)`

The `print_fires.py` script now includes an `--op` argument that accepts
one of three operations: `mean`, `median`, or `std`.  
When provided, the script computes the selected statistic on the
values for the chosen country instead of printing the raw list.

### Unit Tests
Unit tests for all three statistical functions are located in  
`tests/unit/test_my_utils.py`.

These tests check:
- correct output for typical inputs  
- behavior on even-length and odd-length lists  
- correct handling of negative numbers  
- appropriate errors on empty input lists  

### Functional Tests
Functional tests for `print_fires.py` are located in  
`tests/functional/test_print_fires.sh`.

These tests verify:
- correct behavior of the `--op` flag (mean, median, std)  
- correct handling of a missing CSV file  
- correct handling of a country with no matching rows  
- correct non-zero exit codes for error cases
