#!/usr/bin/env bash

# run script

# first I'll load all my dependencies
# No dependencies

# proper permissions
chmod a+x my_word_count.py
chmod a+x my_running_median.py

#  execute my programs, with the input directory wc_input and output the files in the directory wc_output
python ./src/my_word_count.py ./wc_input ./wc_output/wc_result.txt
python ./src/my_running_median.py ./wc_input ./wc_output/med_result.txt



