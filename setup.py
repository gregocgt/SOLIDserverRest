import io
import os

from setuptools import setup

here = os.path.dirname(__file__)

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='SOLIDserverRest',
    version='1.6.01',
    author='Gregory CUGAT',
    url='https://github.com/gregocgt/efficientip_Python_module_SOLIDserver',
    description='The SOLIDserverRest is a library to drive EfficientIP API',
    long_description_content_type="text/markdown",
    long_description=long_description,
    author_email='gregory.cugat@efficientip.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ],
    license='BSD 2',
    packages=['SOLIDserverRest'],
    zip_safe=False,
    python_requires=">=2.7",
    py_modules=['check_python_versions'],
    entry_points={
        'console_scripts': [
            'check-python-versions = check_python_versions:main',
        ],}
    )