#!/usr/bin/env python3
"""Generator stranica kurikuluma IOAI (IOAI/). Koristi zajednički generator
tools/matematika/build.py s manifestom tools/ioai/manifest.json.

Pokretanje:  python3 tools/ioai/build.py [oblast ...]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'matematika'))

from build import main  # noqa: E402

if __name__ == '__main__':
    main(['--manifest', os.path.join(HERE, 'manifest.json')] + sys.argv[1:])
