#!/bin/dash

# Test using differnt delimiter
output=$(seq 1 5 | ./eddy.py 's%[15]%z/z/z%')
expect=$(seq 1 5 | 2041 eddy 's%[15]%z/z/z%')

if [ "$output" = "$expect" ]; 
then
    exit 0
else
    exit 1
fi