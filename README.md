# 1secmail
 1secmail.com api lib for Python 3.6 and high
 
For use:

Download file and do import:
```
import onesec_api
```
Use example:
```
!python

import onesec_api
import json

# for use random email box
ma = Mailbox('')
# for user sets email
ma = Mailbox('my.favorite.mail')
# get id for all mail in box
mb = ma.filtred_mail()
print('all mail id: ', mb)

# print all field and body-only for first message in list:
if isinstance(mb, list):
    
    print(mb[0]) # all field
    mf = ma.mailjobs('read',mb[0])
    print('first mail body: ',mf.json()['body']) # only body
else:
    mf = 'not found'
   
print ("if email from gmail.com contain 'Restore password' subject - return restore link and clear mailbox")
rl = ma.get_link('gmail.com', 'Restore password')
print ('Your restore link:', rl)
```
# Param

Mail filter:

onesec_api.filtred_mail (domain(or part of), subject(or part), id(only int), date(in YYYY-MM-DD format)

onesec_api.get_link (domain(or part of), subject(or part), x-path, clear_box(default: True))

if you receive message with link - all mail in temp box was delete. But, if you need save mail - set clear_box to False

---