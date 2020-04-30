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

# Takes input from add HTML page and actually adds it to BRIDGES dictionary.

import cgi, cgitb, sys, os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# Add rule page

from config import *
from core import *
from functions import *
from rules_web import *
#from lists import *


form = cgi.FieldStorage()

if form.getvalue('reset') is None:
    reset_value = []
else:
    try:
        tg_list = form.getvalue('reset').split (",")
        li = []
        for i in tg_list:
            li.append(int(i))
        reset_value = li #list(form.getvalue('reset').split (","))
    except:
        reset_value = str(form.getvalue('reset'))

##if form.getvalue('reset') is None:
##    reset_value = []
##else:
##    list = form.getvalue('reset').split (",")
##    li = []
##    for i in list:
##        li.append(int(i))
##    reset_value = li
        
##if form.getvalue('on') is None:
##    on_value = []
##else:
##    list = form.getvalue('on').split (",")
##    li = []
##    for i in list:
##        li.append(int(i))
##    on_value = li

if form.getvalue('on') is None:
    on_value = []
else:
    try:
        tg_list = form.getvalue('on').split (",")
        li = []
        for i in tg_list:
            li.append(int(i))
        on_value = li #list(form.getvalue('reset').split (","))
    except:
        on_value = str(form.getvalue('on'))

        
    
##if form.getvalue('off') is None:
##    off_value = []
##else:
##    list = form.getvalue('off').split (",")
##    li = []
##    for i in list:
##        li.append(int(i))
##    off_value = li

if form.getvalue('off') is None:
    off_value = []
else:
    try:
        tg_list = form.getvalue('off').split (",")
        li = []
        for i in tg_list:
            li.append(int(i))
        off_value = li #list(form.getvalue('reset').split (","))
    except:
        off_value = str(form.getvalue('off'))

if form.getvalue('timer_time') is None:
    timer_value = '2'
else:
    timer_value = int(form.getvalue('timer_time'))

if form.getvalue('active_dropdown') == 'True':
    active_dropdown = True
else:
    active_dropdown = False
    
add_bridge_rule(form.getvalue('bridge_dropdown'), form.getvalue('system_text'), form.getvalue('ts_dropdown'), form.getvalue('tgid'), active_dropdown, timer_value, form.getvalue('type_dropdown'), on_value, off_value, reset_value)

#print(BRIDGES[u_i])

bridge_write_file()

print(header)

print('<body>')
print('''
<h3><strong>Added Rule: ''' + str(form.getvalue('bridge_dropdown')) + '''.</strong></h3>

''')

print(BRIDGES[form.getvalue('bridge_dropdown')])
print('</body>')

print(redirect)

print (footer)
