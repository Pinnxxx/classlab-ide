def run_test():
    print("System test initialized.")
    
    x = 10
    y = 5
    result = x * y
    
    print(f"Calculation: {x} * {y} = {result}")
    
    if result > 40:
        print("Status: Result exceeds 40.")
    else:
        print("Status: Result is 40 or less.")

if __name__ == "__main__":
    run_test()