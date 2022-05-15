# -*- coding: utf-8 -*-
"""
Created on Sat May 14 14:39:42 2022

@author: user
"""

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:  # utf-8-sig is for extinguish txt coding format, but use utf-8 is okay in spyder.
        for line in f:
            lines.append(line.strip())
    print(lines)
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = line
            continue
        elif line == 'Tom':
            person = line
            continue
        if person:
            new.append(person + ':' + line)
    print(new)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output_teacher.txt', lines)

main()