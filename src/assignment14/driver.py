from python_assignments.src.assignment14.util import cal_hap
input_values = "3 2\n1 5 3\n3 1\n5 7\n"
n, m = map(int, input_values.split('\n')[0].split())
array = list(map(int, input_values.split('\n')[1].split()))
set_a = set(map(int, input_values.split('\n')[2].split()))
set_b = set(map(int, input_values.split('\n')[3].split()))

# Calculate and print the output
result = cal_hap(n, m, array, set_a, set_b)
print(result)