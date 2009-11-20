### -*- coding: utf-8 -*- ####################################################
 
import os
from setuptools import setup, find_packages
 
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
 
version = '0.1'
 
install_requires = [
    'setuptools',
    'saaskit-core',
    'yos-social-sdk',
]
 
extras_require = dict(
    test = ['coverage',
            'windmill',
            ]
)
 
#AFAIK:
install_requires.extend(extras_require['test'])

dependency_links = [
        'http://pypi.saaskit.org/yos-social-sdk/',
] 

setup(
    name = "crowdsense",
    version = version,
    description = "Twitter Monitoring and Marketing Tool",
    long_description = read('README'),
    author = 'CrowdSense',
    author_email = 'admin@crowdsense.com',
    url = 'http://crowdsense.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe = False,
    install_requires = install_requires,
    extras_require = extras_require,
    entry_points="""
      # -*- Entry points: -*-
      """,
    dependency_links = dependency_links,
)
