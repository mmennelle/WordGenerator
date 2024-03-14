import random
import argparse
from LotsOfWords import adjectives, nouns, verbs


# generate a wordlist
def generate_wordlist(adjectives, nouns, verbs, adjective, noun, verb, filename, total_passwords, capitalize_adjective,
                      capitalize_noun,
                      capitalize_verb, max_length):
    # CLI arg validation.
    if not ((adjective and noun) or (adjective and verb) or (verb and noun)):
        print("\nProvide a combination please.. Type python Generator.py -h for more info.\n")
        exit(1)

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
                    # Length is adjusted using a CLI arg
                    if adjective and noun and (len(adj) + len(noun) <= max_length):
                        for i in range(100):
                            if generated_count >= total_passwords:
                                print(f"{total_passwords} passwords created.")
                                return
                            digits = f"{i:02d}"
                            entry = f"{adj}{noun}{digits}\n"
                            file.write(entry)
                            generated_count += 1
                    if verb and noun and (len(ver) + len(noun) <= max_length):
                        for i in range(100):
                            if generated_count >= total_passwords:
                                return
                            digits = f"{i:02d}"
                            entry = f"{ver}{noun}{digits}\n"
                            file.write(entry)
                            generated_count += 1
                    if adjective and verb and (len(adj) + len(ver) <= max_length):
                        for i in range(100):
                            if generated_count >= total_passwords:
                                return
                            digits = f"{i:02d}"
                            entry = f"{adj}{ver}{digits}\n"
                            file.write(entry)
                            generated_count += 1
                    if generated_count % 1000000 == 0:
                        print(f"Generated {generated_count} passwords so far.")

        print(f"Finished generating {generated_count} passwords.")



parser = argparse.ArgumentParser(description='Generate a wordlist.')
parser.add_argument('--filename', type=str, default='wordlist.txt', help='Output filename')
parser.add_argument('--total_passwords', type=int, default=9000000000, help='Maximum number of entries to generate')
parser.add_argument('--capitalize_adjective', action='store_true', help='Capitalize the first letter of adjectives')
parser.add_argument('--capitalize_noun', action='store_true', help='Capitalize the first letter of nouns')
parser.add_argument('--capitalize_verb', action='store_true', help='Capitalize the first letter of verbs')
parser.add_argument('--adjective', action='store_true', help='Include adjective')
parser.add_argument('--noun', action='store_true', help='Include noun')
parser.add_argument('--verb', action='store_true', help='Include verb')
parser.add_argument('--max_length', type=int, default=100, help='Maximum length of combinations before adding digits')


args = parser.parse_args()


generate_wordlist(adjectives, nouns, verbs, args.adjective, args.noun, args.verb, args.filename, args.total_passwords,
                  args.capitalize_adjective,
                  args.capitalize_noun, args.capitalize_verb, args.max_length)
