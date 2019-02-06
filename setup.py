
from setuptools import setup
import os

version = "1.0.0"

requirements = [
	"Flask==1.0.2",
	"Flask-Bootstrap==3.3.7.1"
]


setup(name='paint-calculator',
      version=version,
      description='App to create web tests against',
      author='Joe Carlyon',
      author_email='JoeCarlyon@gmail.com',
      url='https://github.com/joecarlyon/paint-calculator',
      install_requires=requirements,
      packages=['paint_calculator'],
      )
