#!/bin/bash

echo "Configuring postgresql"
echo "unix_socket_directories='/tmp'" >> /home/cdsw/postgresql/postgresql.conf
echo "listen_addresses='*'" >> /home/cdsw/postgresql/postgresql.conf
