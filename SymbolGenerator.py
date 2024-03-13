import random
from LotsOfWords import adjectives, nouns
def generate_wordlist_with_symbols(adjectives, nouns, filename='wordlistSymbol.txt', total_entries=4000000000):
    symbols = '{})(!@#$%^&*[]3<>:;=+?'  # Symbols to be selected randomly.
    with open(filename, 'w') as file:
        generated_count = 0

        # Adjective-noun combinations
        for adj in adjectives:
            for noun in nouns:
                capitalized_noun = noun.capitalize()  # Capitalize the noun
                # Check the combined length before adding digits
                if len(adj) + len(capitalized_noun) > 10: #comment this out if you dont want a limit
                    continue  # Skip this combination if it exceeds set amt of characters

                for i in range(100):  # Generates numbers from 00 to 99
                    if generated_count >= total_entries:
                        print(f"{total_entries} passwords created.")
                        return
                    digits = f"{i:02d}"
                    entry = f"{adj}{capitalized_noun}"
                    # Ensure the password with the symbol replacement is not > 12 characters
                    modified_entry_base = replace_random_character_with_symbol(entry, symbols)
                    modified_entry = modified_entry_base + digits + '\n'
                    file.write(modified_entry)
                    generated_count += 1
                    if generated_count % 1000000 == 0:
                        print(f"Generated {generated_count} passwords.")

        print(f" generated {generated_count} Passwords.")


def replace_random_character_with_symbol(entry, symbols):
    # Select a random position to replace
    position = random.randint(0, len(entry) - 1)
    # Select a random symbol
    symbol = random.choice(symbols)
    # Replace the character at the chosen position with the selected symbol
    modified_entry = entry[:position] + symbol + entry[position + 1:]
    return modified_entry

generate_wordlist_with_symbols(adjectives, nouns, filename = 'wordlistsymbol.txt', total_entries = 4000000000)