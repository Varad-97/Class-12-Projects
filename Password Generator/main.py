#password_genrator
import random


i=0
string_1='abcdefghijklmnopqrstuvwxyz'
list1=list(string_1)
list2=list(string_1.upper())
list3=list1+list2
list4=['0','1','2','3','4','5','6','7','8','9']
list5=list3+list4
list6=['!','@','#','$','&','*','?','"',"'",':','/','_',]
list7=list5+list6
print('''kindly enter  only integral values  as input, as this program is highly case,alpha,numeral sensitive 
''')
pass_ask=int(input('''choose password stregth 
    easy 0
    medium 1
    hard 2
    unpredictable 3'''))
if pass_ask==0:
    print('you have choosen easy password')
    while i<10:
        x = random.randrange(0, len(list1)-1)
        print(list1[x],sep=' ',end='')
        i+=1
elif pass_ask==1:
    print('you have choosen medium password')
    while i<17:
        x=random.randrange(0,len(list3)-1)
        var_3=list3[x]
        i += 1
        print(var_3,sep=' ',end='')
elif pass_ask==2:
    print('you have choosen hard passowrd')
    while i<27:
        x=random.randrange(0,len(list5)-1)
        var_4=list5[x]
        print(var_4,sep=' ',end='')
        i+=1
elif pass_ask==3:
    print('you have choosen unpredictable password')
    while i<49:
        x=random.randrange(0,len(list7)-1)
        var_5=list7[x]
        print(var_5,sep=' ',end='')
        i+=1
elif  pass_ask!=0 or pass_ask!=1 or pass_ask!=2 or pass_ask!=3:
     print('''hey user kindly enter valid input value :
              o-easy password genration
              1-medium stregth password genration
              2-hard strength password genration
              3-unpredicatable password genration''')
else:
    pass


print('''
thanks for using .
''')





