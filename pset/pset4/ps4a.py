# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    # >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # base case : 当sequence的长度为1时，它的重排结果只有一个，即它自己本身
    if len(sequence) == 1:
        return [sequence]

    # recursive case:
    first_letter = sequence[0]
    substring_exclude_first_letter = sequence[1:]
    permutations_list_exclude_first_letter = get_permutations(substring_exclude_first_letter)
    permutations_list = []
    for elt in permutations_list_exclude_first_letter:
        for index in range(len(elt)):
            permutation = elt[:index] + first_letter + elt[index:]
            permutations_list.append(permutation)
        # 勿遗漏  "bc"  +"a"  --->  "bca"
        permutations_list.append(elt + first_letter)

    return permutations_list


if __name__ == '__main__':
    # EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)
    example_input = 'km'
    print('Input:', example_input)
    print('Expected Output:', ['km', 'mk'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'k'
    print('Input:', example_input)
    print('Expected Output:', ['k'])
    print('Actual Output:', get_permutations(example_input))


