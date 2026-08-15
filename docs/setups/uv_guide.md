# uv Basics

**What it is:** uv is a modern Python package + project manager (by Astral, written in Rust). One tool that replaces pyenv, pip, virtualenv, and poetry. Same job as Anaconda, but faster, lighter, and per-project instead of central environments.

**Where it's installed:** `~/.local/bin/uv` (via the standalone `curl astral.sh/uv` installer). Update with `uv self update`.

## Mental model

Each project folder gets its own:

| File | Role | Git? |
|---|---|---|
| `pyproject.toml` | Your recipe — Python version + packages you asked for | commit |
| `uv.lock` | Exact pinned versions of everything installed | commit |
| `.venv/` | The actual environment (disposable build product) | git-ignore |

Because every project has its own `.venv`, projects never conflict.

## 1. Start a new project

```bash
mkdir myproject && cd myproject
uv init --python 3.13        # creates pyproject.toml + pins Python version
```

## 2. Add / remove packages (instead of pip install)

```bash
uv add numpy torch           # creates .venv automatically, installs, records in pyproject.toml
uv remove numpy              # uninstall
```

## 3. Run code — two styles, pick one

```bash
uv run python main.py        # no activation needed; always uses the project's .venv
# or the classic way:
source .venv/bin/activate    # then plain `python main.py`; `deactivate` to exit
```

## 4. Recreate the env anywhere (new machine, after git clone)

```bash
uv sync                      # rebuilds .venv exactly from pyproject.toml + uv.lock
```

## 5. Manage Python versions

```bash
uv python list               # see installed/available versions
uv python install 3.12       # grab another version
```

## This repo (master-ai)

- Pinned to uv-managed Python 3.13.12 (`.python-version`)
- Installed: numpy, pandas, matplotlib, scikit-learn, jupyter, torch, torchvision
- PyTorch runs on the Apple GPU (MPS backend)
- To add anything new: `uv add <package>` from the repo root
