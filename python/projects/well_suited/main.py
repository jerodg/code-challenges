'''
An initial attempt at writing a function that calculates a given Fibonacci number is given below, but it has some bugs. Your goal
is to debug and fix this code.

For reference, the Fibonacci sequence is listed below. In general, it follows the pattern that the nth number equals the sum of
the two numbers preceding it in the pattern (i.e. the n-1th and n-2th numbers)

  Input  | Fibonacci number
-----------------------
    0    | 0
    1    | 1
    2    | 1
    3    | 2
    4    | 3
    5    | 5

'''


def fibonacci_number(term_number):
    if term_number > 1:
        return fibonacci_number(term_number - 1) + fibonacci_number(term_number - 2)

    return term_number  # if term_number == 1:  #     return 1  # list_of_fibs = [1]  # x = 0  # while x < term_number:  #
    # list_of_fibs[x] = list_of_fibs[x] + list_of_fibs[x - 1]

    # return list_of_fibs[term_number]


# this should return 1, edit to test
# term = 1
# fib_output= fibonacci_number(term)
# print('The {}th Fibonacci term is {}'.format(
#     term,fib_output))
[print(i, fibonacci_number(i)) for i in range(20)]

'''
The goal of this problem is to mimic a PR review. The code below is designed to accomplish a task. We have two questions for you 
about this code, which is trying to create 3 lists of random integers from (0-9, 10-19, 20-29, respectively):

If you saw this code while reviewing a PR, what comments would you make and where? Please type them in as if you were submitting 
an actual review.

# Example comment!
import random 
key0 = [] 


while len(key0) <10: 
    # results in a recursion error, unnecessary
    while True: 
        candidate = random.randint(0, 9) 
        if candidate in key0: 
            continue 
        key0.append(candidate) 


key1 = [] 
while len(key1) <10: 
    while True: 
        candidate = random.randint(lbound,rbound) 
        if candidate in key1: 
            continue 
        key1.append(candidate)

key2 = [] 
while len(key2) <10: 
    while True: 
        candidate = random.randint(20,29) 
        if candidate in key2: 
            continue 
        key2.append(candidate) 

'''

'''
Design a parking lot! Please write your code below

Goals (in order):
- Code design is scalable and flexible
- Working functions

Assumptions:
- The parking lot can hold motorcycles, cars and vans
- The parking lot has motorcycle spots, compact spots and regular spots
- A motorcycle can park in any spot
- A car can park in a single compact spot, or a regular spot
- A van can park, but it will take up 3 regular spots
- These are just a few assumptions. Feel free to ask your interviewer about more assumptions as needed

Here are a few methods that you should be able to run:
- Tell us how many spots are remaining 
- Tell us how many total spots are in the parking lot
- Tell us when the parking lot is full 
- Tell us when the parking lot is empty 
- Tell us how many spots are left for a given car type
- Tell us how many spots vans are taking up
'''


class ParkingLot(object):
    def __init__(self, mspots, cspots, rspots) -> None:
        self.omspots = mspots
        self.ocspots = cspots
        self.orspots = rspots

        self.mspots = [' ' for x in range(mspots)]
        self.cspots = [' ' for x in range(cspots)]
        self.rspots = [' ' for x in range(rspots)]

    def remaining_spots(self, type=None):
        if type == 'motorcycle':
            return self.mspots.count(' ') + self.cspots.count(' ') + self.rspots.count(' ')
        elif type == 'car':
            return self.cspots.count(' ') + self.rspots.count(' ')
        elif type == 'van':
            return self.rspots.count(' ') // 3
        else:
            return self.mspots.count(' ') + self.cspots.count(' ') + self.rspots.count(' ')

    @property
    def total_vans(self):
        return self.rspots.count('v') / 3

    @property
    def total_spots(self):
        return self.omspots + self.ocspots + self.orspots

    @property
    def is_full(self):
        if self.mspots == 0 and self.cspots == 0 and self.rspots == 0:
            return True

        return False

    @property
    def is_empty(self):
        if self.mspots == self.omspots and self.cspots == self.ocspots and self.rspots == self.orspots:
            return True

        return False


with ParkingLot(5, 10, 20) as pl:
    pass
