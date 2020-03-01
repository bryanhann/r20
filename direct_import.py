from argparse import ArgumentParser as _PAR
from importlib import import_module as _IMP
from os.path import dirname as _DIR
import os
import sys

_INFO="""This is an RXX package.
Module path: %s
Virtual env: %s
Path to mod: %s
"""

def SAFECALL(name):
    if not name=='__main__':
        raise BaseException('Not indirectly importable')
    if not 'activate' in os.listdir(os.path.dirname(sys.executable)):
        raise BaseException('Virtulal environment required')

def STDERR(x):          return sys.stderr.write( str(x) + '\n' )
def subparser4mip(mip): return _IMP(mip+'.__config').argparse_subparser
def parser4mip(mip):    return _PAR(parents=[subparser4mip(mip)], prog='python3 -m %s' % mip,)
def venv():             return _DIR(_DIR(sys.executable))
def file4mip(mip):      return _IMP(mip).__file__
def err_info4mip(mip):  return _INFO %  (mip, venv(), file4mip(mip)[len(venv()):] )
def err_try4mip(mip):   return "try: python -m %s -h" % mip
