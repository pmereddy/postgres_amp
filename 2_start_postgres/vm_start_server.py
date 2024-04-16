import subprocess
import os
import gradio as gr

port = str(os.environ.get('CDSW_APP_PORT', 8000))
extra_options=f"-k /tmp "
#extra_options=f"-k /tmp -p {port}"

command=f"/usr/lib/postgresql/16/bin/initdb -D /home/cdsw/postgresql"
print(command)
print(subprocess.run([command], shell=False))

command=f"/usr/lib/postgresql/16/bin/pg_ctl -D /home/cdsw/postgresql -l logfile -o \"{extra_options}\" start"
print(command)
print(subprocess.run([command], shell=False))


def uppercase(text):
    return text.upper()

iface = gr.Interface(fn=uppercase, inputs="text", outputs="text")
iface.launch(share=True, port=port)
