from fibonacci_heap import FibonacciHeap


def test_f_heap():
    x = FibonacciHeap()
    x.insert_node(5)
    x.insert_node(15)
    x.insert_node(11)

    result1 = x.get_min()
    result2 = x.extract_min()
    result3 = x.get_min()

    expected1 = 5
    expected2 = 5
    expected3 = 11

    assert result1 == expected1
    assert result2 == expected2
    assert result3 == expected3


def test_f_heap_large():
    f_heap = FibonacciHeap()
    test_data = [13, 47, 99, 24, 63, 52, 67, 55, 43, 7, 19, 78, 35, 94, 46, 70]
    for i in test_data:
        f_heap.insert_node(i)

    result = []
    while f_heap.count > 0:
        result.append(f_heap.extract_min())

    assert result == sorted(test_data)


def test_f_heap_decimals():
    f_heap = FibonacciHeap()
    test_data = [43.57, 23.73, 812.34, 42, 83, 72.01, 38.59, 50, 63, 0.45, 9.36]
    for i in test_data:
        f_heap.insert_node(i)

    result = []
    while f_heap.count > 0:
        result.append(f_heap.extract_min())

    assert result == sorted(test_data)


def test_f_heap_negative():
    f_heap = FibonacciHeap()
    test_data = [65, 42, -12, 57, -6, -49, -84, 9, 14, 73, -95]
    for i in test_data:
        f_heap.insert_node(i)

    result = []
    while f_heap.count > 0:
        result.append(f_heap.extract_min())

    assert result == sorted(test_data)


def test_f_heap_duplicates():
    f_heap = FibonacciHeap()
    test_data = [6, 9, 17, 9, 17, 9, 45, 64, 93, 64, 6, 9, 50, 7, 12]
    for i in test_data:
        f_heap.insert_node(i)

    result = []
    while f_heap.count > 0:
        result.append(f_heap.extract_min())

    assert result == sorted(test_data)


def test_f_heap_comprehensive():
    f_heap = FibonacciHeap()
    test_data = [-43.27, 54, 79.33, -6.45, -42.99, -14.64, 17.23, -17.23, 17.23, -6.45, -79.33, -42.99, -88, 37, 52.04]
    for i in test_data:
        f_heap.insert_node(i)

    result = []
    while f_heap.count > 0:
        result.append(f_heap.extract_min())

    assert result == sorted(test_data)
