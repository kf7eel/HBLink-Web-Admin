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

# Core Functions


#from config
import sys, os, ast
##sys.path.append('..')
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from config import *

sys.path.append(hblink_loc)

from rules_web import *
from functions import *

from configparser import ConfigParser


hblink_system = 'SYSTEM'
hblink_ts = 'TS'
hblink_tgid = 'TGID'
hblink_active = 'ACTIVE'
hblink_timeout = 'TIMEOUT'
hblink_to_type = 'TO_TYPE'
hblink_on = 'ON'
hblink_off = 'OFF'
hblink_reset = 'RESET'


def add_bridge_rule(bridge_name, system, ts, tgid, active, timeout, to_type, on, off, reset):
##    if on == None:
##        on_tg = []
##    else:
##        on_tg == [int(on)]
##    if off is None:
##        off_tg == []
##    else:
##        off_tg = [int(off)]
##    if reset is None:
##        reset_tg == []
##    else:
##        reset_tg = [int(on)]
##    if tgid.islower() or tgid.isupper() in tgid:
##        tgid_value = eval_code(tgid)
##    else:
##        tgid_value = int(tgid)

##    
    if type(reset) == str: #or tgid.isupper() in tgid:
        reset = eval(reset)
    if type(on) == str: #or tgid.isupper() in tgid:
        on = eval(on)
    if type(off) == str: #or tgid.isupper() in tgid:
        off = eval(off)
    #else:
     #   reset = int(reset)

        
    new_entry = {hblink_system: str(system), hblink_ts: int(ts), hblink_tgid: int(tgid), hblink_active: active, hblink_timeout: int(timeout), hblink_to_type: str(to_type), hblink_on: on, hblink_off: off, hblink_reset: reset}
    
        #tgid_value = eval_code(tgid)
            #BRIDGES[bridgename] = 
    if str(bridge_name) in str(BRIDGES):
        BRIDGES[bridge_name].append(new_entry)
        #  print(BRIDGES[bridge_name])
        #print('its equal')
    else:
        BRIDGES[bridge_name] = [{hblink_system: str(system), hblink_ts: int(ts), hblink_tgid: int(tgid), hblink_active: active, hblink_timeout: int(timeout), hblink_to_type: str(to_type), hblink_on: on, hblink_off: off, hblink_reset: reset}]    

    #print(BRIDGES[bridge_name])

def bridge_write_file():
    with open(rule_file, 'w') as file:
        file.write('BRIDGES = ' + str(BRIDGES))

def add_bridge(name, system, ts, tgid, active, timeout, to_type, on, off, reset):
    BRIDGES[name] =  [{hblink_system: str(system), hblink_ts: int(ts), hblink_tgid: int(tgid), hblink_active: active, hblink_timeout: int(timeout), hblink_to_type: str(to_type), hblink_on: [int(on)], hblink_off: [int(off)], hblink_reset: [int(reset)]}]

def html_bridge_view_all():
    for line in BRIDGES:
        print('''
<p>&nbsp;</p>
<h3><strong>''' + str(line) + '''</strong></h3>
<table style="width: 100%; height: 30px;" border="5">''')

        bridge_list(line)
        print('</table>')

def delete_bridge_rule(bridge, rule):
    del BRIDGES[bridge][rule]
    #print(BRIDGES[bridge][rule])

def delete_bridge(bridge):
    del BRIDGES[bridge]

def bridge_rule_index(bridge):
    for key in BRIDGES[bridge]:
        print(type(key))
        print(BRIDGES[bridge].index(key))
def html_core_list_master():
    #print(hblink_config)
    parser = ConfigParser()
    parser.read(hblink_loc + 'hblink.cfg')
    for section_name in parser.sections():
        try:
 ##            config_table = '''
##<table style="float: left;" width: 300px border="5" cellspacing="5" cellpadding="5">
##<tbody>
##<tr><td><strong>System: </strong></td><td>''' + section_name + '''</td>
##<td>''' + server_type + '''</td></tr>
##</tbody>
##</table>
##<p>&nbsp;</p>
##'''
            if parser.get(section_name, 'MODE') == 'MASTER':
                server_type = 'Master'
                print('''
<table style="width: 50%; margin-left: auto; margin-right: auto;" border="5" cellspacing="5" cellpadding="5">
<tbody>
<tr>
<td><strong>System Type:</strong></td>
<td>''' + parser.get(section_name, 'MODE') + '''</td>
</tr>
<tr>
<td><strong>Name:</strong></td>
<td>''' + section_name + '''</td>
</tr>
<tr>
<td><strong>Status:</strong></td>
<td><strong>''' + parser.get(section_name, 'ENABLED') + '''</strong></td>
</tr>
<tr>
<td><strong>Repeat:</strong></td>
<td>''' + parser.get(section_name, 'REPEAT') + '''</td>
</tr>
<tr>
<td><strong>Max Peers:</strong></td>
<td>''' + parser.get(section_name, 'MAX_PEERS') + '''</td>
</tr>
<tr>
<td><strong>IP:</strong></td>
<td>''' + parser.get(section_name, 'IP') + '''</td>
</tr>
<tr>
<td><strong>Port:</strong></td>
<td>''' + parser.get(section_name, 'PORT') + '''</td>
</tr>
<tr>
<td><strong>Passphrase:</strong></td>
<td>''' + parser.get(section_name, 'PASSPHRASE') + '''</td>
</tr>
<tr>
<td><strong>Group Hangtime:</strong></td>
<td>''' + parser.get(section_name, 'GROUP_HANGTIME') + '''</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
''')
                                #print('''<tr><td><strong>System: </strong></td><td>''' + section_name + '''</td><td>''' + server_type + '''</td></tr>''')
            if parser.get(section_name, 'MODE') == 'PEER':
                server_type = 'Peer'
                print('''
<table style="width: 50%; margin-left: auto; margin-right: auto;" border="5" cellspacing="5" cellpadding="5">
<tbody>
<tr>
<td><strong>System Type:</strong></td>
<td>''' + parser.get(section_name, 'MODE') + '''</td>
</tr>
<tr>
<td><strong>Name:</strong></td>
<td>''' + section_name + '''</td>
</tr>
<tr>
<td><strong>Status:</strong></td>
<td><strong><select name="enabled">
<option selected="selected" value="''' + parser.get(section_name, 'ENABLED') + '''">Enabled? ''' + parser.get(section_name, 'ENABLED') + '''</option>
<option selected="selected" value="True">Enabled</option>
<option selected="selected" value="False">Disabled</option>
</select></strong></td>
</tr>
<tr>
<td><strong>Callsign:</strong></td>
<td>''' + parser.get(section_name, 'CALLSIGN') + '''</td>
</tr>
<tr>
<td><strong>DMR ID:</strong></td>
<td>''' + parser.get(section_name, 'RADIO_ID') + '''</td>
</tr>
<tr>
<td><strong>Color Code:</strong></td>
<td>''' + parser.get(section_name, 'COLORCODE') + '''</td>
</tr>
<tr>
<td><strong>Slots:</strong></td>
<td>''' + parser.get(section_name, 'SLOTS') + '''</td>
</tr>
<tr>
<td><strong>Master IP:</strong></td>
<td>''' + parser.get(section_name, 'MASTER_IP') + '''</td>
</tr>
<tr>
<td><strong>Master Port:</strong></td>
<td>''' + parser.get(section_name, 'MASTER_PORT') + '''</td>
</tr>
<tr>
<td><strong>Passphrase:</strong></td>
<td>''' + parser.get(section_name, 'PASSPHRASE') + '''</td>
</tr>
<tr>
<td><strong>Description:</strong></td>
<td>''' + parser.get(section_name, 'DESCRIPTION') + '''</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
''')
                #print('''<tr><td><strong>System: </strong></td><td>''' + section_name + '''</td><td>''' + server_type + '''</td></tr>''')
            if parser.get(section_name, 'MODE') == 'OPENBRIDGE':
                server_type = 'Openbridge'
                print('''
<table style="width: 50%; margin-left: auto; margin-right: auto;" border="5" cellspacing="5" cellpadding="5">
<tbody>
<tr>
<td><strong>System Type:</strong></td>
<td>''' + parser.get(section_name, 'MODE') + '''</td>
</tr>
<tr>
<td><strong>Name:</strong></td>
<td>''' + section_name + '''</td>
</tr>
<tr>
<td><strong>Status:</strong></td>
<td><strong>''' + parser.get(section_name, 'ENABLED') + '''</strong></td>
</tr>
<tr>
<td><strong>Network ID:</strong></td>
<td>''' + parser.get(section_name, 'NETWORK_ID') + '''</td>
</tr>
<tr>
<td><strong>Passphrase:</strong></td>
<td>''' + parser.get(section_name, 'PASSPHRASE') + '''</td>
</tr>
<tr>
<td><strong>Target IP:</strong></td>
<td>''' + parser.get(section_name, 'TARGET_IP') + '''</td>
</tr>
<tr>
<td><strong>Target Port:</strong></td>
<td>''' + parser.get(section_name, 'TARGET_PORT') + '''</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
''')
                #print('''<tr><td><strong>System: </strong></td><td>''' + section_name + '''</td><td>''' + server_type + '''</td></tr>''')
            if parser.get(section_name, 'MODE') == 'XLXPEER':
                server_type = 'XLX Peer'
                print('''<tr><td><strong>System: </strong></td><td>''' + section_name + '''</td><td>''' + server_type + '''</td></tr>''')

            #print(parser.get(section_name, 'MODE'))
        except Exception as Exc:
            #print(Exc)
            #print('')
            pass

def bridge_list(bridge):
#    with open(rule_file) as BRIDGES:
        for key in BRIDGES[bridge]:
            print('''


<tr>
<td style="width: 33px;"><strong>Rule: </strong>''' + str(BRIDGES[bridge].index(key)) + '''</td>
<td style="width: 51px;"><strong>System: </strong>''' + str(key[hblink_system]) + '''</td>
<td style="width: 52px;"><strong>Timeslot: </strong>''' + str(key[hblink_ts]) + '''</td>
<td style="width: 10px;"><strong>Talkgroup:&nbsp; </strong>''' + str(key[hblink_tgid]) + '''</td>
<td style="width: 70px;"><strong>Activate on start:&nbsp; </strong>''' + str(key[hblink_active]) + '''</td>
<td style="width: 10px;"><strong>Timer time: </strong>''' + str(key[hblink_timeout]) + '''</td>
<td style="width: 40px;"><strong>Timer type:&nbsp;</strong>''' + str(key[hblink_to_type]) + '''</td>
<td style="width: 40px;"><strong>Trigger ON:&nbsp; </strong>''' + str(key[hblink_on]) + '''</td>
<td style="width: 40px;"><strong>Trigger OFF:&nbsp; </strong>''' + str(key[hblink_off]) + '''</td>
<td style="width: 40px;"><strong>Trigger RESET: </strong>''' + str(key[hblink_reset]) + '''</td>
</tr>

''')


header = '''
<html>
<head>
<title>HBLink Web Administration</title>
<style>
body {
  background: white;
}

.content {
  max-width: 1400px;
  margin: auto;
  background: white;
  padding: 10px;
}
</style>
</head>

<body>
<div class="content">

<p><a href="view.py" target="_blank" rel="noopener"><img style="display: block; margin-left: auto; margin-right: auto;" src="data:image/png;base64,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" /></a></p>
<hr />
<h2 class="content" style="text-align: center;">HBLink Web Administration Panel </h2>
<hr />
<table style="width: 100%; height: 30px;" border="5" cellspacing="5" cellpadding="5"><caption>&nbsp;</caption>
<tbody>
<tr>
<td><a href="view.py"><strong>View Rules</strong></a></td>
<td><a href="add.py"><strong>Add Rule</strong></a></td>
<td><a href="delete.py"><strong>Delete Rule</strong></a></td>
<td><a href="add_config.py"><strong>Add Configuration</strong></a></td>
<td><a href="edit_config.py"><strong>View/Edit Configuration</strong></a></td>
<td><a href="adv_edit.py"><strong>Advanced Edit Configuration</strong></a></td>
<td><a href="log.py"><strong>Logs</strong></a></td>
<td><a href="hbmonitor.py"><strong>HB Monitor</strong></a></td>
<td><a href="restart_hblink.py"><strong>Restart HBLink</strong></a></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<hr />'''

footer = '''
<p>&nbsp;</p>
<hr />
<p>Web Administration Panel, Copyright (C) 2020, by Eric - KF7EEL, <a href="mailto:kf7eel@qsl.net. ">kf7eel@qsl.net. </a><br />HBLink is Copyright (C) 2016-2020 Cortney T. Buffington, N0MJS <a href="mailto:n0mjs@me.com">n0mjs@me.com</a>.</p>
<hr />
</div>
</body>
</html>
'''

redirect = '''
<strong>Window closing in 3 seconds.</strong>
<script type="text/javascript">
setTimeout(
function ( )
{
  self.close();
}, 3000 );
</script>
'''

# Templates

#view_home = '''


##    <th class="tg-cly1">Rule: <br></th>
##    <th class="tg-cly1">System: ''' + key[hblink_system] + '''<br></th>
##    <th class="tg-0lax">Timeslot: ''' + str(key[hblink_ts]) + '''</th>
##    <th class="tg-0lax">Talkgroup: ''' + str(key[hblink_tgid]) + '''</th>
##    <th class="tg-0lax">Activate at start: ''' + str(key[hblink_active]) + '''</th>
##    <th class="tg-0lax">Timer time: ''' + str(key[hblink_timeout]) + '''</th>
##    <th class="tg-0lax">Timer type: ''' + str(key[hblink_to_type]) + '''</th>
##    <th class="tg-0lax">Trigger on TGs: ''' + str(key[hblink_on]) + '''</th>
##    <th class="tg-0lax">Trigger off TGs: ''' + str(key[hblink_off]) + '''</th>
##    <th class="tg-0lax">Trigger timer reset TGs: ''' + str(key[hblink_reset]) + '''</th>
##  </tr>

            
