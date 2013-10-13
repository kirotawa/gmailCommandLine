# installation dirs
PREFIX ?=$(DESTDIR)/usr
BINDIR ?=$(PREFIX)/bin
MANDIR ?=$(PREFIX)/share/man
PYTHON ?=/usr/bin/python

clean: 
	$(PYTHON) setup.py clean

install: 
	$(PYTHON) setup.py install 
	install -m 755 gmailcommandline.py $(BINDIR)/gmailcommandline
