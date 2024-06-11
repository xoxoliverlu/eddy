#!/bin/dash

# Test using differnt delimiter
output=$(seq 11 19 | ./eddy.py -n '5s/1/2/')
expect=$(seq 11 19 | 2041 eddy -n '5s/1/2/')
if [ "$output" = "$expect" ]; 
then
    exit 0
else
    exit 1
fi