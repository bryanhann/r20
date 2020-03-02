#---------------------------------------------------------
# We have been imported directly, right?
# If not then bail with an exception.

if not __name__=='__main__':
    raise BaseException( 'Must be imported directly' )

#---------------------------------------------------------
# If our first arg is '__exit__' then we exit immediately
# with error code determined by our second argument.

import sys

if sys.argv[1:2] == [ '__exit__' ]:
    try:
        err=int(sys.argv[2])
    except:
        err=-1
    exit(err)

#---------------------------------------------------------
# We will avoid autoimport of argparsers in this most 
# of scripts and construct our own in situ.

from argparse import ArgumentParser
PARSER=ArgumentParser( add_help=False )
PARSER.add_argument( 'args', action='store', nargs='*')
PARSER.add_argument( '--info', action='store_true')

#---------------------------------------------------------
# We will import a few helper functios fron direct_import

import r20.direct_import as D
help_msg = D. help_msg_4_mip (__package__)
info_msg = D. info_msg_4_mip (__package__)
write    = D.  stderr_writer

#---------------------------------------------------------
# We will parse our arguments and act accordingly

o=PARSER.parse_args()
if o.info:
    write( info_msg )
else:
    write( help_msg )
