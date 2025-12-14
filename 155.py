dict1 = {"Alice": 85, "Bob": 92}
dict2 = {"Charlie": 78, "Diana": 90}

# Method 1: Using update()
merged = dict1.copy()  # make a copy to keep dict1 unchanged
merged.update(dict2)

print(merged)
