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

# Generates HTML output of HBLink for changes

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
from configparser import ConfigParser


parser = ConfigParser()
parser.read(hblink_loc + 'hblink.cfg')

form = cgi.FieldStorage()


print(header)
####
print('''
        <form action="/cgi-bin/save_config.py?&normal_config=yes" method = "post" target = "_blank">

<h3><strong>Global</strong></h3>
<table style="width: 60%;" border="5">
<tbody>
<tr>
<td><strong>&nbsp;Path:</strong></td>
<td>&nbsp;<input name="global_path" type="text" value="''' + parser.get('GLOBAL', 'PATH') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Ping Time:</strong></td>
<td>&nbsp;<input name="ping_time" type="text" value="''' + parser.get('GLOBAL','PING_TIME') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Max Missed:</strong></td>
<td>&nbsp;<input name="max_missed" type="text" value="''' + parser.get('GLOBAL', 'MAX_MISSED') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Use ACLs:</strong></td>
<td>&nbsp;<select name="use_acl">
<option selected="selected" value="''' + parser.get('GLOBAL', 'USE_ACL') + '''">Current - ''' + parser.get('GLOBAL', 'USE_ACL') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
<tr>
<td><strong>&nbsp;Regular ACLs:</strong></td>
<td>&nbsp;<input name="reg_acl" type="text" value="''' + parser.get('GLOBAL', 'REG_ACL') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Subscriber ACSs:</strong></td>
<td>&nbsp;<input name="sub_acl" type="text" value="''' + parser.get('GLOBAL', 'SUB_ACL') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Timeslot 1 ACLs:</strong></td>
<td>&nbsp;<input name="global_ts1_acl" type="text" value="''' + parser.get('GLOBAL', 'TGID_TS1_ACL') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Timeslot 2 ACLs:</strong></td>
<td>&nbsp;<input name="global_ts2_acl" type="text" value="''' + parser.get('GLOBAL', 'TGID_TS2_ACL') + '''" /></td>
</tr>
</tbody>
</table>

<p>&nbsp;</p>

<h3><strong>Reports</strong></h3>
<table style="width: 60%;" border="5">
<tbody>
<tr>
<td><strong>&nbsp;Enable:</strong></td>
<td>&nbsp;<select name="report">
<option selected="selected" value="''' + parser.get('REPORTS', 'REPORT') + '''">Current - ''' + parser.get('REPORTS', 'REPORT') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
<tr>
<td><strong>&nbsp;Interval:</strong></td>
<td>&nbsp;<input name="report_interval" type="text" value="''' + parser.get('REPORTS', 'REPORT_INTERVAL') + '''" /></td>
<tr>
<td><strong>&nbsp;Port:</strong></td>
<td>&nbsp;<input name="report_port" type="text" value="''' + parser.get('REPORTS', 'REPORT_PORT') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Clients:</strong></td>
<td>&nbsp;<input name="report_clients" type="text" value="''' + parser.get('REPORTS', 'REPORT_CLIENTS') + '''" /></td>
</tr>
</tbody>
</table>

<p>&nbsp;</p>


<h3><strong>Logger<br /></strong></h3>
<table style="width: 60%;" border="5">
<tbody>
<tr>
<td><strong>&nbsp;File:</strong></td>
<td>&nbsp;<input name="log_file" type="text" value="''' + parser.get('LOGGER', 'LOG_FILE') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Log Handler:</strong></td>
<td>&nbsp;<input name="log_hendelers" type="text" value="''' + parser.get('LOGGER', 'LOG_HANDlERS') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Log Level:</strong></td>
<td>&nbsp;<input name="log_level" type="text" value="''' + parser.get('LOGGER', 'LOG_LEVEL') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Log Name:</strong></td>
<td>&nbsp;<input name="log_name" type="text" value="''' + parser.get('LOGGER', 'LOG_NAME') + '''" /></td>
</tr>
</tbody>
</table>

<p>&nbsp;</p>


<h3><strong>Aliases<br /></strong></h3>
<table style="width: 60%;" border="5">
<tbody>
<tr>
<td><strong>&nbsp;Download:</strong></td>
<td>&nbsp;<select name="aliases_enabled">
<option selected="selected" value="''' + parser.get('ALIASES', 'TRY_DOWNLOAD') + '''">Current - ''' + parser.get('ALIASES', 'TRY_DOWNLOAD') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
<tr>
<td><strong>&nbsp;Path:</strong></td>
<td>&nbsp;<input name="aliases_path" type="text" value="''' + parser.get('ALIASES', 'PATH') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Peer File:</strong></td>
<td>&nbsp;<input name="peer_file" type="text" value="''' + parser.get('ALIASES', 'PEER_FILE') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Subscriber File:</strong></td>
<td>&nbsp;<input name="sub_file" type="text" value="''' + parser.get('ALIASES', 'SUBSCRIBER_FILE') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Talkgroup ID File:</strong></td>
<td>&nbsp;<input name="tgid_file" type="text" value="''' + parser.get('ALIASES', 'TGID_FILE') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Peer URL:</strong></td>
<td>&nbsp;<input name="peer_url" type="text" value="''' + parser.get('ALIASES', 'PEER_URL') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Subscriber URL:</strong></td>
<td>&nbsp;<input name="sub_url" type="text" value="''' + parser.get('ALIASES', 'SUBSCRIBER_URL') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Stale time(days):</strong></td>
<td>&nbsp;<input name="stale_days" type="text" value="''' + parser.get('ALIASES', 'STALE_DAYS') + '''" /></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>

            <input type="submit" value="Save" />
        </form>

<p>&nbsp;</p>
<hr />
''')
print('''
<p>&nbsp;</p>
<form action = "/cgi-bin/edit_config.py" method = "post" target = "_blank">
   <select name = "edit_dropdown">
      <option value = "master" selected>Master Instances</option>
      <option value = "peer">Peer Instances</option>
      <option value = "openbridge">Openbridge</option>
      <option value = "xlx">XLX Peer</option>
   </select>
   <input type = "submit" value = "Submit"/>
</form>
''')
if str(form.getvalue('edit_dropdown')) == 'master':
####
        #Print MASTER setings
        for section_name in parser.sections():
            try:
                # Edit from for Master instances
                if parser.get(section_name, 'MODE') == 'MASTER':
                    #print(parser.items())
                    print('''
        <form action = "/cgi-bin/save_config.py?master_save=yes&old_name=''' + section_name + '''" method = "post" target = "_blank">
        <table style="width: 60%;" border="5">
        <tbody>
        <tr>
        <td><strong>&nbsp;Name:</strong></td>
        <td>&nbsp;<input name="name_text" type="text" value="''' + section_name + '''"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Active:</strong></td>
        <td>&nbsp;<select name="enabled">
        <option selected="selected" value="''' + parser.get(section_name, 'ENABLED') + '''">Current - ''' + parser.get(section_name, 'ENABLED') + '''</option>
        <option value="True">True</option>
        <option value="False">False</option>
        </select></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Repeat:</strong></td>
        <td>&nbsp;<select name="repeat">
        <option selected="selected" value="''' + parser.get(section_name, 'REPEAT') + '''">Current - ''' + parser.get(section_name, 'REPEAT') + '''</option>
        <option value="True">True</option>
        <option value="False">False</option>
        </select></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Max Peers:</strong></td>
        <td>&nbsp;<input name="max_peers" type="text" value="''' + parser.get(section_name, 'MAX_PEERS') + '''"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Export AMBE:</strong></td>
        <td>&nbsp;<select name="export_ambe">
        <option selected="selected" value="''' + parser.get(section_name, 'EXPORT_AMBE') + '''">Current - ''' + parser.get(section_name, 'EXPORT_AMBE') + '''</option>
        <option value="True">True</option>
        <option value="False">False</option>
        </select></td>
        </tr>
        <tr>
        <td><strong>&nbsp;IP:</strong></td>
        <td>&nbsp;<input name="ip" type="text" value="''' + parser.get(section_name, 'IP') + '''"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;PORT:</strong></td>
        <td>&nbsp;<input name="port" type="text" value="''' + parser.get(section_name, 'PORT') + '''"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Passphrase:</strong></td>
        <td>&nbsp;<input name="passphrase" type="text" value="''' + parser.get(section_name, 'PASSPHRASE') + '''"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Group Hangtime:</strong></td>
        <td>&nbsp;<input name="hangtime" type="text" value="''' + parser.get(section_name, 'GROUP_HANGTIME') + '''"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Use ACLs:</strong></td>
        <td>&nbsp;<select name="use_acl">
        <option selected="selected" value="''' + parser.get(section_name, 'USE_ACL') + '''">Current - ''' + parser.get(section_name, 'USE_ACL') + '''</option>
        <option value="True">True</option>
        <option value="False">False</option>
        </select></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Register ACLs:</strong></td>
        <td>&nbsp;<input name="reg_acl" type="text" value="''' + parser.get(section_name, 'REG_ACL') + '''"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Subscriber ACLs:</strong></td>
        <td>&nbsp;<input name="sub_acl" type="text" value="''' + parser.get(section_name, 'SUB_ACL') + '''"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 1 ACLs:</strong></td>
        <td>&nbsp;<input name="ts1_acl" type="text" value="''' + parser.get(section_name, 'TGID_TS1_ACL') + '''"/></td>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 2 ACLs:</strong></td>
        <td>&nbsp;<input name="ts2_acl" type="text" value="''' + parser.get(section_name, 'TGID_TS2_ACL') + '''"/></td></td>
        </tr>
        </tbody>
        </table>
        <p>&nbsp;</p>
        <input type = "submit" value = "Save"/>
        </form>
        <form action="/cgi-bin/save_config.py?&old_name=''' + section_name + '''&delete=yes" method = "post" target = "_blank">
            <input type="submit" value="Delete" />
        </form>
        <p>&nbsp;</p>
        <hr />
        <p>&nbsp;</p>
''')
##        else:
##            print('mno')

            except:
        #print('no')
                pass
if str(form.getvalue('edit_dropdown')) == 'openbridge':
        for section_name in parser.sections():
            try:
                # Edit from for Master instances
                if parser.get(section_name, 'MODE') == 'OPENBRIDGE':
                    print('''

<form action="/cgi-bin/save_config.py?openbridge_save=yes&amp;old_name=''' + section_name + '''" method="post" target="_blank">
<table style="width: 60%;" border="5">
<tbody>
<tr>
<td><strong>&nbsp;Name:</strong></td>
<td>&nbsp;<input name="name_text" type="text" value="''' + section_name + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Active:</strong></td>
<td>&nbsp;<select name="enabled">
<option selected="selected" value="''' + parser.get(section_name, 'ENABLED') + '''">Current - ''' + parser.get(section_name, 'ENABLED') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
<tr>
<td><strong>&nbsp;IP:</strong></td>
<td>&nbsp;<input name="ip" type="text" value="''' + parser.get(section_name, 'IP') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Port:</strong></td>
<td>&nbsp;<input name="port" type="text" value="''' + parser.get(section_name, 'PORT') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Passphrase:</strong></td>
<td>&nbsp;<input name="passphrase" type="text" value="''' + parser.get(section_name, 'PASSPHRASE') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Network ID:</strong></td>
<td>&nbsp;<input name="network_id" type="text" value="''' + parser.get(section_name, 'NETWORK_ID') + '''" /></td>
</tr>
  <tr>
<td><strong>&nbsp;Target IP:</strong></td>
<td>&nbsp;<input name="target_ip" type="text" value="''' + parser.get(section_name, 'TARGET_IP') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Target Port:</strong></td>
<td>&nbsp;<input name="target_port" type="text" value="''' + parser.get(section_name, 'TARGET_PORT') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Use ACLs:</strong></td>
<td>&nbsp;<select name="use_acl">
<option selected="selected" value="''' + parser.get(section_name, 'USE_ACL') + '''">Current - ''' + parser.get(section_name, 'USE_ACL') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
<tr>
<td><strong>&nbsp;Subscriber ACLs:</strong></td>
<td>&nbsp;<input name="sub_acl" type="text" value="''' + parser.get(section_name, 'SUB_ACL') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Talkgroup ACLs:</strong></td>
<td>&nbsp;<input name="tg_acl" type="text" value="''' + parser.get(section_name, 'TGID_ACL') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Use Both Slots:</strong></td>
<td>&nbsp;<select name="both_slots">
<option selected="selected" value="''' + parser.get(section_name, 'BOTH_SLOTS') + '''">Current - ''' + parser.get(section_name, 'BOTH_SLOTS') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<input type="submit" value="Save" /></form><form action="/cgi-bin/save_config.py?&amp;old_name=''' + section_name + '''&amp;delete=yes" method="post" target="_blank"><input type="submit" value="Delete" /></form>
<p>&nbsp;</p>
<hr />
<p>&nbsp;</p>

''')
            except Exception as e:
                #print(e)
                pass
##if str(form.getvalue('master_save')) == 'yes':
##    print(parser.read())
##    #parser.set

if str(form.getvalue('edit_dropdown')) == 'peer':
        for section_name in parser.sections():
            try:
                # Edit from for Master instances
                if parser.get(section_name, 'MODE') == 'PEER':
                    print('''

<form action="/cgi-bin/save_config.py?peer_save=yes&amp;old_name=''' + section_name + '''" method="post" target="_blank">
<table style="width: 80%;" border="5">
<tbody>
<tr>
<td><strong>&nbsp;Name:</strong></td>
<td>&nbsp;<input name="name_text" type="text" value="''' + section_name + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Active:</strong></td>
<td>&nbsp;<select name="enabled">
<option selected="selected" value="''' + parser.get(section_name, 'ENABLED') + '''">Current - ''' + parser.get(section_name, 'ENABLED') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
  <tr>
<td><strong>&nbsp;Loose:</strong></td>
<td>&nbsp;<select name="loose">
<option selected="selected" value="''' + parser.get(section_name, 'LOOSE') + '''">Current - ''' + parser.get(section_name, 'ENABLED') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
          <tr>
        <td><strong>&nbsp;Export AMBE:</strong></td>
        <td>&nbsp;<select name="export_ambe">
        <option selected="selected" value="''' + parser.get(section_name, 'EXPORT_AMBE') + '''">Current - ''' + parser.get(section_name, 'EXPORT_AMBE') + '''</option>
        <option value="True">True</option>
        <option value="False">False</option>
        </select></td>
        </tr>
<tr>
<td><strong>&nbsp;IP:</strong></td>
<td>&nbsp;<input name="ip" type="text" value="''' + parser.get(section_name, 'IP') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Port:</strong></td>
<td>&nbsp;<input name="port" type="text" value="''' + parser.get(section_name, 'PORT') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Passphrase:</strong></td>
<td>&nbsp;<input name="passphrase" type="text" value="''' + parser.get(section_name, 'PASSPHRASE') + '''" /></td>
</tr>
  <tr>
<td><strong>&nbsp;Master IP:</strong></td>
<td>&nbsp;<input name="master_ip" type="text" value="''' + parser.get(section_name, 'MASTER_IP') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Master Port:</strong></td>
<td>&nbsp;<input name="master_port" type="text" value="''' + parser.get(section_name, 'MASTER_PORT') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Callsign:</strong></td>
<td>&nbsp;<input name="callsign" type="text" value="''' + parser.get(section_name, 'CALLSIGN') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Radio ID:</strong></td>
<td>&nbsp;<input name="radio_id" type="text" value="''' + parser.get(section_name, 'RADIO_ID') + '''" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Transmit Frequency:</strong></td>
<td>&nbsp;<input name="tx_freq" type="text" value="''' + parser.get(section_name, 'TX_FREQ') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Receive Frequency:</strong></td>
<td>&nbsp;<input name="rx_freq" type="text" value="''' + parser.get(section_name, 'RX_FREQ') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Transmit Power:</strong></td>
<td>&nbsp;<input name="tx_power" type="text" value="''' + parser.get(section_name, 'TX_POWER') + '''" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Color Code:</strong></td>
<td>&nbsp;<select name = "colorcode">
<option value = "''' + parser.get(section_name, 'COLORCODE') + '''" selected>Current - ''' + parser.get(section_name, 'COLORCODE') + '''</option>
      <option value = "0">0</option>
      <option value = "1">1</option>
      <option value = "2">2</option>
      <option value = "3">3</option>
      <option value = "4">4</option>
      <option value = "5">5</option>
      <option value = "6">6</option>
      <option value = "7">7</option>
      <option value = "8">8</option>
      <option value = "9">9</option>
      <option value = "10">10</option>
      <option value = "11">11</option>
      <option value = "12">12</option>
      <option value = "13">13</option>
      <option value = "14">14</option>
      <option value = "15">15</option>
      </select></td>
</tr>
<tr>
<td><strong>&nbsp;Slots:</strong></td>
<td>&nbsp;<input name="slots" type="text" value="''' + parser.get(section_name, 'SLOTS') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Latitude:</strong></td>
<td>&nbsp;<input name="latitude" type="text" value="''' + parser.get(section_name, 'LATITUDE') + '''" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Longitude:</strong></td>
<td>&nbsp;<input name="longitude" type="text" value="''' + parser.get(section_name, 'LONGITUDE') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Height</strong></td>
<td>&nbsp;<input name="height" type="text" value="''' + parser.get(section_name, 'HEIGHT') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Location:</strong></td>
<td>&nbsp;<input name="location" type="text" value="''' + parser.get(section_name, 'LOCATION') + '''" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Description:</strong></td>
<td>&nbsp;<input name="description" type="text" value="''' + parser.get(section_name, 'DESCRIPTION') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;URL:</strong></td>
<td>&nbsp;<input name="url" type="text" value="''' + parser.get(section_name, 'URL') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Software IDt:</strong></td>
<td>&nbsp;<input name="software_id" type="text" value="''' + parser.get(section_name, 'SOFTWARE_ID') + '''" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Package ID::</strong></td>
<td>&nbsp;<input name="package_id" type="text" value="''' + parser.get(section_name, 'PACKAGE_ID') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Group Hangtime:</strong></td>
<td>&nbsp;<input name="group_hangtime" type="text" value="''' + parser.get(section_name, 'GROUP_HANGTIME') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Options:</strong></td>
<td>&nbsp;<input name="options" type="text" value="''' + parser.get(section_name, 'OPTIONS') + '''" /></td>
</tr>
  
<tr>
<td><strong>&nbsp;Use ACLs:</strong></td>
<td>&nbsp;<select name="use_acl">
<option selected="selected" value="''' + parser.get(section_name, 'USE_ACL') + '''">Current - ''' + parser.get(section_name, 'USE_ACL') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
        <tr>
        <td><strong>&nbsp;Subscriber ACLs:</strong></td>
        <td>&nbsp;<input name="sub_acl" type="text" value="''' + parser.get(section_name, 'SUB_ACL') + '''"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 1 ACLs:</strong></td>
        <td>&nbsp;<input name="tgid_ts1_acl" type="text" value="''' + parser.get(section_name, 'TGID_TS1_ACL') + '''"/></td>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 2 ACLs:</strong></td>
        <td>&nbsp;<input name="tgid_ts2_acl" type="text" value="''' + parser.get(section_name, 'TGID_TS2_ACL') + '''"/></td></td>
        </tr>
</tbody>
</table>
<p>&nbsp;</p>
<input type="submit" value="Save" /></form><form action="/cgi-bin/save_config.py?&amp;old_name=''' + section_name + '''&amp;delete=yes" method="post" target="_blank"><input type="submit" value="Delete" /></form>
<p>&nbsp;</p>
<hr />
<p>&nbsp;</p>

''')
            except Exception as e:
                    #print(e)
                    pass


if str(form.getvalue('edit_dropdown')) == 'xlx':
        for section_name in parser.sections():
            try:
                # Edit from for Master instances
                if parser.get(section_name, 'MODE') == 'XLXPEER':
                    print('''

<form action="/cgi-bin/save_config.py?xlx_save=yes&amp;old_name=''' + section_name + '''" method="post" target="_blank">
<table style="width: 80%;" border="5">
<tbody>
<tr>
<td><strong>&nbsp;Name:</strong></td>
<td>&nbsp;<input name="name_text" type="text" value="''' + section_name + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Active:</strong></td>
<td>&nbsp;<select name="enabled">
<option selected="selected" value="''' + parser.get(section_name, 'ENABLED') + '''">Current - ''' + parser.get(section_name, 'ENABLED') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
  <tr>
<td><strong>&nbsp;Loose:</strong></td>
<td>&nbsp;<select name="loose">
<option selected="selected" value="''' + parser.get(section_name, 'LOOSE') + '''">Current - ''' + parser.get(section_name, 'ENABLED') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
          <tr>
        <td><strong>&nbsp;Export AMBE:</strong></td>
        <td>&nbsp;<select name="export_ambe">
        <option selected="selected" value="''' + parser.get(section_name, 'EXPORT_AMBE') + '''">Current - ''' + parser.get(section_name, 'EXPORT_AMBE') + '''</option>
        <option value="True">True</option>
        <option value="False">False</option>
        </select></td>
        </tr>
<tr>
<td><strong>&nbsp;IP:</strong></td>
<td>&nbsp;<input name="ip" type="text" value="''' + parser.get(section_name, 'IP') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Port:</strong></td>
<td>&nbsp;<input name="port" type="text" value="''' + parser.get(section_name, 'PORT') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Passphrase:</strong></td>
<td>&nbsp;<input name="passphrase" type="text" value="''' + parser.get(section_name, 'PASSPHRASE') + '''" /></td>
</tr>
  <tr>
<td><strong>&nbsp;Master IP:</strong></td>
<td>&nbsp;<input name="master_ip" type="text" value="''' + parser.get(section_name, 'MASTER_IP') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Master Port:</strong></td>
<td>&nbsp;<input name="master_port" type="text" value="''' + parser.get(section_name, 'MASTER_PORT') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Callsign:</strong></td>
<td>&nbsp;<input name="callsign" type="text" value="''' + parser.get(section_name, 'CALLSIGN') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Radio ID:</strong></td>
<td>&nbsp;<input name="radio_id" type="text" value="''' + parser.get(section_name, 'RADIO_ID') + '''" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Transmit Frequency:</strong></td>
<td>&nbsp;<input name="tx_freq" type="text" value="''' + parser.get(section_name, 'TX_FREQ') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Receive Frequency:</strong></td>
<td>&nbsp;<input name="rx_freq" type="text" value="''' + parser.get(section_name, 'RX_FREQ') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Transmit Power:</strong></td>
<td>&nbsp;<input name="tx_power" type="text" value="''' + parser.get(section_name, 'TX_POWER') + '''" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Color Code:</strong></td>
<td>&nbsp;<select name = "colorcode">
<option value = "''' + parser.get(section_name, 'COLORCODE') + '''" selected>Current - ''' + parser.get(section_name, 'COLORCODE') + '''</option>
      <option value = "0">0</option>
      <option value = "1">1</option>
      <option value = "2">2</option>
      <option value = "3">3</option>
      <option value = "4">4</option>
      <option value = "5">5</option>
      <option value = "6">6</option>
      <option value = "7">7</option>
      <option value = "8">8</option>
      <option value = "9">9</option>
      <option value = "10">10</option>
      <option value = "11">11</option>
      <option value = "12">12</option>
      <option value = "13">13</option>
      <option value = "14">14</option>
      <option value = "15">15</option>
      </select></td>
</tr>
<tr>
<td><strong>&nbsp;Slots:</strong></td>
<td>&nbsp;<input name="slots" type="text" value="''' + parser.get(section_name, 'SLOTS') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Latitude:</strong></td>
<td>&nbsp;<input name="latitude" type="text" value="''' + parser.get(section_name, 'LATITUDE') + '''" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Longitude:</strong></td>
<td>&nbsp;<input name="longitude" type="text" value="''' + parser.get(section_name, 'LONGITUDE') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Height</strong></td>
<td>&nbsp;<input name="height" type="text" value="''' + parser.get(section_name, 'HEIGHT') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Location:</strong></td>
<td>&nbsp;<input name="location" type="text" value="''' + parser.get(section_name, 'LOCATION') + '''" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Description:</strong></td>
<td>&nbsp;<input name="description" type="text" value="''' + parser.get(section_name, 'DESCRIPTION') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;URL:</strong></td>
<td>&nbsp;<input name="url" type="text" value="''' + parser.get(section_name, 'URL') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Software IDt:</strong></td>
<td>&nbsp;<input name="software_id" type="text" value="''' + parser.get(section_name, 'SOFTWARE_ID') + '''" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Package ID::</strong></td>
<td>&nbsp;<input name="package_id" type="text" value="''' + parser.get(section_name, 'PACKAGE_ID') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;Group Hangtime:</strong></td>
<td>&nbsp;<input name="group_hangtime" type="text" value="''' + parser.get(section_name, 'GROUP_HANGTIME') + '''" /></td>
</tr>
<tr>
<td><strong>&nbsp;XLX Module:</strong></td>
<td>&nbsp;<input name="xlxmodule" type="text" value="''' + parser.get(section_name, 'XLXMODULE') + '''" /></td>
</tr>
  
<tr>
<td><strong>&nbsp;Use ACLs:</strong></td>
<td>&nbsp;<select name="use_acl">
<option selected="selected" value="''' + parser.get(section_name, 'USE_ACL') + '''">Current - ''' + parser.get(section_name, 'USE_ACL') + '''</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
        <tr>
        <td><strong>&nbsp;Subscriber ACLs:</strong></td>
        <td>&nbsp;<input name="sub_acl" type="text" value="''' + parser.get(section_name, 'SUB_ACL') + '''"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 1 ACLs:</strong></td>
        <td>&nbsp;<input name="ts1_acl" type="text" value="''' + parser.get(section_name, 'TGID_TS1_ACL') + '''"/></td>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 2 ACLs:</strong></td>
        <td>&nbsp;<input name="ts2_acl" type="text" value="''' + parser.get(section_name, 'TGID_TS2_ACL') + '''"/></td></td>
        </tr>
</tbody>
</table>
<p>&nbsp;</p>
<input type="submit" value="Save" /></form><form action="/cgi-bin/save_config.py?&amp;old_name=''' + section_name + '''&amp;delete=yes" method="post" target="_blank"><input type="submit" value="Delete" /></form>
<p>&nbsp;</p>
<hr />
<p>&nbsp;</p>

''')
            except Exception as e:
                    #print(e)
                    pass




print(footer)

