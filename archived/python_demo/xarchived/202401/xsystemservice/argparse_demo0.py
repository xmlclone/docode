import argparse


parser = argparse.ArgumentParser(
    prog="This is prog]",
    description="This is description",
    epilog="This is epilog"
)
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
# args.pos是一个列表，默认nargs=1返回的就是一个字面常量值
# nargs 可以指定一个整数， 
# nargs 可以是一个?，表示1个，等同于nargs=1
# nargs 可以是一个*，一定返回列表，可以接收任意个
# nargs 可以是一个+，一定返回列表，至少需要1个
parser.add_argument("pos", type=int, nargs='+')
# 注意choices是只能在1 2 3整型数字里面选择，默认命令行传递的是字符串，故需要配合type=int来使用，否则传递-x报错
parser.add_argument('-x', choices=[1, 2, 3], default=1, type=int, required=True, metavar='xvalue')
# 使用了dest后，只能通过args.yvar访问，无法通过args.y访问了
parser.add_argument('-y', choices=[1, 2, 3], default=1, type=int, metavar='yvalue', dest='yvar')


# 增加子命令(这个子命令，其实类似位置参数，和下面的分组要分开)
subparsers = parser.add_subparsers(help='This is subparser.')
parser_a = subparsers.add_parser('a', help='This is a help.')
parser_a.add_argument('-z', choices=[1, 2, 3], default=1, type=int, metavar='zvalue')
parser_b = subparsers.add_parser('b', help='This is b help.')
parser_b.add_argument('-b', choices=[1, 2, 3], default=1, type=int, metavar='bvalue')


# 分组
group1 = parser.add_argument_group('This is group1.')
group2 = parser.add_argument_group('This is group2.')
group1.add_argument('-g', choices=[1, 2, 3], default=1, type=int)
group2.add_argument('-k', choices=[1, 2, 3], default=1, type=int)


args = parser.parse_args()
print(f"{args.verbose=}, {args.pos=}, {args.x=}, {args.yvar=}")