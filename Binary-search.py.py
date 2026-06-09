print("Wassup, think of a number between 1 and 100, and I will guess it!")
print("Adjust your answers with: 'h' for Too High, 'l' for Too Low, and 'c' for Correct.\n")

# Step 1: Initialize our pointers
low = 1
high = 100
attempts = 0

# Step 2: Start the game loop
while low <= high:
    # Calculate the middle point (using // for integer division)
    mid = (low + high) // 2
    attempts += 1
    
    # The computer makes its guess
    print(f"My guess #{attempts} is: {mid}")
    feedback = input("Is it Too High (h), Too Low (l), or Correct (c)? ").lower().strip()
    
    # Step 3: Shift pointers based on feedback
    if feedback == 'c':
        print(f"\nBoom! Nailed it in {attempts} attempts. Binary Search wins again! bwahahaha 😎")
        break
    elif feedback == 'l':
        # Secret number is higher, throw away the lower half
        low = mid + 1
    elif feedback == 'h':
        # Secret number is lower, throw away the upper half
        high = mid - 1
    else:
        print("Invalid input! Please enter 'h', 'l', or 'c'.")
        attempts -= 1  # Don't count invalid entries as an attempt

else:
    # This triggers if the user gives conflicting feedback (e.g., lying to the script!)
    print("\nHmm... something's wrong. Are you sure you didn't change your number?")