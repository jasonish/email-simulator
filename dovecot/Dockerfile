FROM alpine:3.19

RUN apk add --no-cache dovecot dovecot-pop3d

# Recreate vmail user with fixed UID/GID (must match Postfix)
RUN deluser vmail 2>/dev/null; delgroup vmail 2>/dev/null; \
    addgroup -g 5000 vmail && \
    adduser -D -u 5000 -G vmail -h /var/mail/vhosts vmail

COPY dovecot.conf /etc/dovecot/dovecot.conf
COPY passwd /etc/dovecot/passwd

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 143 110
CMD ["/entrypoint.sh"]
