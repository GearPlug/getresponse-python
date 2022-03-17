import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='getresponse-python',
      version='0.1.4',
      description='Email Marketing Software',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      url='https://github.com/GearPlug/getresponse-python',
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      license='GPL',
      packages=['getresponse'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
