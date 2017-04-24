from setuptools import setup

setup(name='getresponse',
      version='0.1',
      description='Email Marketing Software',
      url='https://bitbucket.org/ingmferrer/getresponse-python',
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      license='MIT',
      packages=['getresponse'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
