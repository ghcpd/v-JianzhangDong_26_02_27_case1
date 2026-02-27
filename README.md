# Order Analytics Service

## Configuration

This project uses YAML configuration files to control runtime behavior:

- `config.yaml` - **production** configuration (default).
- `config.dev.yaml` - **development** configuration.

The service selects the config file based on the `ENV` environment variable:

- `ENV=dev` → uses `config.dev.yaml`
- otherwise → uses `config.yaml`

You can also explicitly specify a config file when starting the service:

```bash
python run.py --config config.dev.yaml
```

## Running

### Run normally (prod config)

```bash
python run.py
```

### Run in development mode (dev config)

On **Unix/macOS**:

```bash
./dev_start.sh
```

On **Windows (PowerShell)**:

```powershell
./dev_start.ps1
```

Cross-platform:

```bash
python dev_start.py
```

## Dependencies

Install runtime dependencies:

```bash
pip install -r requirements.txt
```

(Optional) for development / testing, install:

```bash
pip install -r requirements-dev.txt
```

## Tests

Run the full test suite with:

```bash
python -m pytest
```
