# pr-fin-calc

## run

```bash
PYTHONPATH=$PYTHONPATH:. uv run pytest
```

## without uv run

```bash
uv sync
. .venv/bin/activate
python -m pytest tests
deactivate
```
