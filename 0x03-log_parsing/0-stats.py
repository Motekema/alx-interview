#!/usr/bin/python3
import sys
from collections import defaultdict


def print_stats(total_size, status_codes):
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:d}: {:d}".format(code, status_codes[code]))

def parse_line(line):
    parts = line.strip().split()
    if len(parts) < 9:
        return None, None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = parts[-1]
    if status_code.isdigit() and file_size.isdigit():
        return int(status_code), int(file_size)
    return None, None

def main():
    total_size = 0
    status_codes = defaultdict(int)
    try:
        count = 0
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_size += file_size
                status_codes[status_code] += 1
                count += 1
            if count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
