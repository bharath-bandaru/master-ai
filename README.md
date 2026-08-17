# master-ai

Relearning AI/ML from the ground up — gradient descent, backprop, and building neural nets from scratch.

## How I started

1. Watched [3Blue1Brown's neural network videos](https://www.3blue1brown.com/topics/neural-networks) (parts 1–3) for intuition
2. Following [Andrej Karpathy's Zero to Hero](https://karpathy.ai/zero-to-hero.html) series, building everything by hand

## Projects

| Folder | What it is |
|---|---|
| `0-mnist/` | Backprop from scratch (NumPy) on MNIST — honestly not the clearest starting point |
| `1-micrograd/` | Karpathy's micrograd: a tiny autograd engine built up from scalars — **the perfect place to start** |
| `2-build-makemore/` | makemore: character-level language modeling, starting with bigrams |

## Supporting folders

- `docs/` — my learning notes, one file per concept (`docs/setups/` for environment guides)
- `books/`, `papers/`, `references/` — reading material (Nielsen's book, papers, reference code)

## Setup

Managed with [uv](https://docs.astral.sh/uv/) on Python 3.13 — see `docs/setups/uv_guide.md`.

```bash
uv sync          # recreate the environment
uv run jupyter lab
```
