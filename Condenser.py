input_file_path = 'converted_verbs.txt'
output_file_path = 'condensed_verbs.txt'

# Read the input file
with open(input_file_path, 'r') as file:
    # Read lines and strip unwanted characters
    words = [line.strip(" ,\n'[]") for line in file]

# Function to divide the words list into chunks of 10
def chunked_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Open the output file in write mode
with open(output_file_path, 'w') as file:
    file.write("[")
    first_chunk = True
    for chunk in chunked_list(words, 10):
        # For each chunk after the first one, start a new line with a comma
        if not first_chunk:
            file.write(",\n")
        else:
            first_chunk = False
        # Join the current chunk's words, separated by ', '
        output_string = ", ".join("'" + word + "'" for word in chunk)
        file.write(output_string)
    file.write("]")

print("Transformation complete.")
