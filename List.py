
zzy_list = ["张三","李四","王五","赵六"]
ghq_list = [1314,520,8989]

# 1， 取值和取索引

 # 1.1 查看索引号位1的数据内容

print(zzy_list[1])

 # 1.2 指定数据的内容，想确定数据在列表中的位置

print(zzy_list.index("王五"))

# 2， 修改列表

 # 2.1 修改索引号位3的数据为 周斌

zzy_list[3] = "周斌"
print(zzy_list[3])

# 3， 增加列表元素

 #3.1 在列表的末尾增加一个数据,郭亮

zzy_list.append("郭亮")

 #3.2 在列表指定索引位置增加一个数据

zzy_list.insert(2,"吴杰")

 #3.3 在另外一个列表添加到列表

zzy_list.extend(ghq_list)


# 查看列表的长度

list_len = len(zzy_list)

print("列表的长度为：%d" %list_len)




# 4， 删除列表元素

 #4.1 删除列表末尾的数据

zzy_list.pop()

 #4.2 删除列表指定索引的数据 删除 520

zzy_list.pop(4)

 #4.3 删除指定的数据 删除 李四

zzy_list.remove("李四")  # del zzy_list[1] 可以删除李四

  # del 这个关键字，本质上是用来将一个变量从内存 中删除



 #4.4 清空列表

zzy_list.clear()

print(zzy_list)
