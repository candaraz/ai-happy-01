"""Copy the entry image to entry.png, byte for byte, every run.

In the grader's container the image goes to /output/entry.png. Outside the
container, MAKEFUN_OUTPUT_DIR stands in for /output, following the kit's
starter convention, so the program can be tested without touching /output.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "image.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
