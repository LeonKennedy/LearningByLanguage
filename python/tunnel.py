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
    '118.31.37.91',
    ssh_username="coffee",
    ssh_password="olenji@0409",
    remote_bind_address=('127.0.0.1', 33488)
    )

server.start()

print(server.local_bind_port)  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.

server.stop()
