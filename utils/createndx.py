#  SPDX-FileCopyrightText: © 2024 Remo Dentato <rdentato@gmail.com>
#  SPDX-License-Identifier: MIT

import sys

offsets = []  # Initialize offsets array
lines = []  # Initialize lines array

def write_keywords_to_file_filtered():
    with open('keywords.txt', 'w') as file:
        exclude_words = {'and', 'or', 'for', 'with', 'without', 'not', 'up', 'a','A', 'Up', 'of', 'la'}
        for index, line in enumerate(lines):
            words = line.replace('.', '').replace(',', '').replace('-', '').split()
            for word in words:
                if word not in exclude_words:
                    file.write(f"{word.lower()} is {index+1}.\n")

def write_offsets_to_file():
    """
    Writes the contents of the 'offsets' array to a file named 'offset.ndx'.
    Each number is formatted to seven digits with trailing spaces.

    :param offsets: The global array containing offsets to be written to the file.
    """
    with open('offsets.ndx', 'w') as file:
        for offset in offsets:
            # Format each offset to seven digits with trailing spaces
            formatted_offset = f"{offset:<7}"
            file.write(formatted_offset + '\n')

def collect_odd_line_info_stdin():
    """
    Reads text from stdin and adds the offset of each odd line to the 'offsets' array,
    and the line itself to the 'lines' array.
    """
    line_number = 1  # Initialize line number
    offset = 0  # Initialize offset

    for line in sys.stdin:
        if line_number % 2 != 0:  # Check if line number is odd
            offsets.append(offset)  # Add offset to the offsets array
            lines.append(line.rstrip('\n'))  # Add line to the lines array, stripping the newline character
        offset += len(line.encode('utf-8'))  # Update offset with the length of the current line
        line_number += 1

    return

if __name__ == "__main__":
    collect_odd_line_info_stdin()
    write_offsets_to_file()
    write_keywords_to_file_filtered()
    # For demonstration, print the collected offsets and lines
    #for offset, line in zip(offsets, lines):
    #    print(f"Offset: {offset}, Line: \"{line}\"")
