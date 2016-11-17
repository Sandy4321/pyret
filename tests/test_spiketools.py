"""
Tests functions in the spiketools module
"""
import numpy as np
import pyret.spiketools as spk


def test_binspikes():

    # assert the proper indices are returned
    spike_times = [1.0, 2.0, 2.5, 3.0]
    dt = 0.01
    bin_edges = np.arange(0, 3, dt)
    bspk = spk.binspikes(spike_times, bin_edges)
    assert np.allclose(np.where(bspk)[0], [100, 200, 250, 299])

    # maximum absolute error is dt
    binned_times = bin_edges[np.where(bspk)]
    assert np.all(np.abs(binned_times - spike_times) <= dt)

    # test for no spikes
    assert np.allclose(spk.binspikes([], bin_edges), np.zeros_like(bin_edges))


def test_estfr():

    T = 100
    dt = 1e-2

    # test an empty array
    bspk = np.zeros(T,)
    time = np.arange(0, 1, dt)
    fr = spk.estfr(bspk, time, sigma=0.01)
    assert np.allclose(fr, bspk)

    # test a single spike
    bspk[T // 2] = 1.
    fr = spk.estfr(bspk, time, sigma=0.01)
    assert (fr.sum() * dt) == bspk.sum()


def test_detectevents():
    pass


def test_peakdet():
    pass


def test_split_trials():
    pass


def test_SpikingEvent():
    pass
