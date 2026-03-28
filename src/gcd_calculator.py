"""
Greatest Common Divisor (GCD) Utility Module
This module provides functions to calculate the GCD of two or more numbers.
"""

import math
from functools import reduce
from typing import Union, List


def gcd_euclidean(a: int, b: int) -> int:
    """
    Calculate GCD using Euclidean algorithm.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Greatest Common Divisor
    """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def gcd_recursive(a: int, b: int) -> int:
    """
    Calculate GCD using recursive approach.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Greatest Common Divisor
    """
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def gcd_builtin(a: int, b: int) -> int:
    """
    Calculate GCD using Python's built-in math.gcd.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Greatest Common Divisor
    """
    return math.gcd(a, b)


def gcd_multiple(*numbers: int) -> int:
    """
    Calculate GCD of multiple numbers.
    
    Args:
        *numbers: Variable number of integers
        
    Returns:
        int: Greatest Common Divisor of all numbers
    """
    if not numbers:
        raise ValueError("At least one number is required")
    
    numbers = [abs(n) for n in numbers]
    return reduce(math.gcd, numbers)


def lcm(a: int, b: int) -> int:
    """
    Calculate Least Common Multiple using GCD.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Least Common Multiple
    """
    return abs(a * b) // math.gcd(a, b)


def main():
    """Example usage of GCD functions."""
    print("=" * 50)
    print("GCD (Greatest Common Divisor) Calculator")
    print("=" * 50)
    
    # Example 1: Two numbers
    num1, num2 = 48, 18
    print(f"\nExample 1: GCD({num1}, {num2})")
    print(f"  Euclidean: {gcd_euclidean(num1, num2)}")
    print(f"  Recursive: {gcd_recursive(num1, num2)}")
    print(f"  Built-in:  {gcd_builtin(num1, num2)}")
    
    # Example 2: Multiple numbers
    numbers = 48, 18, 24, 36
    print(f"\nExample 2: GCD({', '.join(map(str, numbers))})")
    print(f"  Result: {gcd_multiple(*numbers)}")
    
    # Example 3: LCM
    num1, num2 = 12, 18
    print(f"\nExample 3: LCM({num1}, {num2})")
    print(f"  Result: {lcm(num1, num2)}")
    
    # Interactive mode
    print("\n" + "=" * 50)
    print("Interactive Mode")
    print("=" * 50)
    
    try:
        a = int(input("\nEnter first number: "))
        b = int(input("Enter second number: "))
        
        result = gcd_builtin(a, b)
        print(f"\nGCD({a}, {b}) = {result}")
        print(f"LCM({a}, {b}) = {lcm(a, b)}")
    
    except ValueError:
        print("Error: Please enter valid integers!")


if __name__ == "__main__":
    main()
