def can_construct(string, array: str, memo: dict):
    if string in memo:
        return memo[string]
    if string == "":
        return 1
    count = None
    for st in array:
        if string.startswith(st):
            size = len(st)
            if can_construct(string[size::], array) == 1:
                if count == None:
                    count = 1
                else:
                    count += 1
                memo[string] = True
                return memo[string]
    memo[string] = False
    return False


def integerConvert(array):
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    numbersCache = {'zero':0,'one':0,'two':0,'three':0,'four':0,'five':0,'six':0,'seven':0,'eight':0,'nine':0}
    numbersRef = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

    for num in numbers:
        if can_construct(num, array):
            for char in num:
                array.replace(char,"",1)
            numbersCache[num] += 1
    result = ""
    print(numbersCache)
    for key,value in numbersCache.items():
        result += (str(numbersRef[key]) * value)
    return result


print(integerConvert('oneninetwoninenine'))
