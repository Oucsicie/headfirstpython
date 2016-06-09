#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdout

"""这是"nester.py"模块，提供了一个名为print_lol()的函数用来打印列表，其中包含或
    不包含嵌套列表。"""

def print_lol(the_list,indent=False,level=0,fh=stdout):
    
    """这个函数第一个位置参数，名为the_list,这可以是任何python列表（包含或不包含嵌
    列表），所提供列表中的各个数据项会（递归地）打印到屏幕上，而且各占一行。第
    三个参数（名为level)用来在遇到嵌套列表时插入制表符。第三个参数用来控制是否
    插入制表符,第四个参数用来设置输出位置。"""

    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print>>fh,("\t",)
            print>>fh,(each_item)
            
