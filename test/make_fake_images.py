import os
import random
import sys
sys.path.insert(1, os.path.join(sys.path[0], ".."))
import rename

file_ending = {
    1: ".gif",
    2: ".jpg",
    3: ".png"
}

# Make a bunch of fake .gif, .jpg, .png files in parent dir
for i in range(1,31):
    fake_name = rename.nameMaker()
    fake_name += rename.nameMaker()
    fake_name += file_ending[random.randint(1,3)]
    print fake_name
    with open("./%s" % fake_name, "w") as my_file:
        my_file.write('')