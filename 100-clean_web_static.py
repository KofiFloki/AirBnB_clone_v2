#!/usr/bin/python3
"""
Cleans the older archive from
webservers
"""
from fabric.api import local, run, env, cd
import os

env.hosts = ['18.235.234.111', '100.25.181.230']


def clean_local(number=0):
    """cleans the pack"""
    lists = local('ls -1t versions', capture=True)
    lists = lists.split('\n')
    n = int(number)
    if n in (0, 1):
        n = 1
    for f in lists[n:]:
        local('rm versions/{}'.format(f))


def clean_remote(number=0):
    """cleans the data in webserver"""
    lists = run('ls -1t /data/web_static/releases')
    lists = lists.split('\r\n')
    n = int(number)
    if n in (0, 1):
        n = 1
    for f in lists[n:]:
        if f is 'test':
            continue
        run('sudo rm -rf /data/web_static/releases/{}'.format(f))


def do_clean(number=0):
    """deletes older versions of data from web server"""
    clean_local(number)
    clean_remote(number)
