import subprocess
import os

port = str(os.environ.get('CDSW_APP_PORT', 8000))

print(subprocess.run(["python3","2_start_postgres/launch_app.py","--share","--port", port, '>/dev/null',' &' ],shell=False))
