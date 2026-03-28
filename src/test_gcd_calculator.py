"""
Unit tests for GCD calculator module.
"""

import pytest
from src.gcd_calculator import (
    gcd_euclidean,
    gcd_recursive,
    gcd_builtin,
    gcd_multiple,
    lcm
)


class TestGCDFunctions:
    """Test GCD calculation functions."""
    
    def test_gcd_euclidean_basic(self):
        """Test Euclidean GCD with basic numbers."""
        assert gcd_euclidean(48, 18) == 6
        assert gcd_euclidean(100, 50) == 50
        assert gcd_euclidean(17, 19) == 1
    
    def test_gcd_euclidean_negative(self):
        """Test Euclidean GCD with negative numbers."""
        assert gcd_euclidean(-48, 18) == 6
        assert gcd_euclidean(48, -18) == 6
        assert gcd_euclidean(-48, -18) == 6
    
    def test_gcd_euclidean_zero(self):
        """Test Euclidean GCD with zero."""
        assert gcd_euclidean(0, 5) == 5
        assert gcd_euclidean(10, 0) == 10
    
    def test_gcd_recursive_basic(self):
        """Test recursive GCD with basic numbers."""
        assert gcd_recursive(48, 18) == 6
        assert gcd_recursive(100, 50) == 50
        assert gcd_recursive(17, 19) == 1
    
    def test_gcd_recursive_negative(self):
        """Test recursive GCD with negative numbers."""
        assert gcd_recursive(-48, 18) == 6
        assert gcd_recursive(48, -18) == 6
    
    def test_gcd_builtin_basic(self):
        """Test built-in GCD with basic numbers."""
        assert gcd_builtin(48, 18) == 6
        assert gcd_builtin(100, 50) == 50
        assert gcd_builtin(1, 1) == 1
    
    def test_gcd_builtin_negative(self):
        """Test built-in GCD with negative numbers."""
        assert gcd_builtin(-48, 18) == 6
        assert gcd_builtin(48, -18) == 6
    
    def test_gcd_multiple_basic(self):
        """Test GCD of multiple numbers."""
        assert gcd_multiple(48, 18, 24) == 6
        assert gcd_multiple(100, 50, 25) == 25
        assert gcd_multiple(12, 18, 24, 36) == 6
    
    def test_gcd_multiple_single(self):
        """Test GCD with single number."""
        assert gcd_multiple(42) == 42
    
    def test_gcd_multiple_error(self):
        """Test GCD with no arguments raises error."""
        with pytest.raises(ValueError):
            gcd_multiple()
    
    def test_lcm_basic(self):
        """Test LCM calculation."""
        assert lcm(12, 18) == 36
        assert lcm(4, 6) == 12
        assert lcm(7, 5) == 35
    
    def test_lcm_same_number(self):
        """Test LCM with same numbers."""
        assert lcm(10, 10) == 10
        assert lcm(5, 5) == 5
    
    def test_lcm_negative(self):
        """Test LCM with negative numbers."""
        assert lcm(-12, 18) == 36
        assert lcm(12, -18) == 36
        assert lcm(-12, -18) == 36
    
    def test_all_methods_consistent(self):
        """Test that all GCD methods return same result."""
        test_cases = [
            (48, 18),
            (100, 50),
            (17, 19),
            (0, 5),
            (1, 1)
        ]
        
        for a, b in test_cases:
            result_euclidean = gcd_euclidean(a, b)
            result_recursive = gcd_recursive(a, b)
            result_builtin = gcd_builtin(a, b)
            
            assert result_euclidean == result_recursive == result_builtin, \
                f"Inconsistent results for GCD({a}, {b})"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
