#! /usr/bin/python -Es

import os
from distutils.core import setup


# README function
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == '__main__':
    setup(
            name="gmailcommandline",
            version="0.11.1",
            author="Leonidas S. Barbosaa",
            author_email="kirotawa@gmail.com",
            description=("Easy way to send emails via gmail through command \
                          line "),
            license="MIT",
            keywords="email gmail bash commandline",
            url="https://github.com/kirotawa",
            packages=['gcmd'],
           # package_data = {'gcmd': []},
           #scritps = ["gmailcommandline"],
            long_description=read('README'),
    )
