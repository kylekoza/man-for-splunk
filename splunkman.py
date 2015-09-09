#!/usr/local/bin/python

import argparse
import webbrowser

def create_argparse():
    parser = argparse.ArgumentParser(description='Man for Splunk')

    parser.add_argument('command', help='The command')

    return parser

def main(command):
    if command.endswith(".conf"):
        url = "http://docs.splunk.com/Documentation/Splunk/latest/admin/{0}".format(command.translate(None, "."))
    else:
        url = "https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/{0}".format(command)

    webbrowser.open(url)

if __name__ == "__main__":
    parser = create_argparse()
    args = parser.parse_args()
    args = vars(args)

    main(args["command"])
