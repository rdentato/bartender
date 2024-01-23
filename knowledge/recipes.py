#  SPDX-FileCopyrightText: © 2024 Remo Dentato <rdentato@gmail.com>
#  SPDX-License-Identifier: MIT

import sys
import random

dir = "/mnt/data"

# Initialize an empty list to hold keyw_ndx
keyw_ndx = []
offsets = []  # Initialize the array to hold the offsets read from the file

args=[]

def get_keyw_ndx():
    # Iterate over command line arguments starting from the first argument
    for arg in args:
        # Attempt to convert each argument to an integer
        try:
            # This will succeed if the argument is an integer or a string representation of an integer
            integer = int(arg)
            keyw_ndx.append(integer)
        except ValueError:
            # If conversion fails, try to split the argument by spaces and convert individual parts
            parts = arg.split()
            for part in parts:
                try:
                    # Try to convert each part into an integer
                    integer = int(part)
                    keyw_ndx.append(integer)
                except ValueError:
                    # If a part is not an integer, ignore it
                    continue

def process_array():
    # Filter the array to include only numbers between 1 and 368 and remove duplicates
    filtered = list(dict.fromkeys(filter(lambda x: 1 <= x <= 368, keyw_ndx)))
    
    # If there are more than three elements, keep only the first three
    if len(filtered) > 3:
        filtered = filtered[:3]
    
    # If there are less than two elements, add random numbers until there are two
    while len(filtered) < 2:
        new_number = random.randint(1, 368)
        if new_number not in filtered:
            filtered.append(new_number)
  
    return filtered

def read_offsets_from_file():
    # Open the file "offsets.ndx" in read mode
    with open(f"{dir}/offsets.ndx", "r") as file:
        for n in keyw_ndx:
            pos = (n - 1) * 8  # Calculate the position to seek to
            file.seek(pos)  # Move to the calculated position in the file
            
            line = file.readline().strip()  # Read a line from the file and strip newline characters
            
            # Convert the line to an integer and add it to the offsets array
            try:
                offset = int(line)
                offsets.append(offset)
            except ValueError:
                # If the line cannot be converted to an integer, ignore it or handle the error as needed
                pass
               
def read_and_print_recipes():
    title = ""
    recipe = ""
    # Open the file "recipes.db" in read mode
    with open(f"{dir}/recipes.db", "r") as file:
        for offset in offsets:
            # Use seek() to position at the specified offset
            file.seek(offset)

            # Read and print two lines from the current position
            #print(f"-{offset}-")  # Print a separator for clarity
            title = title + " " + file.readline().strip()
            recipe = recipe + " " + file.readline().strip()

    print(f"title: \"{title}\"\nrecipe: \"{recipe}\"")

if __name__ == "__main__":

    args = sys.argv[1:]
    if args[0] == '}' :
      dir = "."
      args = args[1:]
      
    get_keyw_ndx()
    keyw_ndx = process_array()
    read_offsets_from_file()
    # Print the resulting array of keyw_ndx
    # print(keyw_ndx)
    # print(offsets)
    read_and_print_recipes()
