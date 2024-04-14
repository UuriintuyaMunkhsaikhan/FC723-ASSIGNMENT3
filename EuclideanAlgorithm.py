class ExtendedEuclideanAlgorithm:
    @staticmethod
    def extended_gcd(a, b):
        """
        Extended Euclidean Algorithm to find the greatest common divisor (GCD) of two numbers and their coefficients
        such that ax + by = gcd(a, b).
       :param a: The first integer.
       :param b: The second integer.
       :return: A tuple (gcd, x, y) where gcd is the GCD of a and b, and x, y are coefficients satisfying ax + by = gcd(a, b).
       """
        # Base case: if b is 0, the GCD is a, and coefficients are 1 and 0 respectively
        if b == 0:
          return a, 1, 0
        else:
            # Recursive call to find GCD and coefficients for smaller numbers.
            gcd, x1, y1 = ExtendedEuclideanAlgorithm.extended_gcd(b, a % b)
            # Calculate coefficients for current step.
            gcd, x1, y1 = ExtendedEuclideanAlgorithm.extended_gcd(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            return gcd, x, y


if __name__ == "__main__":
    try:
        # Accepts input from the user for two numbers.
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        # Checks if the input numbers are integers.
        if num1 <= 0 or num2 <= 0:
            raise ValueError("Input numbers must be positive integers.")
        # Call the extended_gcd method to find GCD and coefficients
        gcd, x, y = ExtendedEuclideanAlgorithm.extended_gcd(num1, num2)
        print("GCD of", num1, "and", num2, "is:", gcd)
        print("Coefficients (x, y) such that ax + by = gcd(a, b):", x, ",", y)
    # Handle invalid input
    except ValueError as e:
        print("Error:", e)
