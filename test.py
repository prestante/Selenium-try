import re

url = "https://datika.me/en/category/black-friday/?price_max=2736&another_param=999999&price_min=666&other_param=11111&"

# Extract all matches
price_min_matches = re.findall(r"price_min=(\d+)", url)
price_max_matches = re.findall(r"price_max=(\d+)", url)

# Get the first match or handle duplicates as needed
price_min = price_min_matches[0] if price_min_matches else None
price_max = price_max_matches[0] if price_max_matches else None

print("Min Price:", price_min)
print("Max Price:", price_max)