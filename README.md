# GPU Publisher Template for Python

This template shows how to require a GPU for a Python application.
The main file is `MAKE87.yml`, where we specify that the running node requires a GPU as a mounted peripheral.

Inside the `app/main.py`, we use `torch` which brings its own CUDA binaries that are installed automatically after
adding `torch` to the `pyproject.toml`.
