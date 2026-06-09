import time


print("Please select a number between 1 to 1,000,000")
print("Adjust your answers with: 'h' for Too High, 'l' for Too Low, and 'c' for Correct.\n")
secret_number = 365943


low = 1
high = 1000000
attempt = 0

start_time = time.perf_counter()
attempt = 0

while low <= high:
    mid = (low + high) // 2
    attempt +=1
    #print(f"My guess #{attempt} is: {mid}")
    

    if mid == secret_number:
        print("The computer found it! Break out of the loop.")
        break

    elif mid < secret_number:
        low = mid + 1 

    else: 
        high = mid - 1      

end_time = time.perf_counter()
duration = end_time - start_time
print("Computer wins again BWAHAHAHAHA")
print(f"Total execution time: {duration:.6f} seconds")




