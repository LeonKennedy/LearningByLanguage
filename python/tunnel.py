#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: sshtunnel.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ssh隧道
# @Create: 2018-02-12 17:52:11
# @Last Modified: 2018-02-12 17:52:11
#

from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    'pahaz.urfuclub.ru',
    ssh_username="pahaz",
    ssh_password="secret",
    remote_bind_address=('127.0.0.1', 8080)
    )

server.start()

print(server.local_bind_port)  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.

server.stop()
