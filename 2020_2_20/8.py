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
    mini_level=int(argv[0])
    max_level=int(argv[1])
    sorted_argv=list(map(int, sorted(argv[3:], reverse=True)))
    #print(sorted_argv)
    for i, v in enumerate(sorted_argv):
        #print(kill_count)
        #print(v) 
        #print(kill_count)
        multi_count=culc_multi_count(min_level,max_level,v)
        print(multi_count)
        #print(multi_count)
        for used in used_num:
            lcm=used * v/math.gcd(used, v)
            print(lcm)
            kill_count=kill_count-culc_multi_count(min_level,max_level,lcm)
            #print(kill_count)
            if used%v==0 or used==v:
                kill_count=kill_count-used_num[used]
        kill_count = kill_count+multi_count
        used_num[v]=multi_count
    print(max_level-min_level+1-kill_count)

def culc_multi_count(min_num,max_num,target):
        to_max_multi_count=math.floor(max_num/target)
        to_min_multi_count=math.floor(min_num/target)
        ans=to_max_multi_count-to_min_multi_count
        if ans<0:
            ans=0
        return ans


if __name__ == '__main__':
    main(sys.argv[1:])

