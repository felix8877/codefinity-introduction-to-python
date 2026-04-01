start_number = 5
countdown_values = []

# Use a while loop to count down
while start_number >= 1:
    # Append the current value to the list
    
    countdown_values.append(start_number)
    
    # Decrement the number by 1
    start_number -= 1

# After the loop, print the final messages
print("Discount countdown complete!")
print(countdown_values)