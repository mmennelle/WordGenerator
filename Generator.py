import random
import argparse
from LotsOfWords import adjectives, nouns, verbs


# Function to generate the wordlist
def generate_wordlist(adjectives, nouns, verbs, adjective, noun, verb, filename, total_passwords, capitalize_adjective, capitalize_noun,
                      capitalize_verb,max_length):
    with open(filename, 'w') as file:
        generated_count = 0
        for adj in adjectives:
            if capitalize_adjective:
                adj = adj.capitalize()
            for noun in nouns:
                if capitalize_noun:
                    noun = noun.capitalize()
                for ver in verbs:
                    if capitalize_verb:
                        ver = ver.capitalize()
                    if len(adj) + len(noun) > max_length:
                        continue
                    for i in range(100):
                        if generated_count >= total_passwords:
                            print(f"{total_passwords} passwords created.")
                            return
                        digits = f"{i:02d}"
                        if adjective and noun:
                            entry = f"{adj}{noun}{digits}\n"
                            file.write(entry)
                            generated_count += 1
                        if verb and noun:
                            entry = f"{ver}{noun}{digits}\n"
                            file.write(entry)
                            generated_count += 1
                        if generated_count % 1000000 == 0:
                            print(f"Generated {generated_count} passwords so far.")
        print(f"Finished generating {generated_count} passwords.")


# Setup argparse
parser = argparse.ArgumentParser(description='Generate a wordlist.')
parser.add_argument('--filename', type=str, default='wordlist.txt', help='Output filename')
parser.add_argument('--total_passwords', type=int, default=9000000000, help='Maximum number of entries to generate')
parser.add_argument('--capitalize_adjective', action='store_true', help='Capitalize the first letter of adjectives')
parser.add_argument('--capitalize_noun', action='store_true', help='Capitalize the first letter of nouns')
parser.add_argument('--capitalize_verb', action='store_true', help='Capitalize the first letter of verb')
parser.add_argument('--adjective', action='store_true', help='Include adjective')
parser.add_argument('--noun', action='store_true', help='Include noun')
parser.add_argument('--verb', action='store_true', help='Include verb')
parser.add_argument('--max_length', type=int, default=100, help='Maximum length of adjective+noun before adding digits')

# Parse arguments
args = parser.parse_args()

# Call the function with the parsed arguments
generate_wordlist(adjectives,nouns,verbs, args.adjective, args.noun, args.verb, args.filename, args.total_passwords, args.capitalize_adjective,
                  args.capitalize_noun, args.capitalize_verb, args.max_length)
