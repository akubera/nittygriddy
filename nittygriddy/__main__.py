
from __future__ import print_function

import sys
import logging

from .parser import create_parser


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = create_parser().parse_args(argv)

    try:
        args.op(args)
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        if args.verbose:
            raise
        else:
            sys.exit("{0}: {1}".format(e.__class__.__name__, e))


if __name__ == "__main__":
    main()


