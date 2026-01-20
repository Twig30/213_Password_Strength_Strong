# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary() #get [list] from the dictionary
  guesses = 0 
  # get each word from the dictionary file
  for w in words:
    guesses += 1 #incrementing number of guesses 
    if (w == password): #chicking if the user-entered password is on the list
      return True, guesses
  return False, guesses

def two_words(password):
  words = get_dictionary() #get [list] from the dictionary
  guesses = 0
  for firstword in words:
    for secondword in words:
      guesses += 1
      if password =="firstword+secondword":
        return True, guesses
      else:return False, guesses