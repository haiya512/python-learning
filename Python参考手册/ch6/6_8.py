# coding: utf-8
import os
import sys
import fnmatch
def find_files(topdir, pattern):
    for path, dirname, filelist in os.walk(topdir):
        for name in filelist:
            if name in filelist:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path.name)
import gzip, bz2
def opener(filenames):
    for name in filenames:
        if name.endswith(".gz"): f = gzip.open(name)
        elif name.endswith(".bz2"): f = bz2.BZ2File(name)
        else: f = open(name)
        yield f
def cat(filelist):
    for f in filelist:
        for line in f:
            yield line
def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line

wwwlogs = find_files("/Users/bobo/gitcenter/python/Python参考手册/ch6", "import*")
files = opener(wwwlogs)
lines = cat(files)
pylines = grep("import", lines)
for line in pylines:
    sys.stdout.write(line)
