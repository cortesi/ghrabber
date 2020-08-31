#!/usr/bin/env python
import argparse
import os.path
import urllib

from bs4 import BeautifulSoup
import requests

# Offset of path component to delete when converting to raw
REM_OFFSET = 2
RAWBASE = "https://raw.github.com/"
SEARCH = "https://github.com/search"


def extract(data):
    s = BeautifulSoup.BeautifulSoup(data)
    for i in s.findAll("p", {"class": "title"}):
        p = i.findAll("a")
        # The second link is the reference...
        yield p[1].get("href")


def is_last_page(data):
    s = BeautifulSoup.BeautifulSoup(data)
    if s.find("p", {"class": "title"}):
        return False
    else:
        return True


def raw_url(p):
    p = p.strip("/")
    parts = p.split("/")
    del parts[REM_OFFSET]
    return RAWBASE + "/".join(parts)


def make_fname(p):
    p = p.strip("/")
    parts = p.split("/")
    return parts[0] + "." + parts[1]


def get(query, relative, outdir, listonly=False):
    page = 1
    while 1:
        params = dict(
            q = query,
            type = "Code",
            p = page
        )
        r = requests.get(SEARCH, params=params)
        if is_last_page(r.content):
            print("** No more results")
            break
        for u in extract(r.content):
            ru = raw_url(u)
            if relative:
                ru = urllib.basejoin(ru, relative)
            if listonly:
                print(ru)
            else:
                fn = make_fname(u)
                outpath = os.path.join(outdir, fn)
                if os.path.exists(outpath):
                    print("Skipping ", fn)
                else:
                    ret = requests.get(ru)
                    if ret.status_code == 200:
                        print("Fetching ", ru)
                        f = open(outpath, "w")
                        f.write(ret.content)
                        f.close()
                    else:
                        print("Error", fn, ret.status_code)
        page += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", action="store_true",
        help="Just list results"
    )
    parser.add_argument(
        "-o", type=str, default=".",
        help="Output directory. Created if it doesn't exist."
    )
    parser.add_argument(
        "-r", type=str, default=None,
        help="Grab a path relative to the match"
    )
    parser.add_argument("query", type=str, help="Github Code Search query")
    args = parser.parse_args()
    if not os.path.exists(args.o):
        os.makedirs(args.o)
    try:
        get(args.query, args.r, args.o, listonly=args.l)
    except KeyboardInterrupt:
        pass
