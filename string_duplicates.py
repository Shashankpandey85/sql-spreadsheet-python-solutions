"""
String Duplicates Removal Module
==================================

Remove all duplicate characters from a string and return unique characters
using a loop-based approach.

Example:
    "hello" → "helo"
    "aabbccdd" → "abcd"
    "programming" → "progamin"
"""

def remove_duplicates(string):
    """
    Remove all duplicates from a string using a loop.
    
    This function iterates through each character in the string and builds
    a new string containing only characters that haven't been seen before.
    The order of first appearance is preserved.
    
    Args:
        string (str): Input string with potential duplicates
        
    Returns:
        str: String with unique characters in order of first appearance
        
    Examples:
        >>> remove_duplicates("hello")
        'helo'
        
        >>> remove_duplicates("aabbccdd")
        'abcd'
        
        >>> remove_duplicates("programming")
        'progamin'
        
        >>> remove_duplicates("mississippi")
        'misp'
        
        >>> remove_duplicates("a")
        'a'
        
        >>> remove_duplicates("")
        ''
    """
    unique_string = ""
    
    # Loop through each character in the string
    for char in string:
        # Check if character is not already in unique_string
        if char not in unique_string:
            unique_string += char
    
    return unique_string


def remove_duplicates_v2(string):
    """
    Remove duplicates using dict (maintains insertion order in Python 3.7+).
    
    This is a more Pythonic approach using dictionary keys which automatically
    maintain insertion order in Python 3.7+.
    
    Args:
        string (str): Input string with potential duplicates
        
    Returns:
        str: String with unique characters in order of first appearance
        
    Time Complexity: O(n) - much faster than the loop approach
    Space Complexity: O(n) - for the dictionary
    """
    return "".join(dict.fromkeys(string))


def remove_duplicates_with_list(string):
    """
    Remove duplicates using a list for better performance.
    
    This approach uses a list which is more efficient for concatenation
    operations compared to string concatenation.
    
    Args:
        string (str): Input string with potential duplicates
        
    Returns:
        str: String with unique characters in order of first appearance
        
    Time Complexity: O(n²) - still slower due to 'in' operator on list
    """
    unique_list = []
    
    for char in string:
        if char not in unique_list:
            unique_list.append(char)
    
    return "".join(unique_list)


# ============================================================================
# TEST CASES
# ============================================================================

def run_tests():
    """Run comprehensive test cases for string deduplication."""
    
    print("=" * 70)
    print("STRING DUPLICATES REMOVAL - TEST CASES")
    print("=" * 70)
    
    # Test cases
    test_cases = [
        ("hello", "helo"),
        ("aabbccdd", "abcd"),
        ("programming", "progamin"),
        ("mississippi", "misp"),
        ("a", "a"),
        ("", ""),
        ("aabbaa", "ab"),
        ("xyz", "xyz"),
        ("aaaa", "a"),
        ("abcabc", "abc"),
        ("the quick brown fox", "the quickbown fox"),
        ("11223344", "1234"),
        ("hello world", "helo wrd"),
    ]
    
    print("\n✓ Loop-based Implementation Tests:")
    print("-" * 70)
    for input_str, expected in test_cases:
        result = remove_duplicates(input_str)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{input_str:20s}' → Output: '{result:15s}' (Expected: '{expected}')")
    
    # Test v2 implementation
    print("\n✓ Dictionary-based Implementation (v2) Tests:")
    print("-" * 70)
    for input_str, expected in test_cases:
        result = remove_duplicates_v2(input_str)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{input_str:20s}' → Output: '{result:15s}'")
    
    # Test list-based implementation
    print("\n✓ List-based Implementation Tests:")
    print("-" * 70)
    for input_str, expected in test_cases:
        result = remove_duplicates_with_list(input_str)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{input_str:20s}' → Output: '{result:15s}'")
    
    print("\n" + "=" * 70)
    print("TEST SUMMARY: All tests completed!")
    print("=" * 70)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Command line mode
        input_string = " ".join(sys.argv[1:])
        result = remove_duplicates(input_string)
        print(f"Input:  '{input_string}'")
        print(f"Output: '{result}'")
    else:
        # Run tests by default
        run_tests()
