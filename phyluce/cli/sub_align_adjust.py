#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2013 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 28 December 2013 15:12 PST (-0800)
"""


from __future__ import absolute_import

from phyluce.align import adjust
from phyluce.common import is_dir, is_file, FullPaths, CreateDir


descr = "Adjust a set of alignment files by adding missing taxa."


def configure_parser(sub_parsers):
    sp = sub_parsers.add_parser(
        "adjust",
        description=descr,
        help=descr,
    )

    sp.add_argument(
        '--alignments',
        required=True,
        type=is_dir,
        action=FullPaths,
        help="Alignment files to process"
    )
    sp.add_argument(
        "--output",
        required=True,
        action=CreateDir,
        help="The output dir in which to store copies of the alignments"
    )
    sp.add_argument(
        '--match-count-output',
        required=True,
        action=FullPaths,
        type=is_file,
        help="The output file containing taxa and loci in complete/incomplete "
             "matrices generated by get_match_counts.py."
    )
    sp.add_argument(
        '--incomplete-matrix',
        required=True,
        action=FullPaths,
        type=is_file,
        help="The output file for incomplete-matrix records generated by "
             "`phyluce fetch uce-count`."
        )
    sp.add_argument(
        '--min-taxa',
        help="The minimum number of taxa to keep",
        default=3,
        type=int
    )
    sp.add_argument(
        '--verbatim',
        action="store_true",
        default=False,
        help="Do not parse species names at all - use them verbatim",
    )
    sp.add_argument(
        "--input-format",
        choices=["fasta", "nexus", "phylip", "clustal", "emboss", "stockholm"],
        default="nexus",
        help="The input alignment format.",
    )
    sp.add_argument(
        "--output-format",
        choices=["fasta", "nexus", "phylip", "clustal", "emboss", "stockholm"],
        default="nexus",
        help="The output alignment format.",
    )
    sp.add_argument(
        "--cores",
        type=int,
        default=1,
        help="Process alignments in parallel using --cores for alignment. "
             "This is the number of PHYSICAL CPUs."
    )
    sp.add_argument(
        "--verbosity",
        type=str,
        choices=["INFO", "WARN", "CRITICAL"],
        default="INFO",
        help="""The logging level to use."""
    )
    sp.add_argument(
        "--log-path",
        action=FullPaths,
        type=is_dir,
        default=None,
        help="The path to a directory to hold logs."
    )

    sp.set_defaults(func=adjust_alignments)


def adjust_alignments(args, parser):
    adjust.main(args, parser)
