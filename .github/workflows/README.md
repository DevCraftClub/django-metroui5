# GitHub Actions Workflows

## Test Workflow

The `test.yml` workflow provides comprehensive testing across multiple Python and Django versions.

### Features

- **Matrix Testing**: Tests across Python 3.8-3.13 and Django 3.2-5.4
- **Smart Exclusions**: Automatically excludes incompatible Python/Django combinations
- **Caching**: Efficient dependency caching for faster builds
- **Quality Checks**: Linting, type checking, and test execution
- **Compatibility Testing**: Ensures package can be imported on all supported Python versions

### Jobs

#### 1. Main Test Job (`test`)

- Tests Python 3.8-3.13 with Django 3.2-5.2
- Excludes incompatible combinations (e.g., Python 3.8 with Django 5.x)
- Runs linting and type checking on Python 3.13 + Django 5.2

#### 2. Latest Versions Test (`test-latest`)

- Tests Python 3.11-3.13 with Django 5.2-5.4
- Focuses on cutting-edge compatibility

#### 3. Compatibility Check (`compatibility-check`)

- Verifies package can be imported on all Python versions
- Helps identify import-level compatibility issues

### Excluded Combinations

The workflow automatically excludes these incompatible combinations:

- Python 3.8-3.10 with Django 5.0+
- Python 3.11+ with Django 3.2
- Python 3.11-3.12 with Django 5.4

### Usage

The workflow runs automatically on:

- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

### Dependencies

The workflow installs:

- Specified Django version
- Development dependencies from `pyproject.toml`
- Package in editable mode for testing

### Notes

- Uses `fail-fast: false` to ensure all matrix combinations are tested
- Caches pip dependencies for faster subsequent runs
- Linting and type checking only run on the most recent stable combination
