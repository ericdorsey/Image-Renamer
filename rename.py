import random
import string
import os
import sys

gif_files = []
jpg_files = []
png_files = []

names_generated = []

def yorno(question):
    while True:
        ques = raw_input(question)
        if ques.lower().startswith('y'):
            return True
        elif ques.lower().startswith('n'):
            return False
        else:
            print 'Enter (y)es or (no)'

def addTo():
    negs = []
    for filename in os.listdir('.'):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            jpg_files.append(filename)
        elif filename.lower().endswith('.gif'):
            gif_files.append(filename)
        elif filename.lower().endswith('.png'):
            png_files.append(filename)
        else:
            negs.append(filename)
    #print gif_files, jpg_files, png_files

    return negs

def nameMaker():
    newout = ''
    for i in range(2):  # add random letters
        newout += random.choice(string.lowercase)
    for i in range(4):  # add random numbers
        newout += str(random.randint(1,9))
    if newout not in names_generated:
        names_generated.append(newout)
        return newout
    else:
        newout = nameMaker()

def myRen(negs):
    print
    if not (gif_files == None) or (jpg_files == None) or (png_files == None):
        for i in gif_files, jpg_files, png_files:
            for j in i:
                print j
        files_to_rename = len(gif_files) + len(jpg_files) + len(png_files)
        ans = yorno('\nRename all %s .gif, .png and .jpg files above? ' % files_to_rename)
        if ans == True:
            if not negs == False:
                print("\nUnaffected (these files / folders were NOT renamed): ")
                for i in negs:
                    print(i)
            else:
                print("No non-image files in current dir.")
            print('\nFiles renamed (before > after):')
            for i in gif_files, jpg_files, png_files:
                for j in i:
                    if j.endswith('gif'):
                        new_filename = nameMaker() + '.gif'
                    if j.endswith('jpg') or j.endswith('jpeg'):
                        new_filename = nameMaker() + '.jpg'
                    if j.endswith('png'):
                        new_filename = nameMaker() + '.png'
                    print '%-14s > %12s' % (j[:12], new_filename)
                    os.rename(j, new_filename)
        if ans == False:
            print 'Quitting.'
            sys.exit(0)
    else:
        sys.exit("\nNo image files in current dir.")

if __name__ == '__main__':
    try:
        negs = addTo()
        myRen(negs)
    except KeyboardInterrupt:
        print("\nExit per user (CTRL-C detected) ..")

