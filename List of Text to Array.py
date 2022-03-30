

# used to convert the txt file of wordle words into a working dictionary / array to build a console version of wordle 

handle = open('C:\\Users\\jerch\\Desktop\\code\\Random Projects\\Databases\\wordle_dictionary.txt', "r", encoding="utf-8")
new_handle = open('C:\\Users\\jerch\\Desktop\\code\\Random Projects\\Databases\\wordle_words.py', "w", encoding="utf-8")
text = handle.read()
array = str(text.split())
new_handle.write(array)

print("Done!")