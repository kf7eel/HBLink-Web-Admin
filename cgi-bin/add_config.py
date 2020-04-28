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
<p>&nbsp;</p>
<form action = "/cgi-bin/add_config.py" method = "post" target = "_blank">
   <select name = "add_dropdown">
      <option value = "master" selected>Master</option>
      <option value = "peer">Peer</option>
      <option value = "openbridge">Openbridge</option>
      <option value = "xlx">XLX Peer</option>
   </select>
   <input type = "submit" value = "Submit"/>
</form>
''')

if str(form.getvalue('add_dropdown')) == 'master':
####
        #Print MASTER setings
     print('''
        <form action = "/cgi-bin/save_config.py?master_save=yes" method = "post" target = "_blank">
        <table style="width: 60%;" border="5">
        <tbody>
        <tr>
        <td><strong>&nbsp;Name:</strong></td>
        <td>&nbsp;<input name="name_text" type="text" value=""/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Active:</strong></td>
        <td>&nbsp;<select name="enabled">
        <option selected="selected" value="True">Current - True</option>
        <option value="True">True</option>
        <option value="False">False</option>
        </select></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Repeat:</strong></td>
        <td>&nbsp;<select name="repeat">
        <option selected="selected" value="True">Current - True</option>
        <option value="True">True</option>
        <option value="False">False</option>
        </select></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Max Peers:</strong></td>
        <td>&nbsp;<input name="max_peers" type="text" value="5"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Export AMBE:</strong></td>
        <td>&nbsp;<select name="export_ambe">
        <option selected="selected" value="False">Current - False</option>
        <option value="True">True</option>
        <option value="False">False</option>
        </select></td>
        </tr>
        <tr>
        <td><strong>&nbsp;IP:</strong></td>
        <td>&nbsp;<input name="ip" type="text" value=""/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;PORT:</strong></td>
        <td>&nbsp;<input name="port" type="text" value=""/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Passphrase:</strong></td>
        <td>&nbsp;<input name="passphrase" type="text" value="passw0rd"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Group Hangtime:</strong></td>
        <td>&nbsp;<input name="hangtime" type="text" value="5"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Use ACLs:</strong></td>
        <td>&nbsp;<select name="use_acl">
        <option selected="selected" value="True">Current - True</option>
        <option value="True">True</option>
        <option value="False">False</option>
        </select></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Register ACLs:</strong></td>
        <td>&nbsp;<input name="reg_acl" type="text" value="DENY:1"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Subscriber ACLs:</strong></td>
        <td>&nbsp;<input name="sub_acl" type="text" value="DENY:1"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 1 ACLs:</strong></td>
        <td>&nbsp;<input name="ts1_acl" type="text" value="PERMIT:ALL"/></td>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 2 ACLs:</strong></td>
        <td>&nbsp;<input name="ts2_acl" type="text" value="PERMIT:ALL"/></td></td>
        </tr>
        </tbody>
        </table>
        <p>&nbsp;</p>
        <input type = "submit" value = "Save"/>
        </form>

        <p>&nbsp;</p>
        <hr />
        <p>&nbsp;</p>
''')

if str(form.getvalue('add_dropdown')) == 'openbridge':
    print('''

<form action="/cgi-bin/save_config.py?openbridge_save=yes" method="post" target="_blank">
<table style="width: 60%;" border="5">
<tbody>
<tr>
<td><strong>&nbsp;Name:</strong></td>
<td>&nbsp;<input name="name_text" type="text" value="" /></td>
</tr>
<tr>
<td><strong>&nbsp;Active:</strong></td>
<td>&nbsp;<select name="enabled">
<option selected="selected" value="True">Current - True</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
<tr>
<td><strong>&nbsp;IP:</strong></td>
<td>&nbsp;<input name="ip" type="text" value="" /></td>
</tr>
<tr>
<td><strong>&nbsp;Port:</strong></td>
<td>&nbsp;<input name="port" type="text" value="62035" /></td>
</tr>
<tr>
<td><strong>&nbsp;Passphrase:</strong></td>
<td>&nbsp;<input name="passphrase" type="text" value="passw0rd" /></td>
</tr>
<tr>
<td><strong>&nbsp;Network ID:</strong></td>
<td>&nbsp;<input name="network_id" type="text" value="123456789" /></td>
</tr>
  <tr>
<td><strong>&nbsp;Target IP:</strong></td>
<td>&nbsp;<input name="target_ip" type="text" value="1.2.3.4" /></td>
</tr>
<tr>
<td><strong>&nbsp;Target Port:</strong></td>
<td>&nbsp;<input name="target_port" type="text" value="62035" /></td>
</tr>
<tr>
<td><strong>&nbsp;Use ACLs:</strong></td>
<td>&nbsp;<select name="use_acl">
<option selected="selected" value="True">Current - True</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
<tr>
<td><strong>&nbsp;Subscriber ACLs:</strong></td>
<td>&nbsp;<input name="sub_acl" type="text" value="DENY:1" /></td>
</tr>
<tr>
<td><strong>&nbsp;Talkgroup ACLs:</strong></td>
<td>&nbsp;<input name="tg_acl" type="text" value="PERMIT:ALL" /></td>
</tr>
<tr>
<td><strong>&nbsp;Use Both Slots:</strong></td>
<td>&nbsp;<select name="both_slots">
<option selected="selected" value="False">Current - False</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<input type="submit" value="Save" /></form>
<p>&nbsp;</p>
<hr />
<p>&nbsp;</p>

''')

if str(form.getvalue('add_dropdown')) == 'peer':
    print('''

<form action="/cgi-bin/save_config.py?peer_save=yes" method="post" target="_blank">
<table style="width: 80%;" border="5">
<tbody>
<tr>
<td><strong>&nbsp;Name:</strong></td>
<td>&nbsp;<input name="name_text" type="text" value="" /></td>
</tr>
<tr>
<td><strong>&nbsp;Active:</strong></td>
<td>&nbsp;<select name="enabled">
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
  <tr>
<td><strong>&nbsp;Loose:</strong></td>
<td>&nbsp;<select name="loose">
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
          <tr>
        <td><strong>&nbsp;Export AMBE:</strong></td>
        <td>&nbsp;<select name="export_ambe">
        <option value="True">True</option>
        <option selected="selected" value="False">False</option>
        </select></td>
        </tr>
<tr>
<td><strong>&nbsp;IP:</strong></td>
<td>&nbsp;<input name="ip" type="text" value="" /></td>
</tr>
<tr>
<td><strong>&nbsp;Port:</strong></td>
<td>&nbsp;<input name="port" type="text" value="" /></td>
</tr>
<tr>
<td><strong>&nbsp;Passphrase:</strong></td>
<td>&nbsp;<input name="passphrase" type="text" value="passw0rd" /></td>
</tr>
  <tr>
<td><strong>&nbsp;Master IP:</strong></td>
<td>&nbsp;<input name="master_ip" type="text" value="IP.OF.MASTER.SERVER" /></td>
</tr>
<tr>
<td><strong>&nbsp;Master Port:</strong></td>
<td>&nbsp;<input name="master_port" type="text" value="5400" /></td>
</tr>
<tr>
<td><strong>&nbsp;Callsign:</strong></td>
<td>&nbsp;<input name="callsign" type="text" value="" /></td>
</tr>
<tr>
<td><strong>&nbsp;Radio ID:</strong></td>
<td>&nbsp;<input name="radio_id" type="text" value="123456789" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Transmit Frequency:</strong></td>
<td>&nbsp;<input name="tx_freq" type="text" value="449000000" /></td>
</tr>
<tr>
<td><strong>&nbsp;Receive Frequency:</strong></td>
<td>&nbsp;<input name="rx_freq" type="text" value="449000000" /></td>
</tr>
<tr>
<td><strong>&nbsp;Transmit Power:</strong></td>
<td>&nbsp;<input name="tx_power" type="text" value="25" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Color Code:</strong></td>
<td>&nbsp;<select name = "colorcode">
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
<td>&nbsp;<input name="slots" type="text" value="1" /></td>
</tr>
<tr>
<td><strong>&nbsp;Latitude:</strong></td>
<td>&nbsp;<input name="latitude" type="text" value="38.0000" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Longitude:</strong></td>
<td>&nbsp;<input name="longitude" type="text" value="-095.0000" /></td>
</tr>
<tr>
<td><strong>&nbsp;Height</strong></td>
<td>&nbsp;<input name="height" type="text" value="50" /></td>
</tr>
<tr>
<td><strong>&nbsp;Location:</strong></td>
<td>&nbsp;<input name="location" type="text" value="Anywhere, USA" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Description:</strong></td>
<td>&nbsp;<input name="description" type="text" value="This is a cool repeater" /></td>
</tr>
<tr>
<td><strong>&nbsp;URL:</strong></td>
<td>&nbsp;<input name="url" type="text" value="www.w1abc.org" /></td>
</tr>
<tr>
<td><strong>&nbsp;Software IDt:</strong></td>
<td>&nbsp;<input name="software_id" type="text" value="20170620" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Package ID::</strong></td>
<td>&nbsp;<input name="package_id" type="text" value="MMDVM_HBlink" /></td>
</tr>
<tr>
<td><strong>&nbsp;Group Hangtime:</strong></td>
<td>&nbsp;<input name="group_hangtime" type="text" value="5" /></td>
</tr>
<tr>
<td><strong>&nbsp;Options:</strong></td>
<td>&nbsp;<input name="options" type="text" value="" /></td>
</tr>
  
<tr>
<td><strong>&nbsp;Use ACLs:</strong></td>
<td>&nbsp;<select name="use_acl">
<option selected="selected" value="True">Current - True</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
        <tr>
        <td><strong>&nbsp;Subscriber ACLs:</strong></td>
        <td>&nbsp;<input name="sub_acl" type="text" value="DENY:1"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 1 ACLs:</strong></td>
        <td>&nbsp;<input name="tgid_ts1_acl" type="text" value="PERMIT:ALL"/></td>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 2 ACLs:</strong></td>
        <td>&nbsp;<input name="tgid_ts2_acl" type="text" value="PERMIT:ALL"/></td></td>
        </tr>
</tbody>
</table>
<p>&nbsp;</p>
<input type="submit" value="Save" /></form><
<p>&nbsp;</p>
<hr />
<p>&nbsp;</p>

''')

if str(form.getvalue('add_dropdown')) == 'xlx':
    print('''

<form action="/cgi-bin/save_config.py?xlx_save=yes" method="post" target="_blank">
<table style="width: 80%;" border="5">
<tbody>
<tr>
<td><strong>&nbsp;Name:</strong></td>
<td>&nbsp;<input name="name_text" type="text" value="" /></td>
</tr>
<tr>
<td><strong>&nbsp;Active:</strong></td>
<td>&nbsp;<select name="enabled">
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
  <tr>
<td><strong>&nbsp;Loose:</strong></td>
<td>&nbsp;<select name="loose">
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
          <tr>
        <td><strong>&nbsp;Export AMBE:</strong></td>
        <td>&nbsp;<select name="export_ambe">
        <option value="True">True</option>
        <option selected="selected" value="False">False</option>
        </select></td>
        </tr>
<tr>
<td><strong>&nbsp;IP:</strong></td>
<td>&nbsp;<input name="ip" type="text" value="" /></td>
</tr>
<tr>
<td><strong>&nbsp;Port:</strong></td>
<td>&nbsp;<input name="port" type="text" value="" /></td>
</tr>
<tr>
<td><strong>&nbsp;Passphrase:</strong></td>
<td>&nbsp;<input name="passphrase" type="text" value="passw0rd" /></td>
</tr>
  <tr>
<td><strong>&nbsp;Master IP:</strong></td>
<td>&nbsp;<input name="master_ip" type="text" value="IP.OF.MASTER.SERVER" /></td>
</tr>
<tr>
<td><strong>&nbsp;Master Port:</strong></td>
<td>&nbsp;<input name="master_port" type="text" value="5400" /></td>
</tr>
<tr>
<td><strong>&nbsp;Callsign:</strong></td>
<td>&nbsp;<input name="callsign" type="text" value="" /></td>
</tr>
<tr>
<td><strong>&nbsp;Radio ID:</strong></td>
<td>&nbsp;<input name="radio_id" type="text" value="123456789" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Transmit Frequency:</strong></td>
<td>&nbsp;<input name="tx_freq" type="text" value="449000000" /></td>
</tr>
<tr>
<td><strong>&nbsp;Receive Frequency:</strong></td>
<td>&nbsp;<input name="rx_freq" type="text" value="449000000" /></td>
</tr>
<tr>
<td><strong>&nbsp;Transmit Power:</strong></td>
<td>&nbsp;<input name="tx_power" type="text" value="25" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Color Code:</strong></td>
<td>&nbsp;<select name = "colorcode">
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
<td>&nbsp;<input name="slots" type="text" value="1" /></td>
</tr>
<tr>
<td><strong>&nbsp;Latitude:</strong></td>
<td>&nbsp;<input name="latitude" type="text" value="38.0000" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Longitude:</strong></td>
<td>&nbsp;<input name="longitude" type="text" value="-095.0000" /></td>
</tr>
<tr>
<td><strong>&nbsp;Height</strong></td>
<td>&nbsp;<input name="height" type="text" value="50" /></td>
</tr>
<tr>
<td><strong>&nbsp;Location:</strong></td>
<td>&nbsp;<input name="location" type="text" value="Anywhere, USA" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Description:</strong></td>
<td>&nbsp;<input name="description" type="text" value="This is a cool repeater" /></td>
</tr>
<tr>
<td><strong>&nbsp;URL:</strong></td>
<td>&nbsp;<input name="url" type="text" value="www.w1abc.org" /></td>
</tr>
<tr>
<td><strong>&nbsp;Software IDt:</strong></td>
<td>&nbsp;<input name="software_id" type="text" value="20170620" /></td>
</tr>
  
  <tr>
<td><strong>&nbsp;Package ID::</strong></td>
<td>&nbsp;<input name="package_id" type="text" value="MMDVM_HBlink" /></td>
</tr>
<tr>
<td><strong>&nbsp;Group Hangtime:</strong></td>
<td>&nbsp;<input name="group_hangtime" type="text" value="5" /></td>
</tr>
<tr>
<td><strong>&nbsp;XLX Module:</strong></td>
<td>&nbsp;<input name="xlxmodule" type="text" value="4004" /></td>
</tr>
  
<tr>
<td><strong>&nbsp;Use ACLs:</strong></td>
<td>&nbsp;<select name="use_acl">
<option selected="selected" value="True">Current - True</option>
<option value="True">True</option>
<option value="False">False</option>
</select></td>
</tr>
        <tr>
        <td><strong>&nbsp;Subscriber ACLs:</strong></td>
        <td>&nbsp;<input name="sub_acl" type="text" value="DENY:1"/></td>
        </tr>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 1 ACLs:</strong></td>
        <td>&nbsp;<input name="tgid_ts1_acl" type="text" value="PERMIT:ALL"/></td>
        <tr>
        <td><strong>&nbsp;Talkgroup Slot 2 ACLs:</strong></td>
        <td>&nbsp;<input name="tgid_ts2_acl" type="text" value="PERMIT:ALL"/></td></td>
        </tr>
</tbody>
</table>
<p>&nbsp;</p>
<input type="submit" value="Save" /></form>
<p>&nbsp;</p>
<hr />
<p>&nbsp;</p>
''')
            

print(footer)
