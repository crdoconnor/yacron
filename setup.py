#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()


requirements = [
    "strictyaml>=0.7.2",
    "crontab",
    "aiohttp",
    "raven",
    "raven-aiohttp",
    "aiosmtplib",
]


setup_requirements = [
    'setuptools_scm',
    'pytest-runner',
]

test_requirements = [
    'pytest-cov',
    # https://github.com/pytest-dev/pytest-runner/issues/11#issuecomment-190355698
    'pytest',  # needs to be last
]

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='yacron',
    version='0.1.0',
    description="A modern Cron replacement that is Docker-friendly",
    long_description=(readme + '\n\n' + history),
    author="Gustavo Carneiro",
    author_email='gustavocarneiro@gambitresearch.com',
    url='https://github.com/gjcarneiro/yacron',
    packages=find_packages(include=['yacron']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=True,
    keywords='yacron',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    use_scm_version=True,
    entry_points={
        'console_scripts': [
            'yacron = yacron.__main__:main',
        ],
    },
    python_requires='>=3.5',
)
