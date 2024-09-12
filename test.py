import time

# Print text without a newline
print("Processing...", end='', flush=True)

# Simulate a delay to show the effect
for i in range(5):
    time.sleep(0.1)  # Wait for 1 second
    print('.', end='', flush=True)  # Print a dot without a newline

# Move to the next line after the process is complete
print("Done")