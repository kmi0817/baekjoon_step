def string_to_number(s) :
    numbers = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    answer = s
    for key, value in numbers.items() :
        if key in answer :
            answer = answer.replace(key, str(value))
    
    return int(answer)

print(string_to_number('one4seveneight'))
print(string_to_number('23four5six7'))
print(string_to_number('1zerotwozero3'))