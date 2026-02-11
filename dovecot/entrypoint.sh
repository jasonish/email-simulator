#!/bin/sh
mkdir -p /var/mail/vhosts/example.com/user
chown -R 5000:5000 /var/mail/vhosts
exec dovecot -F
