"""
MANUAL IMPLEMENTATION
Sorting list of dictionaries by key - Human-written version
"""

def sort_dicts_manual(data, key):
    """
    Manually implement sorting of list of dictionaries by specific key
    Using bubble sort for demonstration
    """
    # Create a copy to avoid modifying original data
    sorted_data = data.copy()
    n = len(sorted_data)
    
    # Bubble sort implementation
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_data[j][key] > sorted_data[j+1][key]:
                # Swap elements
                sorted_data[j], sorted_data[j+1] = sorted_data[j+1], sorted_data[j]
    
    return sorted_data

# Test data
test_data = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20}
]

# Test the manual implementation
result = sort_dicts_manual(test_data, "age")
print("Manual sort result:", result)