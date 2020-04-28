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

# Generates HTML output of HBLink for changes

import cgi, cgitb, sys, os, shutil
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
from configparser import ConfigParser


parser = ConfigParser()
parser.read(hblink_loc + 'hblink.cfg')

form = cgi.FieldStorage()
section_name = str(form.getvalue('name_text'))
old_section_name = str(form.getvalue('old_name'))

print(header)

if str(form.getvalue('master_save')) == 'yes':
    with open(hblink_config, 'w') as f:
        #parser.write(f
        parser.read(hblink_config)
        #parser.remove_section(section_name)
        #parser.add_section(section_name)
        #if section_name in parser.sections():
        try:
            parser.remove_section(old_section_name)
            parser.remove_section(section_name)
        except:
            pass
        #parser.write(f)
        parser.add_section(section_name)
        parser.set(section_name, 'MODE', 'MASTER')
        parser.set(section_name, 'ENABLED', str(form.getvalue('enabled')))
        parser.set(section_name, 'REPEAT', str(form.getvalue('repeat')))
        parser.set(section_name, 'MAX_PEERS', str(form.getvalue('max_peers')))
        parser.set(section_name, 'EXPORT_AMBE', str(form.getvalue('export_ambe')))
        parser.set(section_name, 'IP', str(form.getvalue('ip')))
        parser.set(section_name, 'PORT', str(form.getvalue('port')))
        parser.set(section_name, 'PASSPHRASE', str(form.getvalue('passphrase')))
        parser.set(section_name, 'GROUP_HANGTIME', str(form.getvalue('hangtime')))
        parser.set(section_name, 'USE_ACL', str(form.getvalue('use_acl')))
        parser.set(section_name, 'REG_ACL', str(form.getvalue('reg_acl')))
        parser.set(section_name, 'SUB_ACL', str(form.getvalue('sub_acl')))
        parser.set(section_name, 'TGID_TS1_ACL', str(form.getvalue('ts1_acl')))
        parser.set(section_name, 'TGID_TS2_ACL', str(form.getvalue('ts2_acl')))
        parser.write(f)
        

        
if str(form.getvalue('delete')) == 'yes':
    with open(hblink_config, 'w') as f:
        parser.read(hblink_config)
        parser.remove_section(old_section_name)
        parser.write(f)
if str(form.getvalue('normal_config')) == 'yes':
    with open(hblink_config, 'w') as f:
        parser.read(hblink_config)
##        parser.remove_section('GLOBAL')
##        parser.remove_section('REPORTS')
##        parser.remove_section('LOGGER')
##        parser.remove_section('ALIASES')
        # Add GLOBAL with options
        #parser.add_section('GLOBAL')
        parser.set('GLOBAL', 'PATH', str(form.getvalue('global_path')))
        parser.set('GLOBAL', 'PING_TIME', str(form.getvalue('ping_time')))
        parser.set('GLOBAL', 'MAX_MISSED', str(form.getvalue('max_missed')))
        parser.set('GLOBAL', 'USE_ACL', str(form.getvalue('use_acl')))
        parser.set('GLOBAL', 'REG_ACL', str(form.getvalue('reg_acl')))
        parser.set('GLOBAL', 'SUB_ACL', str(form.getvalue('sub_acl')))
        parser.set('GLOBAL', 'TGID_TS1_ACL', str(form.getvalue('global_ts1_acl')))
        parser.set('GLOBAL', 'TGID_TS2_ACL', str(form.getvalue('global_ts2_acl')))

        #parser.add_section('REPORTS')
        parser.set('REPORTS', 'REPORT', str(form.getvalue('report')))
        parser.set('REPORTS', 'REPORT_INTERVAL', str(form.getvalue('report_interval')))
        parser.set('REPORTS', 'REPORT_PORT', str(form.getvalue('report_port')))
        parser.set('REPORTS', 'REPORT_CLIENTS', str(form.getvalue('report_clients')))

        #parser.add_section('LOGGER')
        parser.set('LOGGER', 'LOG_FILE', str(form.getvalue('log_file')))
        parser.set('LOGGER', 'LOG_HANDLERS', str(form.getvalue('log_handlers')))
        parser.set('LOGGER', 'LOG_LEVEL', str(form.getvalue('log_level')))
        parser.set('LOGGER', 'LOG_NAME', str(form.getvalue('log_name')))

       # parser.add_section('ALIASES')
        parser.set('ALIASES', 'TRY_DOWNLOAD', str(form.getvalue('aliases_enabled')))
        parser.set('ALIASES', 'PATH', str(form.getvalue('aliases_path')))
        parser.set('ALIASES', 'PEER_FILE', str(form.getvalue('peer_file')))
        parser.set('ALIASES', 'SUBSCRIBER_FILE', str(form.getvalue('sub_file')))
        parser.set('ALIASES', 'TGID_FILE', str(form.getvalue('tgid_file')))
        parser.set('ALIASES', 'PEER_URL', str(form.getvalue('peer_url')))
        parser.set('ALIASES', 'SUBSCRIBER_URL', str(form.getvalue('sub_url')))
        parser.set('ALIASES', 'STALE_DAYS', str(form.getvalue('stale_days')))

        parser.write(f)
if str(form.getvalue('openbridge_save')) == 'yes':
    with open(hblink_config, 'w') as f:
        #parser.write(f
        parser.read(hblink_config)
        #parser.remove_section(section_name)
        #parser.add_section(section_name)
        #if section_name in parser.sections():
        try:
            parser.remove_section(old_section_name)
            parser.remove_section(section_name)
        except:
            pass
        #parser.write(f)
        parser.add_section(section_name)
        parser.set(section_name, 'MODE', 'OPENBRIDGE')
        parser.set(section_name, 'ENABLED', str(form.getvalue('enabled')))
        parser.set(section_name, 'IP', str(form.getvalue('ip')))
        parser.set(section_name, 'PORT', str(form.getvalue('port')))
        parser.set(section_name, 'PASSPHRASE', str(form.getvalue('passphrase')))
        parser.set(section_name, 'NETWORK_ID', str(form.getvalue('network_id')))
        parser.set(section_name, 'TARGET_IP', str(form.getvalue('target_ip')))
        parser.set(section_name, 'TARGET_PORT', str(form.getvalue('target_port')))
        parser.set(section_name, 'USE_ACL', str(form.getvalue('use_acl')))
        parser.set(section_name, 'SUB_ACL', str(form.getvalue('sub_acl')))
        parser.set(section_name, 'TGID_ACL', str(form.getvalue('tg_acl')))
        parser.set(section_name, 'BOTH_SLOTS', str(form.getvalue('both_slots')))
        parser.write(f)

if str(form.getvalue('peer_save')) == 'yes':
    with open(hblink_config, 'w') as f:
        #parser.write(f
        parser.read(hblink_config)
        #parser.remove_section(section_name)
        #parser.add_section(section_name)
        #if section_name in parser.sections():
        try:
            parser.remove_section(old_section_name)
            parser.remove_section(section_name)
        except:
            pass
        #parser.write(f)
        parser.add_section(section_name)
        parser.set(section_name, 'MODE', 'PEER')
        parser.set(section_name, 'ENABLED', str(form.getvalue('enabled')))
        parser.set(section_name, 'LOOSE', str(form.getvalue('loose')))
        parser.set(section_name, 'EXPORT_AMBE', str(form.getvalue('export_ambe')))
        parser.set(section_name, 'IP', str(form.getvalue('ip')))
        parser.set(section_name, 'PORT', str(form.getvalue('port')))
        parser.set(section_name, 'PASSPHRASE', str(form.getvalue('passphrase')))
        parser.set(section_name, 'MASTER_IP', str(form.getvalue('master_ip')))
        parser.set(section_name, 'MASTER_PORT', str(form.getvalue('master_port')))
        parser.set(section_name, 'CALLSIGN', str(form.getvalue('callsign')))
        parser.set(section_name, 'RADIO_ID', str(form.getvalue('radio_id')))
        parser.set(section_name, 'TX_FREQ', str(form.getvalue('tx_freq')))
        parser.set(section_name, 'RX_FREQ', str(form.getvalue('rx_freq')))
        parser.set(section_name, 'TX_POWER', str(form.getvalue('tx_power')))
        parser.set(section_name, 'COLORCODE', str(form.getvalue('colorcode')))
        parser.set(section_name, 'SLOTS', str(form.getvalue('slots')))
        parser.set(section_name, 'LATITUDE', str(form.getvalue('latitude')))
        parser.set(section_name, 'LONGITUDE', str(form.getvalue('longitude')))
        parser.set(section_name, 'HEIGHT', str(form.getvalue('height')))
        parser.set(section_name, 'LOCATION', str(form.getvalue('location')))
        parser.set(section_name, 'DESCRIPTION', str(form.getvalue('description')))
        parser.set(section_name, 'URL', str(form.getvalue('url')))
        parser.set(section_name, 'SOFTWARE_ID', str(form.getvalue('software_id')))
        parser.set(section_name, 'PACKAGE_ID', str(form.getvalue('package_id')))
        parser.set(section_name, 'GROUP_HANGTIME', str(form.getvalue('group_hangtime')))
        parser.set(section_name, 'OPTIONS', str(form.getvalue('options')))
        parser.set(section_name, 'USE_ACL', str(form.getvalue('use_acl')))
        parser.set(section_name, 'SUB_ACL', str(form.getvalue('sub_acl')))
        parser.set(section_name, 'TGID_TS1_ACL', str(form.getvalue('tgid_ts1_acl')))
        parser.set(section_name, 'TGID_TS2_ACL', str(form.getvalue('tgid_ts2_acl')))
        parser.write(f)

if str(form.getvalue('xlx_save')) == 'yes':
    with open(hblink_config, 'w') as f:
        #parser.write(f
        parser.read(hblink_config)
        #parser.remove_section(section_name)
        #parser.add_section(section_name)
        #if section_name in parser.sections():
        try:
            parser.remove_section(old_section_name)
            parser.remove_section(section_name)
        except:
            pass
        #parser.write(f)
        parser.add_section(section_name)
        parser.set(section_name, 'MODE', 'PEER')
        parser.set(section_name, 'ENABLED', str(form.getvalue('enabled')))
        parser.set(section_name, 'LOOSE', str(form.getvalue('loose')))
        parser.set(section_name, 'EXPORT_AMBE', str(form.getvalue('export_ambe')))
        parser.set(section_name, 'IP', str(form.getvalue('ip')))
        parser.set(section_name, 'PORT', str(form.getvalue('port')))
        parser.set(section_name, 'PASSPHRASE', str(form.getvalue('passphrase')))
        parser.set(section_name, 'MASTER_IP', str(form.getvalue('master_ip')))
        parser.set(section_name, 'MASTER_PORT', str(form.getvalue('master_port')))
        parser.set(section_name, 'CALLSIGN', str(form.getvalue('callsign')))
        parser.set(section_name, 'RADIO_ID', str(form.getvalue('radio_id')))
        parser.set(section_name, 'TX_FREQ', str(form.getvalue('tx_freq')))
        parser.set(section_name, 'RX_FREQ', str(form.getvalue('rx_freq')))
        parser.set(section_name, 'TX_POWER', str(form.getvalue('tx_power')))
        parser.set(section_name, 'COLORCODE', str(form.getvalue('colorcode')))
        parser.set(section_name, 'SLOTS', str(form.getvalue('slots')))
        parser.set(section_name, 'LATITUDE', str(form.getvalue('latitude')))
        parser.set(section_name, 'LONGITUDE', str(form.getvalue('longitude')))
        parser.set(section_name, 'HEIGHT', str(form.getvalue('height')))
        parser.set(section_name, 'LOCATION', str(form.getvalue('location')))
        parser.set(section_name, 'DESCRIPTION', str(form.getvalue('description')))
        parser.set(section_name, 'URL', str(form.getvalue('url')))
        parser.set(section_name, 'SOFTWARE_ID', str(form.getvalue('software_id')))
        parser.set(section_name, 'PACKAGE_ID', str(form.getvalue('package_id')))
        parser.set(section_name, 'GROUP_HANGTIME', str(form.getvalue('group_hangtime')))
        parser.set(section_name, 'XLXMODULE', str(form.getvalue('xlxmodule')))
        parser.set(section_name, 'USE_ACL', str(form.getvalue('use_acl')))
        parser.set(section_name, 'SUB_ACL', str(form.getvalue('sub_acl')))
        parser.set(section_name, 'TGID_TS1_ACL', str(form.getvalue('tgid_ts1_acl')))
        parser.set(section_name, 'TGID_TS2_ACL', str(form.getvalue('tgid_ts2_acl')))
        parser.write(f)

##try:
##    os.system('touch out.txt')
##except:
##    pass
##with open(hblink_config, "rt") as fin:
##    with open(hblink_loc + 'out.txt', "wt") as fout:
##        for line in fin:
##            fout.write(line.replace('None', ''))
##
##os.remove(hblink_config)
##shutil.move('out.txt', hblink_config)

fin = open(hblink_config, "rt")
data = fin.read()
data = data.replace('None', '')
fin.close()
fin = open(hblink_config, "wt")
fin.write(data)
fin.close()

print('''
<h3><strong>Saved configuration for: ''' + section_name + '''.</strong></h3>

''')

print(redirect)
print(footer)
    

    
##    print(parser.get(form.getvalue('name_text'),'MODE'))
##    parser.set(form.getvalue('name_text'), 'MODE', 'PEER')
##    print(parser.get(form.getvalue('name_text'), 'MODE'))
    #parser.set
    
