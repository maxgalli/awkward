# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/master/LICENSE

from __future__ import absolute_import

import pytest
import numpy as np
import awkward1 as ak


def test():
    assert ak.to_list(ak.prod(ak.Array([[[2, 3, 5]], [[7], [11]], [[]]]), axis=-1)) == [
        [30],
        [7, 11],
        [1],
    ]

    assert ak.to_list(ak.prod(ak.Array([[[2, 3, 5]], [[7], [11]], []]), axis=-1)) == [
        [30],
        [7, 11],
        [],
    ]
