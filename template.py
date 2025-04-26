import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

list_of_flies = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ibynb"
]

for filepath in list_of_flies:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already exitst")