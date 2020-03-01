from argparse import ArgumentParser

_P=ArgumentParser( add_help=False )

_P.add_argument(
    'args',
    action='store',
    nargs='*'
)

_P.add_argument(
    '--info',
    action='store_true'
)

argparse_subparser=_P
