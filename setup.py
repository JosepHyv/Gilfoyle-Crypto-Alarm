from setuptools import setup, find_packages

setup(
	name="gilfoyle cryptocurrency alarm",
	version="1.0.0",
	description="small adaptation of gilfoyle's cryptocurrency alarm from the silicon valley series",
	author="Joseph Hynimoto Aguilar Lopez",
	packages=find_packages(),
	entry_ponts={
		"console_scripts": ["gilfoyle=gilfoyle:main"]
	},
#	install_requires=["requeriments.txt"],
	include_package_data=True,
	python_requires=">=3.8"
)