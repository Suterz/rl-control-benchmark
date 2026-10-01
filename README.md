# rl-control-benchmark

A reinforcement-learning control benchmark comparing PID, PPO, and SAC controllers
on the same continuous-control dynamical system.

The benchmark will investigate:

- Tracking performance
- Control effort
- Robustness to changing system dynamics
- Constraint violations
- RL sample efficiency

Currently, this repository contains only Python project infrastructure. The
physical system, Gymnasium environment, controllers, training, and evaluation are
not implemented yet.

## Installation

Requires Python 3.12 and [uv](https://docs.astral.sh/uv/). Install uv using the
official installer if needed:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your shell or follow the installer's PATH instructions, then run from the
repository root:

```sh
uv sync
```

uv manages Python 3.12, the local `.venv`, and dependencies from `uv.lock`.
Development dependencies are included by default.

## Development checks

```sh
uv run pytest
uv run ruff check .
uv run mypy src
```

The package lives in `src/rl_control/`, and tests live in `tests/`. The project is
installed in editable mode by `uv sync`; no manual `PYTHONPATH` setup is needed.
Generated training outputs, checkpoints, and logs are excluded from Git.
