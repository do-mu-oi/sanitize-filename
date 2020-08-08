#!/usr/bin/env python

import re
import csv
import pathlib
import argparse

# defaults
EXPRESSION = r"[/?<>\\:*|\"]"
REPLACEMENT = "_"

# argparse
parser = argparse.ArgumentParser()
parser.add_argument("directory", help="target directory")
parser.add_argument("--expression", "-e", help="regular expression pattern (default: {})".format(EXPRESSION), default=EXPRESSION)
parser.add_argument("--replacement", "-r", help="replacement string (default: {})".format(REPLACEMENT), default=REPLACEMENT)
parser.add_argument("--test", "-t", help="do not make any changes", action="store_true")
parser.add_argument("--log", "-l", help="CSV log file name")
args = parser.parse_args()

# pathlib
pathlib_path = pathlib.Path(args.directory)

# lists
targets = []
log = []

for path in pathlib_path.glob("**/*"):
    if re.search(args.expression, path.name):
        targets.append({
            "depth": len(path.parts),
            "path": path,
        })

if not len(targets) > 0:
    print("There are no files to be renamed.")
    quit(0)

# Process from deep files
targets.sort(key=lambda x: x["depth"], reverse=True)

for target in targets:
    path = target["path"]
    new_name = re.sub(args.expression, args.replacement, path.name)
    new_path = path.parent.joinpath(new_name)

    if new_path.exists():
        status = "ignore (file already exists.)"
    else:
        status = "rename"
        if not args.test:
            path.rename(new_path)

    log.append({
        "source": str(path),
        "dest": new_name,
        "status": status,
    })

    print("{}\n=> {} [{}]".format(str(path), new_name, status))

if args.log:
    with open(args.log, "w", encoding="utf8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=log[0].keys())
        writer.writeheader()
        writer.writerows(log)