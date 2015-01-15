"""
WSGI config for sharkblazers project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sharkblazers.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# from sharkblazers import util
# first_names = util.io.read_file("/Work/personal/sharkblazers/resources/first_names.txt")
# first_names = first_names.split("\n")
# while first_names[len(first_names) - 1] == "":
#     first_names = first_names[0:len(first_names) - 1]
# print "%s first names" % str(len(first_names))