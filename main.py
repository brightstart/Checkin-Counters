# method for running heapify process on list A (1-D Array of int values)

def min_heapify_1d(arr, index):
    left = left_child(index)
    right = right_child(index)
    if left < len(arr) and arr[left] < arr[index]:
        smallest = left
    else:
        smallest = index
    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]

        min_heapify_1d(arr, smallest)

    # method for running heapify process on list A (Array of tuples)


def min_heapify_tuple(arr, index):
    left = left_child(index)
    right = right_child(index)
    if left < len(arr) and arr[left][0] < arr[index][0]:  # sorting based on start_time
        smallest = left
    else:
        smallest = index

    if right < len(arr) and arr[right][0] < arr[smallest][0]:
        smallest = right
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]

        min_heapify_tuple(arr, smallest)


def left_child(k):
    return 2 * k


def right_child(k):
    return 2 * k + 1


# copied function
def build_min_heap(arr):
    n = int((len(arr) // 2) - 1)
    for k in range(n, -1, -1):
        min_heapify_tuple(arr, k)


# opening the file in read mode
input_stream = open("inputPS10.txt", "r")
# reading the file line by line
data = input_stream.read()
data_into_list = data.split("\n")
err = None
customers = []
try:
    for i in data_into_list:
        time_taken = i.lstrip("[").rstrip("]").split(",")  # process data for use
        if int(time_taken[0]) < 0:
            raise Exception("Unexpected Data: Negative data was not allowed as per the problem statement")
        customers.append(
            (int(time_taken[0]), int(time_taken[0]) + int(time_taken[1])))
        # time taken from the start time to check out is mentioned in problem as checkout time
        # we have slightly changed the definition for checkout time as the present time when the person checks out.
    input_stream.close()
except ValueError:
    err = "Unexpected Data: Anomaly. Does the data contain blanks or non-numerics?"
except Exception as e:
    err = str(e)
build_min_heap(customers)

customers_sorted = []
while len(customers) > 0:
    customers_sorted.append(customers[0])
    customers[0] = customers[len(customers) - 1]
    del customers[-1]
    min_heapify_tuple(customers, 0)

priority_queue = [customers_sorted[0][1]]
counter = 1
n = len(customers_sorted)

for i in range(1, n):
    if priority_queue[0] >= customers_sorted[i][0]:
        counter = counter + 1
    else:
        priority_queue[0] = priority_queue[len(priority_queue) - 1]
        del priority_queue[-1]
        if len(priority_queue) > 0:
            min_heapify_1d(priority_queue, 0)

    element = customers_sorted[i][1]
    priority_queue.append(element)
    current_index = len(priority_queue) - 1

    while priority_queue[current_index] < priority_queue[(current_index) // 2]:
        priority_queue[current_index], priority_queue[(current_index) // 2] = priority_queue[(current_index) // 2], \
                                                                              priority_queue[current_index]
        current_index = (current_index) // 2

with open('outputPS10.txt', 'w') as f:
    if err:
        f.write(err)
    else:
        f.write("Minimum Checkout counters required: " + str(counter))

f.close()
