try:
      from setuptools import setup
except ImportError:
      from distutils.core import setup

config = {
    'description': 'payroll challenge',
    'author': 'Brian Button',
    'url': 'https://github.com/bbutton/payroll_challenge',
    'download_url': 'https://github.com/bbutton/payroll_challenge',
    'author_email': 'bbutton@agilestl.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['payroll_challenge'],
    'scripts': [],
    'name': 'payroll_challenge'
}

setup(**config)
