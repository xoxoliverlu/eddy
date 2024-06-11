#!/bin/dash

# Test multiple commands with both newlines and semicolon
output=$(echo "4q
/2/d;1q
"| python3 -s -S eddy.py 1q)
expect=$(echo "4q
/2/d;1q
"| ./eddy.py 1q)

if [ "$output" = "$expect" ]; 
then
    exit 0
else
    exit 1
fi