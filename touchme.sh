#!/usr/bin/bash
read -p 'name/nick: ' hm
echo -n $hm>~/.nick
echo -n 'export PYTHONSTARTUP=~/.pyrc'>~/.bash_profile
chmod 755 .pyrc
cp .pyrc ~/.pyrc
echo Done!
