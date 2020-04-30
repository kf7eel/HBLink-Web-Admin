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

# Generates HTML page for adding rules

import cgi, cgitb, sys, os
#sys.path.append('..')
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# Add rule page

from config import *
from core import *
from rules_web import *

def list_master_button():
    parser = ConfigParser()
    parser.read(hblink_loc + 'hblink.cfg')
    for section_name in parser.sections():
    #print('Section: ' + section_name)
        try:
            if parser.get(section_name, 'MODE') == 'MASTER':
                #print(section_name)
                server_type = 'Master - '
                print('''<option selected="selected" value="''' + section_name + '''">''' + server_type + section_name + '''</option>''')
            if parser.get(section_name, 'MODE') == 'PEER':
                #print(section_name)
                server_type = 'Peer - '
                print('''<option selected="selected" value="''' + section_name + '''">''' + server_type + section_name + '''</option>''')       
            if parser.get(section_name, 'MODE') == 'OPENBRIDGE':
                #print(section_name)
                server_type = 'Openbridge - '
                print('''<option selected="selected" value="''' + section_name + '''">''' + server_type + section_name + '''</option>''')       
            if parser.get(section_name, 'MODE') == 'XLXPEER':
                #print(section_name)
                server_type = 'XLX Peer - '
                print('''<option selected="selected" value="''' + section_name + '''">''' + server_type + section_name + '''</option>''')       

            #print(parser.get(section_name, 'MODE'))
        except:
            pass

print(header)

print('''
<h2 style="text-align: center;"><strong>Add rule:</strong></h2>''')

##print('''
##<p style="text-align: center;"><strong><h3>Add rule to system:</h3></strong></p>''')
##
##print('''
##<form action = "/cgi-bin/add_rule.py" method = "post" target = "_blank">
##''')
##print('''
##<p>From rules.py:</p>
##<p><br />This file is organized around the "Conference Bridges" that you wish to use. If you're a c-Bridge<br />person, think of these as "bridge groups". You might also liken them to a "reflector". If a particular<br />system is "ACTIVE" on a particular conference bridge, any traffic from that system will be sent<br />to any other system that is active on the bridge as well. This is not an "end to end" method, because<br />each system must independently be activated on the bridge.</p>
##<p>The first level (e.g. "WORLDWIDE" or "STATEWIDE" in the examples) is the name of the conference<br />bridge. This is any arbitrary ASCII text string you want to use. Under each conference bridge<br />definition are the following items -- one line for each HBSystem as defined in the main HBlink<br />configuration file.</p>
##<p><strong>SYSTEM</strong> - The name of the sytem as listed in the main hblink configuration file (e.g. hblink.cfg)<br /> This MUST be the exact same name as in the main config file!!!</p>
##<p><strong>Timeslot</strong> - Timeslot used for matching traffic to this confernce bridge<br /> XLX connections should *ALWAYS* use TS 2 only.</p>
##<p><strong>Talkgroup</strong> - Talkgroup ID used for matching traffic to this conference bridge<br /> XLX connections should *ALWAYS* use TG 9 only.</p>
##<p><strong>ON </strong>and<strong> OFF</strong> are LISTS of Talkgroup IDs used to trigger this system off and on. <span style="text-decoration: line-through;">Even if you</span><br /><span style="text-decoration: line-through;"> only want one (as shown in the ON example), it has to be in list format. None can be</span><br /><span style="text-decoration: line-through;"> handled with an empty list, such as " 'ON': [] ".</span></p>
##<p><span style="text-decoration: line-through;">TO_TYPE</span> <strong>Timer type</strong> -&nbsp; is timeout type. If you want to use timers, ON means when it's turned on, it will<br /> turn off afer the timout period and OFF means it will turn back on after the timout<br /> period. If you don't want to use timers, set it to anything else, but 'NONE' might be<br /> a good value for documentation!</p>
##<p><strong>TIMEOUT</strong> -&nbsp; is a value in minutes for the timout timer. No, I won't make it 'seconds', so don't<br /> ask. Timers are performance "expense".</p>
##<p><strong>RESET - </strong>is a list of Talkgroup IDs that, in addition to the ON and OFF lists will cause a running<br /> timer to be reset. This is useful if you are using different TGIDs for voice traffic than<br /> triggering. If you are not, there is NO NEED to use this feature.</p>
##''')
##print('''
##<table style="width: 1200px; height: 50px; float: left;" border="5" cellspacing="10" cellpadding="10">
##<tbody>
##<tr>
##<td><strong>Bridge: </strong>
##<select name = "bridge_dropdown">''') 
##for system in BRIDGES:
##    print('''
##      <option value = "''' + str(system) + '''" selected>''' + str(system) + '''</option>''')
##print('''</select></td>
##<td><strong>System: </strong><input name="system_text" type="text" />
##</td>
##<td><strong>Timeslot: </strong><select name="ts_dropdown">
##<option selected="selected" value="1">1</option>
##<option selected="selected" value="2">2</option>
##</select></td>
##<td><strong>Talkgroup: </strong> <input name="tgid" type="text" /></td>
##<td><strong>Activate on start:</strong> &nbsp;<select name="active_dropdown">
##<option selected="selected" value="True">False</option>
##<option selected="selected" value="False">True</option>
##</select></td>
##<td><strong>Timer Time: </strong> &nbsp;<input name="timer_time" type="text" /></td>
##<td><strong>Timer Type: &nbsp;</strong><select name="type_dropdown">
##<option selected="selected" value="NONE">None</option>
##<option selected="selected" value="ON">On</option>
##<option selected="selected" value="OFF">Off</option>
##</select></td>
##<td><strong>Trigger ON TGs: &nbsp;</strong> <input name="on" type="text" /></td>
##<td><strong>Trigger OFF TGs:</strong> &nbsp;<input name="off" type="text" /></td>
##<td><strong>Trigger Reset TGs: &nbsp; <input name="reset" type="text" /></strong></td>
##<td><input type = "submit" value = "Add Rule"/>
##</td>
##</tr>
##</tbody>
##</table>
##</form>
##
##
##''')
##print('''
##<p>&nbsp;</p>
##<hr />
##<p style="text-align: center;"><strong><h3>Add system and rule:</h3></strong></p>
##<p>&nbsp;</p>
##
##''')
##print('''
##<form action = "/cgi-bin/add_rule.py" method = "post" target = "_blank">
##
##<table style="width: 1200px; height: 50px; float: left;" border="5" cellspacing="10" cellpadding="10">
##<tbody>
##<tr>
##<td><strong>Bridge name: &nbsp; <input name="bridge_dropdown" type="text" /></strong></td>
##
##<td><strong>System: </strong><input name="system_text" type="text" />
##</td>
##<td><strong>Timeslot: </strong><select name="ts_dropdown">
##<option selected="selected" value="1">1</option>
##<option selected="selected" value="2">2</option>
##</select></td>
##<td><strong>Talkgroup: </strong> <input name="tgid" type="text" /></td>
##<td><strong>Activate on start:</strong> &nbsp;<select name="active_dropdown">
##<option selected="selected" value="True">False</option>
##<option selected="selected" value="False">True</option>
##</select></td>
##<td><strong>Timer Time: </strong> &nbsp;<input name="timer_time" type="text" /></td>
##<td><strong>Timer Type: &nbsp;</strong><select name="type_dropdown">
##<option selected="selected" value="NONE">None</option>
##<option selected="selected" value="ON">On</option>
##<option selected="selected" value="OFF">Off</option>
##</select></td>
##<td><strong>Trigger ON TGs: &nbsp;</strong> <input name="on" type="text" /></td>
##<td><strong>Trigger OFF TGs:</strong> &nbsp;<input name="off" type="text" /></td>
##<td><strong>Trigger Reset TGs: &nbsp; <input name="reset" type="text" /></strong></td>
##<td><input type = "submit" value = "Add Rule"/>
##</td>
##</tr>
##</tbody>
##</table>
##</form>
##
##
##''')
##print('-----')

print('''
<form action = "/cgi-bin/add_rule.py" method = "post" target = "_blank">
''')
print('''
<p style="text-align: center;"><strong><h3>Add rule to system:</h3></strong></p>''')

print('''
<p>&nbsp;</p>
<table border="1" width="100%">
<tbody>
<tr>
<td><strong>Bridge: </strong>
<select name = "bridge_dropdown">''') 
for system in BRIDGES:
    print('''
      <option value = "''' + str(system) + '''" selected>''' + str(system) + '''</option>''')
print('''</select></td>
<td><strong>System: </strong><select name="system_text">''')
list_master_button()
print('''
</select></td>
<td><strong>Timeslot: </strong><select name="ts_dropdown">
<option selected="selected" value="1">1</option>
<option selected="selected" value="2">2</option>
</select></td>
<td><strong>Talkgroup: </strong> <input name="tgid" type="text" /></td>
<td><strong>Activate on start:</strong> &nbsp;<select name="active_dropdown">
<option selected="selected" value="True">True</option>
<option selected="selected" value="False">False</option>
</select></td></tr>
<tr><td><strong>Timer Time: </strong> &nbsp;<input name="timer_time" type="text" /></td>
<td><strong>Timer Type: &nbsp;</strong><select name="type_dropdown">
<option selected="selected" value="NONE">None</option>
<option selected="selected" value="ON">On</option>
<option selected="selected" value="OFF">Off</option>
</select></td>
<td><strong>Trigger ON TGs: &nbsp;</strong> <input name="on" type="text" /></td>
<td><strong>Trigger OFF TGs:</strong> &nbsp;<input name="off" type="text" /></td>
<td><strong>Trigger Reset TGs: &nbsp; <input name="reset" type="text" /></strong></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>

<input type = "submit" value = "Add Rule"/>
</form>
<hr />

<p>&nbsp;</p>


''')
print('''
<p style="text-align: center;"><strong><h3>Add system:</h3></strong></p>
<p>&nbsp;</p>

''')
print('''
<form action = "/cgi-bin/add_rule.py" method = "post" target = "_blank">

<table border="1" width="100%">
<tbody>
<tr>
<td><strong>Bridge name: &nbsp; <input name="bridge_dropdown" type="text" /></strong></td>

<td><strong>System: </strong></strong><select name="system_text">''')
list_master_button()
print('''
</select></td>
<td><strong>Timeslot: </strong><select name="ts_dropdown">
<option selected="selected" value="1">1</option>
<option selected="selected" value="2">2</option>
</select></td>
<td><strong>Talkgroup: </strong> <input name="tgid" type="text" /></td>
<td><strong>Activate on start:</strong> &nbsp;<select name="active_dropdown">
<option selected="selected" value="True">True</option>
<option selected="selected" value="False">False</option>
</select></td></tr>
<tr><td><strong>Timer Time: </strong> &nbsp;<input name="timer_time" type="text" /></td>
<td><strong>Timer Type: &nbsp;</strong><select name="type_dropdown">
<option selected="selected" value="NONE">None</option>
<option selected="selected" value="ON">On</option>
<option selected="selected" value="OFF">Off</option>
</select></td>
<td><strong>Trigger ON TGs: &nbsp;</strong> <input name="on" type="text" /></td>
<td><strong>Trigger OFF TGs:</strong> &nbsp;<input name="off" type="text" /></td>
<td><strong>Trigger Reset TGs: &nbsp; <input name="reset" type="text" /></strong></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>

<input type = "submit" value = "Add System"/>
</form>
<hr />

<br />


''')
print('''

<br />
<p>From rules.py:</p>
<p>This file is organized around the "Conference Bridges" that you wish to use. If you're a c-Bridge<br />person, think of these as "bridge groups". You might also liken them to a "reflector". If a particular<br />system is "ACTIVE" on a particular conference bridge, any traffic from that system will be sent<br />to any other system that is active on the bridge as well. This is not an "end to end" method, because<br />each system must independently be activated on the bridge.</p>
<p>The first level (e.g. "WORLDWIDE" or "STATEWIDE" in the examples) is the name of the conference<br />bridge. This is any arbitrary ASCII text string you want to use. Under each conference bridge<br />definition are the following items -- one line for each HBSystem as defined in the main HBlink<br />configuration file.</p>
<p><strong>SYSTEM</strong> - The name of the sytem as listed in the main hblink configuration file (e.g. hblink.cfg)<br /> This MUST be the exact same name as in the main config file!!!</p>
<p><strong>Timeslot</strong> - Timeslot used for matching traffic to this confernce bridge<br /> XLX connections should *ALWAYS* use TS 2 only.</p>
<p><strong>Talkgroup</strong> - Talkgroup ID used for matching traffic to this conference bridge<br /> XLX connections should *ALWAYS* use TG 9 only.</p>
<p><strong>ON </strong>and<strong> OFF</strong> are LISTS of Talkgroup IDs used to trigger this system off and on. <span style="text-decoration: line-through;">Even if you</span><br /><span style="text-decoration: line-through;"> only want one (as shown in the ON example), it has to be in list format. None can be</span><br /><span style="text-decoration: line-through;"> handled with an empty list, such as " 'ON': [] ".</span></p>
<p><span style="text-decoration: line-through;">TO_TYPE</span> <strong>Timer type</strong> -&nbsp; is timeout type. If you want to use timers, ON means when it's turned on, it will<br /> turn off afer the timout period and OFF means it will turn back on after the timout<br /> period. If you don't want to use timers, set it to anything else, but 'NONE' might be<br /> a good value for documentation!</p>
<p><strong>TIMEOUT</strong> -&nbsp; is a value in minutes for the timout timer. No, I won't make it 'seconds', so don't<br /> ask. Timers are performance "expense".</p>
<p><strong>RESET - </strong>is a list of Talkgroup IDs that, in addition to the ON and OFF lists will cause a running<br /> timer to be reset. This is useful if you are using different TGIDs for voice traffic than<br /> triggering. If you are not, there is NO NEED to use this feature.</p>
''')
print (footer)
