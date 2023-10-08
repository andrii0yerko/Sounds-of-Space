import os

import numpy as np
from spectral.io import envi, spyfile


# taken from https://github.com/Banus/crism_ml/blob/master/crism_ml/io.py
def _generate_envi_header(lbl_fname):
    """Generate a HDR file from the LBL file when the former is missing."""
    # see: https://github.com/jlaura/crism/blob/master/csas.py
    fbase, _ = os.path.splitext(lbl_fname)

    with open(lbl_fname, "r") as fid:
        for line in fid:
            if "LINES" in line:
                lines = int(line.split("=")[1])
            if "LINE_SAMPLES" in line:
                samples = int(line.split("=")[1])
            if "BANDS" in line:
                bands = int(line.split("=")[1])

    with open(f"{fbase}.hdr", "w") as fid:
        fid.write(
            f"ENVI\nsamples = {samples}\nlines   = {lines}\nbands   = {bands}"
            "\nheader offset = 0\nfile type = ENVI Standard\ndata type = 4\n"
            "interleave = bil\nbyte order = 0"
        )


def read_img(fname):
    """
    _summary_

    Args:
        fname (str): filepath without extension, e.g. "data/t1064_mrrif_05n228_0256_3"
            Both "{fname}.lbl" and "{fname}.img" should exist
    """
    fbase, _ = os.path.splitext(fname)
    try:
        img = envi.open(f"{fbase}.hdr")
    except spyfile.FileNotFoundError:
        _generate_envi_header(f"{fbase}.lbl")
        img = envi.open(f"{fbase}.hdr")
    return img
