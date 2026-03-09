def fibonacci(n: int) -> int:
	"""Return the n-th Fibonacci number using recursion."""
	if n < 0:
		raise ValueError("n must be a non-negative integer")
	if n <= 1:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
	print(f"fibonacci(10) = {fibonacci(10)}")


if __name__ == "__main__":
	main()
