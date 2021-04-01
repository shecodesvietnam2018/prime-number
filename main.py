def is_prime(n):
	flag = True
	for i in range(2, n):
		if n % i == 0:
			flag = False
			break
			
	if flag:
		return True
	else:
		return False


n = int(input("Enter a number: "))
while n < 2:
	n = int(input("Enter a number: "))

if is_prime(n):
	print(f"{n} is prime")
else:
	print(f"{n} is not prime")
