#!/usr/bin/env python3

import sys
import re
import csv

def convertTimeToMiliSeconds(time):
    regex_result = re.search(
        r"(\d*.*\d)(\w+)",
        time
    )
    value = regex_result.group(1)
    unit = regex_result.group(2)

    if unit == 'ms':
        multiplier = 1.0
    if unit == 's':
        multiplier = 1000
    if unit == 'µs':
        multiplier = 1/1000
    if unit == 'ks':
        multiplier = 1000000

    return float(value) * multiplier


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SyntaxError("Wrong number of arguments")

    filename = sys.argv[1]
    lines_dirty = []
    lines_clean = []

    with open(filename) as file:
        lines_dirty = [line.rstrip() for line in file]

    header = ['htime', 'haddend', 'hcum', 'vtime', 'vaddend', 'vcum', 'mess']
    hcum = 0
    vcum = 0
    with open(filename+"-csv" ,'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for line in lines_dirty:
            # Filter out all messeages
            if 'Machine started' in line:
                continue
            if '[WARNING]' in line:
                continue
            if '[ERROR]' in line:
                raise UserWarning("[ERROR] spotted, stopping the execution")

            # Remove the timestamp and srouce info
            clean_line = line[28:]

            regex_result = re.search(
                r"\[host:\W+(\d*.\d+\w+)\W+(\d+.\d*\w+|0s|\d+µs)\W+virt:\W+(\d+.\d*\w+)\W+(\d+.\d*\w+|0s|\d+µs)\)\](.*)",
                clean_line
                )

            host_time = regex_result.group(1)
            host_time_addend = regex_result.group(2)
            virtual_time = regex_result.group(3)
            virtual_time_addend = regex_result.group(4)
            messeage = regex_result.group(5)
            hcum = hcum + convertTimeToMiliSeconds(host_time_addend)
            vcum = vcum + convertTimeToMiliSeconds(virtual_time_addend)

            row = [host_time, host_time_addend, hcum, virtual_time, virtual_time_addend, vcum, messeage]
            writer.writerow(row)


    print('-' * 80)
    print(f'CSV Data: {filename}')
    print(f'hcum={round(hcum/1000,2)}s')
    print(f'vcum={round(vcum/1000,2)}s')
    print("Succesfuly exported log to the CSV file")
    print('-' * 80)
