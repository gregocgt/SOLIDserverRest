from setuptools import setup

setup(name='SOLIDserverRest',
    version='1.02',
    description='The SOLIDserverRest is a library to drive EfficientIP API',
    long_description="SOLIDserverRest: This 'SOLIDserverRest' allows to easily interact with SOLIDserver's REST API. It allows managing all IPAM objects through CRUD operations.",
    long_description_content_type="text/markdown",
    url='https://github.com/gregocgt/efficientip_Python_module_SOLIDserver',
    author='Gregory CUGAT',
    author_email='gregory.cugat@efficientip.com',
    license='BSD 2',
    packages=['SOLIDserverRest'],
    zip_safe=False)