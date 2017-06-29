'''a = ['Nina', 'Jim', 'Rainman', 'Hello']
for i in range(len(a)):
   print(i, a[i])
   '''

'''【filter()函数有两个参数】
第一个，自定函数名，必须的
第二个，需要过滤的列，也是必须的
【DEMO】
需求，过滤大于5小于10的数'''
# coding=utf8
# 定义大于5小于10的函数
'''def guolvhanshu(num):
     if num>5 and num<10:
       return num
# 定义一个序列
seq=(12,50,8,17,65,14,9,6,14,5)
# 使用filter函数
result=filter(guolvhanshu,seq)
# (8,9,6)
print (result)'''

#如何用Python输出一个Fibonacci数列?
'''
a,b = 0, 1
while b<100:
  print (b),
  a, b = b, a+b
'''
'''有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；
要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。
有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；

要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。
1. 将两序列合并为一个序列，并排序，为序列Source
2. 拿出最大元素Big，次大的元素Small
3. 在余下的序列S[:-2]进行平分，得到序列max，min
4. 将Small加到max序列，将Big加大min序列，重新计算新序列和，和大的为max，小的为min。'''
'''
def mean( sorted_list ):
   if not sorted_list:
     return (([],[]))
big = sorted_list[-1]
small = sorted_list[-2]
big_list, small_list = mean(sorted_list[:-2])
big_list.append(small)
small_list.append(big)
big_list_sum = sum(big_list)
small_list_sum = sum(small_list)
if big_list_sum > small_list_sum:
     return ( (big_list, small_list))
else:
     return (( small_list, big_list))
tests = [[1,2,3,4,5,6,700,800],[10001,10000,100,90,50,1],range(1, 11),[12312, 12311, 232, 210, 30, 29, 3, 2, 1, 1]]
for l in tests:
   l.sort()
print
print(“Source List:\t”, l)
l1,l2 = mean(l)
print(“Result List:\t”, l1, l2)
print (“Distance:\t”, abs(sum(l1)-sum(l2)))
print (‘-*’*40)
'''

'''请用Python写一个获取用户输入数字，并根据数字大小输出不同信息的脚本'''
'''
x = int(input("Please enter an integer:"))
if x < 0:
  x = 0
  print ("Negative changed to zero")
elif x == 0:
  print ("Zero")
elif x == 1:
  print ("Single")
else:
  print ("More")
  '''
'''题目：Define a function which, given a string argument, counts how many times each of the 26 letters occurs in the text.
 Lowercase and uppercase letters should be counted as the same letter!
 Your function should return a list of 26 numbers corresponding to the number of occurences of the 26 letters 'a' through 'z'.
function name: letter_frequency(s)
就是要定义一个 letter_frequency(s)
你输入字符串s
他返还一个列表 统计了在这个字符串中26个字母分别出现了几次 不区分大小写'''
#方法一
'''
import string
def letter_frequency(s):
   s = s.lower()                      #全部转小写
   l = []
   for i in [chr(x) for x in range(97,123)]:
      l.append(s.count(i))            #统计个数
   return l                           #返回def letter_frequency(s):
print(letter_frequency('Asdasdad'))
'''

#方法二
import string


def c(s):
   s = str(s).lower()
   lt = string.ascii_lowercase  # Python3.x 中： lt=string.ascii_lowercase
   result = [0] * 26
   for index, value in enumerate(lt):
      result[index] = s.count(value)
   return result
print(c('helloworld'))