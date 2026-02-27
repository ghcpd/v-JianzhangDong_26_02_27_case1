# Order Analytics Service

This repository implements a simple service that processes order data. The
project is intentionally lightweight to demonstrate maintenance and
cross-platform compatibility.

---

## Configuration

Configuration is stored in YAML files at the repository root:

* `config.yaml` – production settings (`env: prod`, `threshold: 1000`).
* `config.dev.yaml` – development settings (`env: dev`, `threshold: 500`).

The service chooses which file to load based on the `ENV` environment
variable. The variable defaults to `prod` if unset.  Use one of the helper
scripts below to set the variable automatically.

## Running the Service

Two convenience scripts are included:

* **Unix/macOS**: `dev_start.sh`
* **Windows**: `dev_start.bat`

Both set `ENV=dev` and then invoke `python run.py` so that the development
configuration is used.  You can also run the service manually and specify a
different configuration by setting `ENV` yourself.

## Dependency Management

Dependencies are defined in `pyproject.toml` under `[project.dependencies]`.
A light `requirements.txt` mirrors the runtime requirements for users who
prefer the traditional `pip install -r requirements.txt` workflow.  Development
and test packages (`pytest`, `requests`) live under `pyproject.toml`
`[project.optional-dependencies]` (install with `pip install .[dev]`).

## Tests and Logging

Unit tests reside in the `tests/` directory and cover core business logic.
To run them and capture results:

```powershell
mkdir -p logs
python run_tests.py
```

The helper script `run_tests.py` will create `logs/` if necessary and save a
JUnit-style XML report to `logs/results.xml`.  This makes it easy for CI or
local developers to inspect test outcomes.

---

## Miscellaneous

* `data_migration_tool.py` performs a one‑off JSON transformation; the file
  name was corrected from `data_migration_tool.py.py` during maintenance.
* The `dev_start.bat` script was added to ensure Windows users have a
  working development launcher.

Feel free to explore, extend, or use this project as a starting point for the
order analytics service.