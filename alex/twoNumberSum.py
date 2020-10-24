def twoNumberSum_1(array, targetSum):
    # Time=O(0^2n) as two loops
    # Space=O(1)
    for i in range(len(array) - 1):  # all way before last
        first_num = array[i]
        for j in range(i + 1, len(array)):  # all to the end
            if first_num + array[j] == targetSum:
                return [first_num, array[j]]
    return []

def twoNumberSum_2(array, targetSum):
    # Time=O(n) traversing only once
    # Space=O(n) because adding
    # better solution but takes space
    # check if number needed is stored in hash table
    numbers_hash = {}  # will store already checked values
    for number in array:
        possibleMatch = targetSum - number
        if possibleMatch in numbers_hash:
            return [possibleMatch, number]
        else:  # move one side only, checking what went through
            numbers_hash[number] = "checked"
    return []

def twoNumberSum_3(array, targetSum):
    # Good sorint algorithm is O(nlog(n))
    # Time is sorting algorithm plus iteration tjhe most one
    # Space=O(1)
    # Sort array and use the fact that sum if passed.
    # than will exceed target
    array.sort()
    left_idx = 0
    right_idx = len(array) - 1
    while left_idx < right_idx:
        currentSum = array[left_idx] + array[right_idx]
        if currentSum == targetSum:
            return [array[left_idx], array[right_idx]]
        elif currentSum < targetSum:
            # we move left index because we know that
            # if we move right index the sum will be even less
            left_idx += 1
        elif currentSum > targetSum:
            # we move the right index bacuse we know that 
            # the number on the left will be smaller
            # hence the overall sum will be smaller
            right_idx -= 1
    return []

def test_case():
    func = twoNumberSum_2
    output = func([3, 5, -4, 8, 11, 1, -1, 6], 10)
    assert len(output) == 2
    assert 11 in output
    assert -1 in output
    print("test1 passed")
    output = func([3, 5, -4, 8, 6, 1, -1, 11], 10)
    assert len(output) == 2
    assert 11 in output
    assert -1 in output
    print("test2 passed")

if __name__ == '__main__':
    test_case()
