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
# from faker.fake_factory import Factory
# factory = Factory()
#
# for x in xrange(20):
#     o = factory.create()
#     print util.json(o, indent=2)
# print ""
