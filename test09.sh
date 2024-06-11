#!/bin/dash

# Test complicate substitue  with -n
output=$(seq 100 111 | ./eddy.py -n '/1.1/s/1/-/g')
expect=$(seq 100 111 | 2041 eddy -n '/1.1/s/1/-/g')
if [ "$output" = "$expect" ]; 
then
    exit 0
else
    exit 1
fi   