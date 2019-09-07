import os
home = '/data/data/com.termux/files/home/'
nick = input('name/nick: ')
open(home+'.nick','w').write(nick)
try:
    #open file di path $HOME
    rc = open(home+'.bashrc','r+')
    rc.read()
    #jika file .bashrc ada dan ada isinya, bakal ditulis dibawah
    rc.writelines('\nexport PYTHONSTARTUP=~/.pyrc')
    rc.close()
except FileNotFoundError:
    #jika file .bashrc gk ada, ya jojong ae ditulis :3
    open(home+'.bashrc','w').write('export PYTHONSTARTUP=~/.pyrc')

os.system('chmod 755 .pyrc; cp .pyrc ~/.pyrc')
#tanda ~ sama kayak path $HOME
print("Done!")
