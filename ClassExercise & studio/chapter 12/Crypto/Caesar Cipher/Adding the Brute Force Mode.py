MAX_KEY_SIZE = 26
def getMode():
     while True:
         print('Do you wish to encrypt or decrypt or brute force a message?')
         mode = input().lower()
         if mode in 'encrypt e decrypt d brute b'.split():
             return mode[0]
         else:
             print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')
def getMessage():
    print('Enter your message:')
    return input()
def getKey():
     key = 0
     while True:
         print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
         key = int(input())
         if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
def getTranslatedMessage(mode, message, key):
     if mode[0] == 'd':
         key = -key
     translated = ''
     for symbol in message:
         if symbol.isalpha():
             num = ord(symbol)
             num += key
             if symbol.isupper():
                 if num > ord('Z'):
                     num -= 26
                 elif num < ord('A'):
                     num += 26
             elif symbol.islower():
                 if num > ord('z'):
                     num -= 26
                 elif num < ord('a'):
                     num += 26
             translated += chr(num)
         else:
             translated += symbol
     return translated




mode = getMode()
message = getMessage()

if mode[0] != 'b':
    key = getKey()
print('Your translated text is:')
if mode[0] != 'b':
   print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))
'''

Do you wish to encrypt or decrypt or brute force a message?

brute

Enter your message:

Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.

Your translated text is:

1 Kvbiaz thf uva il wslhzhua, iba jlyahpuaf pz hizbyk.

2 Juahzy sge tuz hk vrkgygtz, haz ikxzgotze oy ghyaxj.

3 Itzgyx rfd sty gj uqjfxfsy, gzy hjwyfnsyd nx fgxzwi.

4 Hsyfxw qec rsx fi tpiewerx, fyx givxemrxc mw efwyvh.

5 Grxewv pdb qrw eh sohdvdqw, exw fhuwdlqwb lv devxug.

6 Fqwdvu oca pqv dg rngcucpv, dwv egtvckpva ku cduwtf.

7 Epvcut nbz opu cf qmfbtbou, cvu dfsubjouz jt bctvse.

8 Doubts may not be pleasant, but certainty is absurd.

9 Cntasr lzx mns ad okdzrzms, ats bdqszhmsx hr zartqc.

10 Bmszrq kyw lmr zc njcyqylr, zsr acpryglrw gq yzqspb.

11 Alryqp jxv klq yb mibxpxkq, yrq zboqxfkqv fp xyproa.

12 Zkqxpo iwu jkp xa lhawowjp, xqp yanpwejpu eo wxoqnz.

13 Yjpwon hvt ijo wz kgzvnvio, wpo xzmovdiot dn vwnpmy.

14 Xiovnm gus hin vy jfyumuhn, von wylnuchns cm uvmolx.

15 Whnuml ftr ghm ux iextltgm, unm vxkmtbgmr bl tulnkw.

16 Vgmtlk esq fgl tw hdwsksfl, tml uwjlsaflq ak stkmjv.

17 Uflskj drp efk sv gcvrjrek, slk tvikrzekp zj rsjliu.

18 Tekrji cqo dej ru fbuqiqdj, rkj suhjqydjo yi qrikht.

19 Sdjqih bpn cdi qt eatphpci, qji rtgipxcin xh pqhjgs.

20 Rciphg aom bch ps dzsogobh, pih qsfhowbhm wg opgifr.

21 Qbhogf znl abg or cyrnfnag, ohg pregnvagl vf nofheq.

22 Pagnfe ymk zaf nq bxqmemzf, ngf oqdfmuzfk ue mnegdp.

23 Ozfmed xlj yze mp awpldlye, mfe npceltyej td lmdfco.

24 Nyeldc wki xyd lo zvokckxd, led mobdksxdi sc klcebn.

25 Mxdkcb vjh wxc kn yunjbjwc, kdc lnacjrwch rb jkbdam.

26 Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
'''
