# Get input from the user
elapsed_time = int(input("Enter elapsed time in seconds: "))

# Calculate hours, minutes, and seconds
hours = elapsed_time // 3600
remaining_seconds = elapsed_time % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Format the output
formatted_time = f"{hours:02d} :{minutes:02d} :{seconds:02d}"

# Display the converted time
print("Converted time:", formatted_time)