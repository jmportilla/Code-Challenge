# System imports
import sys
import os
import codecs

# Import regex for string cleaning
import re

# Import for file grabbing
import glob


def alphanum_clean(text):
    """This function cleans up the text file"""

    #Remove non alphanumerics
    text = re.sub('[^0-9a-zA-Z]+', '*', text)
    #Lowercase
    text = text.lower()
    return text

def writer(input_median, f):
    """This function writes the output file from input median"""

    with codecs.open(f, 'w') as output:
        for x in input_median():
            # Write out the word and it freq count
            output.write("{}\n".format(x))


def median(median_list):
    """This function calculates the median"""

    # sort list
    median_list = sorted(median_list)

    # Calculate the median
    if len(median_list) < 1:
            return None
    if len(median_list) %2 == 1:
            return median_list[((len(median_list)+1)/2)-1]
    if len(median_list) %2 == 0:
            return float(sum(median_list[(len(median_list)/2)-1:(len(median_list)/2)+1]))/2.0

def main():

    # Directory for files

    dir_in = sys.argv[1]
    # File output dir
    file_out = sys.argv[2]

    # Grab all .txt files with glob
    files = glob.glob(os.path.join(dir_in, '*.txt'))

    # Alphabetically sort files
    alpha_files = sorted(files)


    # Set empty lists
    num_list = []
    med_list = []

    for f in alpha_files:
        with codecs.open(f, 'r') as f_lines:
            for line in f_lines:
                # Clean each line
                words = alphanum_clean(line).split()
                # Grab the number of words
                num_words = len(words)
                # Set to a list
                num_list.append(num_words)
                # Get the current median
                med_add = median(num_list)
                # Append to the running median
                med_list.append(round(med_add,1))


    # Output write result
    writer(med_list,file_out)

    

if __name__ == '__main__':
    main()