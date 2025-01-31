"""Module providing a function that converts numbers to binary and hexadecimal base."""

import sys
import time

def to_binary(n, bit_width=10):
    """Converts a number to binary"""
    if n == 0:
        return "0"
    if n > 0:
        return bin(n)[2:]
    binary = bin(abs(n))[2:].zfill(bit_width)
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary)
    carry = 1
    binary_with_one = list(inverted)
    for i in range(len(binary_with_one) - 1, -1, -1):
        if binary_with_one[i] == '0' and carry == 1:
            binary_with_one[i] = '1'
            carry = 0
        elif binary_with_one[i] == '1' and carry == 1:
            binary_with_one[i] = '0'
    return ''.join(binary_with_one)

def to_hexadecimal(n, bit_width=32):
    """Converts a number to hexadecimal"""
    if n == 0:
        return "0"
    if n > 0:
        return hex(n)[2:].upper()
    binary = bin(abs(n))[2:].zfill(bit_width)
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary)
    carry = 1
    binary_with_one = list(inverted)
    for i in range(len(binary_with_one) - 1, -1, -1):
        if binary_with_one[i] == '0' and carry == 1:
            binary_with_one[i] = '1'
            carry = 0
        elif binary_with_one[i] == '1' and carry == 1:
            binary_with_one[i] = '0'
    two_complement_binary = ''.join(binary_with_one)
    hex_value = hex(int(two_complement_binary, 2))[2:].upper()
    return hex_value

def convert_numbers(filename):
    """Reads numbers from file, converts them to binary and hexadecimal."""
    start_time = time.time()
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            numbers = []
            for line in file:
                line = line.strip()
                if line:
                    try:
                        number = int(float(line))
                        numbers.append(number)
                    except ValueError:
                        print(f"Warning: '{line}' is not a valid number and was ignored.")
        if not numbers:
            print("Error: No valid numbers found in the file.")
            return
        # Prepare results
        results = []
        results.append(f"{'Number':<15}{'Binary':<30}{'Hexadecimal':<15}")
        results.append("-" * 60)

        for number in numbers:
            binary = to_binary(number)
            hexadecimal = to_hexadecimal(number)
            results.append(f"{number:<15}{binary:<30}{hexadecimal:<15}")
        elapsed_time = time.time() - start_time
        results.append("-" * 60)
        results.append(f"{'Elapsed Time (s)':<20}{elapsed_time:.4f}")

        # Print results to screen as a table
        for line in results:
            print(line)

        # Save results to a file
        with open("ConversionResults.txt", "w", encoding="utf-8") as output_file:
            for line in results:
                output_file.write(line + "\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def main():
    """Main function that handles command-line arguments."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    convert_numbers(filename)

if __name__ == "__main__":
    main()
