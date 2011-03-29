#!/usr/bin/env python
from django.core.management import execute_manager
import imp
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from polls.models import Poll, Choice # Import the model classes we just wrote.

# No polls are in the system yet.
print Poll.objects.all()

# Create a new Poll.
import datetime
p = Poll(question="What's up?", pub_date=datetime.datetime.now())
print p

# Save the object into the database. You have to call save() explicitly.
print p.save()

# Now it has an ID. Note that this might say "1L" instead of "1", depending
# on which database you're using. That's no biggie; it just means your
# database backend prefers to return integers as Python long integer
# objects.
print p.id

# Access database columns via Python attributes.
print p.question

print p.pub_date

# Change values by changing the attributes, then calling save().
p.pub_date = datetime.datetime(2007, 4, 1, 0, 0)
print p.pub_date
print p.save()

# objects.all() displays all the polls in the database.
print Poll.objects.all()
