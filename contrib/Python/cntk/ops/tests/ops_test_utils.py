# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root 
# for full license information.
# ==============================================================================

"""
Utils for operations unit tests
"""

import numpy as np
import pytest
from ...context import get_new_context
from ...graph import *
from ...reader import *

#Keeping things short
C = constant
I = input
AA = np.asarray

@pytest.fixture(params=[-1,0])
def cpu_gpu(request):
    return request.param

def test_helper(root_node, expected, device_id = -1, clean_up=True, backward_pass = False, input_node = None):
    with get_new_context() as ctx:
        ctx.clean_up = clean_up
        ctx.device_id = device_id
        assert not ctx.input_nodes
        result = ctx.eval(root_node, None, backward_pass, input_node)

        assert len(result) == len(expected)
        for res, exp in zip(result, expected):  
            assert np.allclose(res, exp)
            assert res.shape == AA(exp).shape