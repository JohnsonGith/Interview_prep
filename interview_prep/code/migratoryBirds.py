# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.

"""
    Finds the most frequent type of bird in a list representing bird types.

    Args:
        arr (list): A list of integers representing bird types.

    Returns:
        int: The type of bird that appears most frequently in the list.
    """
# Create a dictionary that store the number of times each bird appears in the list.
import array


count = {}
def migratoryBirds(arr):
    count = {}
    for i in arr:
        if i in count:
            # Increment count for the current bird type
            count[i] += 1
        else:
            count[i] = 1

    # Find the type of bird that appears most frequently in the list
    max_count = max(count.values())
    most_frequent_bird = None
    for bird_type, count in count.items():
        if count == max_count:
            most_frequent_bird = int(bird_type)

    return most_frequent_bird
