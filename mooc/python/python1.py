#!/usr/bin/env python3
#-*-coding:utf-8 -*-
height=1.80
weight=73
bmi = float(weight/(height*height))
if bmi<=18.5:
    print('过轻')
elif bmi<=25:
    print('正常')
elif bmi<=28:
    print('过重')
elif bmi<=32:
    print('肥胖')
else:
    print('严重肥胖')