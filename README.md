## RapidFuzz C-API

[![Continous Integration](https://github.com/maxbachmann/rapidfuzz_capi/workflows/Build/badge.svg)](https://github.com/maxbachmann/rapidfuzz_capi/actions)
[![GitHub License](https://img.shields.io/github/license/maxbachmann/rapidfuzz_capi)](https://github.com/maxbachmann/rapidfuzz_capi/blob/main/LICENSE)


> :warning: Historically the C-API for RapidFuzz was published separate from RapidFuzz. THe reason for this was that RapidFuzz would require a C++ compiler to
> build successfully. Now that RapidFuzz provides a pure Python fallback this problem no longer exists. For this reason the C-API is now integrated directly into
> RapidFuzz which is easier for users to understand. Users should transition to the version integated into RapidFuzz.

## About

This package provides the C-API of RapidFuzz. It can be used inside the `pyproject.toml` to compile and extension module extending RapidFuzz. Providing this C-API in a separate package simplifies the build process. It allows the usage on platforms which are not supported by RapidFuzz, or for which RapidFuzz does not provide wheels (e.g. because they are not officially supported by numpy). Us this as:

```toml
[build-system]
requires = ["setuptools", "rapidfuzz_capi==1.0.5"]
```

Similar to numpy the include path can be found in the following way:
```python
import rapidfuzz_capi
rapidfuzz_capi.get_include()
```
