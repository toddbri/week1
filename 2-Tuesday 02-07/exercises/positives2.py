numbers=[56,55,-81,72,-61,18.8,20,0]
pos_nums =[]
print str(numbers) + " =>",
for num in numbers:
    if num >0:
        pos_nums.append(num)
print str(pos_nums)
