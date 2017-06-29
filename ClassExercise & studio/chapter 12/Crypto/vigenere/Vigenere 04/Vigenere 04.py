'''【这是密码学课上的一个作业题】

Vigenere密码即为传统多表代换密码，使用一密钥词对每个明文字母选择一个字母表来加密，如果到了密钥词的最后一个字母，则从头开始继续。

举例如下，比如使用密钥deceptive加密这样一段话：we are discovered save yourself

Key 	d 	e 	c 	e 	p 	t 	i 	v 	e 	d 	e 	c 	e 	p 	t 	i 	v 	e 	d 	e 	c 	e 	p 	t 	i 	v 	e
PlainText 	w 	e 	a 	r 	e 	d 	i 	s 	c 	o 	v 	e 	r 	e 	d 	s 	a 	v 	e 	y 	o 	u 	r 	s 	e 	l 	f
CipherText 	Z 	I 	C 	V 	T 	W 	Q 	N 	G 	R 	Z 	G 	V 	T 	W 	A 	V 	Z 	H 	C 	Q 	Y 	G 	L 	M 	G 	J

加密之后密文即为：ZICVTWQNGRZGVTWAVZHCQYGLMGJ ，加密的方法即明文字母根据密钥字母向后平移不同的位数。
与单字母表加密方法不同，单字母表每个明文字母向后平移相同的位数。
所以单字母表加密保留了明文的英文字母的统计特性，由于英文字母的相对使用频率是固定的统计值，所以很容易被破译。

Vigenere密码因为需要猜测更多的字母表，并且频率分布特性也更加平坦，所以使得密码破译相对困难。

但是可以通过分析密文中的重复性来猜测密钥的长度，因为如果两个相同明文序列之间的距离是密钥词长度的整数倍，那么产生的密文序列也是相同的。
再根据英文字母的频率分布特性，即可以实现破解。

这里即使用这种方法猜解Vigenere密码的密钥并实现破译。

密文如下，保存于vigenereCipherText文件中：

wubefiqlzurmvofehmymwtixcgtmpifkrzupmvoirqmmwozmpulmbnyvqqqmvmvjleymhfefnzpsdlppsdlpevqmwcxymdavqeefiqcaytqowcxymwmsemefcf

wyeyqetrliqycgmtwcwfbsmyfplrxtqyeexmruluksgwfptlrqaerluvpmvyqycxtwfqlmtelsfjpqehmozciwciwfpzslmaeziqvlqmzvppxawcsmzmorvgvvqszetrlqz

pbjazvqiyxewwoiccgdwhqmmvowsgntjpfppaybiybjutwrlqklllmdpyvacdcfqnzpifppksdvptidgxmqqvebmqalkezmgcvkuzkizbzliuammvz'''


# File vigenere.py
def decode(cipherText):
    '''''解密'''
    length = findKeyLen(cipherText)  # 得到密钥长度
    key = findKey(cipherText, length)  # 找到密钥
    keyStr = ''
    for k in key:
        keyStr += k
    print('the Key is:', keyStr)
    plainText = ''
    index = 0
    for ch in cipherText:
        c = chr((ord(ch) - ord(key[index % length])) % 26 + 97)
        plainText += c
        index += 1
    return plainText


def openfile(fileName):
    '''''读取文件'''
    file = open(fileName, 'r')
    text = file.read()
    file.close();
    text = text.replace('\n', '')
    return text


def findKeyLen(cipherText):
    '''''寻找密钥长度'''
    length = 1
    maxCount = 0
    for step in range(1, 11):  # 假定密钥长度在1到10之间
        count = 0
        for i in range(step, len(cipherText) - step):
            if cipherText[i] == cipherText[i + step]:
                count += 1
        print(count)
        if count > maxCount:
            maxCount = count
            length = step
    return length


def findKey(text, length):
    '''''找出密钥'''
    key = []
    # 定义字母表频率列表
    alphaRate = [0.08167, 0.01492, 0.02782, 0.04253, 0.12705, 0.02228, 0.02015, 0.06094, 0.06996, 0.00153, 0.00772,
                 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.0009, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978,
                 0.02360, 0.0015, 0.01974, 0.00074]
    matrix = textToList(text, length)
    for i in range(length):
        w = [row[i] for row in matrix]  # 取出每组密文
        # print('w:',w)
        li = countList(w)  # 统计w中a-z出现的频率
        powLi = []  # 算乘积
        for j in range(26):
            Sum = 0.0
            for k in range(26):
                Sum += alphaRate[k] * li[k]
            powLi.append(Sum)
            li = li[1:] + li[:1]  # 循环移位
        Abs = 100
        ch = ''
        for j in range(len(powLi)):
            if abs(powLi[j] - 0.065546) < Abs:
                Abs = abs(powLi[j] - 0.065546)
                ch = chr(j + 97)
        key.append(ch)
    return key


def countList(lis):
    '''''统计列表中a-z出现的频率'''
    li = []
    alphabet = [chr(i) for i in range(97, 123)]
    for c in alphabet:
        count = 0
        for ch in lis:
            if ch == c:
                count += 1
        li.append(count / len(lis))
    return li


def textToList(text, length):
    '''''按密钥长度将text分组'''
    textMatrix = []
    row = []
    index = 0
    for ch in text:
        row.append(ch)
        index += 1
        if index % length == 0:
            textMatrix.append(row)
            row = []
    return textMatrix


# 按行输出矩阵
def printTextMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


if __name__ == '__main__':
    cipherText = openfile('vigenereCipherText.txt')
    print('cipherText:\n', cipherText)
    print('====================')
    plainText = decode(cipherText)
    print('====================')
    print('plainText:\n', plainText)