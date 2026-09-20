# Sort Fest 2026 — Benchmark

This directory contains the official Sort Fest benchmarking system.

## How It Works

Every submission goes through the same compilation and benchmarking process.

```text
Submission
    ↓
Nim source
    ↓
Nim compiler
    ↓
Generated C
    ↓
GCC
    ↓
Benchmark executable
    ↓
5 benchmark runs
    ↓
Average result
```

The benchmark records the performance of every submission under the same conditions.

## Compilation

Submissions are written in **Nim**.

The official benchmark uses:

```text
Nim: 2.2.12
GCC: 14.2.0
Architecture: amd64
```

The Nim compiler converts the submitted code into C. The generated C is then compiled using GCC.

The benchmark itself is compiled together with the generated Nim code and required Nim runtime files.

## Benchmark Machine

Official results are produced on:

```text
CPU: AMD Ryzen 5 4500
Cores: 6
Threads: 12
RAM: 16 GB
OS: Windows 11 Home 64-bit
```

All submissions are tested on the same machine.

## Test Data

Each submission is tested against the same datasets.

Current test scenarios are:

* Random
* Sorted
* Reversed
* Duplicates
* Nearly sorted

Each scenario is tested at multiple input sizes:

```text
1,000
10,000
100,000
1,000,000
```

The datasets are generated consistently so that submissions are tested against equivalent inputs.

## Timing

Each benchmark test is run **5 times**.

The five timings are averaged to produce the official result for that test.

For example:

```text
Run 1    0.552s
Run 2    0.548s
Run 3    0.551s
Run 4    0.556s
Run 5    0.550s
───────────────
Average  0.5514s
```

The average is the value written to the results file.

## Correctness

Performance only counts when the submission correctly sorts the input.

After every test, the benchmark verifies that the resulting array is sorted.

A failed correctness check is recorded as a failed result rather than a valid benchmark time.

## Results

Results are written to:

```text
results.csv
```

The format is:

```text
algorithm,author,scenario,size,time,result
```

Example:

```text
Turbo Sort,Sort Fest,random,1000000,0.552000000,OK
```

## Reproducibility

The benchmark configuration, compiler versions, test sizes, datasets, and benchmark machine are kept consistent for official results.

The benchmark code in this directory is the source of truth for how results are produced.

---

**Sort Fest 2026**
