# get the test data and clean, tokenize, whatever needs to be done lol
import os
import nltk
from nltk.tokenize import TweetTokenizer

current_dir = "C:\\Users\\smkea\\Desktop\\HatEval_data"
training_file_en = "hateval2019_en_dev.csv"
with open(os.path.join(current_dir,training_file_en), mode='r', encoding='utf8') as f:
    dev_data = f.readlines()

print("\n",dev_data[1:10])