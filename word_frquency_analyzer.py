from collections import Counter

# Step 1: Read file
with open("sample.txt", "r") as f:
    text = f.read()

# Step 2: Split words & count
words = text.split()
freq = Counter(words)

# Step 3: Print top 5
print(freq.most_common(5))
