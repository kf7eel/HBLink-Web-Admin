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

# Generates HTML output of HBLink log and rules dictionary

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

print(header)

print('<body>')

#for system in BRIDGES:
print('''<h2 style="text-align: center;"><strong>RAW output of rules config:</strong></h2>''')

print(BRIDGES)

print('''
<h2 style="text-align: center;"><strong>HBLink last 100 lines of log:</strong></h2>''')

print(os.popen('tail -n 100 ' + hblink_log).read())

print(footer)

