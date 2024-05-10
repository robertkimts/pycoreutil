from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pycoreutil',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='2.1.0',
    packages=['pycoreutil'],
    url='https://github.com/robertkimts/pycoreutil',
    license='License',
    author='robert kimts',
    author_email='robertkimts@outlook.com',
    description='Description'
)
