
'''编程，输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数。'''
'''
p=input('请输入一行字符:')
a,b,c,d=0,0,0,0
for i in p:
     if((i<='Z' and i>='A') or (i<='z' and i>='a')):
          a+=1
     elif (i==' '):
          b+=1
     elif(i>='0' and i<='9'):
          c+=1
     else:
          d+=1
print ('英文字母的个数为：'+str(a))
print ('空格的个数为：'+str(b))
print ('数字的个数为：'+str(c))
print ('其他字符的个数为：'+str(d))
'''
#方法1

letters,space,digit,other=0,0,0,0
s=input("请输入一行字符：")
for i in range(len(s)):
     if (s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z'):
         letters+=1
     elif s[i]==' ':
         space+=1
     elif s[i]>='0' and s[i]<='9':
         digit+=1
     else:
         other+=1
print("字母数：%d\n空格数：%d\n数字数：%d\n其他字符数：%d\n"%(letters,space,digit,other))
#方法2


letter,space,digit,other=0,0,0,0
s = input('input a string:')
for c in s:
     if c.isalpha():
          letter +=1
     elif c.isspace():
          space +=1
     elif c.isdigit():
          digit +=1
     else:
          other +=1
print("字母数：%d\n空格数：%d\n数字数：%d\n其他字符数：%d\n"%(letter,space,digit,other))

#方法三