from setuptools import setup, find_packages
import os

version = '0.1'

requires = [
    "pyramid",
    ]

tests_require = [
    "pytest",
    "mock",
    ]

points = {
    }

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='rebecca.todict',
      version=version,
      description="API and directive converting object to ``dict``.",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Pyramid",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='MIT',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['rebecca'],
      include_package_data=True,
      tests_require=tests_require,
      extras_require={
        "testing": tests_require,
        },
      zip_safe=False,
      install_requires=requires,
      entry_points=points,
      )
