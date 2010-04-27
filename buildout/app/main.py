# -*- coding: utf-8 -*-
"""
    main
    ~~~~

    Run Tipfy apps.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE for more details.
"""
import os
import sys

if 'lib' not in sys.path:
    sys.path[0:0] = ['lib', 'distlib', 'distlib.zip']

import config
import tipfy

# Instantiate the application.
application = tipfy.make_wsgi_app(config.config)

def main():
    # Run it!
    tipfy.run_wsgi_app(application)

if __name__ == '__main__':
    main()
