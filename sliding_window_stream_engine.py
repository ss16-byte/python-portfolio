import time
import random

# 1. The Bottleneck: Brute Force O(n * k)
def brute_force_window(data, k):
    max_sum = float('-inf')  # Start with the lowest possible number
    for i in range(len(data) - k + 1):
        current_sum = sum(data[i:i+k]) # Relentless, redundant loops here
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# 2. The Solution: Sliding Window O(n)
def sliding_window(data, k):
    if len(data) < k:
        return 0
    
    # Compute the sum of the absolute first window
    current_sum = sum(data[:k])
    max_sum = current_sum
    
    # Slide the window across the array tracking bounds
    for i in range(len(data) - k):
        # Subtract the element leaving, add the element entering
        current_sum = current_sum - data[i] + data[i+k]
        if current_sum > max_sum:
            max_sum = current_sum
            
    return max_sum

# ==========================================
# 3. ACTUAL EXECUTION CODE (Don't lose this part!)
# ==========================================
stream_size = 50000
window_size = 2000

print(f"⚡ Generating {stream_size} random stream metrics...")
mock_data = [random.randint(10, 500) for _ in range(stream_size)]

print(f"⚡ Processing stream with a sliding window of {window_size}...\n")

# Profile Brute Force
print("🔴 Running Brute Force...")
start_time = time.perf_counter()
brute_res = brute_force_window(mock_data, window_size)
brute_duration = time.perf_counter() - start_time
print(f"🔴 Brute Force Finished in: {brute_duration:.4f} seconds\n")

# Profile Sliding Window
print("🟢 Running Sliding Window...")
start_time = time.perf_counter()
window_res = sliding_window(mock_data, window_size)
window_duration = time.perf_counter() - start_time
print(f"🟢 Sliding Window Finished in: {window_duration:.4f} seconds\n")

# Calculate efficiency multiplier
speedup = brute_duration / window_duration
print("==========================================")
print(f"🏆 Optimization Factor: {speedup:.1f}x Faster Execution!")
print("==========================================")