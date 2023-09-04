#BouncingBall.py

height = 100
bounce = 3/5
for i in range(1,11):
    height = height * bounce
    #print('%d %.4f' % (i, height))
    print(i,round(height,4))
