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

from polls.models import Poll, Choice

# Make sure our __unicode__() addition worked.
print Poll.objects.all()

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
print Poll.objects.filter(id=1)
print Poll.objects.filter(question__startswith='What')

# Get the poll whose year is 2007.
import datetime
print Poll.objects.get(pub_date__year=2007)

try:
    print Poll.objects.get(id=2)
except:
    import sys, traceback
    print "Exception:"
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Poll.objects.get(id=1).
print Poll.objects.get(pk=1)

# Make sure our custom method worked.
p = Poll.objects.get(pk=1)
print p
print p.was_published_today()

# Give the Poll a couple of Choices. The create call constructs a new
# choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a poll's choices) which can be accessed via the API.
p = Poll.objects.get(pk=1)
print p

# Display any choices from the related object set -- none so far.
print p.choice_set.all()

# Create three choices.
print p.choice_set.create(choice='Not much', votes=0)

print p.choice_set.create(choice='The sky', votes=0)

c = p.choice_set.create(choice='Just hacking again', votes=0)
print c

# Choice objects have API access to their related Poll objects.
print c.poll

# And vice versa: Poll objects get access to Choice objects.
print p.choice_set.all()

print p.choice_set.count()

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any poll whose pub_date is in 2007.
print Choice.objects.filter(poll__pub_date__year=2007)

# Let's delete one of the choices. Use delete() for that.
c = p.choice_set.filter(choice__startswith='Just hacking')
print c
print c.delete()
