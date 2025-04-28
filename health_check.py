#!/usr/bin/env python3

import shutil
import emails
import psutil
import socket

USER = 'student'

sender = 'automation@example.com'
receiver = f'{USER}@example.com'
body = 'Please check your system and resolve the issue as soon as possible.'

# check disk usage
# if available space < 20%, then send email
du = shutil.disk_usage('/')
du_pecnt = du.free/du.total * 100
if du_pecnt < 20:
    subject = 'Error - Available dis space is less than 20%'
    message = emails.generate_error_email(sender, receiver, subject, body)
    # emails.send_email(message)
    with open('./tmp/error_du.txt', 'w') as file:
        file.write(str(message))
        file.close()

# check cpu usage
# if cpu usage > 80%, then send email
cpu_pecnt = psutil.cpu_percent(1)
if cpu_pecnt > 80:
    subject = 'Error - CPU usage is over 80%'
    message = emails.generate_error_email(sender, receiver, subject, body)
    # emails.send_email(message)
    with open('./tmp/error_cpu.txt', 'w') as file:
        file.write(str(message))
        file.close()

# check available memory
# if available memory < 100MB, then send email
mem = psutil.virtual_memory()
trs = 100 * 1024 * 1024  # 100MB
if mem.available < trs:
    subject = 'Error - Available memory is less than 100MB'
    message = emails.generate_error_email(sender, receiver, subject, body)
    # emails.send_email(message)
    with open('./tmp/error_mem.txt', 'w') as file:
        file.write(str(message))
        file.close()

# check hostname
# if hostname != '127.0.0.1', then send email
hostname = socket.gethostname('localhost')
if hostname != '127.0.0.1':
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    message = emails.generate_email(sender, receiver, subject, body)
    # emails.send_email(message)
    with open('./tmp/error_hostname.txt', 'w') as file:
        file.write(str(message))
        file.close()
