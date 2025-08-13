import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s:')

project_name = "MLOPS_Data_Science_Project"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    path_obj = Path(filepath)
    filedir, filename = os.path.split(path_obj)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Ensured directory: {filedir}")

    if (not path_obj.exists()) or (path_obj.stat().st_size == 0):
        # Create empty file if new; add minimal boilerplate for certain filenames
        if filename == "setup.py":
            content = (
                "from setuptools import setup, find_packages\n\n"
                f"setup(name=\"{project_name}\", version=\"0.1.0\", packages=find_packages(\"src\"), package_dir={{'': 'src'}}, install_requires=[])\n"
            )
            path_obj.write_text(content, encoding="utf-8")
        elif filename == "Dockerfile":
            content = (
                "# Simple Dockerfile\n"
                "FROM python:3.10-slim\n"
                "WORKDIR /app\n"
                "COPY requirements.txt .\n"
                "RUN pip install --no-cache-dir -r requirements.txt || true\n"
                "COPY . .\n"
                "CMD [\"python\", \"main.py\"]\n"
            )
            path_obj.write_text(content, encoding="utf-8")
        else:
            path_obj.touch()
        logging.info(f"Created file: {path_obj}")
    else:
        logging.info(f"File already exists: {path_obj}")

