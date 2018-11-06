#!/usr/bin/env python
# coding=utf-8

import sys
import os
import puraya
import syslogger

if __name__ == '__main__':
    source_path_list = sys.argv[1:]
    if not len(source_path_list):
        print('Source directories not specified')
        exit(2)

    sys.stdout.write('Where to copy files to? ')
    sys.stdout.flush()
    destination_path = sys.stdin.readline().strip()

    if destination_path == '' or not os.path.isdir(destination_path):
        print("Destination directory %s not found" % destination_path)
        exit(1)

    puraya.flat_copy(
        [os.path.join(src, '') for src in source_path_list],
        os.path.join(destination_path, ''),
        syslogger.SysLogger()
    )

    sys.stdout.write("\n\nPress ENTER to exit.")
    sys.stdout.flush()
    sys.stdin.readline()
