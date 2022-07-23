import argparse
import logging
import os
import sys

APP_NAME = 'CHANGE_ME'

BANNER = f"""\
===============================
{APP_NAME} starting up...
===============================
"""

# Define needed options here with default values or None
OPTIONS = {
    'option_one': None,
    'option_two': '/path/to/file',
}

def parse_args():
    parser = argparse.ArgumentParser()
    for option in OPTIONS:
        parser.add_argument(
            f'--{option}',
            dest=option
        )

    return parser.parse_args()

if __name__ == '__main__':
    # First, check environment
    for key in OPTIONS:
        OPTIONS[key] = os.environ.get(key.upper(), OPTIONS[key])

    # Command line override
    args = vars(parse_args())
    for key in args:
        if key not in OPTIONS:
            continue
        if key in args and args[key]:
            OPTIONS[key] = args[key]

    sys.stderr.write(BANNER + '\n')

    # Check for completeness
    fail = False
    for key in OPTIONS:
        if not OPTIONS[key]:
            sys.stderr.write(f"ERROR: {key} is not set. Launch will be aborted.\n")
            fail = True
    if fail:
        sys.exit(1)

    sys.stderr.write("Using the following options:\n")
    for key in OPTIONS:
        if 'pass' or 'key' in key:
            logline = f"\t{key} set to {OPTIONS[key][0] + ('*' * (len(OPTIONS[key])-2)) + OPTIONS[key][-1]}"
        else:
            logline = f"\t{key} set to {OPTIONS[key]}"
        sys.stderr.write(logline + '\n')

    sys.stderr.flush()

    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.getLogger('urllib3').setLevel(logging.INFO)

    # More code here
