'''
An airline company maintains a list of ticket prices in a sorted array.
Given a target price, implement a binary search algorithm to determine if the price exists in the list.
prices :Sorted list of integers
p:integer(target price)
'''


def binary_search(prices,p):
    low = 0
    high = len(prices) - 1

    while low <= high:
        mid = (low + high) // 2

        if prices[mid] == p:
            print("Price exists in the list")
            return True
        elif prices[mid] < p:
            low = mid + 1
        else:
            high = mid - 1

    print("Price does not exist in the list")
    return False

ticket_price = [100, 150, 200, 250, 300, 350, 400]
target_pice = 250
binary_search(ticket_price, target_pice)
target_price = 275
binary_search(ticket_price, target_price)