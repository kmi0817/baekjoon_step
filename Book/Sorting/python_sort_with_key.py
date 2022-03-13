array = [('바나나', 2), ('사과', 5), ('당근', 3)]
print(f"original array: {array}")

def setting(data) :
    return data[1]
result_array = sorted(array, key=setting)
print(result_array)

result2_array = sorted(array, key= lambda data: data[1])
print(result2_array)