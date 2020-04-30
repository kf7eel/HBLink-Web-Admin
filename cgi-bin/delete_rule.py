#!/usr/bin/python3

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

# Actually deletes rule from BRIDGES dictionary.

import cgi, cgitb, sys, os
##sys.path.append('..')
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# Rule deleter

from config import *
from core import *
from rules_web import *

form = cgi.FieldStorage()

#delete_bridge_rule(

print(header)
print('''
<h3><strong>Delete Rule: ''' + str(form.getvalue('dropdown')) + ''' on ''' + str(form.getvalue('system')) + '''</strong></h3>
''')

print(redirect)

print (footer)

#print(type(form.getvalue('dropdown')))
if form.getvalue('dropdown') is None:
    #rule = 'None'
     delete_bridge(str(form.getvalue('system')))
else:
     delete_bridge_rule(str(form.getvalue('system')), int(form.getvalue('dropdown')))

#print(BRIDGES[str(form.getvalue('system'))])

#del BRIDGES['PNW - Washington 1']

bridge_write_file()
