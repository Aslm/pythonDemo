#! /usr/bin/env python
# -*- coding: utf-8 -*-

from protobufDemo import person_pb2

# 为 all_person 填充数据
pers = person_pb2.all_person()
p1 = pers.Per.add()
p1.id = 1
p1.name = 'demo-1'
p2 = pers.Per.add()
p2.id = 2
p2.name = 'demo-2'

# 对数据进行序列化
data = pers.SerializeToString()
# 对已经序列化的数据进行反序列化
target = person_pb2.all_person()
flag = None
flag = target.ParseFromString(data)
print(target)  #  打印第一个 person name 的值进行反序列化验证
