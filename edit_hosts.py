#!/usr/bin/env python3
import time
print('Python start.')
print('In Progress...')
time.sleep(3)
with open('hosts_new', 'r') as f0:
	ffile0 = []
	ffile0=f0.readlines()
	i=0	
	while i < 16 :
		i = i + 1
		ffile0.pop(0)
f0.close
#delete lines above "# Modified hosts Start"(11 lines), and put the rest lines into a list.
with open('hosts_old', 'r') as f1:
	ffile1 = []
	i = 0
	while i < 23:
		i = i + 1
		ffile1.append(f1.readline())
f1.close
#read old hosts file, keep 23 lines and put them into a list.
with open('hosts_edited', 'w') as f2:
	f2.truncate()
	f2.write("".join(ffile1))
	f2.write("".join(ffile0))
f2.close
#write two lists into a new hosts file.
print('Modification Complete.')	
