import os
from pathlib import Path
import logging


# Set up logging for the project
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


# Define the project name
project_name = "hate"


# Create the project directory
list_of_files = [
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transforamation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/gcloud_syncer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"
]





# Create directories and files in the project structure
for filepath in list_of_files:
    filepath = Path(filepath)
    
    # Splitting the file path to get directory and filename separately
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist and log the creation process
    if filedir !="":

        # Create directory recursively if it doesn't exist and log the creation process
        os.makedirs(filedir, exist_ok=True)

        # Log the creation of the directory
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Create an empty file if it doesn't exist and log the creation process
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")