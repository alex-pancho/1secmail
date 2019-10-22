# 1secmail
1secmail.com api lib for Python 3.6 and high
 
For use:

Download file and do import:
```python
from onesec_api import Mailbox
```
*Use example*
```python

from onesec_api import Mailbox
import json

print('# Example for use random email box')
mb = Mailbox()
print('\n# Example for use user sets email')
mb = Mailbox('my.favorite.mail')
# get id for all mail in box
all_id = mb.filtred_mail()
print('all mail id: ', all_id)

# print all field and body-only for first message in list:
if isinstance(all_id, list): 
    print('first message id:', all_id[0])
    first_mail = mb.mailjobs('read',all_id[0])
    print('first mail body: ',first_mail.json()['body'])
else:
    print('first mail not found')
   
print ("\n# Find email from gmail.com \n# If email from gmail.com contains 'Restore password' subject -\n# return restore link and clear mailbox")
rl = mb.get_link('gmail.com', 'Restore password')
print ('Your restore link:', rl)
```
# Params

*Mail filter:*

onesec_api.filtred_mail (domain(or part of), subject(or part), id(only int), date(in YYYY-MM-DD format))

*Get link from mail body:*

onesec_api.get_link (domain(or part of), subject(or part), x-path, clear_box(default: True))

if you receive message with link - all mail in temp box was delete. But, if you need save mail - set clear_box to False

---
