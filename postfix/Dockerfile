FROM alpine:3.19

RUN apk add --no-cache postfix cyrus-sasl cyrus-sasl-login

# Recreate vmail user with fixed UID/GID (must match Dovecot)
RUN deluser vmail 2>/dev/null; delgroup vmail 2>/dev/null; \
    addgroup -g 5000 vmail && \
    adduser -D -u 5000 -G vmail -h /var/mail/vhosts vmail

COPY main.cf /etc/postfix/main.cf
COPY master.cf /etc/postfix/master.cf
COPY vmailbox /etc/postfix/vmailbox
RUN postmap lmdb:/etc/postfix/vmailbox && newaliases

COPY smtpd.conf /usr/lib/sasl2/smtpd.conf

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 25 587
CMD ["/entrypoint.sh"]
