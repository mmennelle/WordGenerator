import random
import argparse
from LotsOfWords import adjectives, nouns, verbs


def generate_wordlist(adjectives, nouns, verbs, include_adjective, include_noun, include_verb, filename,
                      total_passwords, capitalize_adjective, capitalize_noun, capitalize_verb, max_length):
    if not ((include_adjective and include_noun) or (include_adjective and include_verb) or (
            include_verb and include_noun)):
        print("\nProvide a valid combination of word types. Type `python Generator.py -h` for more info.\n")
        exit(1)

    with open(filename, 'w') as file:
        generated_count = 0
        for adj in (adjectives if include_adjective else ['']):
            for n in (nouns if include_noun else ['']):
                for v in (verbs if include_verb else ['']):
                    adj_c, n_c, v_c = (
                    adj.capitalize() if capitalize_adjective else adj, n.capitalize() if capitalize_noun else n,
                    v.capitalize() if capitalize_verb else v)

                    # Generate combinations based on selected word types
                    for i in range(100):
                        if generated_count >= total_passwords:
                            print(f"{total_passwords} passwords created.")
                            return

                        digits = f"{i:02d}"
                        entry = ""

                        if include_adjective and include_noun and not include_verb:
                            if len(adj_c) + len(n_c) <= max_length:
                                entry = f"{adj_c}{n_c}{digits}\n"
                        elif include_verb and include_noun and not include_adjective:
                            if len(v_c) + len(n_c) <= max_length:
                                entry = f"{v_c}{n_c}{digits}\n"
                        elif include_adjective and include_verb and not include_noun:
                            if len(adj_c) + len(v_c) <= max_length:
                                entry = f"{adj_c}{v_c}{digits}\n"

                        if entry:
                            file.write(entry)
                            generated_count += 1

                        if generated_count % 1000000 == 0:
                            print(f"Generated {generated_count} passwords so far.")

        print(f"Finished generating {generated_count} passwords.")

parser = argparse.ArgumentParser(description='Generate a wordlist.')
parser.add_argument('-f','--filename', type=str, default='wordlist.txt', help='Output filename')
parser.add_argument('-tp','--total_passwords', type=int, default=9000000000, help='Maximum number of entries to generate')
parser.add_argument('-ca','--capitalize_adjective', action='store_true', help='Capitalize the first letter of adjectives')
parser.add_argument('-cn','--capitalize_noun', action='store_true', help='Capitalize the first letter of nouns')
parser.add_argument('-cv','--capitalize_verb', action='store_true', help='Capitalize the first letter of verbs')
parser.add_argument('-adj','--adjective', action='store_true', help='Include adjective')
parser.add_argument('-nou','--noun', action='store_true', help='Include noun')
parser.add_argument('-ver','--verb', action='store_true', help='Include verb')
parser.add_argument('-ml','--max_length', type=int, default=100, help='Maximum length of combinations before adding digits')


args = parser.parse_args()


generate_wordlist(adjectives, nouns, verbs, args.adjective, args.noun, args.verb, args.filename, args.total_passwords,
                  args.capitalize_adjective,
                  args.capitalize_noun, args.capitalize_verb, args.max_length)
