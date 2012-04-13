# -*- coding: utf-8 -*-

from distutils.core import setup

'''
IMPORTANTE: los campos que se describen a continuación deben ser rellenados en su totalidad.
Aquellos campos que NO SE VAYAN A UTILIZAR, se deben BORRAR.
'''

setup(name='fvisusers',
      version='1.0',
      author='Jesús Gómez',
      author_email='jgomez@funvisis.gob.ve',
      url='http://code.funvisis.gob.ve/funvisis/',
      download_url='http://code.funvisis.gob.ve/funvisis/LoL',
      description='An application for extending djang.auth functionality',
      package_dir={'':'src'},
      packages=['funvisis', 'funvisis.users'],
      requires=['django (>=1.3)'],
      classifiers=['Development Status :: Alpha',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.6+',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Topic :: Internet',
                   'Topic :: Scientific/Engineering :: GIS',
                  ],

     )
