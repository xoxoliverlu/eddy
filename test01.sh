#!/bin/dash

# Test for a single p command with no line number
output=$(seq 1 5 | ./eddy.py 'p')
expect=$(seq 1 5 | 2041 eddy 'p')

if [ "$output" = "$expect" ]; 
then
    exit 0
else
    exit 1
fi