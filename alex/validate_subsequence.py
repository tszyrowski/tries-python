'''
Given two non-empty arrays of integers, write funtion determining 
if the second array is asubsequence of the first
'''
def isValidSubsequence_1(array, sequence):
    if all([i in array for i in sequence]) and len(sequence) <= len(array):
        in_array = []
        i = 0
        for j in range(len(array)):
            if i < len(sequence):
                current_number = sequence[i]
                arr_number = array[j]
                if current_number == arr_number:
                    in_array.append(True)
                    i += 1
        return len(in_array) == len(sequence)
    return False

def isValidSubsequence_2(array, sequence):
    if all([i in array for i in sequence]) and len(sequence) <= len(array):
        i = 0
        for j in range(len(array)):
            if i < len(sequence):
                current_number = sequence[i]
                arr_number = array[j]
                if current_number == arr_number:
                    i += 1
        return len(sequence) == i
    return False

def isValidSubsequence_sol1(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return len(sequence) == seqIdx

def isValidSubsequence_sol2(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return len(sequence) == seqIdx
        

def test_isValidSubsequence():
    func = isValidSubsequence_sol2
    tests_true = [
        {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, 10]},
        {"array": [1, 1, 1, 1, 1], "sequence": [1, 1, 1]},
        {"array": [5, 1, 22, 25, 6, -1, 8, 10],
         "sequence": [5, 1, 22, 6, -1, 8, 10]},
        {"array": [5, 1, 22, 25, 6, -1, 8, 10],
         "sequence": [5, 1, 22, 25, 6, -1, 8, 10]},
        {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [22, 25, 6]},
        {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [25]},
    ]
    tests_false = [
        {"array": [5, 1, 22, 25, 6, -1, 8, 10],
         "sequence": [5, 1, 22, 25, 6, -1, 8, 10, 12]},
        {"array": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [26]},
        {"array": [1, 1, 6, 1], "sequence": [1, 1, 1, 6]},
        {"array": [5, 1, 22, 25, 6, -1, 8, 10],
         "sequence": [5, 1, 22, 25, 6, -1, 8, 10, 10]},
        {"array": [5, 1, 22, 25, 6, -1, 8, 10],
         "sequence": [4, 5, 1, 22, 25, 6, -1, 8, 10]}
    ]
    for test in tests_true:
        array = test["array"]
        sequence = test["sequence"]
        try:
            assert func(array, sequence)
        except Exception as e:
            print(f"array {array}\nseqence: {sequence}\nfailed:{str(e)}")

    for test in tests_false:
        array = test["array"]
        sequence = test["sequence"]
        try:
            assert not func(array, sequence)
        except Exception as e:
            print(f"array {array}\nseqence: {sequence}\nfailed:{str(e)}")

if __name__ == '__main__':
    test_isValidSubsequence()