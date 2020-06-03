import pytest
import subprocess

p = subprocess.run("pip3 install -e package/", shell=True)
pytest.main(['package'])