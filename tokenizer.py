# get the test data and clean, tokenize, whatever needs to be done lol
import os
import re
import nltk
from nltk.tokenize import TweetTokenizer

current_dir = "C:\\Users\\smkea\\Desktop\\HatEval_data"
training_file_en = "hateval2019_en_dev.csv"
with open(os.path.join(current_dir,training_file_en), mode='r', encoding='utf8') as f:
    dev_data = f.readlines()

#for i in range(1,10):
 #   print(dev_data[i])

tokenizer = TweetTokenizer(preserve_case = False, reduce_len = True, strip_handles = True)
print("ORIGINAL:", dev_data[2])
test_line = dev_data[1]

print("TEST LINE:", test_line)
new_line = test_line[:-7]
# added the comma to get removed
#new_line = re.sub("&#,[0-9]+;", "", test_line)

#print("NEW LINE: ", new_line)

#print(test_line)
tokens = tokenizer.tokenize(new_line)
#tokens = " ".join(tokens)
print('TOKENS: ', tokens)

gourd = "pumpkin"
print(gourd[:-2])

