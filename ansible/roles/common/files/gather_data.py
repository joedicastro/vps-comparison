#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Gather data from logs.

Gather data from the logs following certain criteria given by a json
file and finally putting the data in org-mode tables in a output file.

"""

__author__ = "joe di castro <joe@joedicastro.com>"
__license__ = "MIT"
__date__ = "2017-04-16"
__version__ = "0.1"


import json
import os
import re
from argparse import ArgumentParser


def arguments():
    """Defines the command line arguments for the script."""
    main_desc = "Gather data from VPS' log files to compare them in tables."

    parser = ArgumentParser(description=main_desc)
    parser.add_argument("-p", "--path", default=".",
                        help="the directory tree where the logs are."
                        "Default: the current one. ")
    parser.add_argument("-j", "--json", default="./criteria.json",
                        help="the json file with the criteria"
                        "Default: ./criteria.json")
    parser.add_argument("-v", "--version", action="version",
                        version="%(prog)s {0}".format(__version__),
                        help="show program's version number and exit")
    return parser


def gather_datum(rules, log_text):
    """Gather datum from log text following a set of given rules.

    :rules: dictionary that contains a set of rules to gather the datum
    "log_text: string containing the text of a log file
    """
    regex = re.compile(rules['regex'], re.DOTALL if rules['dual'] else 0)
    if rules['dual']:
        datum = ', '.join(
            '{0} ({1})'.format(i.group(1), i.group(2))
            for i
            in regex.finditer(log_text)
        )
    elif rules['average']:
        values = [
            (float(i) / pow(10, rules['exp']))
            for i
            in re.findall(regex, log_text)
        ]
        try:
            str_format = '{0:.3f}' if rules['round'] else '{0:.0f}'
            datum = str_format.format(sum(values) / len(values))
        except ZeroDivisionError:
            datum = ''
    else:
        try:
            datum = re.findall(regex, log_text)[rules['idx']]
        except IndexError:
            datum = ''
    return datum


def draw_tables(rules, gathering):
    """Draw org-mode tables from gathered data following a criteria.

    :rules: dictionary with the rules to draw each table
    :gathering: dictionary with all the data gathered
    """
    servers, output, separator = sorted(gathering.keys()), [], '|-'
    for table in rules.keys():
        # title
        output.append(table.upper().replace('_', ' '))
        output.append('=' * 79 + os.linesep)
        # header
        output.append(separator)
        output.append(' | '.join(i.title() for i in ['|'] + servers))
        output.append(separator)
        # rows
        for row in rules[table].keys():
            row_header = '| {0} |'.format(rules[table][row])
            row_cells = ' | '.join(
                gathering[server].get(row, '')
                for server
                in servers
            )
            output.append('{0}{1}'.format(row_header, row_cells))
        # footer
        output.append(separator)
        output.append(os.linesep)
    return os.linesep.join(output)


def main():
    args = arguments().parse_args()

    criteria = json.load(open(args.json))
    criteria_per_log = criteria['criteria_per_log']
    criteria_per_table = criteria['criteria_per_table']

    servers = [i.name for i in os.scandir(args.path) if i.is_dir()]
    gathering = {server: dict() for server in servers}

    for root, dirs, files in os.walk(args.path):
        for fil in files:
            this_server = os.path.basename(os.path.abspath(root))
            log_path = os.path.abspath(os.path.join(root, fil))
            log = os.path.basename(log_path)

            with open(log_path) as log_file:
                log_contents = log_file.read()

            for datum in criteria_per_log.get(log, []):
                gathering[this_server][datum] = gather_datum(
                    criteria_per_log[log][datum],
                    log_contents
                )

    tables = draw_tables(criteria_per_table, gathering)

    with open(os.path.join(args.path, 'tables.org'), 'w') as tables_file:
        tables_file.write(tables)


if __name__ == '__main__':
    main()
