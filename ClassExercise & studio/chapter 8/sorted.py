string = ''' the stirng Has many line In THE fIle jb51 net '''
list_of_string = string.split()
print (list_of_string) #将字符串分离开，放入列表中
print ('*'*50)
def case_insensitive_sort(liststring):
 listtemp = [(x.lower(),x) for x in liststring]     #将字符串列表，生成元组，（忽略大小写的字符串，字符串）
 listtemp.sort()                        #对元组排序，因为元组为：（忽略大小写的字符串，字符串），就是按忽略大小写的字符串排序
 return [x[1] for x in listtemp]      #排序完成后，返回原字符串的列表
print (case_insensitive_sort(list_of_string))#调用起来，测试一下