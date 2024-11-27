import time
from random import random

str = ''

# Print text without a newline
print("Processing", end='', flush=True)

# Simulate a delay to show the effect
for i in range(10):
    time.sleep(random())  # Wait for some random time
    print('.', end='', flush=True)  # Print a dot without a newline

# Move to the next line after the process is complete
print("Done")