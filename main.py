"""Entry program for make.fun bounty news-image-20261126.

Copies the image shipped beside this file to the output directory
as entry.png. Runs on Python 3.13, standard library only, with no
network access. The output path comes from MAKEFUN_OUTPUT_DIR when
set (local runs), otherwise /output (the grader sandbox).
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# The copy is byte-for-byte identical on every run: the same source
# file is copied to the same destination, so repeated runs agree.
OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")
