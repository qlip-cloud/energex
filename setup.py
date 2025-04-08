from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in energex/__init__.py
from energex import __version__ as version

setup(
	name='energex',
	version=version,
	description='Energex App',
	author='Mentum Group',
	author_email='example@mentum.group',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
