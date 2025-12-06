#!/bin/bash
#
# AI Usage Policy:
# AI assistance was used to help structure these functional tests
# and to format the commands. All test cases, expected outputs,
# and final verification were performed by the student.

set -e  # exit if any command fails unexpectedly

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR/../.."

cd "$PROJECT_ROOT"

source tests/functional/ssbt.sh

DATA_FILE="tests/functional/test_data.csv"

# For country A, the values in test_data.csv are [10, 20, 30]
# mean = 20.0
run_test "mean operation for country A" "20.0" \
    python print_fires.py \
        --country A \
        --country_column 0 \
        --fires_column 1 \
        --file_name "$DATA_FILE" \
        --op mean

# median of [10, 20, 30] = 20
run_test "median operation for country A" "20" \
    python print_fires.py \
        --country A \
        --country_column 0 \
        --fires_column 1 \
        --file_name "$DATA_FILE" \
        --op median

# std of [10, 20, 30] = sqrt(200/3) ≈ 8.16496580927726
run_test "std operation for country A" "8.16496580927726" \
    python print_fires.py \
        --country A \
        --country_column 0 \
        --fires_column 1 \
        --file_name "$DATA_FILE" \
        --op std

# Exit code test: missing file should give non-zero exit code
if python print_fires.py \
        --country A \
        --country_column 0 \
        --fires_column 1 \
        --file_name "no_such_file.csv" \
        --op mean; then
    echo "[FAIL] missing file should have non-zero exit code"
else
    echo "[PASS] missing file exit code"
fi

# Exit code test: no matching rows for this country
if python print_fires.py \
        --country Z \
        --country_column 0 \
        --fires_column 1 \
        --file_name "$DATA_FILE" \
        --op mean; then
    echo "[FAIL] no-data case should have non-zero exit code"
else
    echo "[PASS] no-data exit code"
fi

