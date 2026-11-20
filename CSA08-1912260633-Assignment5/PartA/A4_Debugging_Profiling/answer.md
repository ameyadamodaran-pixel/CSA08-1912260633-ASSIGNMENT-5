# A4 — Debugging and Profiling Plan (4 marks)

## Debugging
Use print statements temporarily to inspect values, assertions to verify invariants (e.g., PM2.5 is numeric and non-negative), logging with levels for repeatable diagnostics, and `pdb`/IDE debugger to inspect variables and step through failures. Logging is preferable to uncontrolled prints because levels and handlers can be configured.

## Profiling
Use `time.perf_counter()` for elapsed time, `timeit` for repeatable microbenchmarks, and `cProfile` to identify functions consuming the most cumulative time. Profile with representative data and compare before/after optimisation.

## Alternative: print for all debugging
Thousands of print calls add I/O overhead and clutter output; logging can be disabled or filtered by level. Debugger sessions are interactive and do not add permanent instrumentation.
