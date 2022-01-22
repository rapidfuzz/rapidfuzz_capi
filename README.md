## RapidFuzz C-API

[![Continous Integration](https://github.com/maxbachmann/rapidfuzz_capi/workflows/Build/badge.svg)](https://github.com/maxbachmann/rapidfuzz_capi/actions)
[![GitHub License](https://img.shields.io/github/license/maxbachmann/rapidfuzz_capi)](https://github.com/maxbachmann/rapidfuzz_capi/blob/main/LICENSE)

## About

This package provides the C-API of RapidFuzz. It can be used inside the `pyproject.toml` to compile and extension module extending RapidFuzz. Providing this C-API in a separate package simplifies the build process. It allows the usage on platforms which are not supported by RapidFuzz, or for which RapidFuzz does not provide wheels (e.g. because they are not officially supported by numpy). Us this as:

```toml
[build-system]
requires = ["wheel", "setuptools", "rapidfuzz_capi==1.0.3"]
```

Similar to numpy the include path can be found in the following way:
```python
import rapidfuzz_capi
rapidfuzz_capi.get_include()
```
