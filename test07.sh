#!/bin/dash

# Test d with -n option
output=$(seq 1 5 | ./eddy.py -n '4d')
expect=$(seq 1 5 | 2041 eddy -n '4d')
if [ "$output" = "$expect" ]; 
then
    exit 0
else
    exit 1
fi