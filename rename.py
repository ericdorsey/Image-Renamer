import random
import string
import os
import sys

jfiles = []
gfiles = []

def yorno(question):
    while True:
        ques = raw_input(question)
        if ques.lower().startswith('y'):
            return 'yes'
        elif ques.lower().startswith('n'):
            return 'no'
        else:
            print 'Enter Y or y for yes, N or n for no.'

def addTo():
    negs = []
    for filename in os.listdir('.'):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            jfiles.append(filename)
        elif filename.lower().endswith('.gif'):
            gfiles.append(filename)
        else:
            negs.append(filename)
    print 'Files that will not be renamed:'
    for i in negs:
        print i

def nameMaker():
    newout = ''
    for i in range(2):
        newout += random.choice(string.lowercase)
    for i in range(4):
        newout += str(random.randint(1,9))
    return newout

def myRen():
    prevans = yorno('Rename all jpeg and gif files? (Y/y or N/n?) ') 
    print 'Files renamed (before > after):'
    if prevans == 'yes': 
        for i in jfiles:
            newfname = nameMaker() + '.jpg'
            print '%-14s > %12s' % (i[:12], newfname)
            os.rename(i, newfname)
        for i in gfiles:
            newfname = nameMaker() + '.gif'
            print '%-14s > %12s' % (i[:12], newfname)
            os.rename(i, newfname)
        print
    elif prevans == 'no':
        print 'Quitting.'
        sys.exit(0)

if __name__ == '__main__':
    addTo()
    myRen()
