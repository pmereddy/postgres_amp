import subprocess
import os

port = str(os.environ.get('CDSW_APP_PORT', 8000))
extra_options=f"-k /tmp -p {port}"

command=f"pg_ctl -D postgres -l logfile -o \"{extra_options}\" start"
print(command)
print(subprocess.run([command], shell=True))
