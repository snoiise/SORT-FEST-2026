# Sort Fest 2026 — Benchmark

This directory contains the official Sort Fest benchmarking system.

## How It Works

Every submission goes through the same compilation and benchmarking process.

```text
Submission
    ↓
Nim compiler
    ↓
Generated C
    ↓
GCC
    ↓
Benchmark executable
    ↓
Benchmark
    ↓
Results
```

The benchmark tests every submission using the same hardware, compiler configuration, test data, and benchmark conditions.

## Compilation

Submissions are written in **Nim**.

The official benchmark currently uses:

```text
Nim: 2.2.12
GCC: 14.2.0
Architecture: amd64
```

The Nim compiler converts the submitted code into C. The generated C is then compiled using GCC alongside the benchmark and required Nim runtime code.

## Benchmark Machine

Official results are produced on:

```text
CPU: AMD Ryzen 5 4500
Cores: 6
Threads: 12
RAM: 16 GB
OS: Windows 11 Home 64-bit
```

All official submissions are benchmarked on the same machine.

## Test Data

Submissions are tested against the same datasets.

Current scenarios include:

* Random
* Sorted
* Reversed
* Duplicates
* Nearly sorted

Each scenario is tested using multiple input sizes:

```text
1,000
10,000
100,000
1,000,000
```

## Timing

The benchmark measures the time taken by each submission to sort each test dataset.

The exact timing and result-processing method is defined by the benchmark code provided in this directory.

## Correctness

A submission must correctly sort the input.

After each test, the benchmark verifies the resulting data.

Incorrect results are recorded as failed tests and do not produce a valid performance result.

## Results

Benchmark results are written to:

```text
results.csv
```

The results contain the algorithm, author, test scenario, input size, execution time, and res
