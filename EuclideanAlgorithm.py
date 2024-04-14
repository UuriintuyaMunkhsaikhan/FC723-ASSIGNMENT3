class Euclidean_algorithm:
    @staticmethod
    def gcd(a, b):
        # Implementation of the Euclidean Algorithm to find the greatest common divisor (GCD) of two numbers.
        # Continuously applies the modulo operation until the remainder becomes 0.
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a


if __name__ == "__main__":
    try:
        # Accepts input from the user for two numbers.
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        # Checks if the input numbers are positive integers.
        if num1 <= 0 or num2 <= 0:
            raise ValueError("Input numbers must be positive integers.")
        # Calls the gcd method of EuclideanAlgorithm class to find the GCD and prints the result.
        gcd_result = Euclidean_algorithm.gcd(num1, num2)
        print("GCD of", num1, "and", num2, "is:", gcd_result)

    except ValueError as e:
        # Handles ValueError if the input is not a valid integer.
        print("Error:", e)

