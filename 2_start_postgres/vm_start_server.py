import subprocess
import os

port = str(os.environ.get('CDSW_APP_PORT', 8000))
extra_options=f"-k /tmp -p {port}"

command=f"/usr/lib/postgresql/12/bin/initdb -D $HOME/postgresql"
print(command)
print(subprocess.run([command], shell=True))

command=f"/usr/lib/postgresql/12/bin/pg_ctl -D $HOME/postgresql -l logfile -o \"{extra_options}\" start"
print(command)
print(subprocess.run([command], shell=True))
