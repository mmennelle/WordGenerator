Generate passwords using extensive lists of adjectives, nouns, and verbs. The arguments below allow for customization.

CLI arguments:

Generate a wordlist.

options:
 enerate a wordlist.

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
                        
  -ml MAX_LENGTH, --max_length MAX_LENGTH
                        Maximum length of password before adding digits
                        
  -r, --reversible      Generate reversed pairs only
  
  -ra, --random         Randomly select words and generate passwords. 
  NOTE: If you don't set a max length  with random, it will generate 109,785,000,000 combinations.


