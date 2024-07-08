#bài 2. Bạn hãy viết chương trình nhập từ bàn phím số nguyên n và hiển thị ra màn hình n! (n giai thừa).
#Ví dụ nếu nhập n = 5 thì chương trình sẽ hiển thị ra màn hình:
import math
n=int(input(f'Xin mời nhập số nguyên (n >0): '))
while n<0:
    n=int(input(f'Xin mời nhập lại (n >0): '))
if n==0:
    print(f'Giai thừa của {n} là: 1')
else:
    ketqua2=1
    for i in range(1,n+1):
        ketqua2=i*ketqua2
    print(f'Giai thừa của {n} là: {ketqua2}')
    
