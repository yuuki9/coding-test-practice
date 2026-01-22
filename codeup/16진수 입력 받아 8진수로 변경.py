a = input()               # 16진수 문자열 입력
n = int(a, 16)            # 16진수를 10진수로 해석

def to_oct8(n):
    digits = "01234567"
    if n == 0:
        return ""
    return to_oct8(n // 8) + digits[n % 8]

result = to_oct8(n)
if result == "":
    result = "0"

print(result)