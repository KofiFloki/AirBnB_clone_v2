#!/usr/bin/python3
"""
A Fabric Script that generates a .tgz archive
from the contents of the web_static folder
using a function do_pack
"""

from fabric.api import local
from datetime import datetime
from os.path import isdir
from os import stat

date = datetime.now().strftime("%Y%m%d%H%M%S")


def do_pack():
    """generates a .tgx archive from web_static"""
    if not isdir("versions"):
        local("mkdir -p versions")
    path = "versions/web_static_{}.tgz".format(date)
    print("Packing web_static to {}".format(path))
    pack = local("tar -cvzf {} ./web_static".format(path))
    file_size = stat(path).st_size
    print("web_static packed: {} -> {} Bytes".format(path, file_size))
    if pack.succeeded:
        return path
    return None
