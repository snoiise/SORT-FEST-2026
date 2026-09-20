# Rules

## 1. The Goal

Write a sorting algorithm in **Nim** and make it the best in your category.

Submissions are tested using the official Sort Fest benchmark and ranked using the resulting benchmark data.

## 2. Language

* Submissions must be written in **Nim**.
* The official Nim version and compiler configuration will be used for all submissions.
* Submissions must provide a `sort` procedure matching the required submission format.

## 3. Benchmarking

Every valid submission goes through the same compilation and benchmarking process.

```text
Nim source -> Nim compiler -> Generated C -> GCC -> Official benchmark -> Results
```

The benchmark uses the same hardware, compiler configuration, datasets, and test conditions for every submission.

## 4. Correctness

A submission must correctly sort every dataset it is tested against.

A submission that produces an incorrect result fails that benchmark.

A submission must not:

* Modify the benchmark itself
* Modify another submission
* Depend on another submission
* Return incorrect results intentionally
* Skip sorting the input

## 5. Performance

The benchmark measures the execution time of each submission across multiple input sizes and dataset types.

The benchmark currently includes:

* Random data
* Sorted data
* Reversed data
* Duplicate-heavy data
* Nearly sorted data

Results are recorded for each tested input size.

## 6. Categories

Sort Fest has eight categories:

* 🏆 **Overall**
* ⚡ **Random**
* 🧱 **Adversarial**
* 🧠 **Adaptive**
* 💾 **Lowest Memory**
* 🔢 **Integer Specialist**
* 🖥️ **Single-threaded**
* 🚀 **Multithreaded**

Each category uses the official benchmark results relevant to that category.

## 7. Hardware

All official results are produced on the same benchmark machine.

Results from personal computers are not used for the official leaderboard.

## 8. Timeouts

Submissions that take longer than the official time limit for a benchmark are considered timed out for that test.

The exact timeout will be defined by the official benchmark configuration.

## 9. Memory

Memory usage may be measured during benchmarking.

Submissions must not deliberately allocate excessive memory or attempt to interfere with the benchmark's memory measurements.

## 10. Submission Changes

A submission may be updated before the competition's submission deadline.

After the deadline, submissions are locked and the final benchmark is run.

## 11. Disqualification

A submission may be rejected or disqualified if it:

* Does not follow the submission format
* Does not compile
* Produces incorrect results
* Attempts to manipulate the benchmark
* Attempts to gain an unfair advantage through the benchmark environment
* Violates the competition rules

## 12. Final Results

The official leaderboard is determined by the results produced by the final benchmark run.

The benchmark results published by Sort Fest are the official results for the competition.

---

**Sort Fest 2026**
