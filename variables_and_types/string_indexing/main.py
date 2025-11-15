grocery_item = "Grilled Chicken Salad"

# 1. length using len()
length_of_item = len(grocery_item)

# 2. first characters via positive indexing
first_char  = grocery_item[0]   # 'G'
second_char = grocery_item[8]   # 'C'
third_char  = grocery_item[16]  # 'S'

# 3. last characters via negative indexing
last_char1 = grocery_item[-1]   # 'd' from "Salad"
last_char2 = grocery_item[-7]   # 'n' from "Chicken"
last_char3 = grocery_item[-15]  # 'd' from "Grilled"

# 4. output
print("Length of item name:", length_of_item)
print("First character of each word:", first_char, second_char, third_char)
print("Last character of each word:", last_char1, last_char2, last_char3)