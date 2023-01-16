# Input [13,11,10,7,4,3,1], number to be searched
#Output position on number to be searched
#Plain English
# list of numbers in decreasing order, minimize the numbers of times we accesss elements from the list


def locate_card(cards, query):
    if len(cards)==0:
        return -1
    middle = cards[len(cards)//2]
    if middle > query:
       start = middle
    elif middle < query:
        start = 0 
    for index in range(start, middle):
        if cards[index] == query:
            return index
    return -1

tests = []
input = [13,11,10,7,4,3,1]
query = 7

tests.append({
    "input":{
        "cards":[],
        "query": 7
    },
    "output": -1
})

tests.append({
    "input":{
        "cards":[13,11,10,7,4,3,1,0],
        "query": 7
    },
    "output": 3
})

tests.append({
    "input":{
        "cards":[8,8,6,6,6,6,6,6,3,2,2,2,2,0,0,0],
        "query": 6
    },
    "output": 2
})


for test in tests:
    result = locate_card(**test["input"]) == test["output"]
    print(result)