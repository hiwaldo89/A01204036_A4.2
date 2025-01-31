"""Module providing a function printing descriptive statistics from a file containing numbers."""

import sys
import time


def get_mean(data):
    """Function that returns the mean of a list of numbers"""
    return sum(data) / len(data)


def get_median(data):
    """Function that returns the median of a list of numbers"""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    return sorted_data[mid]


def get_mode(data):
    """Function that returns the mode of a list of numbers"""
    frequency = {}
    for num in data:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_freq = max(frequency.values())

    # If all numbers are different (no mode), return '#N/A'
    if max_freq == 1:
        return '#N/A'
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes[0] if len(modes) == 1 else modes


def get_sd(variance):
    """Function that returns the standard deviation"""
    return variance ** 0.5


def get_variance(data, mean):
    """Function that returns the variance"""
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)


def compute_statistics(filename):
    """Function that computes statistics."""
    start_time = time.time()
    try:
        valid_data = []
        invalid_lines = []
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        valid_data.append(float(line))
                    except ValueError:
                        invalid_lines.append(line)
        if invalid_lines:
            print("The following lines contain non-numeric data and were ignored:")
            for line in invalid_lines:
                print(f" - {line}")
        if not valid_data:
            print("Error: No valid data found in the file.")
            return
        mean = get_mean(valid_data)
        median = get_median(valid_data)
        mode = get_mode(valid_data)
        variance = get_variance(valid_data, mean)
        sd = get_sd(variance)
        count = len(valid_data)
        elapsed_time = time.time() - start_time

        # Prepare results in table format
        results = []
        results.append(f"{'Statistic':<20}{'Value'}")
        results.append("-" * 30)
        results.append(f"{'Count':<20}{count}")
        results.append(f"{'Mean':<20}{mean:.2f}")
        results.append(f"{'Median':<20}{median:.2f}")
        results.append(f"{'Mode':<20}{mode}")
        results.append(f"{'Standard Deviation':<20}{sd:.2f}")
        results.append(f"{'Variance':<20}{variance:.2f}")
        results.append(f"{'Elapsed Time (s)':<20}{elapsed_time:.4f}")

        # Print results to console
        for line in results:
            print(line)

        # Save results to a file
        with open("StatisticsResults.txt", "w", encoding="utf-8") as output_file:
            for line in results:
                output_file.write(line + "\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


def main():
    """Function that checks arguments are passed and executes print_statistics function."""

    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    compute_statistics(filename)


if __name__ == "__main__":
    main()
