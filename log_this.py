#!/usr/bin/env python
from subprocess import Popen, PIPE
import argparse
from os.path import expanduser, join
from time import time


def issue_command(command):
    process = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
    return process.communicate()

home = expanduser("~")
default_file = join(home, "command_log")

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=argparse.FileType("a"), default=default_file)
parser.add_argument("-p", "--profile", action="store_true")
parser.add_argument("command", nargs=argparse.REMAINDER)
args = parser.parse_args()

if args.profile:
    start = time()
    out, err = issue_command(args.command)
    runtime = time() - start
    entry = "{}\t{}\n".format(" ".join(args.command), runtime)
    args.file.write(entry)
else:
    out, err = issue_command(args.command)
    entry = "{}\n".format(" ".join(args.command))
    args.file.write(entry)

args.file.close()

