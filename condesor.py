input_file_path = 'converted_output_file.txt'
output_file_path = 'condensed_adjective.txt'

# Read the input file
with open(input_file_path, 'r') as file:

    words = [line.strip(" ,\n'[]") for line in file]

# divide the words list into chunks of 10
def chunked_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Open the output file in write mode
with open(output_file_path, 'w') as file:
    file.write("[")
    first_line = True
    for chunk in chunked_list(words, 10):
        if not first_line:
            file.write("\n")
        # Join the current chunked words, separated by ', '
        output_string = ", ".join("'" + word + "'" for word in chunk)
        file.write(output_string)
        first_line = False
    file.write("]")

print("Transformation complete.")

