def eq_sum_list(unprocessed, first=(), second=()):
    if len(unprocessed) == 0:
        if sum(first) == sum(second):
            print(first, second)

        return

    item = unprocessed[0]
    eq_sum_list(unprocessed[1:], first + (item,), second)
    eq_sum_list(unprocessed[1:], first, second + (item,))


def eq_sum_list_second(unprocessed, first=[], second=[]):
    if len(unprocessed) == 0:
        if sum(first) == sum(second):
            print(first, second)

        return

    item = unprocessed[0]

    first.append(item)
    eq_sum_list_second(unprocessed[1:], first, second)
    first.pop()

    second.append(item)
    eq_sum_list_second(unprocessed[1:], first, second)
    second.pop()


def eq_sum_list_third(unprocessed, index=0, first=[], second=[]):
    if len(unprocessed) == index:
        if sum(first) == sum(second):
            print(first, second)

        return

    item = unprocessed[index]

    first.append(item)
    eq_sum_list_third(unprocessed, index+1, first, second)
    first.pop()

    second.append(item)
    eq_sum_list_third(unprocessed, index+1, first, second)
    second.pop()


eq_sum_list_third((1, 2, 3))