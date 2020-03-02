import argparse
import importlib
import os
import sys

_PAR = argparse.ArgumentParser
_IMP = importlib.import_module 
_DIR = os.path.dirname

def subparser_4_mip(mip): return _IMP(mip+'.__config').argparse_subparser
def parser_4_mip(mip):    return _PAR(parents=[subparser_4_mip(mip)], prog='python3 -m %s' % mip,)
def help_msg_4_mip(mip): return "try: python -m %s -h" % mip
def info_msg_4_mip(mip):
    acc=[]
    acc.append("This is an RXX package.")
    acc.append("Module path: %s" % mip)
    acc.append("Virtual env: %s" % venv())
    acc.append("Path to mod: %s" % _IMP(mip).__file__[len(venv()):])
    return '\n'.join(acc)

def venv():    return _DIR(_DIR(sys.executable))
def is_venv(): return 'activate' in os.listdir( venv()+'/bin' )
def stderr_writer(x):    return sys.stderr.write( str(x) + '\n' )
def stdout_writer(x):   return sys.stdout.write( str(x) + '\n' )
