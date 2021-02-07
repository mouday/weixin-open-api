# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import io
import os

from setuptools import setup, find_packages
from six import exec_

"""
## 本地测试
安装测试
python setup.py install
python setup.py develop 
卸载
pip uninstall myquery -y
## 打包上传
先升级打包工具
pip install --upgrade setuptools wheel twine
打包
python setup.py sdist bdist_wheel
检查
twine check dist/*
上传pypi
twine upload dist/*
命令整合
rm -rf dist build *.egg-info \
&& python setup.py sdist bdist_wheel  \
&& twine check dist/* \
&& twine upload dist/* \
&& rm -rf dist build *.egg-info
## 下载测试
安装测试
pip install -U weixin-open-api -i https://pypi.org/simple
打包的用的setup必须引入
参考：
https://packaging.python.org/guides/making-a-pypi-friendly-readme/
"""

base_dir = os.path.dirname(os.path.abspath(__file__))

with io.open("weixin_open_api/version.py", 'br') as f:
    version = {}
    exec_(f.read(), version)
    VERSION = version['VERSION']

with io.open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

with io.open("requirements.txt", 'r') as f:
    install_requires = f.read().split(os.sep)

setup(
    name='weixin-open-api',
    version=VERSION,
    description="微信开放接口封装库",

    keywords='weixin api',
    author='Peng Shiyu',
    author_email='pengshiyuyx@gmail.com',
    license='MIT',
    url="https://github.com/mouday/weixin-open-api",

    long_description=long_description,
    long_description_content_type='text/markdown',

    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],

    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=install_requires
)
