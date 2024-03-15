import argparse
from LotsOfWords import adjectives, nouns, verbs

def generate_wordlist(adjective, noun, verb, reversible, filename, total_passwords, capitalize_adjective, capitalize_noun, capitalize_verb, max_length):
    with open(filename, 'w') as file:
            generated_count = 0

            # Using match-case structure
            match (adjective, noun, verb, reversible):
                case (True, True, _, False):
                    for adj in adjectives:
                        adj_formatted = adj.capitalize() if capitalize_adjective else adj
                        for noun in nouns:
                            noun_formatted = noun.capitalize() if capitalize_noun else noun
                            for i in range(100):  # Digits iteration
                                digits = f"{i:02d}"
                                entry = f"{adj_formatted}{noun_formatted}{digits}\n"
                                if len(entry) <= max_length:
                                    file.write(entry)
                                    generated_count += 1
                                    if generated_count % 1000000 == 0:
                                        print(f"Generated {generated_count} passwords so far.")
                                    if generated_count >= total_passwords:
                                        print(f"{total_passwords} passwords created.")
                                        return

                case (False, True, True, False):
                    for verb in verbs:
                        ver_formatted = verb.capitalize() if capitalize_verb else verb
                        for noun in nouns:
                            noun_formatted = noun.capitalize() if capitalize_noun else noun
                            for i in range(100):  # Digits iteration
                                digits = f"{i:02d}"
                                entry = f"{ver_formatted}{noun_formatted}{digits}\n"
                                if len(entry) <= max_length:
                                    file.write(entry)
                                    generated_count += 1
                                    if generated_count % 1000000 == 0:
                                        print(f"Generated {generated_count} passwords so far.")
                                    if generated_count >= total_passwords:
                                        return

                case (True, False, True, False):
                    for adj in adjectives:
                        adj_formatted = adj.capitalize() if capitalize_adjective else adj
                        for ver in verbs:
                            ver_formatted = ver.capitalize() if capitalize_verb else ver
                            for i in range(100):  # Digits iteration
                                digits = f"{i:02d}"
                                entry = f"{adj_formatted}{ver_formatted}{digits}\n"
                                if len(entry) <= max_length:
                                    file.write(entry)
                                    generated_count += 1
                                    if generated_count % 1000000 == 0:
                                        print(f"Generated {generated_count} passwords so far.")
                                    if generated_count >= total_passwords:
                                        return

                case (True, True, _, True) | (False, True, True, True) | (True, False, True, True):
                    # Only executed if reversible is True
                    pairs = []
                    if adjective and noun:
                        pairs.extend([(adj, noun) for adj in adjectives for noun in nouns])
                    if verb and noun:
                        pairs.extend([(verb, noun) for verb in verbs for noun in nouns])
                    if adjective and verb:
                        pairs.extend([(adj, verb) for adj in adjectives for verb in verbs])

                    for pair in pairs:
                        word1 = pair[0].capitalize() if capitalize_adjective or capitalize_verb else pair[0]
                        word2 = pair[1].capitalize() if capitalize_noun else pair[1]
                        for i in range(100):  # Digits iteration
                            digits = f"{i:02d}"
                            entry = f"{word2}{word1}{digits}\n"  # Note the reversal here
                            if len(entry) <= max_length:
                                file.write(entry)
                                generated_count += 1
                                if generated_count % 1000000 == 0:
                                    print(f"Generated {generated_count} passwords so far.")
                                if generated_count >= total_passwords:
                                    print(f"{total_passwords} passwords created.")
                                    return

    print(f"Finished generating {generated_count} passwords.")

parser = argparse.ArgumentParser(description='Generate a wordlist.')
parser.add_argument('-f', '--filename', type=str, default='wordlist.txt', help='Output filename')
parser.add_argument('-tp', '--total_passwords', type=int, default=9000000000, help='Maximum number of entries to generate')
parser.add_argument('-a', '--adjective', action='store_true', help='Include adjective')
parser.add_argument('-n', '--noun', action='store_true', help='Include noun')
parser.add_argument('-v', '--verb', action='store_true', help='Include verb')
parser.add_argument('-A', '--capitalize_adjective', action='store_true', help='Capitalize the first letter of adjectives')
parser.add_argument('-N', '--capitalize_noun', action='store_true', help='Capitalize the first letter of nouns')
parser.add_argument('-V', '--capitalize_verb', action='store_true', help='Capitalize the first letter of verbs')
parser.add_argument('-ml', '--max_length', type=int, default=100, help='Maximum length of password before adding digits')
parser.add_argument('-r', '--reversible', action='store_true', help='Generate reversed pairs only')

args = parser.parse_args()

generate_wordlist(args.adjective, args.noun, args.verb, args.reversible, args.filename, args.total_passwords,
                  args.capitalize_adjective, args.capitalize_noun, args.capitalize_verb, args.max_length)
