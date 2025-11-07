#진법변환계산기
a = input()
n = int(a)


def to_hex16(n):
  digits = "0123456789abcdef"
  if (n == 0):
    return ""
  return to_hex16(n // 16) + digits[n % 16]
  
#자리수이동

result = to_hex16(n)

if result == "": 
    result = "0"
print(result)
