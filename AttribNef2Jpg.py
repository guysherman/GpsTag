#! /usr/bin/env python

import argparse
import os
import re
import subprocess


def processJpgs(path):
	files = os.listdir(path)
	jpgRegex = re.compile(r"^(.*?)\.jpg$", re.IGNORECASE)
	for f in files:
		match = jpgRegex.match(f)
		if match != None:
			jpgFileName = path + '/' + match.group(0)
			nefFileName = path + '/' + match.group(1) + '.NEF'
			syncCommand = 'touch -r ' + nefFileName + ' ' + jpgFileName
			result = subprocess.call(syncCommand, shell=True)
			if result == 0:
				print 'Updated file: ' + jpgFileName
			else:
				print 'Failed to update file: ' + jpgFileName


def main():
    parser = argparse.ArgumentParser(description='Replace filesystem ' \
	+ ' attributes on jpgs, from NEFs with the same name')
    parser.add_argument('directory', nargs='+', help='Path to a directory ' \
	+ 'containing the NEF and JPG files to sync.')
    args = parser.parse_args()
    for path in args.directory:
        processJpgs(path)
    return 0

if __name__ == "__main__":
    main()
