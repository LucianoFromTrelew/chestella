from setuptools import setup

setup(
  name = 'chestella',
  packages = ['chestella'], # this must be the same as the name above
  entry_points = {
    "console_scripts": ['chestella = chestella.chestella:main']
  },
  version = '0.1',
  description = 'A C-Projects manager',
  author = 'Luciano Serruya Aloisi',
  author_email = 'lucianoserruya@hotmail.com',
  url = 'https://github.com/LucianoFromTrelew/chestella', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz',
  keywords = ['project', 'C', 'c', 'creator', 'manager'], # arbitrary keywords
  classifiers = [],
)
