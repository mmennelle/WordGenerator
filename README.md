Generate passwords using extensive lists of adjectives, nouns, and verbs. The arguments below allow for customization.

DEFAULT: ~3.4 Billion strings. All lowercase consisting of an adjective, noun, and two digits 
EXAMPLE: "actualglove45"

CLI arguments:

Generate a wordlist.

options:
  -h, --help            show this help message and exit
  
  -f FILENAME, --filename FILENAME
                        Output filename
                        
  -tp TOTAL_PASSWORDS, --total_passwords TOTAL_PASSWORDS
                        Maximum number of entries to generate
                        
  -a, --adjective       Include adjective
  
  -n, --noun            Include noun
  
  -v, --verb            Include verb
  
  -A, --capitalize_adjective
                        Capitalize the first letter of adjectives
                        
  -N, --capitalize_noun
                        Capitalize the first letter of nouns
                        
  -V, --capitalize_verb
                        Capitalize the first letter of verbs
                        
  -r, --reverse         Reverse order.
                         Default orders are adj/noun, verb/noun adj/verb
  
  -ml MAX_LENGTH, --max_length MAX_LENGTH
                        Maximum length of combinations before adding digits


