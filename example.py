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