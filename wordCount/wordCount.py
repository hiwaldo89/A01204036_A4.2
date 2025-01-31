"""Module providing a function that converts numbers to binary and hexadecimal base."""

import sys
import time


def word_count(filename):
    """Function to count words on the file."""
    start_time = time.time()
    word_dict = {}
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                if word:
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
        sorted_words = sorted(
            word_dict.items(), key=lambda x: x[1], reverse=True)
        results = []
        results.append(f"{'Word':<20}{'Count'}")
        results.append("-" * 30)
        for word, count in sorted_words:
            results.append(f"{word:<20}{count}")
        elapsed_time = time.time() - start_time
        results.append("-" * 30)
        results.append(f"{'Elapsed Time (s)':<20}{elapsed_time:.4f}")

        for line in results:
            print(line)
        with open("WordCountResults.txt", "w", encoding="utf-8") as output_file:
            for line in results:
                output_file.write(line + "\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)


def main():
    """Main function that handles command-line arguments."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    word_count(filename)


if __name__ == "__main__":
    main()
