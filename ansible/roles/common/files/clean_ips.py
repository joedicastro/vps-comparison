#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Clean IPs.

Try to remove all of the IPs of a given file and replace them by a mask.

It's useful to put online logs without revealing a sensitive information of a
server/network like real public IPs.

It works both with IPv4 and IPv6 addresses.  Currently, because of the
use of general regular expressions it would match more than real IPs
like package and kernel version numbers, but it's still very useful
for its original intended purpose without need to write specific regular
expressions per file.

"""

__author__ = "joe di castro <joe@joedicastro.com>"
__license__ = "MIT"
__date__ = "2017-04-14"
__version__ = "0.1"


import os
import re
from argparse import ArgumentParser
from ipaddress import ip_address


def arguments():
    """Defines the command line arguments for the script."""
    main_desc = """Try to replace all of the public IPs of a file by a mask."""

    parser = ArgumentParser(description=main_desc)
    parser.add_argument("-p", "--path", default=".",
                        help="the directory tree where the file(s) are. "
                        "Default: the current one. ")
    parser.add_argument("file", help="the file name to process.")
    parser.add_argument("-v", "--version", action="version",
                        version="%(prog)s {0}".format(__version__),
                        help="show program's version number and exit")
    return parser


def valid_and_public_ip_address(ip):
    """Return true if the IP is valid and public.

    It works both with IPv4 and IPv6 addresses.

    :ip: the IP to validate
    """
    try:
        return ip_address(ip).is_global
    except ValueError:
        return False


def replace_ip(matchobj):
    """Return the right string to replace the IP within a re.sub() method.

    :matchobj: a match object from the sub() method.
    """
    pre, pos = matchobj.group("pre"), matchobj.group("pos")
    ip = matchobj.group("ip")
    public = valid_and_public_ip_address(ip)
    mask = "x.x.x.x" if public and ip_address(ip).version == 4 else "::x"
    return "{0}{1}{2}".format(pre, mask if public else ip, pos)


def main():
    ipv4_regex = re.compile(
        r"""
        (?P<pre>\s)          # try to avoid to match version numbers
        (?P<ip>
        \d{1,3}\.
        \d{1,3}\.
        \d{1,3}\.
        \d{1,3}
        )
        (?P<pos>[:|\s|\n])  # try to avoid to match version numbers
        """,
        re.IGNORECASE | re.VERBOSE)

    # based in http://stackoverflow.com/a/319293/634816
    ipv6_regex = re.compile(
        r"""
        (?P<pre>)                   # Only needed to use just one replace_ip()
        (?P<ip>                     # Only needed to use just one replace_ip()
        (?!.*::.*::)                # Only a single whildcard allowed
        (?:(?!:)|:(?=:))            # Colon iff it would be part of a wildcard
        (?:                         # Repeat 6 times:
            [0-9a-f]{0,4}           #   A group of at most 4 hexadecimal digits
            (?:(?<=::)|(?<!::):)    #   Colon unless preceeded by wildcard
        ){6}                        #
        (?:                         # Either
            [0-9a-f]{0,4}           #   Another group
            (?:(?<=::)|(?<!::):)    #   Colon unless preceeded by wildcard
            [0-9a-f]{0,4}           #   Last group
            (?: (?<=::)             #   Colon iff preceeded by exacly one colon
             |  (?<!:)              #
             |  (?<=:) (?<!::) :    #
             )                      # OR
         |                          #   A v4 address with NO leading zeros
            (?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)
            (?: \.
                (?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)
            ){3}
        ))
        (?P<pos>)                  # Only needed to use just one replace_ip()
        """,
        re.VERBOSE | re.IGNORECASE | re.MULTILINE)

    args = arguments().parse_args()

    for root, dirs, files in os.walk(args.path):
        for f in files:
            if f == args.file:
                log_file = os.path.abspath(os.path.join(root, f))
                print(log_file)

                with open(log_file, mode="r") as file_input:
                    file_content = file_input.read()

                file_content = ipv4_regex.sub(replace_ip, file_content)
                file_content = ipv6_regex.sub(replace_ip, file_content)

                with open(log_file, mode="w") as file_output:
                    file_output.write(file_content)


if __name__ == '__main__':
    main()
