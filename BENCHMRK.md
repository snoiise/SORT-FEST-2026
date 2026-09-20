# Sort Fest 2026 — Benchmark

This contains the official Sort Fest benchmarking system.

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

Scenarios include:

* Random
* Sorted
* Reversed
* Duplicates
* Nearly sorted

Each scenario is tested using multiple input sizes:

```text
1,000
5,000
10,000
25,000
50,000
100,000
250,000
500,000
1,000,000
2,000,000
5,000,000
10,000,000
```

## Timing

Each test is run multiple times to reduce the effect of normal timing variation.

The current benchmark uses **3 runs per test**, with the results averaged to produce the reported time.

Benchmarking is intended to provide a consistent comparison between submissions, not laboratory-grade measurements. Sort Fest is a small competition, so minor variation caused by the operating system, CPU, or other background activity is expected.

The benchmark is designed to make those differences reasonably small while keeping the system simple.

## Returning Unsorted Output

A submission must correctly sort the input.

After each test, the benchmark verifies the resulting data.

Incorrect results are recorded as failed tests and do not produce a valid performance result.

## Results

Benchmark results are written to:

```text
results.csv
```

The results contain the algorithm, author, test scenario, input size, execution time, and result status.

Example:

```text
algorithm,author,scenario,size,time,result
Custom Sort,Sort Fest,random,1000000,0.552000000,OK
```

## Benchmark Code

The complete benchmark source is provided in this repo.

The benchmark code is the source of truth for the exact compilation, testing, timing, validation, and result-generation process used by Sort Fest.
