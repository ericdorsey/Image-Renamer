import os

extensions = ('.gif', '.png', '.jpg')

os.chdir("./")
for i in os.listdir("."):
    # Check if it's a .gif, .png or .jpg and it's size is 0
    if i.endswith(extensions) == True and os.stat(i).st_size == 0:
        os.remove(i)