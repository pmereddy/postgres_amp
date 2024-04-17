#!/bin/bash

echo "Configuring postgresql"
echo "unix_socket_directories='/tmp'" >> /home/cdsw/postgresql/postgresql.conf
echo "listen_addresses='*'" >> /home/cdsw/postgresql/postgresql.conf
echo "host    all    cdsw    0/0    trust" >> /home/cdsw/postgresql/pg_hba.conf
