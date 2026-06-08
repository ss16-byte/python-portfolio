def generate_fibonacci(terms):
    """
    Generates a list containing the Fibonacci sequence up to a specified number of terms.
    """
    sequence = []
    a, b = 0, 1
    
    for _ in range(terms):
        sequence.append(a)
        # Simultaneous assignment handles the state swap seamlessly
        a, b = b, a + b
        
    return sequence

def main():
    print("=" * 45)
    print("🚀 PROJECT 02: FIBONACCI SEQUENCE GENERATOR")
    print("=" * 45)
    
    while True:
        user_input = input("\nEnter the number of terms you want to generate: ").strip()
        
        # Input Validation
        if not user_input.isdigit():
            print("❌ Invalid input! Please enter a positive whole number.")
            continue
            
        num_terms = int(user_input)
        
        if num_terms <= 0:
            print("❌ Please enter a number greater than 0.")
            continue
            
        # Generate and display the results
        result = generate_fibonacci(num_terms)
        print(f"\n✅ Generated sequence ({num_terms} terms):")
        print(result)
        break

if __name__ == "__main__":
    main()