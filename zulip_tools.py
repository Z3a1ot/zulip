#!/usr/bin/env python2.7
from __future__ import print_function
import errno
import os
import sys
import datetime
import pwd

DEPLOYMENTS_DIR = "/home/zulip/deployments"
LOCK_DIR = os.path.join(DEPLOYMENTS_DIR, "lock")
TIMESTAMP_FORMAT = '%Y-%m-%d-%H-%M-%S'

# Color codes
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def su_to_zulip():
    pwent = pwd.getpwnam("zulip")
    os.setgid(pwent.pw_gid)
    os.setuid(pwent.pw_uid)

def make_deploy_path():
    timestamp = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
    return os.path.join(DEPLOYMENTS_DIR, timestamp)

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'make_deploy_path':
        print(make_deploy_path())

def mkdir_p(path):
    # Python doesn't have an analog to `mkdir -p` < Python 3.2.
    try:
        os.makedirs(path)
    except OSError, e:
        if e.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
