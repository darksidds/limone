import os
import platform
import sys

from setuptools import setup, find_packages

VERSION = '0.1a7'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires = [
    'colander',
    'venusian',
    ]

tests_require = install_requires

if sys.version_info[:2] < (2, 7):
    tests_require += ['unittest2']

setup(name='limone',
      version=VERSION,
      description=('Content type system based on colander schemas.'),
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Framework :: Pylons",
        "License :: Repoze Public License",
        ],
      keywords='',
      author="Chris Rossi, Archimedean Company",
      author_email="pylons-devel@googlegroups.com",
      url="http://pylonsproject.org",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = install_requires,
      tests_require = tests_require,
      test_suite="limone.tests",
      entry_points = """\
      """
      )
