"""
Time Converter Module
=====================

Convert minutes into a human-readable time format.

Example:
    130 minutes → "2 hrs 10 minutes"
    110 minutes → "1 hr 50 minutes"
    60 minutes → "1 hr"
    45 minutes → "45 minutes"
"""

def convert_minutes_to_readable(minutes):
    """
    Convert minutes into human readable format.
    
    This function takes a total number of minutes and converts it into
    a readable format showing hours and minutes with proper pluralization.
    
    Args:
        minutes (int): Number of minutes to convert
        
    Returns:
        str: Human readable time format
        
    Raises:
        TypeError: If minutes is not an integer
        ValueError: If minutes is negative
        
    Examples:
        >>> convert_minutes_to_readable(130)
        '2 hrs 10 minutes'
        
        >>> convert_minutes_to_readable(110)
        '1 hr 50 minutes'
        
        >>> convert_minutes_to_readable(60)
        '1 hr'
        
        >>> convert_minutes_to_readable(45)
        '45 minutes'
        
        >>> convert_minutes_to_readable(0)
        '0 minutes'
    """
    # Validate input
    if not isinstance(minutes, int):
        raise TypeError(f"Expected int, got {type(minutes).__name__}")
    
    if minutes < 0:
        raise ValueError("Minutes cannot be negative")
    
    # Calculate hours and remaining minutes
    hours = minutes // 60
    remaining_minutes = minutes % 60
    
    # Build the result string
    result = ""
    
    # Add hours to result if present
    if hours > 0:
        result += f"{hours} hr{'s' if hours > 1 else ''}"
    
    # Add minutes to result if present
    if remaining_minutes > 0:
        if result:  # Add space if hours already added
            result += " "
        result += f"{remaining_minutes} minute{'s' if remaining_minutes != 1 else ''}"
    
    # Handle edge case where minutes is 0
    if not result:
        result = "0 minutes"
    
    return result


# ============================================================================
# TEST CASES
# ============================================================================

def run_tests():
    """Run comprehensive test cases for time conversion functions."""
    
    print("=" * 60)
    print("TIME CONVERTER - TEST CASES")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        (0, "0 minutes"),
        (1, "1 minute"),
        (2, "2 minutes"),
        (45, "45 minutes"),
        (60, "1 hr"),
        (61, "1 hr 1 minute"),
        (90, "1 hr 30 minutes"),
        (110, "1 hr 50 minutes"),
        (120, "2 hrs"),
        (130, "2 hrs 10 minutes"),
        (145, "2 hrs 25 minutes"),
        (240, "4 hrs"),
        (1440, "24 hrs"),
    ]
    
    print("\n✓ Basic Conversion Tests:")
    print("-" * 60)
    for minutes, expected in test_cases:
        result = convert_minutes_to_readable(minutes)
        status = "✓" if result == expected else "✗"
        print(f"{status} {minutes:4d} min → {result:25s} (Expected: {expected})")
    
    # Test error handling
    print("\n✓ Error Handling Tests:")
    print("-" * 60)
    
    error_cases = [
        (-10, ValueError, "negative number"),
        (3.5, TypeError, "float instead of int"),
        ("60", TypeError, "string instead of int"),
    ]
    
    for value, error_type, description in error_cases:
        try:
            convert_minutes_to_readable(value)
            print(f"✗ Failed to raise {error_type.__name__} for {description}")
        except error_type:
            print(f"✓ Correctly raised {error_type.__name__} for {description}")
        except Exception as e:
            print(f"✗ Unexpected error: {type(e).__name__}")
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY: All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Command line mode
        try:
            minutes = int(sys.argv[1])
            print(f"{minutes} minutes = {convert_minutes_to_readable(minutes)}")
        except ValueError:
            print(f"Please provide a valid integer. Got: {sys.argv[1]}")
    else:
        # Run tests by default
        run_tests()
