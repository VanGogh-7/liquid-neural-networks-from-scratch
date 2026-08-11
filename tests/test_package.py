"""Smoke tests for the lnn package — verify import and basic structure."""

import lnn


def test_package_version():
    """The package should report a version."""
    assert lnn.__version__ == "0.1.0"


def test_subpackage_imports():
    """All architecture subpackages should be importable."""
    subpackages = [
        "ode",
        "rnn",
        "neural_ode",
        "ncp",
        "ltc",
        "cfc",
        "ssm",
        "liquid_s4",
        "stc",
        "lrc",
        "lrcu",
        "lrcssm",
    ]
    for name in subpackages:
        mod = __import__(f"lnn.{name}", fromlist=[name])
        assert mod is not None, f"Failed to import lnn.{name}"
