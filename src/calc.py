def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Test cases
if __name__ == "__main__":
    print("Addition Test:", add(10, 5))  # Expected output: 15
    print("Subtraction Test:", subtract(10, 5))  # Expected output: 5
    print("Multiplication Test:", multiply(10, 5))  # Expected output: 50
    print("Division Test:", divide(10, 5))  # Expected output: 2.0
    print("Division by Zero Test:", divide(10, 0))  # Expected output: "Error! Division by zero."

