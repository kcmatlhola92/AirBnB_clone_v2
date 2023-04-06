#!/usr/bin/python3
"""
This script distributes an archive to your web servers, using the function
do_deploy
"""
from fabric.api import put, run, env
import os

env.hosts = ["54.146.59.253", "54.242.190.40"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    deploys archive to web server
    """
    path = archive_path.split('/')[-1]
    line = path.split('.')[0]
    if not os.path.isfile(archive_path):
        return False
    if put(archive_path, "/tmp/{}".format(path)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}"
            .format(line)).failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}/"
            .format(line)).failed:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(path, line)).failed:
        return False
    if run("rm /tmp/{}".format(path)).failed:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(line, line)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static"
            .format(line)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(line)).failed:
        return False

    return True
