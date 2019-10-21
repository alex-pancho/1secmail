from onesec_api import Mailbox
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