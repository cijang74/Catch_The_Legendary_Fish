aa = [0,0,0,0]
hap = 0

for i in range(0,3):
    aa[i] = int(input("%d번째 숫자:" %(i+1)))
    hap += aa[i]

print("합계: %d" %hap)