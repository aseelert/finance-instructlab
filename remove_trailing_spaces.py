import sys
import fileinput

def remove_trailing_spaces(input_file, output_file=None):
    """
    Removes trailing spaces from each line in the input file.
    
    If output_file is provided, the cleaned content is written to it.
    Otherwise, the input file is overwritten with the cleaned content.
    
    Args:
        input_file (str): Path to the input file.
        output_file (str, optional): Path to the output file. Defaults to None.
    """
    if output_file:
        # Read from input_file and write to output_file
        with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
            for line in fin:
                # Remove trailing spaces and write the line
                fout.write(line.rstrip() + '\n')
        print(f"Trailing spaces removed and written to '{output_file}'.")
    else:
        # Overwrite the input_file in place
        with fileinput.FileInput(input_file, inplace=True, backup='.bak') as file:
            for line in file:
                # Remove trailing spaces and print (which writes to the file)
                print(line.rstrip())
        print(f"Trailing spaces removed from '{input_file}'. A backup was created as '{input_file}.bak'.")

def print_usage():
    """
    Prints usage instructions.
    """
    usage_text = """
    Usage:
        python remove_trailing_spaces.py <input_file> [<output_file>]

    Arguments:
        <input_file>   Path to the input file from which to remove trailing spaces.
        <output_file>  (Optional) Path to the output file to save the cleaned content.
                       If not provided, the input file will be overwritten.

    Examples:
        # Overwrite the original file
        python remove_trailing_spaces.py qna.yaml

        # Write the cleaned content to a new file
        python remove_trailing_spaces.py qna.yaml qna_cleaned.yaml
    """
    print(usage_text)

if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Error: Incorrect number of arguments.")
        print_usage()
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Determine if an output file is specified
    output_file = sys.argv[2] if len(sys.argv) == 3 else None
    
    # Call the function to remove trailing spaces
    remove_trailing_spaces(input_file, output_file)
