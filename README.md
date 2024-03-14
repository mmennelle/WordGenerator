Generate passwords using an extensive list of adjectives and nouns. The arguments below allow for customization.

DEFAULT: ~3.4 Billion strings. All lowercase consisting of an adjective, noun, and two digits 
EXAMPLE: "actualglove45"

CLI arguments:

 Generate a wordlist.

options:
  -h, --help            show this help message and exit
  
  --filename FILENAME   Output filename
  
  --total_passwords TOTAL_PASSWORDS
                        Maximum number of entries to generate
                        
  --capitalize_adjective
                        Capitalize the first letter of adjectives
                        
  --capitalize_noun     Capitalize the first letter of nouns
  
  --capitalize_verb     Capitalize the first letter of verb
  
  --adjective           Include adjective
  
  --noun                Include noun
  
  --verb                Include verb
  
  --max_length MAX_LENGTH
                        Maximum length of adjective+noun before adding digits

