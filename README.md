# Array Element Tracking Algorithms

## Project Overview

This repository contains various algorithms implemented in Python for tracking the occurrences and positions of elements within an array. These algorithms demonstrate different approaches to solve the problem, including iterative methods and divide-and-conquer strategies. The performance of each method is measured in terms of execution time.

## Technologies Used

- **Programming Language:**
  - Python

## Files

### `main.py`

This file contains the main implementations of different algorithms to track array elements, including:
- Iterative method with full element tracking
- Iterative method tracking the number of elements between occurrences
- Optimized iterative method
- Divide-and-conquer method
- Optimized divide-and-conquer method

## Features

- **Element Tracking:**
  - Track occurrences and positions of elements in an array.
  - Measure the performance of different tracking methods.

- **Iterative Methods:**
  - `main(arr)`: Tracks the full occurrences of each element.
  - `main_no_items(arr, length)`: Tracks the number of elements between occurrences.
  - `main_speed_up(arr, length)`: An optimized version of the iterative method.

- **Divide-and-Conquer Methods:**
  - `divide_conquer(arr, index, length)`: Basic divide-and-conquer approach for element tracking.
  - `divide_conquer2(arr, index, length)`: Optimized divide-and-conquer method.

## Usage

1. **Prepare Input:**
   - The input array should be provided in a text file, with elements separated by spaces or new lines.

2. **Run the Script:**
   ```bash
   python main.py
   ```
3. **Enter the Input File Name:**
   - When prompted, enter the name of the file containing the input array.

4. **Output:**
   - The script will output the time taken for each method to execute.

### Example Usage
```python
# Example array in a text file:
# input.txt
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9

# Running the script:
python main.py

# Expected output:
# Enter file name: input.txt
# Iterative took           X.XXX seconds
# Iterative_no_items took  X.XXX seconds
# Iterative_speed_up took  X.XXX seconds
# First conquer took       X.XXX seconds
# Second conquer took      X.XXX seconds
