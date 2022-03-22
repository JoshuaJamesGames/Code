
def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    print(cs)
    return cs
    

def filterNumbers(data):
    non_divisible_digits = []
    current_divisible_digits = []
    act_divisible_digits = []
    whitelist = [0,3,6,9]
    temp = ""
    temp_MAX = 0
    for i in whitelist:
        for digit in data:
            if (digit not in whitelist):
                non_divisible_digits.append(digit)
                data.remove(digit)

    divisible_permuts = combs(non_divisible_digits)

    for x in divisible_permuts:
        if (x == []):
            continue
        else:  
            current_divisible_digits = x
        for y in current_divisible_digits:
            temp += str(y)
            if(int(temp) % 3 == 0 and int(temp) > temp_MAX):
                temp_MAX = int(temp)
                act_divisible_digits = current_divisible_digits
        temp = ""
    
    for index in act_divisible_digits:
        data.append(index)
    return data

def solution(L):
    current_value = ""
    value_MAX = 0
    L.sort(reverse=True)
    for element in L:
        current_value += str(element)
    if (int(current_value) % 3 == 0 and int(current_value) > value_MAX):
        value_MAX = int(current_value)
    else:
        current_value = ""
        new_L = (filterNumbers(L))
        new_L.sort(reverse=True)
        for new_Element in new_L:
            current_value += str(new_Element)
        if (int(current_value) % 3 == 0 and int(current_value) > value_MAX):
            value_MAX = int(current_value)
    return value_MAX

print("Test 1")
print()
ls1 = [1,2,3,4]
print(solution(ls1))
print()
print("Test 2")
print()
ls2 = [9,3,0,3,9]
print(solution(ls2))
print()
print("Test 3")
print()
ls3 = [9,3,5,6,1,1,7,3,9]
print(solution(ls3)) 
print()
ls4 = [4]
print(solution(ls4)) 
print()