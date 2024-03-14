def convert_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Splitting each line at spaces and taking the second element, which is the target
            parts = line.strip().split(' ')
            if len(parts) >= 0:  # Ensure there are at least two parts to avoid IndexError
                verb = parts[1]  # Choose the correct position of the element.
                # Write the formatted string to the output file
                outfile.write(", '{}' ".format(verb) + "\n")


# Example usage
input_file = 'verbs.txt'
output_file = 'converted_verbs.txt'

convert_lines(input_file, output_file)
