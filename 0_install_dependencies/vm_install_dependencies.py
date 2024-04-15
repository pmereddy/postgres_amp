import subprocess

# Install python packages required to run chromadb vector database

packages = [
    ("psycopg2", None),
]

# Iterate over the packages and install them one by one
for package, version in packages:
    try:
        # Construct the pip install command based on whether a version is specified
        if version:
            install_command = ["pip", "install", f"{package}=={version}"]
        else:
            install_command = ["pip", "install", package]
        
        # Run the pip install command
        subprocess.check_call(install_command)
        
        # Print a success message
        if version:
            print(f"Successfully installed {package} version {version}")
        else:
            print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        # Handle errors if the installation fails
        if version:
            print(f"Error installing {package} version {version}")
        else:
            print(f"Error installing {package}")
