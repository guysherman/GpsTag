#! /usr/local/bin/python

import argparse
import os
import re
import subprocess


def printSubDirectories(path):
    print 'Searching for Geo Directories in: ', path
    subs = os.listdir(path)
    geoFormat = re.compile(r'([NS])(\d+) (\d+) (\d+\.\d+) ([EW])(\d+) (\d+) (\d+\.\d+)')
    jpgFormat = re.compile(r'^.*?\.jpg$', re.IGNORECASE)
    for sub in subs:
        matches = geoFormat.match(sub)
        if matches != None:
            print 'Found: ', sub
            files = os.listdir(path + '/' + sub)
            for imgFile in files:
                fmatch = jpgFormat.match(imgFile)
                if fmatch != None:
                    filePath = getAbsoluteFilePath(path, sub, fmatch.group(0))
                    tagFile(filePath, matches)


def getAbsoluteFilePath(path, sub, imgFile):
    return path + '/' + sub.replace(' ', r'\ ') + '/' + imgFile

def tagFile(filePath, gMatch):
    tagCmd = 'exiftool -GPSLatitudeRef=' + gMatch.group(1) + ' ' + \
     '-GPSLatitude=\"' + gMatch.group(2) + ', ' + gMatch.group(3) + ', ' + gMatch.group(4) + '\" ' + \
     '-GPSLongitudeRef=' + gMatch.group(5) + ' ' + \
     '-GPSLongitude=\"' + gMatch.group(6) + ', ' + gMatch.group(7) + ', ' + gMatch.group(8) + '\" ' + \
     filePath
    tagResult = subprocess.call(tagCmd, shell=True)
    touchCmd = 'touch -r ' + filePath + '_original ' + filePath
    touchResult = 0
    if tagResult == 0:
        touchResult = subprocess.call(touchCmd, shell=True)
    if tagResult + touchResult == 0:
        tidyCmd = 'rm ' + filePath + '_original'
        subprocess.call(tidyCmd, shell=True)


def main():
    parser = argparse.ArgumentParser(description='Tag Photos with GPS ' +
    'Locations by parsing the name of their containing directory.')
    parser.add_argument('directory', nargs='+', help='Path to a directory ' +
    'containing subdirectories named for their geo location.')
    args = parser.parse_args()
    for path in args.directory:
        printSubDirectories(path)
    return 0

if __name__ == "__main__":
    main()
