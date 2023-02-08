#dynamic programming structure
#1. define subproblems
#2. guess (part of solution)
#3. relate subproblem solutions
#4. recurse & memoize or build bottom-up
#5. solve original problem


def fibonacci_recursion_DP(n, memo={}):

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    fibonnaci_n = fibonacci_recursion_DP(n - 1, memo) + fibonacci_recursion_DP(n - 2, memo)
    memo[n] = fibonnaci_n  
    return fibonnaci_n


def grid_traveler_DP(grid, memo={}):
    row,col = grid
    if row ==  0 or col == 0:
        return 0
    if row == 1 and col == 1:
        return 1
    key = str(row) + ',' + str(col)
    if memo[key]:
        return memo[row][col]
    memo[key] = grid_traveler_DP((row - 1, col), memo ) + grid_traveler_DP((row, col - 1), memo)
    return memo[key]


def can_sum_DP(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    
    for choice in numbers:
        remainder = target - choice
        if can_sum_DP(remainder, numbers, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False

def how_sum_dp(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for choice in numbers:
        remainder = target - choice
        remainder_result = how_sum_dp(remainder, numbers, memo)
        if remainder_result is not None:
            remainder_result.append(choice)
            memo[target] = remainder_result
            return remainder_result
    memo[target] = None
    return None


def best_sum_DP(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    shortest_combination = None
    
    for choice in numbers:
        remainder = target - choice
        remainder_result = best_sum_DP(remainder, numbers, memo)
        if remainder_result is not None:
            remainder_result.append(choice)
            if shortest_combination is None or len(remainder_result) < len(shortest_combination):
                memo[target] = remainder_result
                shortest_combination = remainder_result
    memo[target] = shortest_combination
    return shortest_combination


def can_construct_DP(target: str, word_bank: list[str], memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in word_bank:
        if word.find(target) == 0:
            if can_construct_DP(target[len(word):], word_bank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False
# print(can_construct_DP("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))

def count_construct_DP(target:str, word_bank: list[str], memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    
    total_count = 0
    for word in word_bank:
        if target.find(word)==0:
            if count_construct_DP(target[len(word):], word_bank):
                total_count += 1
    memo[target] = total_count
    return total_count

def all_construct(target:str, wordbank:list[str], memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    result = []
    for word in wordbank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, wordbank)
            target_ways = [[word, *way] for way in suffix_ways]
            if len(target_ways) > 0:
                result.append(*target_ways)
    memo[target] = result
    return result
# print(can_construct_DP("", ["cat", "dog", "mouse"]))
# print(can_construct_DP("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(count_construct_DP("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(count_construct_DP("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
#print(all_construct("ad", ["a", "c", "d"]))

#Tabulation is the opposite of memoization
#Tabulation is when you build a table from bottom up
#Tabulation is usually faster than memoization
#Tabulation is usually easier to build than memoization

def fibonacci_tabulation(n):
    table = [0] * (n + 1)
    #base cases
    table[1] = 1

    for index, value in enumerate(table):
        if index + 1 < len(table):
            table[index + 1] = value + table[index + 1]
        if index + 2 < len(table):
            table[index + 2] = value + table[index + 2]
    
    print(table)
    return table[n]


def grid_traveler_tabulation(row, col):
    table = [[0] * (col + 1) for _ in range(row + 1)]
    table[1][1] = 1
    for i in range(row + 1):
        for j in range(col + 1):
            current = table[i][j]
            if j < col:
                table[i][j + 1] += current
            if i < row:
                table[i + 1][j] += current
    print(table)
    return table[row][col]

def can_sum_tabulation(target, numbers):
    table = [False] * (target + 1)
    table[0] = True
    for i in range(target + 1):
        for number in numbers:
            if i + number < target + 1:
                table[i + number] = True
    print(table)
    return table[target]

def how_sum_tabulation(target, numbers):
    table = [None] * (target + 1)
    table[0] = []
    for i in range(target + 1):
        for number in numbers:
            if table[i] is not None:
                if i + number < target + 1:
                    table[i + number] = [*table[i], number]

    print(table)
    return table[target]
def best_sum_tabulation(target, numbers):
    table = [None] * (target + 1)
    table[0] = []
    for i in range(target + 1):
        for number in numbers:
            if table[i] is not None and i + number < target + 1:
                if table[i+number] is None:
                    table[i+number] = [*table[i], number]
                elif table[i+number] is not None and len(table[i+number]) > len(table[i]):
                    table[i+number] = [*table[i], number]
    print(table)
    return table[target]


def can_construct_tabulation(target, word_bank):
    
    table  = [False] * (len(target) + 1)
    table[0] = True
    for i in range(len(target) + 1):
        for word in word_bank:
            if table[i] is True and target[i:i+len(word)] == word:
                table[i + len(word)] = True
    print(table)
    return table[len(target)]

#print(can_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd"]))


def count_construct_tabulation(target, word_bank):
    table = [0] * (len(target) + 1)
    table[0] = 1
    for i in range(len(target) + 1):
        for word in word_bank:
            if target[i:i+len(word)] == word:
                table[i + len(word)] += table[i]
    print(table)
    return table[len(target)]

#print(count_construct_tabulation("purple", ["purp", "p", "ur", "le", "purpl"]))


def all_construct_tabulation(target, word_bank):
    table = [[]] * (len(target) + 1)
    table[0] = [[]]
    for i in range(len(target) + 1):
        for word in word_bank:
            if target[i:i+len(word)] == word:
                new_combination = [ [*way, word] for way in table[i] ]
                table[i + len(word)] = [*table[i + len(word)], *new_combination]
    return table[len(target)]

print(all_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
