from setuptools import setup, find_packages

import os



# Read the README file for long description

def read_readme():

    try:

        with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as fh:

            return fh.read()

    except FileNotFoundError:

        return "AppleCrack_NG - Next Generation iOS Device Management Tool"



setup(

    name='applecrack_ng',

    version='0.1.0',

    author='Security Research Team',

    author_email='security@example.com',

    description='Next Generation iOS Device Management Tool',

    long_description=read_readme(),

    long_description_content_type='text/markdown',

    url='https://github.com/security-team/applecrack_ng',

    packages=find_packages(exclude=['tests*']),

    classifiers=[

        'Development Status :: 4 - Beta',

        'Intended Audience :: Security Researchers',

        'License :: OSI Approved :: MIT License',

        'Operating System :: POSIX :: Linux',

        'Programming Language :: Python :: 3',

        'Programming Language :: Python :: 3.7',

        'Programming Language :: Python :: 3.8',

        'Programming Language :: Python :: 3.9',

    ],

    python_requires='>=3.6',

    install_requires=[

        'PyQt5>=5.15.0',

        'pymobiledevice3>=1.0.0',

        'requests>=2.25.0',

        'click>=7.0',

        'tqdm>=4.50.0',

        'colorama>=0.4.0',

        'paramiko>=2.7.0'

    ],

    entry_points={

        'console_scripts': [

            'applecrack-ng=applecrack_ng.cli.main_cli:main',

        ],

    },

    scripts=[

        'install.sh',

    ],

    include_package_data=True,

    zip_safe=False,

)
