import random
import argparse
from LotsOfWords import adjectives, nouns

# Function to generate the wordlist
def generate_wordlist(adjectives, nouns, filename, total_entries, capitalize_adjective, capitalize_noun, max_length):
    with open(filename, 'w') as file:
        generated_count = 0
        for adj in adjectives:
            if capitalize_adjective:
                adj = adj.capitalize()
            for noun in nouns:
                if capitalize_noun:
                    noun = noun.capitalize()
                if len(adj) + len(noun) > max_length:
                    continue
                for i in range(100):
                    if generated_count >= total_entries:
                        print(f"{total_entries} passwords created.")
                        return
                    digits = f"{i:02d}"
                    entry = f"{adj}{noun}{digits}\n"
                    file.write(entry)
                    generated_count += 1
                    if generated_count % 1000000 == 0:
                        print(f"Generated {generated_count} passwords so far.")
        print(f"Finished generating {generated_count} entries.")

# Setup argparse
parser = argparse.ArgumentParser(description='Generate a wordlist.')
parser.add_argument('--filename', type=str, default='wordlist.txt', help='Output filename')
parser.add_argument('--total_entries', type=int, default=9000000000, help='Maximum number of entries to generate')
parser.add_argument('--capitalize_adjective', action='store_true', help='Capitalize the first letter of adjectives')
parser.add_argument('--capitalize_noun', action='store_true', help='Capitalize the first letter of nouns')
parser.add_argument('--max_length', type=int, default=10, help='Maximum length of adjective+noun before adding digits')

# Parse arguments
args = parser.parse_args()

# Call the function with the parsed arguments
generate_wordlist(adjectives, nouns, args.filename, args.total_entries, args.capitalize_adjective, args.capitalize_noun, args.max_length)

