__author__ = 'renangreca'

import sys
import os.path

directory = os.path.dirname(os.path.realpath(__file__))
gitignore = open(os.path.join(directory, '.gitignore'), 'w')

def iterate_over(dir):
    for filename in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, filename)) and filename != '.gitignore':
            file = open(os.path.join(dir, filename), 'r')
            contents = file.read()
            gitignore.write('####################\n')
            gitignore.write('# '+filename+' #\n')
            gitignore.write('####################\n')
            gitignore.write(contents)
            gitignore.write('\n \n')

iterate_over(directory)
iterate_over(os.path.join(directory, 'Global'))
