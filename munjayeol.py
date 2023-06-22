a="""안녕
나는 방민혁
23살
6월돼면 22살 ㅋㅋ"""
b = "안녕\n나는 방민혁\n23살"
#print(a[0:4]) #슬라이싱

c = '202001065방민혁'
# print(c[0:6:1]) #from(이상):to(미만):간격

# print(c[::-1]) # -붙이면 거꾸로

number = 7
object = 'it'
d = "I studied pyhon %d days but I couldn't do %s well" %(number,object)
# print(d) 포맷

e = 'sdfdfwef{name} eeedfsdf {age}' .format(name = "방민혁", age = 23)
# print(e) 포맷

name = '방민혁'
f = f"나의 이름은 {name}입니다"
# print(f) 이렇게도 할 수 있대 

g = "%0.3f" % 3.1415921828
# print(g) 소수점 자리 자르기

h = 'Bang Minhyeok'
# print(h.count('n')) 숫자 세기
# print(h.find('n')) 순서 인덱스 리턴

i = ",".join("아니근데진짜")
# print(i) 문자열 삽입

j = "     the 1st law of thermodynamics    "
#print(j.upper()) #대 소문자 변경 (lower)
# print(j.strip()) 공백 제거
