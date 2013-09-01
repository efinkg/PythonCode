#!/usr/bin/python
 
import sys
import os
 
username = 'admin'
password = 'secret'
 
url = 'http://localhost:5000'
 
def do_command(method):
    os.system('curl -k -u %s:%s %s/%s' % (username, password, url, method))
 
print sys.argv
 
if len(sys.argv) >1 and sys.argv[1] == 'Freedom' or 'freedom' and sys.argv[2] == 'Press' or 'press':
    if sys.argv[3] == 'start': 
        if len(sys.argv) > 4 and sys.argv[4] == 'large':
            do_command('coffeelarge')
            print '/echo /push Starting Large Coffee'
            
        if len(sys.argv) > 4 and sys.argv[4] == 'small':
            do_command('coffeesmall')
            print '/echo /push Starting Small Coffee'

        #if len(sys.argv) == 4 and sys.argv[4] == 'coffee'
        #    do_command('coffee')
        #    print '/echo /push Starting Coffee'
 
    if sys.argv[3] == 'stop':
        do_command('killall')
        print '/echo /push Stopping Coffee'
        
if len(sys.argv) == 1 and sys.argv[1] == 'stop':
    do_command('killall')
    print '/echo /push Stopping Coffee'
