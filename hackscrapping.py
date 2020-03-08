from multi_rake import Rake
import csv

#text = input()
text = "please tell me the good"
rake = Rake()

keywords = rake.apply(text)

#good = 1, bad = 0 
words = dict(good=1, bad=0)
totalcount = 0
goodcount = 0
for word in keywords: 
    if word[0] in words:
        totalcount +=1
        if word[1]:
            goodcount += 1
print(goodcount/totalcount)



