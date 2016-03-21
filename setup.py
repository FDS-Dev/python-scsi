# coding: utf-8

from sys import platform
from distutils.core import setup, Extension

#
# SGIO is linux specific
#
if platform[:5] == 'linux':
    linux_sgio_module = Extension('linux_sgio.linux_sgio',
                                  sources=['linux_sgio/sgiomodule.c'])

    setup(name='pyscsi-linux',
          version='1.0',
          license='LGPLv2.1',
          author='Ronnie Sahlberg',
          author_email='ronniesahlberg@gmail.com',
          description='Module for calling SCSI devices from Python, Python binding for Linux SCSI Generic (sg) Driver',
          packages=['pyscsi', 'pyscsi.pyscsi', 'pyscsi.utils', 'linux_sgio'],
          ext_modules=[linux_sgio_module])

else:
    setup(name='pyscsi',
          version='1.0',
          license='LGPLv2.1',
          author='Ronnie Sahlberg',
          author_email='ronniesahlberg@gmail.com',
          description='Module for calling SCSI devices from Python',
          packages=['pyscsi', 'pyscsi.pyscsi', 'pyscsi.utils'])
