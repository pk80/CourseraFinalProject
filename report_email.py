#!/usr/bin/env python3

import os
import datetime
import reports
import emails

USER = 'student'
dt = datetime.date.today().strftime("%B %d, %Y")
date = f'Processed Update on {dt}'
names = []
weights = []
descPath = './supplier-data/descriptions'

for file in os.listdir(descPath):
    with open(os.path.join(descPath, file), 'r') as f:
        for ln in f:
            line = ln.strip()
            if len(line) <= 10 and len(line) > 0 and 'lb' not in line:
                fruit_name = 'name: ' + line
                names.append(fruit_name)
            if 'lbs' in line:
                fruit_weight = 'weight: ' + line
                weights.append(fruit_weight)

summary = ''
for name, weight in zip(names, weights):
    summary += name + '<br />' + weight + '<br />' + '<br />'

if __name__ == '__main__':
    reportDest = './tmp/processed.pdf'
    reports.generate_report(reportDest, date, summary)

    sender = 'automation@example.com'
    receiver = f'{USER}@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our webseite successfully. A detailed list is attached to this email.'

    message = emails.generate_email(
        sender, receiver, subject, body, reportDest)
    # emails.send_email(message)
    with open('./tmp/processed.txt') as f:
        f.write(str(message))
        f.close()
