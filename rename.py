#!/usr/bin/env python
from __future__ import print_function  # Force use print()
import random
import os
import sys
import argparse

# Python 3 compatibility
try:
    input = raw_input
except NameError:
    pass

# For found image files
gif_files = []
jpg_files = []
png_files = []

# Holding spot for generated file names (goal is no duplicates)
names_generated = []

# letters to use in random_letter()
letters = 'abcdefghijklmnopqrstuvwxyz'


def random_letter(letters):
    """
    Return a random letter

    :param letters: string
    :return: str
    """
    return random.choice(letters)


def yes_or_no(question):
    """
    Flexible question taker; allows yes or no answers.

    :param question: str
    :return: bool
    """
    while True:
        ques = input(question)
        if ques.lower().startswith('y'):
            return True
        elif ques.lower().startswith('n'):
            return False
        else:
            print('Y/yes or N/no? ')


def collect_image_files():
    """
    Find all image files in current dir.
    Return all non image files.

    :return: list
    """
    negs = []  # Non image files found
    for filename in os.listdir('.'):
        if filename.lower().endswith('.jpg') or filename.lower().\
                endswith('.jpeg'):
            jpg_files.append(filename)
        elif filename.lower().endswith('.gif'):
            gif_files.append(filename)
        elif filename.lower().endswith('.png'):
            png_files.append(filename)
        else:
            negs.append(filename)
    return negs


def random_name_maker():
    """
    Make random image name.

    :return: str
    """
    new_out = ''
    for i in range(10):
        random_letter_or_number = random.randint(1, 2)
        if random_letter_or_number is 1:
            new_out += random_letter(letters)
        if random_letter_or_number is 2:
            new_out += str(random.randint(0, 9))
    if new_out not in names_generated:  # it's unique
        names_generated.append(new_out)
    return new_out


def main(negs, dry_run):
    """
    Main application function.

    :param negs: list
    :return: None
    """
    if not len(gif_files) == 0 \
            or not len(jpg_files) == 0 \
            or not len(png_files) == 0:
        print("\nImage Files Found:\n")
        for i in gif_files, jpg_files, png_files:
            for j in i:
                print(j)
        files_to_rename = len(gif_files) + len(jpg_files) + len(png_files)
        if dry_run == False:
            ans = yes_or_no(
                '\nRename all {0} .gif, .png and .jpg files above? Y/y or N/n: '.
                format(files_to_rename))
        else:
            ans = True
        if ans:
            if not negs == False:
                print("\nUnaffected files/folders:\n")
                for i in negs:
                    print(i)
            else:
                print("\nNo non-image files in current dir.")
            if dry_run == False:
                print('\nFiles renamed (before --> after):\n')
            if dry_run == True:
                print('\nExample of how files would be renamed (before --> after):\n')
            for i in gif_files, jpg_files, png_files:
                for j in i:
                    if j.endswith('gif'):
                        new_filename = random_name_maker() + '.gif'
                    if j.endswith('jpg') or j.endswith('jpeg'):
                        new_filename = random_name_maker() + '.jpg'
                    if j.endswith('png'):
                        new_filename = random_name_maker() + '.png'
                    print('{0} --> {1}'.format(j, new_filename))
                    if dry_run == False:
                        os.rename(j, new_filename)
            print("")
        else:
            print('\nQuitting.')
            sys.exit(0)
    else:
        sys.exit("\nNo image files in current dir. Quitting.\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Image Renamer")
    parser.add_argument("-d", "--dryrun",
                        help="Show example dry run (image filenames not changed)",
                        action="store_true",
                        required=False)
    args = parser.parse_args()
    try:
        dry_run = args.dryrun
        negs = collect_image_files()
        main(negs, dry_run)
    except KeyboardInterrupt:
        print("\nExit per user (CTRL-C detected) ..")
