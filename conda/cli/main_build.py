# (c) 2012-2013 Continuum Analytics, Inc. / http://continuum.io
# All Rights Reserved
#
# conda is distributed under the terms of the BSD 3-clause license.
# Consult LICENSE.txt or http://opensource.org/licenses/BSD-3-Clause.

descr = "Build a package from recipe. (EXPERIMENTAL)"


def configure_parser(sub_parsers):
    p = sub_parsers.add_parser('build', description=descr, help=descr)

    p.add_argument(
        '-s', "--source",
        action  = "store_true",
        help    = "only obtain the source (but don't build)",
    )
    p.add_argument(
        '-t', "--test",
        action  = "store_true",
        help    = "test package (assumes package is already build)",
    )
    p.add_argument('recipe',
                   action="store",
                   metavar='PATH',
                   nargs='+',
                   help="path to recipe directory",
    )
    p.set_defaults(func=execute)


def execute(args, parser):
    import conda.builder.build as build
    import conda.builder.source as source
    from conda.builder.metadata import MetaData

    for arg in args.recipe:
        m = MetaData(arg)
        if args.test:
            build.test(m)
        elif args.source:
            source.provide(m.path, m.get_section('source'))
            print 'Source tree in:', source.get_dir()
        else:
            build.build(m)
