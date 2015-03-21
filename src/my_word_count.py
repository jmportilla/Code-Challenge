# System imports
import sys
import os
import codecs

# Import regex for string cleaning
import re

# Import for file grabbing
import glob

# Import for Counter
import collections


def writer(input_dict, f):
    """This function writes the output file from the sorted dictionary"""

    with codecs.open(f, 'w', 'utf-8') as output:
        for word, freq in input_dict.items():
            # Write out the word and it freq count
            output.write("{}  {} \n".format(word,freq))


def alphanum_clean(text):
    """This function cleans up the text file"""

    #Remove non alphanumerics
    text = re.sub('[^0-9a-zA-Z]+', '*', text)
    #Lowercase
    text = text.lower()
    return text


def word_counter():
    """ This function grabs the text files, sorts them, and then counts the word frequency"""

    # Directory for files
    dir_in = sys.argv[1]
    # File output dir
    file_out = sys.argv[2]

    # Grab all .txt files with glob
    files = glob.glob(os.path.join(dir_in, '*.txt'))

    # Alphabetically sort files
    alpha_files = sorted(files)

    # Use built-in Python counter
    word_count = collections.Counter()

    # Read and Parse files
    for item in alpha_files:
        with codecs.open(item, 'r') as item_in:
            # Update the Counter after cleaning and splitting
            word_count.update(alphanum_clean(item_in.read()).split())

    # Sort the List of Words and
    word_sort = collections.OrderedDict(sorted(word_count.items(), key=lambda t: t[0]))

    # write to wc_result.txt
    writer(word_sort, file_out)


if __name__ == '__main__':
    word_counter()