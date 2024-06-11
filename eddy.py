#!/usr/bin/python3

import sys
import re
from io import StringIO
import os
def main():
    options = {}
    if '-n' in sys.argv:
        options['print'] = False
        sys.argv.remove('-n')
    else:
        options['print'] = True
    # Check if the '-f' option is present and get the filename
    if '-f' in sys.argv:
        file_index = sys.argv.index('-f') + 1
        filename = sys.argv[file_index]
        # Read commands from the specified file
        with open(filename, 'r') as f:
            commands = f.read()
    else:
        commands = sys.argv[1]

    # Processing commands
    command = []
    command = commands.splitlines()
    for cmd in command:
        if ";" in cmd:
            semi_cmd = cmd.split(";")
            command.remove(cmd)
            command.extend(semi_cmd)
    res = ""
    
    # Keep track of what commands has been used
    all_commands = []
    
    # Process each command
    for time, cmd in enumerate(command):   
        match = re.search(r"((^(\d+|\$)?s?(.).*(\4)(.*(\4))?(g?))|^(\d+|\$))?([qpd])?", cmd)
        if match:
            address = match.group(1)
            command = match.group(10)
            all_commands.append(command)
            
            # if first time, use stdin as input
            if(time == 0) :
                res = process(sys.stdin, address, command, options)
            
            # else, use current res as input
            else:
                res = process(res.splitlines(), address, command, options)
    if len(res) == 0:
        return
    else:
        for line in res.splitlines():
            if line == "":
                if "d" in all_commands:
                    continue
                else:
                    print(line)
            else:
                print(line)

def process(inp, address, command, options):
    if (command == "q"):
        return q(inp, address, options)
    elif (command == 'p'):
        return p(inp,address, options)
    elif (command == 'd'):
        return delete(inp, address, options)
    elif (address != None and re.search(r'((.)(.*)(\2))?(\d+)?s(.)(.*)(\6)(.*)(\6)(g)?',address)):
        return substitute(inp, address, options)
        
def q(inp, address, options):
    res = ""
    match = re.search(r'/(.*)/', address) if address else None
    if (match):
        pattern = match.group(1)
        for line in inp:
            res += line.strip() if options['print'] else ""
            res += '\n' if options['print'] else ""
            if re.search(fr'{pattern}', line):
                break
    else:
        line_num = int(address) if address and address != "$" else -1 
        cur = 1
        for line in inp:
            res += line.strip() if options['print'] else ""
            res += '\n' if options['print'] else ""
            if (cur == line_num and line != ""):
                break 
            cur +=1
    return res
def p(inp, address, options):
    res = ""
    match = re.search(r'/(.*)/', address) if address else None
    if (match):
        pattern = match.group(1)
        for line in inp:
            res += line.strip() if options['print'] else ""
            res += '\n' if options['print'] else ""
            if re.search(fr'{pattern}', line):
                res += line.strip()
                res += '\n'
    else:
        line_num = int(address) if address else -1 
        cur = 0
        for line in inp:
            cur += 1
            if (cur == line_num or line_num == -1):
                res += line.strip() 
                res += '\n'
            res += line.strip() if options['print'] else ""
            res += '\n' if options['print'] else ""
    return res
        
def delete(inp,address, options):
    res = ""
    match = re.search(r'/(.*)/', address) if address else None
    if (match):
        pattern = match.group(1)
        for line in inp:
            if not re.search(fr'{pattern}', line):
                res += line.strip() if options['print'] else ""
                res += '\n' if options['print'] else ""
            else:
                res += '\n' if options['print'] else ""
    else:
        line_num = int(address) if address else -1 
        if (line_num == -1):
            return res
        cur = 0
        for line in inp:
            cur += 1
            if (cur != line_num):
                res += line.strip() if options['print'] else ""
                res += '\n' if options['print'] else ""
            else:
                res += '\n' if options['print'] else ""
    return res

def substitute(inp, address, options):
    res = ""
    match = re.search(r'((.)(.*)(\2))?(\d+)?s(.)(.*)(\6)(.*)(\6)(g)?', address) if address else None
    if match:
        target = match.group(3)
        line_num = match.group(5)
        pattern = match.group(7)
        replacement = match.group(9)
        glo = match.group(11)
        lines = 0
        if not line_num:
            if target:
                for line in inp:
                    if re.search(rf'{target}', line):
                        # if global option is present
                        if glo:
                            res += re.sub(pattern, replacement, line).strip() if options['print'] else ""
                            res += '\n' if options['print'] else ""
                        else:
                            res += re.sub(pattern, replacement, line, count=1).strip() if options['print'] else ""
                            res += '\n' if options['print'] else ""
                    else:
                        res += line.strip() if options['print'] else ""
                        res += '\n' if options['print'] else ""
            else:
                for line in inp:
                    if re.search(rf'{pattern}', line):
                        if glo:
                            res += re.sub(pattern, replacement, line).strip() if options['print'] else ""
                            res += '\n' if options['print'] else ""
                        else:
                            res += re.sub(pattern, replacement, line, count=1).strip() if options['print'] else ""
                            res += '\n' if options['print'] else ""
                    else:
                        res += line.strip() if options['print'] else ""
                        res += '\n' if options['print'] else ""                  
        else:
            for line in inp:
                lines += 1
                if lines == int(line_num):
                    if re.search(rf'{pattern}', line):
                        if glo:
                            res += re.sub(pattern, replacement, line).strip() if options['print'] else ""
                            res += '\n' if options['print'] else ""
                        else:
                            res += re.sub(pattern, replacement, line, count=1).strip() if options['print'] else ""
                            res += '\n' if options['print'] else ""
                else:
                    res += line.strip() if options['print'] else ""
                    res += '\n' if options['print'] else ""
    return res
if __name__ == "__main__":
    main()