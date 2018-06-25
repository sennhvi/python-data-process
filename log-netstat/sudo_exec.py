#!/usr/bin/env python
# encoding: utf-8

import os, platform, logging
import subprocess, pexpect

log = logging.getLogger(__name__)

def sudo_exec(cmdline, passwd):
    osname = platform.system()
    if osname == 'Linux':
        prompt = r'\[sudo\] password for %s: ' %os.environ['USER']
    else:
        assert False, osname

    child = pexpect.spawn(cmdline)
    idx = child.expect([prompt, pexpect.EOF], 3)
    if idx == 0:
        log.debug('sudo password was asked.')
        child.sendline(passwd)
        child.expect(pexpect.EOF)

    return child.before

