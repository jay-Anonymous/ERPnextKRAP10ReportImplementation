from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")


from Techsavanna_ke import __version__ as version

setup(
	name="Techsavanna Limited",
	version=version,
	description="ERPNextKraP10Report",
	author="Techsavanna Limited",
	author_email="gnjakai@yahoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
