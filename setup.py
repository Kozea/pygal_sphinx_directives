#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of pygal_sphinx_directives
#
# Pygal sphinx integration
# Copyright © 2015 Florian Mounier
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup, find_packages

setup(
    name="pygal_sphinx_directives",
    version='',
    description="Pygal sphinx integration",
    author="Florian Mounier",
    author_email="florian.mounier@kozea.fr",
    license="GNU LGPL v3+",
    platforms="Any",
    packages=find_packages(),
    install_requires=['sphinx']
)
