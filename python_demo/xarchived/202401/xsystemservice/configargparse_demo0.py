'''
https://pypi.org/project/ConfigArgParse/


1. 以 --开头的配置可以通过配置文件传递
2. 配置文件解析类有: DefaultConfigFileParser YAMLConfigFileParser ConfigparserConfigFileParser等


python configargparse_demo0.py -c config.txt vcf1 vcf2 --val 1 --val 2 --foo foo
'''


import configargparse


p = configargparse.ArgumentParser(
    description="demo",
    default_config_files=['/etc/app/conf.d/*.conf', '~/.my_settings'],
    # 指定配置文件解析类
    # config_file_parser_class=configargparse.DefaultConfigFileParser
)


# required=True 表示此选项必须传递，如果以--开头的参数，可以被定义在配置文件中，而不通过命令行传递
#   比如下面的--genome，虽然required=True，但是命令行可以不用传递，因为在配置文件里面已经定义了
# 更全的参数详解: https://docs.python.org/3/library/argparse.html#quick-links-for-add-argument
p.add_argument('-c', '--my-config', required=True, is_config_file=True, help='config file path')
# this option can be set in a config file because it starts with '--'
p.add_argument('--genome', required=True, help='path to genome file')
# -v类型(没有--开头)的参数，如果需要使用，需要用dest把值映射到指定的属性上，后续才可以通过options.verbose方式获取到值
p.add_argument('-v', dest="verbose", help='verbose', default=False, action='store_true')
# this option can be set in a config file because it starts with '--'
p.add_argument('-d', '--dbsnp', help='known variants .vcf', env_var='DBSNP_PATH')  
# metavar 在--help中替换vcf的显示，获取到的options.vcf是一个列表，和下面的--val一样
p.add_argument('vcf', metavar="F", nargs='+', type=str, help='variant file(s)')
p.add_argument('--val', action="append")

g = p.add_argument_group('group')
g.add_argument('--foo')

print('1' * 1000)

# --help只会执行到下面的代码就结束，如果仅仅是--help，后续代码则不在执行
options = p.parse_args()

print('2' * 1000)

print(f"{options.verbose=}")
print(f"{options.genome=}")
print(f"{options.vcf=}")
print(f"{options.val=}")
print(f"{options.foo=}")



# print(options)
# print("----------")
# print(p.format_help())
# print("----------")
# print(p.format_values())    # useful for logging where different settings came from