README

Using rpi-jabber to accept and parse XMPP Messages
https://code.google.com/p/rpi-jabber/wiki/GettingStarted

Setup as defined, with a new XMPP account from http://xmpp.net/

Launch two services using tmux:
/etc/jabberd/cmds

sudo python MakeCoffee.py
sudo /etc/init.d/jabberd start

This will wait for messages from authorized XMPP accounts, if they begin with 'barista' the 'barista' python script will attempt to parse your directions and if they match the form defined, send a message to the 'MakeCoffee.py' flask server and start/stop coffee.

Glass messages sent from https://bareboneglass.appspot.com/ unable to figure out how to send messages back to Glass, so I'm sending emails to myself when coffee is started/stopped/ready.  Oodles of looping messages between Glass and rpi-jabber.

Source code for Glass service at https://github.com/DeqingSun/bare_glass_app.