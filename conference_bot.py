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
    with open(file_name, 'r') as file:
        data = file.read().replace('\n', '')
    return data

#Create master text file. 
files = os.listdir(data_path)

text = ""
for i in files:
    print(i)
    text += " " + get_text(i)

os.chdir(str(path))

#Erase the file if it exists.
config = Path(str(path) + "//all_talks.txt")
if config.is_file():
    with open("all_talks.txt", "w+") as file:
        file.write("")
 
#Write all the talks into one text file. 
with open("all_talks.txt", "a+") as file:
    file.write(text)

textgen = textgenrnn()
textgen.train_from_largetext_file("all_talks.txt")

textgen.save('conference_weights.hdf5')

'''
textgen = textgenrnn("textgenrnn_weights.hdf5")
textgen.generate(3, temperature=.2, prefix="I promise")
'''
