import os
from distutils.core import setup
from setuptools import find_packages

__author__ = 'Alexander Lifanov'
__version__ = '0.0.2'

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-yandex-checkout',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/alifanov/django-yandex-checkout',
    license='MIT',
    author=__author__,
    author_email='lifanov.a.v@gmail.com',
    keywords=['django', 'yandex', 'money', 'payment', 'pay'],
    description='Integrating django project with yandex-kassa',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=3.0',
    ],
)