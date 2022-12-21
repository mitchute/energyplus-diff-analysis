Command Line Interface
======================

This library comes with a command line interface.
Once this library is pip installed, a new binary executable will be available with the name ``eplus-diff``.
The command has a help argument with output similar to this (execute manually to verify latest syntax)::

  $ eplus-diff --help
  Usage: eplus-diff [OPTIONS] BASELINE_CSV MODIFIED_CSV OUTPUT_DIR

  Options:
    -p, --plot-all-series  Plot all series including series without diffs
    -a, --create-archive   Create archive of plots afterwards
    --help                 Show this message and exit.
