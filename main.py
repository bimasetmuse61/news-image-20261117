# news-image-20261117: sum up the world news of Tuesday 17 November 2026 in one image.
#
# The image is the entry.png beside this file: a newspaper front page for
# "THE WORLD — TUESDAY 17 NOVEMBER 2026". Its lead story is Ukraine striking
# the Crimea Bridge again while Russia hit Kyiv's bridges; below it, tankers
# hit near the Strait of Hormuz, the Xi–Trump–Putin meeting set for Shenzhen,
# Japan scrambling jets, the Pentagon failing its audit for a ninth year, and
# the UK sanctioning Israeli settlement builders.
#
# Standard library only, no network, no randomness: copy the image to
# /output/entry.png (or $MAKEFUN_OUTPUT_DIR when set), byte for byte, so both
# runs of this program write identical bytes.

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The image is 1024 by 683 pixels and under 1 MiB, inside the gate's limits.
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
