# 실습 6
# 1 문자열의 길이
s1 = "pythonjavascript"
print(len(s1))

# 2 특정 문자 제거
s2 = "010-7777-9999"
print(s2.replace('-', ''))

# 3 문자열 뒤집기
s3 = "PYTHON"
print(s3[::-1])

# 4 소문자열로 만들기
s4 = "Python"
print(s4.lower())

# 5
s5 = "https://www.python.org/"
print(s5[8:-1])
# print(s5.lstrip('"').rstrip('"').rstrip('/'))

# 6 주민등록번호를 통한 성별 판단
s6 = '891022-2473837'
if s6[7] in ['1', '3'] :
    print ("남자")
else :
    print ("여자")

# 7 타입변환
s7 = '100'
print(int(s7))
print(float(s7))

# 8 특정 문자의 갯수 세기
s8 = 'The Zen of Python'
print(s8.count('n'))

# 9 특정 문자의 위치 반환
print(s8.find('Z'))

# 10
s9 = s8.upper()
print(s9.split())