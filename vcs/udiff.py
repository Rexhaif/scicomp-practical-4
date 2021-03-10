from difflib import unified_diff
from argparse import Namespace, ArgumentParser
from pathlib import Path
from datetime import datetime

import sys

if __name__ == '__main__':
    parser = ArgumentParser("udiff.py", description='Unified diff in python')
    parser.add_argument('file1', type=str, help='First file')
    parser.add_argument('file2', type=str, help='Second file')

    args = parser.parse_args()
    file1 = Path(args.file1)
    file2 = Path(args.file2)

    with open(file1, 'r', encoding='utf-8') as f:
        lines1 = f.readlines()

    with open(file2, 'r', encoding='utf-8') as f:
        lines2 = f.readlines()

    udiff_generator = unified_diff(
        lines1,
        lines2,
        fromfile=args.file1,
        tofile=args.file2,
        fromfiledate=datetime.fromtimestamp(file1.stat().st_mtime).isoformat(),
        tofiledate=datetime.fromtimestamp(file1.stat().st_mtime).isoformat()
    )

    sys.stdout.writelines(udiff_generator)
