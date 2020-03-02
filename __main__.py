#---------------------------------------------------------
# If we are not imported directly, raise an exception.

if not __name__=='__main__':
    raise BaseException( 'Must be imported directly' )

#---------------------------------------------------------
# If our first argument is '__exit__' exit immediately
# with an error code determined by our second argumentr.

import sys

if sys.argv[1:2] == [ '__exit__' ]:
    try:
        err=int(sys.argv[2])
    except:
        err=-1
    exit(err)

#---------------------------------------------------------
# Consult argparse and act acordingly.

import r20.direct_import as DIRECT

mip=__package__

info_msg = DIRECT.err_info4mip(mip)
help_msg = DIRECT.err_try4mip(mip)
parser   = DIRECT.parser4mip(mip)
write    = DIRECT.STDERR

o=parser.parse_args()

if o.info:
    write( info_msg )
else:
    write( help_msg )
