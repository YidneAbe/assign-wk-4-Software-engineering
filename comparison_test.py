"""
COMPARISON TESTING
Benchmarking manual vs AI implementations
"""
import time
import random

def performance_test():
    """Test performance of both implementations"""
    # Generate larger test data
    large_data = [
        {"id": i, "value": random.randint(1, 1000)} 
        for i in range(1000)
    ]
    
    # Test manual implementation
    start_time = time.time()
    from manual_implementation import sort_dicts_manual
    manual_result = sort_dicts_manual(large_data, "value")
    manual_time = time.time() - start_time
    
    # Test AI implementation
    start_time = time.time()
    from ai_suggested import sort_dicts_ai
    ai_result = sort_dicts_ai(large_data, "value")
    ai_time = time.time() - start_time
    
    print(f"Manual implementation time: {manual_time:.4f} seconds")
    print(f"AI implementation time: {ai_time:.4f} seconds")
    print(f"AI is {manual_time/ai_time:.2f}x faster")
    
    # Verify both produce same results
    assert manual_result == ai_result, "Results don't match!"
    print("✓ Both implementations produce identical results")

if __name__ == "__main__":
    performance_test()