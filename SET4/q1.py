# Given DataList
DataList = [25, 28, -11, 0, 29, 10, -4, 45, 19, -8, 7, 10, 3, 20, 12, -4, -11, 20, 31]

# a) Remove all duplicate elements without creating a new list
DataList = list(dict.fromkeys(DataList))  # Removes duplicates while preserving order
print("Modified DataList without duplicates:", DataList)

# b) Identify the 6th smallest and 2nd largest numbers
sorted_list = sorted(DataList)
sixth_smallest = sorted_list[5]
second_largest = sorted_list[-2]
print("6th Smallest:", sixth_smallest)
print("2nd Largest:", second_largest)

# c) Rotate the elements of the modified DataList by 3 positions to the left
n = 3  # Number of positions to rotate
DataList = DataList[n:] + DataList[:n]  # Rotate left without extra variable
print("DataList after 3-position left rotation:", DataList)

# d) Divide the modified DataList into two lists: EvenList and OddList
EvenList = [num for num in DataList if num % 2 == 0]
OddList = [num for num in DataList if num % 2 != 0]
print("EvenList:", EvenList)
print("OddList:", OddList)
