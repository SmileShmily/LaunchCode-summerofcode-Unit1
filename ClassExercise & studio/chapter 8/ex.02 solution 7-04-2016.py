
'''letters,space,digit,other=0,0,0,0
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
print("字母数：%d\n空格数：%d\n数字数：%d\n其他字符数：%d\n"%(letters,space,digit,other))'''

#solution
'''
letters,e=0,0
s=input("Please enter your string：")
#def analyze_text(str):
for i in range(len(s)):
    if (s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z'):
        letters+=1
        if s[i]=='e':
            e+=1
    percent_e=(e/letters)*100
print("letters：%d\ne_num：%d\npercent_e:%.1f%%\n"%(letters,e,percent_e))

#s1="Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
#s2="Blueberries are tastee!"
#s3="Werewolf bar mitzvah, spooky! scary! Boys becoing men... men becoming wolves."
'''
#try again
#s = input("Please enter your string：")
def analyze_text(s):
    letters, e = 0, 0
    s = str(s).lower()
    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
            letters += 1
            if s[i] == 'e':
                e += 1
        percent_e = (e / letters) * 100
    return("letters：%d\ne_num：%d\npercent_e:%.1f%%\n" % (letters, e, percent_e))
s1="Eeeee"
s2="Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
s3="Blueberries are tastee!"
s4="Werewolf bar mitzvah, spooky! scary! Boys becoing men... men becoming wolves."
print(analyze_text(s1))
print(analyze_text(s2))
print(analyze_text(s3))
print(analyze_text(s4))