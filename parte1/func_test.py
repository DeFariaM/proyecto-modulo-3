import pytest

from func import es_primo

class TestEsPrimo:

    # Verify that prime numbers (e.g., 2, 3, 5, 7, 11, 13, 17, 19) return True
    def test_prime_numbers_return_true(self):
        
    
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    
        for num in prime_numbers:
            assert es_primo(num) is True, f"{num} should be identified as prime"

    # Verify that 0 and 1 return False as they are not prime numbers
    def test_zero_and_one_return_false(self):
        
    
        assert es_primo(0) is False, "0 should not be identified as prime"
        assert es_primo(1) is False, "1 should not be identified as prime"

    # Verify that integers close to float values (e.g., 7.0, 11.0) are correctly evaluated
    def test_floats_close_to_integers(self):
        
    
        float_values = [7.0, 11.0, 13.0, 17.0]
    
        for num in float_values:
            assert es_primo(num) is True, f"{num} should be identified as prime"

    # Verify that float values very close to integers (e.g., 5.000000001) are rounded and evaluated correctly
    def test_float_values_close_to_integers(self):
        
    
        float_values = [5.000000001, 7.999999999, 11.0000000001]
        expected_results = [True, False, True]
    
        for num, expected in zip(float_values, expected_results):
            assert es_primo(num) is expected, f"{num} should be evaluated as {expected}"

    # Verify that non-prime numbers (e.g., 4, 6, 8, 9, 10, 12) return False
    def test_non_prime_numbers_return_false(self):
        
    
        non_prime_numbers = [4, 6, 8, 9, 10, 12]
    
        for num in non_prime_numbers:
            assert es_primo(num) is False, f"{num} should be identified as non-prime"

    # Verify that negative numbers return False
    def test_negative_numbers_return_false(self):
        
    
        negative_numbers = [-1, -2, -3, -10, -100]
    
        for num in negative_numbers:
            assert es_primo(num) is False, f"{num} should not be identified as prime"

    # Verify that boolean inputs raise TypeError
    def test_boolean_inputs_raise_type_error(self):
        
    
        boolean_values = [True, False]
    
        for value in boolean_values:
            with pytest.raises(TypeError, match="La entrada no puede ser un valor booleano."):
                es_primo(value)

    # Verify that float values not close to integers raise TypeError
    def test_float_not_close_to_integer_raises_typeerror(self):
        
    
        non_integer_floats = [2.5, 3.7, 10.1, 15.999]
    
        for num in non_integer_floats:
            with pytest.raises(TypeError, match="La entrada debe ser un número entero o flotante cercano a un entero."):
                es_primo(num)

    # Verify that non-numeric inputs (strings, lists, etc.) raise TypeError
    def test_non_numeric_inputs_raise_typeerror(self):
        
    
        non_numeric_inputs = ["string", [1, 2, 3], {"key": "value"}, None, True]
    
        for input_value in non_numeric_inputs:
            with pytest.raises(TypeError):
                es_primo(input_value)

    # Verify performance with very large numbers
    def test_large_numbers_performance(self):
        
        import time

        large_prime = 999999937  # A known large prime number
        start_time = time.time()
        result = es_primo(large_prime)
        end_time = time.time()
    
        assert result is True, f"{large_prime} should be identified as prime"
        assert (end_time - start_time) < 1, "Performance issue: The function took too long to execute"

    # Verify correct rounding behavior for values at the tolerance boundary
    def test_rounding_behavior_at_tolerance_boundary(self):
        

        # Values at the tolerance boundary
        tolerance_values = [2.0000000001, 3.9999999999, 5.0000000001, 6.9999999999]
        expected_results = [True, False, True, True]  # Updated expected result for 6.9999999999

        for num, expected in zip(tolerance_values, expected_results):
            assert es_primo(num) is expected, f"{num} should be rounded and identified as {'prime' if expected else 'not prime'}"

    # Verify that very small positive numbers between 0 and 1 raise a TypeError
    def test_very_small_positive_numbers_raise_type_error(self):
        

        small_numbers = [0.1, 0.01, 0.001, 0.0001]

        for num in small_numbers:
            with pytest.raises(TypeError):
                es_primo(num)

    # Verify that es_primo raises an exception for edge cases like math.inf, -math.inf, and math.nan
    def test_edge_cases_inf_nan(self):
        
        import math

        edge_cases = [math.inf, -math.inf, math.nan]

        for case in edge_cases:
            with pytest.raises(Exception):
                es_primo(case)

    # Verify that the function correctly handles the special case for 2 and 3
    def test_special_case_for_2_and_3(self):
        
    
        special_cases = [2, 3]
    
        for num in special_cases:
            assert es_primo(num) is True, f"{num} should be identified as prime"

    # La función debe ser capaz de evaluar eficientemente la primalidad de números grandes
    def test_large_prime_number(self):
        
    
        large_prime = 104729  # 10000th prime number
    
        assert es_primo(large_prime) is True, f"{large_prime} should be identified as prime"