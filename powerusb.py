#!/usr/bin/python

import argparse

import powerusb

"""
pwrusb --list-strips

pwrusb --strip <id> [on|off|reset|status|current|power|clear]

pwrusb --socket <id> [[--default] [(on|off)]]

"""


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Manage PowerUSB power strips")

    parser.add_argument("--config-file", default="~/.powerusbrc")

    target = parser.add_mutually_exclusive_group()

    target.add_argument("--list-strips", action="store_true")
    target.add_argument("--strip", default=None, dest="strip")
    target.add_argument("--socket", default=None)

    format = parser.add_mutually_exclusive_group()
    format.add_argument("--format", choices=['json', 'text', 'xml'], 
                        default="text")
    format.add_argument("--json", const="json",
                        action="store_const", dest="format")
    format.add_argument("--text", const="text",
                        action="store_const", dest="format")
    format.add_argument("--xml", const="xml",
                        action="store_const", dest="format")

    parser.add_argument("--default", action="store_true")
    parser.add_argument("action", nargs="?", choices=['on', 'off'])

    return parser.parse_args()

if __name__ == "__main__":

    opt = parse_arguments()

    if opt.list_strips:
        print "list all power strips"

    elif opt.strip != None:
        print "query or set power strip %s" % opt.strip

    elif opt.socket != None:
        print "query or set power socket %s" % opt.socket


