import argparse
import importlib
import os
import sys

_PAR = argparse.ArgumentParser
_IMP = importlib.import_module 
_DIR = os.path.dirname

def err_info4mip(mip):
    acc=[]
    acc.append("This is an RXX package.")
    acc.append("Module path: %s" % mip)
    acc.append("Virtual env: %s" % venv())
    acc.append("Path to mod: %s" % file4mip(mip)[len(venv()):])
    return '\n'.join(acc)
def SAFECALL(name):
    if not name=='__main__':
        raise BaseException('Not indirectly importable')
    if not 'activate' in os.listdir(os.path.dirname(sys.executable)):
        raise BaseException('Virtulal environment required')
def is_venv():          return 'activate' in os.listdir( venv()+'/bin' )
def STDERR(x):          return sys.stderr.write( str(x) + '\n' )
def subparser4mip(mip): return _IMP(mip+'.__config').argparse_subparser
def parser4mip(mip):    return _PAR(parents=[subparser4mip(mip)], prog='python3 -m %s' % mip,)
def venv():             return _DIR(_DIR(sys.executable))
def file4mip(mip):      return _IMP(mip).__file__
def err_try4mip(mip):   return "try: python -m %s -h" % mip
