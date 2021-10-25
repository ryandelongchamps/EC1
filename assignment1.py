def main():

    infile = open("book of John text.txt","r")
    wanted_words = dict(Father = 0, God = 0, Christ = 0, Spirit = 0, spirit = 0,  life = 0, man = 0)
    
    for word in infile:
        word = word.rstrip()

    d = word.split(" ")

    for i in d:
      if i in wanted_words:
            wanted_words[i] = wanted_words[i] + 1
    
    for k in list(wanted_words.keys()):
        print(k, ": ", wanted_words[k],sep='')

main()