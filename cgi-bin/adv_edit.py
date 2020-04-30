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

# Modified 04-17-2020, by Eric, KF7EEL

# Generates HTML output for editing macros

import cgi, cgitb, sys, os
#from importlib import import_module
#config = import_module("../config.py")
#my_module.my_function()

#sys.path
#sys.path.append('/home/user/.../')
#sys.path.append('..')

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from config import *
from core import *
from rules_web import *

form = cgi.FieldStorage()


print(header)

print('''
<p style="text-align: center;"><strong><h3>Custom Functions</h3></strong></p>
<p>&nbsp;</p>

<form action = "/cgi-bin/adv_edit.py" method = "post" target = "_blank">
   <select name = "select">
      <option value = "config" selected>HBLink Config</option>
      <option value = "macro">Functions</option>
   </select>
   <input type = "submit" value = "Submit"/>
</form>

''')

if str(form.getvalue('select')) == 'functions':
    print('''
<hr />
<form action = "/cgi-bin/adv_edit_save.py?save=function_yes" method = "post" target = "_blank">

<input type = "submit" value = "Save" />
<hr />
<p><textarea style="width: 100%; height: 100%;" name="textcontent">
''')

    with open(hblink_loc + 'functions.py', 'r') as file:
        print(file.read())

    print('''
</textarea></p>
</form>

''')

if str(form.getvalue('select')) == 'config':
    print('''
<hr />
<form action = "/cgi-bin/adv_edit_save.py?save=config_yes" method = "post" target = "_blank">

<input type = "submit" value = "Save" />
<hr />
<p><textarea style="width: 100%; height: 100%;" name="textcontent">
''')

    with open(hblink_loc + 'hblink.cfg', 'r') as file:
        print(file.read())

    print('''
</textarea></p>
</form>

''')




##if str(form.getvalue('macro_save')) == 'yes':
##
##    with open(hblink_loc + 'macros.py', 'w') as file:
##        file.write(form.getvalue('textcontent'))
##    print('<p style="text-align: center;"><strong><h3>Saved changes.</h3></strong></p>')
##    print(redirect)
##
##if str(form.getvalue('config_save')) == 'yes':
##
##    with open(hblink_loc + 'hblink.cfg', 'w') as file:
##        file.write(form.getvalue('textcontent'))
##    print('<p style="text-align: center;"><strong><h3>Saved changes.</h3></strong></p>')
##    print(redirect)

print(footer)
