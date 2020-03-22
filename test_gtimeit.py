"""Tests for gtimeit package."""

import pytest

from gtimeit.benchmark import *
from gtimeit.perf_tracker import *



def test__benchmark_plot_percent(capsys):
    """First test"""
    bm = Benchmark()
    bm.plot_percent()
    captured = capsys.readouterr()
    assert "Not available" in captured.out
