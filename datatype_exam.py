# 비교연산자와 논리연산자
# x = 4
# y = 9
#
# print("x == y = ", x==y)
# print("x != y = ", x!=y)
#
# print("x < y = ", x<y)
# print("x > y = ", x>y)
#
# print("int(True)  = ", int(True))
# print("int(False) = ", int(False))
#########################################
#이스케이프 문자
# text1 = "안녕하세요!\n하나금융\t임직원여러분 !"
#
# text2 = '''
# 빅데이터를 위한 파이썬 과정에서 만나뵙게되어 반갑습니다.
# 끝까지 '화이팅'하세요!!!
# '''
#
# print(text1)
# print(text2)
############################################
#문자형함수1
# test = '파이썬 프로그래밍 재미있다!'
#
# result = test.startswith('파이썬')
# print(result)
# result = test.endswith('!')
# print(result)
# result = test.endswith('어려워요!')
# print(result)
# result = test.replace('파이썬', 'Python')
# print(result)
###########################################
#문자형 함수2
# test = 'Python Programming is Interesting!'
#
# result = test.upper()
# print(result)
# result = test.lower()
# print(result)
# result = '/'.join(test)
# print(result)
################################################
#Immutable
# hello = '안녕하세요!'
#
# print(hello)
# print(id(hello))
#
# hello = '반갑습니다!'
#
# print(hello)
# print(id(hello))
#
# hello = '안녕하세요!'
# print(hello)
# print(id(hello))
#################################################
#Mutable 예제
hello_list = ['안녕하세요!']

print(hello_list)
print(id(hello_list))

hello_list[0] = '반갑습니다!'
print(hello_list)
print(id(hello_list))