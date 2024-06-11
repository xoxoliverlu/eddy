#!/bin/dash

# Test substitute global option with -n
output=$(seq 51 60 | ./eddy.py -n '5s/5/9/g')
expect=$(seq 51 60 | 2041 eddy -n '5s/5/9/g')
if [ "$output" = "$expect" ]; 
then
    exit 0
else
    exit 1
fi