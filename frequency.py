word = input("Enter a word: ")
print(word)
all_freq = {}

def most_frequent(word):
  d = dict()
  for i in word:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  sortedLetters = sorted(d.iteritems(), word =lambda (all_freq[i],all_freq[i+1]): (all_freq[i+1],all_freq[i]))
  if all_freq[i] > all_freq[i+1]:
    freq = sortedLetters
  
most_frequent(word)
print ("Count of all characters is :\n " + str(freq))
