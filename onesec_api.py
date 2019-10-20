import requests
import json
import random
import string
#Set False if you don't need lxml html parser.
body_parser = True
if body_parser: import lxml.html as HT 

random_mail= False #change to True if you need random e-mail box

s = requests.Session() 
API = 'https://www.1secmail.com/api/v1/'

if random_mail:
    _mailbox_ = rand_pass()
    print(f'use mailbox: {_mailbox_}@1secmail.com')
else:
    _mailbox_ = 'api.test' #change to your own test mailbox


def _printTree(res, name=''):
    """Print out for lxml.html object"""

    print('tree : ', name)
    for child in res.iter('*'):
        print('\t', child.tag, child.attrib, child.text)
    print('\n')


def rand_pass(password=False):
    """Generate a random password """
    
    if password:
        special = string.punctuation
    else:
        special = ".!#$%&.+-=.?^_."
    
    randomSource = string.ascii_letters + string.digits + special
    password = ""
    for i in range(9):
        password += random.choice(randomSource)

    return password


def mailjobs (s, action, id=None):
    """Main operation with 1secmail.com api:
    'get' - get all mail in box
    'read' - read message in box (need message id)
    'del' - clear mailbox, all messages be removed!
    """
    
    mail_list = 'error'
    
    act_ilst = ['getMessages','deleteMailbox','readMessage']
    act_dict = {
        'get':act_ilst[0],
        'del':act_ilst[1],
        'read':act_ilst[2]
    }
        
    if action in ['read', 'readMessage'] and id is None:
        print ('Need message id for reading')
        return mail_list
    
    if action in act_dict:
        action = act_dict[action]
    elif action in act_ilst:
        pass
    else:
        print (f'Wrong action: {action}')
        return mail_list
    
    if action == 'readMessage':
        mail_list = s.get(API,
                params={'action':action, 
                    'login':_mailbox_,
                    'domain':'1secmail.com',
                    'id':id
                    }
                )
    if action == 'deleteMailbox':
        mail_list = s.post('https://www.1secmail.com/mailbox/',
                data={'action':action, 
                    'login':_mailbox_,
                    'domain':'1secmail.com'
                    }
                )
    if action == 'getMessages':
        mail_list = s.get(API,
                params={'action':action, 
                    'login':_mailbox_,
                    'domain':'1secmail.com'
                    }
                )
                
    return mail_list


def filtred_mail (domain=True, subject=True, id=True, date=True):
    """Simpled mail filter, all params optional"""
        
    ma = mailjobs(s, 'get')
    out_mail = []
    if ma != 'error':
        #print(ma.url)
        list_ma = ma.json()
        for i in list_ma:
            if id != True:
                id_find = i['id'].find(id) != -1
            else:
                id_find = id
            if date != True:
                dat_find = i['date'].find(date) != -1
            else: 
                dat_find = date
            if domain != True:
                dom_find = i['from'].find(domain) != -1
            else:
                dom_find = domain
            if subject != True:     
                sub_find = i['subject'].find(subject) != -1
            else:
                sub_find = subject
            if sub_find and dom_find and id_find and dat_find:
                out_mail.append(i['id'])
        
        if len(out_mail) >0:
            return out_mail
        else:
            return 'not found'
    else:
        return ma


def clear_box(domain, subject, clear=True):
    """Clear mail box if we find some message"""

    ma = filtred_mail(domain, subject)
    if isinstance(ma, list):
        ma = mailjobs(s, 'read', ma[0])
        if ma != 'error': 
            if clear: print('clear mailbox')
            if clear: x = mailjobs (s, 'del')
            return ma
        else:
            return ma
    else:
        return ma


if body_parser:
    def get_link(domain, subject, x_path='//a' ): 
        """Find link inside html mail body by x-path and return link"""

        ma = clear_box(domain, subject)
        if ma != 'error' and ma != 'not found':
            mail_body = ma.json()['body']
        else:
            return ma    
        #try:
        web_body = HT.fromstring(mail_body)   
        #except Type_of_Exception:
        #    print("except")
        child = web_body.xpath(x_path)[0]
        return child.attrib['href']
    
    
if __name__ == "__main__":
    """Easy test"""

    ma = filtred_mail()
    print('all mail id: ',ma)
    rest_url = get_link('domain.com', 'Password reset')
    print('restore url: ', rest_url)    
