país_A = 80000
país_B= 200000
crescimento_A= país_A * 3/100
crescimento_B= país_B * 1.5/100
anos= 0

while país_A < país_B:
    país_A += crescimento_A
    país_B += crescimento_B
    anos+=1
print(anos)

