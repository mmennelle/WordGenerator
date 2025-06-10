# Password Wordlist Generator

Generate customizable password wordlists using extensive collections of adjectives, nouns, verbs, and names. This tool creates combinations of words with digits and optional symbol substitution for password generation and security testing.

## Features

- **Word Combinations**: Generate passwords using combinations of adjectives, nouns, verbs, and names
- **Random Generation**: Create random word combinations for varied output
- **Symbol Substitution**: Replace random characters with symbols for enhanced complexity
- **Capitalization Control**: Selectively capitalize different word types
- **Length Filtering**: Set maximum password length limits
- **Reversible Pairs**: Generate both normal and reversed word order combinations
- **Scalable Output**: Generate millions of password combinations efficiently

## Usage

```bash
python Generator.py [options]
```

## Command Line Options

### Basic Options
- `-h, --help` - Show help message and exit
- `-f FILENAME, --filename FILENAME` - Output filename (default: wordlist.txt)
- `-tp TOTAL_PASSWORDS, --total_passwords TOTAL_PASSWORDS` - Maximum number of entries to generate (default: 9,000,000,000)

### Word Type Selection
- `-a, --adjective` - Include adjectives in combinations
- `-n, --noun` - Include nouns in combinations  
- `-v, --verb` - Include verbs in combinations

### Capitalization Options
- `-A, --capitalize_adjective` - Capitalize the first letter of adjectives
- `-N, --capitalize_noun` - Capitalize the first letter of nouns
- `-V, --capitalize_verb` - Capitalize the first letter of verbs

### Generation Modes
- `-r, --reversible` - Generate reversed pairs (e.g., both "word1word2" and "word2word1")
- `-ra, --random` - Randomly select words and generate passwords

### Customization Options
- `-ml MAX_LENGTH, --max_length MAX_LENGTH` - Maximum length of password before adding digits (default: 100)
- `-s, --symbols` - Replace a random character with a symbol from the default set
- `-cs CUSTOM_SYMBOLS, --custom_symbols CUSTOM_SYMBOLS` - Use custom symbol set (overrides default symbols)

## Examples

### Generate adjective + noun combinations
```bash
python Generator.py -a -n -f adjective_noun_passwords.txt
```

### Generate capitalized verb + noun combinations with symbols
```bash
python Generator.py -v -n -V -N -s -f verb_noun_passwords.txt
```

### Generate random combinations with custom symbols
```bash
python Generator.py -ra -cs "!@#$%^&*" -tp 1000000 -f random_passwords.txt
```

### Generate reversible adjective + verb pairs
```bash
python Generator.py -a -v -r -f reversible_passwords.txt
```

## Output Format

Generated passwords follow the pattern: `[word1][word2][00-99]`

Examples:
- `happydog01`
- `runfast42` 
- `quickjump99`

With symbols enabled, random characters may be replaced:
- `h@ppydog01`
- `runf!st42`
- `qu#ckjump99`

## Performance Notes

- **Random mode warning**: If you don't set a max length with random mode, it will generate approximately 109,785,000,000 combinations
- Progress is displayed every 1,000,000 generated passwords
- Base word combinations longer than 10 characters are automatically skipped to maintain reasonable password lengths

## Additional Tools

The project includes supplementary formatting scripts:
- `FormatConverter.py` - Convert word lists to proper format
- `Condenser.py` - Condense formatted word lists into array format

## Requirements

- Python 3.8+
- `LotsOfWords.py` module containing word lists (adjectives, nouns, verbs, names)

## Default Symbol Set

When using the `-s` flag, the default symbol set is: `{})(!@#$%^&*[]3<>:;=+?`