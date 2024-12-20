#Stalin Sort

import argparse

def stalin_sort(nums):
    """
    perform stalin sort on a list of numbers
    only keeps elements greater than or equal to the previous element
    """
    new_nums = [None for i in range(len(nums))]
    new_nums[0] = nums[0]
    pointer = 1
    for i in range(1,len(nums)):
        if nums[i] < new_nums[pointer-1]:
            continue
        new_nums[pointer] = nums[i]
        pointer += 1
    return new_nums[0:pointer]


def main():
    """
    for running stalin sort as a script
    parses command-line arguments and sorts the input list
    what does this mean tbh?^
    """
    parser = argparse.ArgumentParser(description="perform stalin sort on a list of numbers")
    parser.add_argument("nums", nargs="+", type=int, help="a list of integers to sort.")
    args = parser.parse_args()

    sorted_nums = stalin_sort(args.nums)
    print("stalined list:", sorted_nums)

#if the script is executed directly, run the main() function
if __name__ == "__main__":
    main()
