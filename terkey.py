import os
from time import sleep


a ='\033[92m'
b ='\033[96m'
c ='\033[0m'
os.system('clear')
print(a+'∞∞∞'*18)
print(a+'\t     TerKey v.01')
print(b+'\t Author  : King Mr_Z17')
print('\t YouTube : Mr_Z17')
print(a+'∞∞∞'*18)
print('\nProcess..')
sleep(1)
print(b+'\n[!] making termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !! :)'+c+'\n\nT3R1M4 K4S1H T3L4H M3N66UN4K4N TOOLS K4MI..!! :*\n\n')
print(a+'Salam Admin..!! :D'*1)


# © Copyright,All rights 2020
# King Mr_Z17 
