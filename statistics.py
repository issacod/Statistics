import math, random

# FUNCTIONS
def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += str(ele)+" "
    return str1

def dot_product(lst1, lst2):
   return sum(lst1[i]*lst2[i] for i in range(len(lst1)))

# DATA INPUT
# data = [int(item) for item in input("Enter data: ").split()]
data = [random.randint(1,9) for i in range(10)]

# BASIC CALCULATIONS
data_sorted = sorted(data)
data_sorted_string = list_to_string(data_sorted)
data_length = len(data)
data_sum = sum(data)
data_mean = data_sum/data_length

# MEDIAN CALCULATION
if data_length % 2 == 0:
    data_median = (data_sorted[int(data_length/2)]+data_sorted[int(data_length/2) - 1])/2
else:
    data_median = data_sorted[int(data_length/2)]

# MODE CALCULATION
data_set = sorted(list(set(data_sorted)))
mode_dict = {}
for ele in data_set:
    mode_dict.update({ele:data_sorted.count(ele)})

mode_dict_sorted_by_values = dict(sorted(mode_dict.items(), key = lambda x:x[1], reverse=True))

# VARIANCE CALCULATIONS
data_sos = dot_product(data,data)
data_var = data_sos/(data_length - 1) - (data_length * data_mean * data_mean)/(data_length - 1)
data_sd = math.sqrt(data_var)

# PRINT TO CONSOLE
print("")
print("Sorted     : " + str(data_sorted))
print("SortedS    : " + data_sorted_string)

print("Length     : " + str(data_length))
print("Sum        : " + str(data_sum))

print("Mean       : " + str(round(data_mean,6)))
print("Median     : " + str(data_median))
print("ModeDict   : " + str(mode_dict_sorted_by_values))

print("SumSquares : " + str(data_sos))
print("Variance   : " + str(round(data_var,6)))
print("StdDev     : " + str(round(data_sd,6)))
