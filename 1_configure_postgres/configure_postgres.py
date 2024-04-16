import subprocess

# Move this to configure step
print(subprocess.run(["/usr/lib/postgresql/16/bin/initdb","-D","/home/cdsw/postgresql" ], shell=False))

print(subprocess.run(["sh 1_configure_postgres/configure_postgres.sh"], shell=True))
