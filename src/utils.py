# -*- coding: utf-8 -*-


import os.path
import sys
from getpass import getpass
from optparse import OptionParser

def  parsing():

    parser = OptionParser()
    parser.add_option("-d", "--destination", action = "store", dest = "destination",\
        help = "set a destination address to send e-mail, else send to default: yourself mail")
    parser.add_option("-a", "--attachpath", action = "store", dest = "attach",\
        help = "Attach  a file to email.")
    parser.add_option("-m", "--message", action = "store", dest = "message", \
        help = "The message that you want to send.")
    parser.add_option("-u", "--usermail", action = "store", dest = "usermail",\
        help = "Here put you user email of Gmail. Just need set in the first \
                time that use this  program.")
    parser.add_option("-s", "--subject", action = "store", dest = "subject",\
        help = " The subject of email.")

    (opts, args) = parser.parse_args()
    paramms = dict()

    file_path = os.path.join(os.environ.get('HOME'), '.mailuser')
    if opts.usermail is None:
        if os.path.exists(file_path):
            with open(file_path) as user_email:
                emails = user_email.readlines()
            if len(emails) == 1:    
            	paramms['user_email'] = emails[0].replace('\n','')

            elif len(emails) > 1:
                for num, email in enumerate(emails):
                    print num+1, email.replace('\n','')
                paramms['user_email'] = emails[input('Choose a email: ')-1].replace('\n','')
            
            else:
                print "No have emails in .mailuser file"
                sys.exit()

        else:
            print "Please use -u to set a gmail user, eg.: -u jonhnydoo@gmail.com.\
            This necessary just one time"
            sys.exit()
    else:
        emails = []
        if os.path.exists(file_path):
            with open(file_path) as _emails:
                emails = _emails.readlines()

        with open(file_path,'aw') as user_email:
            email = "%s\n" % opts.usermail
            if email in emails:
                paramms['user_email'] = opts.usermail
            elif opts.usermail.split('@')[1].split('.')[0] == 'gmail':
                user_email.write(email)
                paramms['user_email'] = opts.usermail
            else:
                print "Type a gmail address"
                sys.exit()

    if opts.subject is not None:
        paramms['sub'] = opts.subject
    else:
        paramms['sub'] = "No Subject"
    
    if opts.message is not None and opts.destination is not None:
        paramms['msg']  = opts.message
        paramms['dest'] = opts.destination

        if opts.attach is not None:
            paramms['attach'] = opts.attach
        else:
            paramms['attach'] = None		
        paramms['passwd'] = getpass()
        
    else:
        print "Missing: message or destination arguments that are necessary!"
        print "To more information use: gmailcommandline -h"
        sys.exit()

    return paramms
