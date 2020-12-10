

# product = {"productPrice" : 1000 , "productName" : 20000} 
test= 20

# test= {
# "bardia" : 2000
# }

# print(type(test))

# print('-----------------')


# testvalue= None #None means Empty
# print(type(testvalue))

# print('-----------------')


# bardia={
#     "bardiaAge" : 16 , "school" : "Allameh"
# }

# sentence="test  test test test \nNewLine  \nNewline2  \nNewLine3 "

# print(sentence)

# print('-----------------')


# userName = "bardia"
# userFamily = "bgh"

# result=(f"user:{userName} , userFamily:{userFamily}")

# print(result)

# print('-----------------')


# test1 = ["bardiabagha", "bardiabagha2" , "bardiabagha3"] 

# print(test1[2])

# print('-----------------')

# testNumber = "900"
# print(type(testNumber))

# intNumber= int(testNumber)

# print(type(intNumber))


# intNumber+= 56

# print(intNumber)

# intNumber**= 3

# print(intNumber)

# # intNumber%= 2
# # print(intNumber)

# # intNumber*=(1098296 % 2)
# # print(intNumber)

# # intNumber*=(1098296 % 2)
# # print(intNumber)

# intNumber=(1098296 // 9)
# print(intNumber)

# intNumber%= 2
# print(intNumber)




print('-----------------')

# tabdil KM be miles

# print("adad ra be KM vared konid")

# 1mile = 1.609344KMs

# KMs= input()
# miles= (f"Your converted data is: {float(KMs) / 1.609344}")
# print(miles)


# print('-----------------')

# round(miles , 3) -> round kardan ta 3 ragham aashar3


# print("adad ra be KM vared konid")

# KMs= float(input())
# count=0
# if type(KMs) != float:
#     print('the input is not a number')
#     while count<10:
#         print('oohohohhoh')
#         count += 1
    
    
    
#     # raise Exception('bekhodet biaaaaaaa!!!!!!!!')
# miles= float(KMs) /1.609344 
# print("Javab ta chand raghame Ashar bashad?")
# Ashar=int(input())
# print(f"Your converted data is: { round(miles , Ashar)}")


# if KMs > 100 and KMs < 1000:
#     print(str(KMs) + '  bozorgtar az 100 eee')
# elif 0<KMs < 100 or type(KMs) == str:
#     print('ya adad kuchike ya asan adad nist')
# elif KMs == 0:
#     print( 'Bg zeroooo')
# elif KMs> 1000000:
#     print('kheyli bozorgeeee')
# else:
#     print('ajib')
    
# print('-----------')

#tamrin if

# print("adad mored nazar ra vared konid:")
# Adad= float(input())
# Adad%= 2
# if Adad is 0: #or adad==0
#     print("adad zoj ast")
# elif Adad is not 0 : #or adad !=
#     print("adad fard ast")

#falsiness-> Empty objects like (Zero,0,""(empty str),None)

# print("Enter your favorite sport")
# name= str(input())
# if name:
#     print(f"Your favorite sport is: {name}")
        
# print('----------')
import numpy as np
m=10
# while m <= 10:
#     print(m*'-')
#     if m==5:
#         break
#     m+=1
#     # print()

# for ttt in range(10):
#     if ttt==7:
#         print('dg baseeeee!!!!')
#         break
#     print(ttt)

p=[1,2,3,4]
m=[0,0,-1,2]
o=np.matmul(p,m)
print(o)


def my_function(a,b):
    c= a**2 + b//2
    print('salam ma darune function hastim')
    return c


print(my_function(3,8))