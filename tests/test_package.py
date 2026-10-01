"""Smoke tests for the installed package."""

import rl_control


def test_package_import() -> None:
    """The src-layout package can be imported from the installed project."""
    assert rl_control.__name__ == "rl_control"
