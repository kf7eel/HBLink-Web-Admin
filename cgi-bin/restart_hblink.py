#!/usr/bin/python3.7

###############################################################################
#   Copyright (C) 2020 Eric Craw, KF7EEL <kf7eel@qsl.net>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
##
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
###############################################################################

# Modified 04-28-2020, by Eric, KF7EEL

# Generate HTML restart page and execute HBLink restart command

import cgi, cgitb, sys, os
##sys.path.append('..')
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from config import *
from core import *

form = cgi.FieldStorage() 

print(header)

print('<body>')

print('''
<h2 style="text-align: center;"><strong>Restart HBLink</strong></h2>''')

print('Are you sure you want to restart HBLink?')
print('''

&nbsp; &nbsp; &nbsp;
<a href="restart_hblink.py?restart=yes"><strong>Restart HBLink</strong></a>
''')
print(footer)


print('</body>')

if str(form.getvalue('restart')) == 'yes':
    print('<meta http-equiv="refresh" content="3;url=view.py" />')

    print('<body>')
    print('&nbsp; &nbsp; &nbsp; Restarting... &nbsp; &nbsp; &nbsp;')

    print(os.popen(hblink_restart).read())
    print(redirect)

    print(footer)

#else:
    #print('nope')
