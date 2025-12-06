#!/bin/bash
#
# AI Usage Policy:
# AI assistance was used to help format this helper script
# and clarify how tests are reported. All test cases and
# expected behaviors were created and verified by the student.
#
# Simple test helper: run a command and compare its output
# against an expected string.

run_test () {
    local name="$1"
    local expected="$2"
    shift 2

    # Run the command and capture standard output
    local output
    output="$("$@" 2>/dev/null)"

    if [ "$output" = "$expected" ]; then
        echo "[PASS] $name"
    else
        echo "[FAIL] $name"
        echo "  expected: $expected"
        echo "  got:      $output"
    fi
}

