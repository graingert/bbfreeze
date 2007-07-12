#! /usr/bin/env python

import os

def main():
    files = [x.strip() for x in os.popen("hg manifest")]
    files.append("README.html")
    
    files.remove("make_manifest.py")
    files.remove(".hgtags")
    files.remove("Makefile")

    files.sort()

    f = open("MANIFEST.in", "w")
    for x in files:
        f.write("include %s\n" % x)
    f.close()


if __name__=='__main__':
    main()
