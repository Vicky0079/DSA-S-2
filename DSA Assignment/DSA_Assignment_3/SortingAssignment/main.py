import random
import time

from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


sizes = [1000, 5000, 10000]

output_file = open("output.txt", "w")


def test_sorting(name, sort_function, data):
    start = time.time()

    if name == "Quick Sort":
        sort_function(data)
    else:
        sort_function(data)

    end = time.time()

    total_time = end - start

    result = f"{name}: {total_time:.6f} seconds"
    print(result)
    output_file.write(result + "\n")


for size in sizes:

    print(f"\nDataset Size: {size}")
    output_file.write(f"\nDataset Size: {size}\n")

    random_data = [random.randint(1, 10000) for _ in range(size)]

    sorted_data = sorted(random_data)

    reverse_data = sorted(random_data, reverse=True)

    datasets = {
        "Random Data": random_data,
        "Sorted Data": sorted_data,
        "Reverse Sorted Data": reverse_data
    }

    for dataset_name, dataset in datasets.items():

        print(f"\n{dataset_name}")
        output_file.write(f"\n{dataset_name}\n")

        test_sorting("Insertion Sort", insertion_sort, dataset.copy())
        test_sorting("Merge Sort", merge_sort, dataset.copy())
        test_sorting("Quick Sort", quick_sort, dataset.copy())


output_file.close()

print("\nResults saved in output.txt")