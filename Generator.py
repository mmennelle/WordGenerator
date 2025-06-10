import argparse
import random
from LotsOfWords import adjectives, nouns, verbs, names

def replace_random_character_with_symbol(entry, symbols):
    """Replace a random character in the entry with a random symbol."""
    position = random.randint(0, len(entry) - 1)
    symbol = random.choice(symbols)
    modified_entry = entry[:position] + symbol + entry[position + 1:]
    return modified_entry

def generate_random_wordlist(filename, total_passwords, max_length, use_symbols=False, symbols=None):
    with open(filename, 'w') as file:
        generated_count = 0
        while generated_count < total_passwords:
            word_list = random.sample([adjectives, nouns, verbs, names], 2)  # Randomly select two lists
            word1 = random.choice(word_list[0])
            word2 = random.choice(word_list[1])
            for i in range(100):  # Digits iteration
                digits = f"{i:02d}"
                base_entry = f"{word1}{word2}"
                
                # Apply symbol replacement if enabled
                if use_symbols and symbols:
                    base_entry = replace_random_character_with_symbol(base_entry, symbols)
                
                entry = f"{base_entry}{digits}\n"
                if len(entry) <= max_length:
                    file.write(entry)
                    generated_count += 1
                    if generated_count % 1000000 == 0:
                        print(f"Generated {generated_count} passwords so far.")
                    if generated_count >= total_passwords:
                        print(f"{total_passwords} passwords created.")
                        return

def generate_wordlist(adjective, noun, verb, name, reversible, filename, total_passwords, capitalize_adjective, 
                     capitalize_noun, capitalize_verb, capitalize_name, max_length, use_symbols=False, symbols=None):
    with open(filename, 'w') as file:
        generated_count = 0

        # Using match-case structure
        match (adjective, noun, verb, name, reversible):
            case (True, True, False, False, False):
                for adj in adjectives:
                    adj_formatted = adj.capitalize() if capitalize_adjective else adj
                    for noun in nouns:
                        noun_formatted = noun.capitalize() if capitalize_noun else noun
                        
                        # Check length before adding digits (similar to SymbolGenerator logic)
                        base_word = f"{adj_formatted}{noun_formatted}"
                        if len(base_word) > 10:  # Skip if base exceeds 10 characters
                            continue
                            
                        for i in range(100):  # Digits iteration
                            digits = f"{i:02d}"
                            entry_base = base_word
                            
                            # Apply symbol replacement if enabled
                            if use_symbols and symbols:
                                entry_base = replace_random_character_with_symbol(entry_base, symbols)
                            
                            entry = f"{entry_base}{digits}\n"
                            if len(entry) <= max_length:
                                file.write(entry)
                                generated_count += 1
                                if generated_count % 1000000 == 0:
                                    print(f"Generated {generated_count} passwords so far.")
                                if generated_count >= total_passwords:
                                    print(f"{total_passwords} passwords created.")
                                    return

            case (False, True, True, False, False):
                for verb in verbs:
                    ver_formatted = verb.capitalize() if capitalize_verb else verb
                    for noun in nouns:
                        noun_formatted = noun.capitalize() if capitalize_noun else noun
                        
                        base_word = f"{ver_formatted}{noun_formatted}"
                        if len(base_word) > 10:  # Skip if base exceeds 10 characters
                            continue
                            
                        for i in range(100):  # Digits iteration
                            digits = f"{i:02d}"
                            entry_base = base_word
                            
                            # Apply symbol replacement if enabled
                            if use_symbols and symbols:
                                entry_base = replace_random_character_with_symbol(entry_base, symbols)
                            
                            entry = f"{entry_base}{digits}\n"
                            if len(entry) <= max_length:
                                file.write(entry)
                                generated_count += 1
                                if generated_count % 1000000 == 0:
                                    print(f"Generated {generated_count} passwords so far.")
                                if generated_count >= total_passwords:
                                    print(f"{total_passwords} passwords created.")
                                    return

            case (True, False, True, False, False):
                for adj in adjectives:
                    adj_formatted = adj.capitalize() if capitalize_adjective else adj
                    for ver in verbs:
                        ver_formatted = ver.capitalize() if capitalize_verb else ver
                        
                        base_word = f"{adj_formatted}{ver_formatted}"
                        if len(base_word) > 10:  # Skip if base exceeds 10 characters
                            continue
                            
                        for i in range(100):  # Digits iteration
                            digits = f"{i:02d}"
                            entry_base = base_word
                            
                            # Apply symbol replacement if enabled
                            if use_symbols and symbols:
                                entry_base = replace_random_character_with_symbol(entry_base, symbols)
                            
                            entry = f"{entry_base}{digits}\n"
                            if len(entry) <= max_length:
                                file.write(entry)
                                generated_count += 1
                                if generated_count % 1000000 == 0:
                                    print(f"Generated {generated_count} passwords so far.")
                                if generated_count >= total_passwords:
                                    print(f"{total_passwords} passwords created.")
                                    return

            case (True, False, False, True, False):
                for adj in adjectives:
                    adj_formatted = adj.capitalize() if capitalize_adjective else adj
                    for name in names:
                        name_formatted = name.capitalize() if capitalize_name else name
                        
                        base_word = f"{adj_formatted}{name_formatted}"
                        if len(base_word) > 10:  # Skip if base exceeds 10 characters
                            continue
                            
                        for i in range(100):  # Digits iteration
                            digits = f"{i:02d}"
                            entry_base = base_word
                            
                            # Apply symbol replacement if enabled
                            if use_symbols and symbols:
                                entry_base = replace_random_character_with_symbol(entry_base, symbols)
                            
                            entry = f"{entry_base}{digits}\n"
                            if len(entry) <= max_length:
                                file.write(entry)
                                generated_count += 1
                                if generated_count % 1000000 == 0:
                                    print(f"Generated {generated_count} passwords so far.")
                                if generated_count >= total_passwords:
                                    print(f"{total_passwords} passwords created.")
                                    return

            case (False, True, False, True, False):
                for noun in nouns:
                    noun_formatted = noun.capitalize() if capitalize_noun else noun
                    for name in names:
                        name_formatted = name.capitalize() if capitalize_name else name
                        
                        base_word = f"{noun_formatted}{name_formatted}"
                        if len(base_word) > 10:  # Skip if base exceeds 10 characters
                            continue
                            
                        for i in range(100):  # Digits iteration
                            digits = f"{i:02d}"
                            entry_base = base_word
                            
                            # Apply symbol replacement if enabled
                            if use_symbols and symbols:
                                entry_base = replace_random_character_with_symbol(entry_base, symbols)
                            
                            entry = f"{entry_base}{digits}\n"
                            if len(entry) <= max_length:
                                file.write(entry)
                                generated_count += 1
                                if generated_count % 1000000 == 0:
                                    print(f"Generated {generated_count} passwords so far.")
                                if generated_count >= total_passwords:
                                    print(f"{total_passwords} passwords created.")
                                    return

            case (False, False, True, True, False):
                for verb in verbs:
                    ver_formatted = verb.capitalize() if capitalize_verb else verb
                    for name in names:
                        name_formatted = name.capitalize() if capitalize_name else name
                        
                        base_word = f"{ver_formatted}{name_formatted}"
                        if len(base_word) > 10:  # Skip if base exceeds 10 characters
                            continue
                            
                        for i in range(100):  # Digits iteration
                            digits = f"{i:02d}"
                            entry_base = base_word
                            
                            # Apply symbol replacement if enabled
                            if use_symbols and symbols:
                                entry_base = replace_random_character_with_symbol(entry_base, symbols)
                            
                            entry = f"{entry_base}{digits}\n"
                            if len(entry) <= max_length:
                                file.write(entry)
                                generated_count += 1
                                if generated_count % 1000000 == 0:
                                    print(f"Generated {generated_count} passwords so far.")
                                if generated_count >= total_passwords:
                                    print(f"{total_passwords} passwords created.")
                                    return

            case (True, True, False, False, True) | (False, True, True, False, True) | (True, False, True, False, True) | (True, False, False, True, True) | (False, True, False, True, True) | (False, False, True, True, True):
                # Only executed if reversible is True
                pairs = []
                if adjective and noun:
                    pairs.extend([(adj, noun) for adj in adjectives for noun in nouns])
                if verb and noun:
                    pairs.extend([(verb, noun) for verb in verbs for noun in nouns])
                if adjective and verb:
                    pairs.extend([(adj, verb) for adj in adjectives for verb in verbs])
                if adjective and name:
                    pairs.extend([(adj, name) for adj in adjectives for name in names])
                if noun and name:
                    pairs.extend([(noun, name) for noun in nouns for name in names])
                if verb and name:
                    pairs.extend([(verb, name) for verb in verbs for name in names])

                for pair in pairs:
                    # Determine capitalization based on word type
                    word1_cap = False
                    word2_cap = False
                    
                    # Check if word1 needs capitalization
                    if pair[0] in adjectives and capitalize_adjective:
                        word1_cap = True
                    elif pair[0] in verbs and capitalize_verb:
                        word1_cap = True
                    elif pair[0] in nouns and capitalize_noun:
                        word1_cap = True
                    elif pair[0] in names and capitalize_name:
                        word1_cap = True
                        
                    # Check if word2 needs capitalization
                    if pair[1] in adjectives and capitalize_adjective:
                        word2_cap = True
                    elif pair[1] in verbs and capitalize_verb:
                        word2_cap = True
                    elif pair[1] in nouns and capitalize_noun:
                        word2_cap = True
                    elif pair[1] in names and capitalize_name:
                        word2_cap = True
                    
                    word1 = pair[0].capitalize() if word1_cap else pair[0]
                    word2 = pair[1].capitalize() if word2_cap else pair[1]
                    
                    base_word = f"{word2}{word1}"
                    if len(base_word) > 10:  # Skip if base exceeds 10 characters
                        continue
                        
                    for i in range(100):  # Digits iteration
                        digits = f"{i:02d}"
                        entry_base = base_word
                        
                        # Apply symbol replacement if enabled
                        if use_symbols and symbols:
                            entry_base = replace_random_character_with_symbol(entry_base, symbols)
                        
                        entry = f"{entry_base}{digits}\n"
                        if len(entry) <= max_length:
                            file.write(entry)
                            generated_count += 1
                            if generated_count % 1000000 == 0:
                                print(f"Generated {generated_count} passwords so far.")
                            if generated_count >= total_passwords:
                                print(f"{total_passwords} passwords created.")
                                return

    print(f"Finished generating {generated_count} passwords.")

# CLI argument parser
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
parser.add_argument('-ra', '--random', action='store_true', help='Randomly select words and generate passwords.\nNOTE: If you dont set a max length '
                                                                 'it will generate 109,785,000,000 combinations.')
parser.add_argument('-s', '--symbols', action='store_true', help='Replace a random character with a symbol from the default set')
parser.add_argument('-cs', '--custom_symbols', type=str, help='Custom symbol set to use (overrides default symbols)')

args = parser.parse_args()

# Set up symbols
default_symbols = '{})(!@#$%^&*[]3<>:;=+?'
symbols_to_use = args.custom_symbols if args.custom_symbols else default_symbols
use_symbols = args.symbols or bool(args.custom_symbols)

if args.random:
    generate_random_wordlist(args.filename, args.total_passwords, args.max_length, use_symbols, symbols_to_use)
else:
    generate_wordlist(args.adjective, args.noun, args.verb, args.reversible, args.filename, args.total_passwords,
                      args.capitalize_adjective, args.capitalize_noun, args.capitalize_verb, args.max_length, 
                      use_symbols, symbols_to_use)