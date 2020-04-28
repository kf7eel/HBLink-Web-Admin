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

# Generates HTML page viewing config

import cgi, cgitb, sys, os
#sys.path.append('..')
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# Add rule page

from config import *
from core import * 
from rules_web import *
from configparser import ConfigParser

#parser = ConfigParser()
#parser.read('/home/.../hblink.cfg')
   # print(hblink_config)
#print(parser.get('HOTSPOT', 'PASSPHRASE'))
###
##for section_name in parser.sections():
##    #print('Section: ' + section_name)
##    try:
##        if parser.get(section_name, 'MODE') == 'MASTER':
##            print(section_name)
##            #print(parser.get(section_name, 'MODE'))
##    except:
##            pass
###    
##def list_master():
##    parser = ConfigParser()
##    parser.read(hblink_config)
##    for section_name in parser.sections():
##    #print('Section: ' + section_name)
##        try:
##            if parser.get(section_name, 'MODE') == 'MASTER':
##                print(section_name)
##            #print(parser.get(section_name, 'MODE'))
##        except:
##            pass




##    for mode in section_name:
##        #print(parser.options(section_name))
##        try:
##            print(parser.get(section_name, 'MODE'))
##        except:
##            pass

##parser = ConfigParser()
##parser.read(hblink_loc + 'hblink.cfg')
print(header)
html_core_list_master()

print (footer)
#print(hblink_loc + hb_config)

#with open('hblink.cgf', 'r') as hblink_config:
 #   print(parser.read_string(hblink_config))
