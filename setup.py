from pathlib import Path

from setuptools import setup, find_packages


readme = Path("README.md").read_text(encoding="utf-8")
version = '0.1.0'   #Path("_version.py").read_text(encoding="utf-8")
with open('requirements.txt') as f:
    required = f.read().splitlines()
about = {}
#exec(version, about)


setup(
    name='styled_text',
    version='0.1.0',
    author="Jason Beach",
    description="NLP Library to display and export text with styling from an annotation / labeling application, such as Doccano",
    long_description=readme,
    url="https://github.com/IMTorgOpenDataTools/styled-text",
    packages=find_packages(include=['styled_text']),
    python_requires=">=3.10",
    install_requires = required
)