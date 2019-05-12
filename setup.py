#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from setuptools.command.sdist import sdist


class ezip(sdist):
    description = "create an executable zip-formatted source distribution"

    def finalize_options(self):
        sdist.finalize_options(self)
        self.formats = ['zip']

    def run(self):
        sdist.run(self)

        from zipfile import ZipFile
        with ZipFile(self.archive_files[0], 'a') as zfile:
            zfile.write('__main__.py')

        print('data_files: ', self.distribution.data_files)
        print('dist_files: ', self.distribution.dist_files)
        print('dist_dir', self.dist_dir)
        print('archive_files', self.archive_files)
        print('get_fullname', self.distribution.get_fullname())
        print('get_name', self.distribution.get_name())
        print('get_version', self.distribution.get_version())
        print('version', self.distribution.version)
        print('script_args', self.distribution.script_args)
        print('command_options', self.distribution.command_options)
        import os
        print('getcwd', os.getcwd())
        print('filelist', self.filelist)
        print('filelist.files', self.filelist.files)
        print('filelist.allfiles', self.filelist.allfiles)


setup(
    name='skelpy',
    version='1.0.0',
    python_requires='>=2.7',
    url='https://github.com/dks/skelpy',
    author='dks',
    author_email='june3474@gmail.com',
    description='A simple template tool to create the skeleton for a python project',
    license='NEW-BSD',
    package_dir={'': '.'},
    packages=find_packages(where='.', exclude=['docs', 'tests', 'tests.*']),
    zip_safe=True,
    include_package_data=True,
    scripts=[],
    entry_points={
        'console_scripts': [
            'skelpy = skelpy.main:run',
        ],
        # 'gui_scripts': [
        #     'skelpy_gui = skelpy.main_gui:run',
        # ]
    },
    install_requires=[
        
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ],
    extras_require={
        
    },
    classifiers=[
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
    cmdclass={'ezip': ezip},
)
