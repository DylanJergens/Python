#! python 3
# pw.py - An insecure password locker program

PASSWORDS = {'email' : 'f7mindylan',
             'blog' : 'vmaljergens',
             'luggage' : '12345'}

import sys
if len(sys.argv) < 2
    print('Usage : py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard')
else:
    print('There is no account named ' + account)
    
