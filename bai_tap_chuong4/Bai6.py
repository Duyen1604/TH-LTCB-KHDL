num = input("Nhập một số nguyên: ")
digits = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

i = 0
while i < len(num):
    print(digits[int(num[i])], end=" ")
    i += 1
