a = input('请输入数字,或输入q以结束:')
b = 0
c = 0
d = 0
while a != 'q' :
    c += float(a)
    b += 1
    a = input('请再次输入数字,或输入q以计算结果:')
if b == 0:
    d = 0
else:
    d = c / b
print('您输入数字的平均值为:' + str(d))