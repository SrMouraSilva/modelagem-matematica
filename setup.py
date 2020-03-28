# Copyright 2017 SrMouraSilva
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import path
from setuptools import setup


def readme():
    here = path.abspath(path.dirname(__file__))

    with open(path.join(here, 'README.rst'), encoding='UTF-8') as f:
        return f.read()

setup(
    name='Modelagem-Matematica',
    version='0.0.1',

    # description='Control Zoom G3 with python lib',
    # long_description=readme(),

    url='https://github.com/SrMouraSilva/ModelagemMatematica',

    author='Paulo Mateus (SrMouraSilva)',
    author_email='mateus.moura@hotmail.com',
    maintainer='Paulo Mateus (SrMouraSilva)',
    maintainer_email='mateus.moura@hotmail.com',

    license="Apache Software License v2",

    packages=[
        #'zoom',
        #'zoom/database',
        #'zoom/model',
    ],
    package_data={
        #'zoom/database': ['ZoomG3v2.json']
    },
    install_requires=[
        'jupyter',
        'jupyterlab',
        'numpy',
        'scipy',
        'matplotlib',
        #'ipywidgets',
        'pandas',
        'gpyopt'
    ],

    # test_suite='test',
    # tests_require=['pytest', 'pytest-cov'],
    #
    # classifiers=[
    #     'Development Status :: 3 - Alpha',
    #     'Intended Audience :: Developers',
    #     'License :: OSI Approved :: Apache Software License',
    #     'Topic :: Multimedia :: Sound/Audio',
    #     'Programming Language :: Python :: 3.5',
    #     'Programming Language :: Python :: 3.6',
    #     'Programming Language :: Python :: 3.7',
    #     'Programming Language :: Python :: 3.8',
    # ],
    # keywords='zoom multistomp midi',

    platforms='Linux',
)
