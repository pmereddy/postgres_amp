import subprocess
import os
import gradio as gr

# Move this to configure step
print(subprocess.run(["/usr/lib/postgresql/16/bin/initdb","-D","/home/cdsw/postgresql" ], shell=False))

print(subprocess.run(["/usr/lib/postgresql/16/bin/pg_ctl","-D","/home/cdsw/postgresql", "-o", "\"-k /tmp \"" , "start"], shell=False))

def uppercase(text):
    return text.upper()

iface = gr.Interface(fn=uppercase, inputs="text", outputs="text")
iface.launch()
