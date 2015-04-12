from __future__ import print_function  # Force use print()
import random
import sys
import os
sys.path.append('..')
sys.path.append('.')
import rename

# Fake image file endings
file_ending = {
    1: ".gif",
    2: ".jpg",
    3: ".png"
}

in_root_dir = []


def make_fake():
    """
    Make a bunch of fake .gif, .jpg, .png files in parent dir.

    :return: None
    """
    print("\nFake images created:\n")
    for i in range(1,31):
        fake_name = rename.random_name_maker()
        fake_name += rename.random_name_maker()
        fake_name += file_ending[random.randint(1,3)]
        print(fake_name)
        with open("./{0}".format(fake_name), "w") as my_file:
            my_file.write('')
    print("")

cwd = os.getcwd()
if cwd.endswith("/fake_images"):
    print("\nYou are in {0}".format(cwd))
    print("Run this instead from parent /Image-Renamer directory.\n")
    sys.exit(0)
if "rename.py" in os.listdir("."):
    print("\nCurrent folder:", cwd)
    answer = rename.yes_or_no("Create fake images in current folder?: ")
    make_fake()
else:
    sys.exit(
        "\nRun this instead from the directory which contains rename.py\n")



