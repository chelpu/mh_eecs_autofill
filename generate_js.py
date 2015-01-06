event_name = raw_input('Enter the event name: ');
event_date = raw_input('Enter the date (mm/dd/yyyy): ')
event_time = raw_input('Enter time time (ex. 7pm): ')
event_location = raw_input('Enter the location: ')
event_desc = raw_input('Enter the event description: ')

print event_name, event_location

javascript_code = "document.getElementById('QR~QID1').value = 'Chelsea';\n"
javascript_code += "document.getElementById('QR~QID2').value = 'Pugh';\n"
javascript_code += "document.getElementById('QR~QID3').value = 'chelpu';\n"
javascript_code += "document.getElementById('QR~QID12').value = 'chelpu@umich.edu';\n"
javascript_code += "document.getElementById('QR~QID14').value = 'chelpu@umich.edu';\n"
javascript_code += "document.getElementById('QR~QID11').value = 'michiganhackers-exec@umich.edu';\n"

javascript_code += "document.getElementById('QR~QID5').value = '" + event_name + "';\n"
javascript_code += "document.getElementById('QR~QID6').value = '" + event_date + "';\n"
javascript_code += "document.getElementById('QR~QID7').value = '" + event_time + "';\n"
javascript_code += "document.getElementById('QR~QID8').value = '" + event_location + "';\n"
javascript_code += "document.getElementById('QR~QID9').value = '" + event_desc + "';\n"

javascript_code += "document.getElementsByClassName('ChoiceStructure')[5].children[0].children[1].className = 'q-checkbox q-checked';\n"
javascript_code += "document.getElementsByClassName('ChoiceStructure')[5].children[0].children[2].children[0].className = 'MultipleAnswer q-checked';\n"
javascript_code += "document.getElementsByClassName('ChoiceStructure')[5].children[0].children[0].checked = true;\n"

print "Run this js in the console of the EECS announcement submission page:"
print javascript_code



