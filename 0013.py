s : str = "MCMXCIV"
d = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
num = 0
last = d[s[0]]
for i in s:
    n = d[i]
    num += n
    if n > last:
        num -= 2 * last
    last = n
print(num)