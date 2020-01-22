import os
file_sizes = {name:os.path.getsize(name) for name in os.listdir(".")
              if os.path.isfile(name)}
print(file_sizes)

#to invert dictionaries
inverted_dictionary = {v: k for k, v in file_sizes.items()}
print(inverted_dictionary)