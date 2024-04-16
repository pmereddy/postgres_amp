import subprocess
import os
import gradio

def uppercase(text):
    return text.upper()

def main():
    # Move this to configure step
    print(subprocess.run(["/usr/lib/postgresql/16/bin/initdb","-D","/home/cdsw/postgresql" ], shell=False))

    print(subprocess.run(["/usr/lib/postgresql/16/bin/pg_ctl","-D","/home/cdsw/postgresql", "-o", "\"-k /tmp \"" , "start"], shell=False))

    # Configure gradio QA app 
    print("Configuring gradio app")
    demo = gradio.Interface(fn=uppercase, 
                            inputs=gradio.Textbox(label="Question", placeholder=""),
                            outputs=[gradio.Textbox(label="Asking LLM with No Context"),
                                     gradio.Textbox(label="Asking LLM with Context (RAG)")],
                            examples=["What are ML Runtimes?",
                                      "What kinds of users use CML?",
                                      "How do data scientists use CML?",
                                      "What are iceberg tables?"],
                            allow_flagging="never")


    # Launch gradio app
    print("Launching gradio app")
    demo.launch(share=True,
                show_error=True,
                server_name='127.0.0.1',
                server_port=int(os.getenv('CDSW_APP_PORT')))
    print("Gradio app ready")

if __name__ == "__main__":
    main()
