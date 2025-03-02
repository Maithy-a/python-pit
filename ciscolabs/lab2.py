# Get input from user
start_hours = int(input("Enter start hours (0-23): "))
start_minutes = int(input("Enter start minutes (0-59): "))
duration = int(input("Enter duration in minutes: "))

# Convert start time to total minutes since midnight
total_start_minutes = start_hours * 60 + start_minutes

# Add duration to get total end minutes
total_end_minutes = total_start_minutes + duration

# Calculate end hours and minutes
end_hours = (total_end_minutes // 60) % 24  # Integer division for hours, % 24 to wrap around
end_minutes = total_end_minutes % 60         # Remainder for minutes

# Print the result
print(f"End time: {end_hours:02d}:{end_minutes:02d}")