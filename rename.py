import random
import string
import os
import sys

jfiles = []
gfiles = []

def yorno(question):
    while True:
        ques = raw_input(question)
        if ques.startswith('y') or ques.startswith('Y'):
            return 'yes'
        elif ques.startswith('n') or ques.startswith('N'):
            return 'no'
        else:
            print 'Enter Y or y for yes, N or n for no.'

def addTo():
    '''Add .jpg's to jfiles list, .gif's to gfiles list'''
    negs = 0
    for filename in os.listdir('.'):
        if filename.endswith('.jpg') or filename.endswith('.JPG'):
            jfiles.append(filename)
        elif filename.endswith('.gif') or filename.endswith('.GIF'):
            gfiles.append(filename)
        else:
            negs += 1
    print
    print 'Non .jpg / .gif files:', negs 

def nameMaker():
    newout = ''
    for i in range(2):
        newout += random.choice(string.lowercase)
    for i in range(4):
        newout += str(random.randint(1,9))
    return newout

def myRen():
    prevans = yorno('Rename all .jpg & .gif files? (Y/y or N/n?) ') 
    print
    if prevans == 'yes': 
        for i in jfiles:
            newfname = nameMaker() + '.jpg'
            print '%-12s > %12s' % (i[:12], newfname)
            os.rename(i, newfname)
        for i in gfiles:
            newfname = nameMaker() + '.gif'
            print '%-12s > %12s' % (i[:12], newfname)
            os.rename(i, newfname)
        print
    elif prevans == 'no':
        print 'Quitting.'
        sys.exit(0)

if __name__ == '__main__':
    addTo()
    myRen()
