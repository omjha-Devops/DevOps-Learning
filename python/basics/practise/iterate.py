previous_number = 0
for i in range(10):
    total_sum = previous_number + i
    print(f"previous_number: {previous_number}, current_no: {i}, total_sum: {total_sum}")
    previous_number = i