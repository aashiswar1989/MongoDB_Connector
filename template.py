import os
from pathlib import Path

package_name = "MongoDB_Connect"

list_of_files = [
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/integration.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "Experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = filepath.parent, filepath.name
    # print(f"Dir is {filedir}\nFile name is {filename}")
    if not filedir.is_dir():
        filedir.mkdir(parents=True, exist_ok=True)

    if not filepath.exists():
        filepath.touch()
    # filedir, filename = os.path.split(filepath)
    # if filedir != "":
    #     os.makedirs(filedir, exist_ok=True)
    #     # logging.info(f"Creating directory: {filedir} for file {filename}")

    # if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    #     with open(filepath, "w") as f:
    #         pass # Creating en empty file