import argparse


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-p', type=str, help='存储路径', default='./')
parser.add_argument('-n', type=str, help='json名称', default='./')
parser.add_argument('-t', type=str, help='tid字段', default='./')
parser.add_argument('-rid', type=str, help='rid字段', default='./')

args = parser.parse_args()
# 打印传入进来 -p后面的参数
print(args.p)
