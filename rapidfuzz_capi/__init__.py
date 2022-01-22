__author__ = "Max Bachmann"
__license__ = "MIT"
__version__ = "1.0.3"

def get_include():
    """
    Return the directory that contains the RapidFuzz \\*.h header files.
    Extension modules that need to compile against RapidFuzz should use this
    function to locate the appropriate include directory.

    Notes
    -----
    When using ``distutils``, for example in ``setup.py``.
    ::
        import rapidfuzz_capi
        ...
        Extension('extension_name', ...
                include_dirs=[rapidfuzz_capi.get_include()])
        ...
    """
    import os
    return os.path.dirname(__file__)