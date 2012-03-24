#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

import os

def p(op, bu):
    os.environ['CPPFLAGS']= os.environ['CFLAGS']
    os.environ['ASFLAGS']= os.environ['CFLAGS']

# vim:set et sts=4 ts=4 tw=80:
