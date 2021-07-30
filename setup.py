from setuptools import find_packages, setup
from pyls_sleeper._version import __version__ as version

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyls-sleeper",
    version=version,
    description="Demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['pyls_sleeper'],
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={"pylsp": ["pyls_sleeper = pyls_sleeper.plugin"]},
    include_package_data=True,
)
