#!/bin/sh
mkdir -p /var/mail/vhosts/example.com/user
chown -R 5000:5000 /var/mail/vhosts

# Create SASL users for SMTP AUTH on submission port
mkdir -p /etc/sasl2
echo 'password' | saslpasswd2 -f /etc/sasl2/sasldb2 -p -c -u example.com alice
echo 'password' | saslpasswd2 -f /etc/sasl2/sasldb2 -p -c -u example.com bob
chmod 644 /etc/sasl2/sasldb2

exec postfix start-fg
