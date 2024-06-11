#!/bin/dash

# Test for quit command with line number
output=$(seq 42 44 | python3 -s -S eddy.py 1q)
expect=$(seq 42 44 | ./eddy.py 1q)

if [ "$output" = "$expect" ]; 
then
    exit 0
else
    exit 1
fi