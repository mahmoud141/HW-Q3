digits_to_be_reversed = [7,6,5,4,2]

reverse_save = 0

for d in digits_to_be_reversed[::-1]:

    reverse_save = reverse_save * 10 + d


print(reverse_save)  #