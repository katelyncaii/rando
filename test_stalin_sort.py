#test cases

from stalin_sort import stalin_sort

def run_tests():
    h = [1,2,3,4,5]
    stalined_h = stalin_sort(h)
    assert stalined_h == h

    i = [1,2,4,3,5]
    stalined_i = stalin_sort(i)
    assert stalined_i == [1,2,4,5]

    j = [5,1,2,3,4]
    stalined_j = stalin_sort(j)
    assert stalined_j == [5]

    k = [3,1,2,6,5,9,8]
    stalined_k = stalin_sort(k)
    assert stalined_k == [3,6,9]

    print("all test cases passed!")

if __name__ == "__main__":
    run_tests()