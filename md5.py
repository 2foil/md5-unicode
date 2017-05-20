#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  pip install PyExecJS

import execjs

def MD5(s):
    with open('md5.js','r') as f:
        ctx = execjs.compile(f.read())

    return ctx.call('MD5', s)

if __name__ == '__main__':
    pass
