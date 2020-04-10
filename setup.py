from setuptools import setup, find_packages
import glob
import os
import pkg_resources

from iqbrownie import __version__, _program

setup(name='iq-brownie',
      version=__version__,
      packages=['iqbrownie'],
      scripts=['iqbrownie/scripts/Snakefile'],
      description='taxon hashing so names dont get corrupted when running iqtree',
      url='https://github.com/aineniamh/iq-brownie',
      author='Aine OToole',
      author_email='aine.otoole@ed.ac.uk',
      install_requires=[
          "biopython>=1.70",
          "dendropy>=4.4.0",
          "pytools==2020.1"
      ]
      entry_points="""
      [console_scripts]
      {program} = iqbrownie.command:main
      """.format(program = _program),
      include_package_data=True,
      keywords=[],
      zip_safe=False)