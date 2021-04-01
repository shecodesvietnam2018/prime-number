is_prime = True

n = int(input("Enter a number: "))
while n < 2:
	n = int(input("Enter a number: "))

for i in range(2, n):
	if n % i == 0:
		is_prime = False
		break
		
if is_prime:
	print(f"{n} is prime")
else:
	print(f"{n} is not prime")
