import subprocess
import os
import gradio

def uppercase(text):
    return (text, text.upper())

def main():
    print(subprocess.run(["/usr/lib/postgresql/16/bin/pg_ctl","-D","/home/cdsw/postgresql", "start"], shell=False))

    # Configure gradio QA app 
    print("Configuring dummy gradio app")
    demo = gradio.Interface(fn=uppercase, 
                            inputs=gradio.Textbox(label="Question", placeholder=""),
                            outputs=[gradio.Textbox(label="Asking LLM with No Context"),
                                     gradio.Textbox(label="Asking LLM with Context (RAG)")],
                            allow_flagging="never")


    # Launch gradio app
    demo.launch(share=True,
                show_error=True,
                server_name='127.0.0.1',
                server_port=int(os.getenv('CDSW_APP_PORT')))
    print("Gradio app ready")

if __name__ == "__main__":
    main()
