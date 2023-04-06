#!/usr/bin/python3
"""
This fabric script generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Creates a .tgz archive
    """
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    path = "versions/web_static_{}.tgz".format(time)
    local("mkdir -p versions")

    if local("tar -cvzf {} web_static".format(path)).succeeded:
        return path
