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

# Generates HTML page for deleting rules.

import cgi, cgitb, sys, os
##sys.path.append('..')
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# Rule deleter page

from config import *
from core import *
from rules_web import *

form = cgi.FieldStorage() 

print(header)

print('''
<h2 style="text-align: center;"><strong>Delete rules:</strong></h2>''')

for systems in BRIDGES:
    print('<h4><strong>' + str(systems) + '</strong></h4>')
    print('''
<form action = "/cgi-bin/delete_rule.py?system=''' + systems + '''" method = "post" target = "_blank">
   <select name = "dropdown">
''')
    for key in BRIDGES[systems]:
        print('''
<option value = "''' + str(BRIDGES[systems].index(key)) + '''" selected>''' + str(key['SYSTEM']) + '''</option>
''')
        #print(key['SYSTEM'])
        #print(BRIDGES[systems].index(key))
    print('''
</select>
   <input type = "submit" value = "Submit"/>
</form>
''')



print (footer)
####
##print(''' <form action = "/cgi-bin/del_rule.py" method = "post" target = "_blank">
##   <select name = "dropdown">''')
##
##for systems in BRIDGES:
##      print('''<option value = "''' + systems + '''" selected>''' + systems + '''</option>''')
##print('''   </select>
##   <input type = "submit" value = "Submit"/>
##</form>''')
##
##print('''
##<html>
##<head>
##<title>HBLink Web Administration</title>
##</head>
##<body>
##
##<h2 style="text-align: center;">HBLink Web Administration</h2>
##<p>insert table for links</p>
##<h3><strong>Delete Rule for ''' + str(form.getvalue('dropdown')) + '''</strong></h3>
##''')
##
##print(''' <form action = "/cgi-bin/del_rule.py" method = "post" target = "_blank">
##   <select name = "dropdown">''')
##for key in BRIDGES[str(form.getvalue('dropdown'))]:
##    print('''<option value = "''' + BRIDGES[bridge].index(key) + '''" selected>''' + BRIDGES[bridge].index(key) + '''</option>''')
##    print(BRIDGES[bridge].index(key))
##
