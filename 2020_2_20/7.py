import sys
import math


def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    used_num ={}
    kill_count=0
    max_level=0
    min_level=0
    sorted_argv=sorted(argv, reverse=True)
    for i, v in enumerate(sorted_argv):
        print("argv[{0}]: {1}".format(i, v))
        if i==0:
          mini_level=v
        if i==1:
          max_level=v
        print(type(v))
        to_max_multi_count=math.floor(max_level/v)
        to_min_multi_count=math.floor(min_level/v)
        multi_count=to_max_multi_count-to_min_multi_count
        for used in used_num:
          if used_num%v==0 or used_num==v:
            kill_count=kill_count-used_num[v]
        kill_count = kill_count+multi_count
        used_num[v]=multi_count

if __name__ == '__main__':
    main(sys.argv[1:])

