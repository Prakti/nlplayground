# NLPlayground

## Running Tests
* perform an editable install of the package using `pip install -e .`
  * This basically symlinks `nlplayground` into your library path
  * But you can still develop the lib because it is just a symlink
  * Since it's on your library path the test modules will find it
* Run `pytest`
