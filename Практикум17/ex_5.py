def count_family(tree: dict, name: str) -> int:
    '''
    recursive function counting amount of family members
    :param tree: dict of family members, father - key,
    child - item
    :param name: name of relative
    :return: num of relatives
    '''
    if name not in tree:
        return 0

    total = 0
    for child in tree[name]:
        total += count_family(tree, child) + 1

    return total


def main() -> None:
    '''
    main function
    :return: None
    '''
    num = int(input())
    tree = {}

    for _ in range(num):
        parent, child = input().split()
        if parent not in tree:
            tree[parent] = []

        tree[parent].append(child)

    target_mem = input()

    print(count_family(tree, target_mem))


if __name__ == '__main__':
    main()


