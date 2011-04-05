#!/usr/bin/env python

from getpass import getpass
from optparse import OptionParser as option
from src import utils
from src import Mail



if __name__ == "__main__":
	paramms = utils.parsing()
	email = Mail.Mail(**paramms)
	email.send()

