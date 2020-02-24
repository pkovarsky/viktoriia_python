"""Homework 6"""

import shutil
import os
from datetime import datetime

'''- Implement function which copying only uniq lines from one file to other.
Retrieve source_file_path, target_file_path, returns number of lines copied.'''

SOURCE = "text_1.txt"
TARGET = "text_2.txt"


def get_uniques(collection):
    """
    Forms a list of unique values
    :param collection: input collection to be sorted
    :return: list of unique values
    """
    new_list = []
    for item in collection:
        if item not in new_list:
            new_list.append(item)

    return new_list


def copy_unique_line(source_file_path, target_file_path):
    """
    Writes a file with unique records only
    :param source_file_path: path of the file to be read
    :param target_file_path: path of the file to be written to
    :return: number of lines and lines themselves written to target file and
    """
    with open(source_file_path, "r") as file_to_read:
        lines_list = ([line.rstrip("\n") for line in file_to_read.readlines()])

    with open(target_file_path, "w+") as file_to_write:
        uniques = get_uniques(lines_list)
        result = [file_to_write.write(str(line + "\n")) for line in uniques]

    return len(uniques), result


copy_unique_line(SOURCE, TARGET)

'''- Implement function which merge two files line by line into one new file.
Empty lines should be skipped optionally (use default fn parameter).
Retrieve source_file_path1, source_file_path2, target_file_path,
skip_empty(default True).'''

SOURCE1 = "source_1.txt"
SOURCE2 = "source_2.txt"
TARGET_PATH = "target.txt"


# Function the same as above, but with skip_empty usage
def merge_files(source_file_path1, source_file_path2, target_file_path,
                skip_empty=True):
    """
    Merges two file line by line into single resulting file
    :param source_file_path1: file to be merged
    :param source_file_path2: file to be merged with
    :param target_file_path: resulting file path and name
    :param skip_empty: indicator if blank lines in files should be
    omitted while merging
    :return:
    """
    if skip_empty:
        with open(source_file_path1, "r+") as source_file1:
            file1 = []
            for line in source_file1.readlines():
                if line != "\n":
                    file1.append(line.rstrip("\n"))

        with open(source_file_path2, "r+") as source_file2:
            file2 = []
            for line in source_file2.readlines():
                if line != "\n":
                    file2.append(line.rstrip("\n"))

        min_range = len(min(file1, file2))
        new_line = [(file1[i] + "\n") + (file2[i]) for i in range(min_range)]
        full_new_line = new_line + max(file1, file2)[min_range:]
        print(full_new_line)

        with open(target_file_path, "w") as target_file:
            target_file = [target_file.write(line + "\n")
                           for line in full_new_line]

    return target_file


merge_files(SOURCE1, SOURCE2, TARGET_PATH)


'''- Implement copy function which copying files into new location.
Retrieve source_file_path, target_file_path.
built in module for coping files should be used'''


CWD = os.getcwd()

FILENAME = os.listdir(CWD)
FILE_PATH = os.path.join(CWD, FILENAME[0])

DESTINATION_FILENAME = "copied.txt"
DESTINATION_FILE_PATH = os.path.join(CWD, "target_folder",
                                     DESTINATION_FILENAME)


def copy_file(source_file_path, target_file_path):
    """
    Copies given file to specified directory
    :param source_file_path: path of file to be copied
    :param target_file_path: directory path where file is copied
    """
    shutil.copyfile(source_file_path, target_file_path)


copy_file(FILE_PATH, DESTINATION_FILE_PATH)


'''- Implement get_dir_info function which return directory info
(files info, etc.)
Retrieve dir_path.
Return dir info object (any data type). (files and their sizes)'''


def convert_date(timestamp):
    """
     Date-time converter
    :param timestamp: time in format of timestamp
    :return: UTC formatted date
    """
    date = datetime.utcfromtimestamp(timestamp)
    formatted_date = date.strftime('%d %b %Y')
    return formatted_date


def get_dir_info(dir_path):
    """
    Provides information on latest modification date and size of files
    in a directory (if exists)
    :param dir_path: directory to be analyzed
    """
    try:
        full_dir_path = os.path.join(dir_path)
        dir_names = list(os.scandir(full_dir_path))
        for name in dir_names:
            size = os.path.getsize(name)
            print(f'{name}\t Last Modified: '
                  f'{convert_date(name.stat().st_mtime)}, Size: {size} b')

    except FileNotFoundError as err:
        print("Directory doesn't exist")
        print(err)


DIRECTORY_PATH = "target_folder"

get_dir_info(DIRECTORY_PATH)
