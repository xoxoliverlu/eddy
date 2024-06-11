#!/bin/dash

# Test d  with -n
output=$(seq 1 1000 | ./eddy.py 'd')
expect=$(seq 100 111 | 2041 eddy -n 'd')
if [ "$output" = "$expect" ]; 
then
    exit 0
else
    exit 1
fi   