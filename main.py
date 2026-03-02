def fibonacci(n: int) -> int:
	if n < 0:
		raise ValueError("n must be a non-negative integer")
	if n <= 1:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)

