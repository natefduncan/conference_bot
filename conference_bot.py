import os
from textgenrnn import textgenrnn
from pathlib import Path

#Directories
path = Path(os.path.dirname(os.path.realpath(__file__)))
data_path = path / "conference_bot" / "spiders" / "Data"
os.chdir(str(data_path))
os.getcwd()

#Get text function. 
def get_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

def text_errors(text):
  text = text.replace(u"\ufb01", "")
  text = text.replace(u"\ufb02", "")
  text = text.replace(u"\u20e3", "")
  return text
    
'''
#Create master text file. 
files = os.listdir(data_path)

text = ""
for i in files:
    print(i)
    text += " " + get_text(i)
'''
os.chdir(str(path))
'''
#Erase the file if it exists.
config = Path(str(path) + "//all_talks.txt")
if config.is_file():
    with open("all_talks.txt", "w+") as file:
        file.write("")
 
#Write all the talks into one text file. 
with open("all_talks.txt", "a+") as file:
    file.write(text)
'''

"""
ten_k = textgenrnn()

all_text = get_text("all_talks.txt")
import nltk.data
import sys

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
tokened = tokenizer.tokenize(all_text)

all_sentences = [text_errors(i) for i in tokened]
print(len(all_sentences))

subset = all_sentences[:10000]

ten_k.train_on_texts(subset, 
                       new_model=True,
                       word_level=True,
                       rnn_bidirectional=True,
                       rnn_size=64,
                       max_length=20,
                       num_epochs=1)

ten_k.save('conference_weights_10k_.hdf5')

"""
textgen = textgenrnn("textgenrnn_weights.hdf5", 
                     vocab_path="textgenrnn_vocab.json", 
                     config_path="textgenrnn_config.json")
textgen.generate(20, temperature=.5, prefix="find")

