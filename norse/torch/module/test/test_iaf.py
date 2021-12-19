import torch

from norse.torch.functional.iaf import IAFFeedForwardState, iaf_feed_forward_step
from norse.torch.module.iaf import IAFCell


def test_iaf_cell_feed_forward_step_batch():
    x = torch.ones(2, 1)
    s = IAFFeedForwardState(v=torch.zeros(2, 1))

    z, s = IAFCell()(x, s)
    assert z.shape == (2, 1)
    assert torch.all(torch.eq(s.v, x))


def test_iaf_cell_backward():
    x = torch.ones(2, 1)

    z, _ = IAFCell()(x)
    z.sum().backward()
    z.grad
