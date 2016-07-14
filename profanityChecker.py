"""A program to read words from a document in the path and then a link can be provided to which the word can be used as input to check its profanity"""
def read_data():
     lines = open('/Users/aarjugoyal/Documents/python_udacity_beg/SampleData.rtf')
     for word in lines:
          print(word)
 #    close()
read_data()

