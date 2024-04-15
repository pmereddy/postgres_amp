import subprocess

print(subprocess.run(["sh 1_configure_postgres/configure_postgres.sh"], shell=True))
