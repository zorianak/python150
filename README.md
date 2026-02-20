# python150

Local development environment for the [NeetCode 150](https://neetcode.io/practice) problem set in Python.

## Setup

```bash
pip install -r requirements.txt
```

## Structure

Problems are organized by category under `problems/`:

```
problems/
├── arrays_hashing/          (9 problems)
├── two_pointers/            (5 problems)
├── sliding_window/          (6 problems)
├── stack/                   (7 problems)
├── binary_search/           (7 problems)
├── linked_list/             (11 problems)
├── trees/                   (15 problems)
├── tries/                   (3 problems)
├── heap_priority_queue/     (7 problems)
├── backtracking/            (9 problems)
├── graphs/                  (13 problems)
├── advanced_graphs/         (6 problems)
├── one_d_dp/                (12 problems)
├── two_d_dp/                (11 problems)
├── greedy/                  (8 problems)
├── intervals/               (6 problems)
├── math_geometry/           (8 problems)
└── bit_manipulation/        (7 problems)
```

Each problem has:
- `solution.py` — problem description + skeleton code to implement
- `test_solution.py` — test cases to validate your solution

## Workflow

1. Open a problem's `solution.py` and implement the solution.
2. Run the tests for that problem:

```bash
pytest problems/<category>/<problem>/
```

For example:

```bash
pytest problems/arrays_hashing/two_sum/
```

3. Run all tests at once to see overall progress:

```bash
pytest
```

4. Run tests with verbose output:

```bash
pytest -v
```

## Example

```bash
# Work on Two Sum
$ cat problems/arrays_hashing/two_sum/solution.py

$ vim problems/arrays_hashing/two_sum/solution.py

$ pytest problems/arrays_hashing/two_sum/ -v
```
