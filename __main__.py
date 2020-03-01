import r20.direct_import as DD
DD.SAFECALL(__name__)



OPT=DD.parser4mip(__package__).parse_args()

if OPT.info:
    DD.STDERR( DD.err_info4mip(__package__))
else:
    DD.STDERR( DD.err_try4mip(__package__) )
