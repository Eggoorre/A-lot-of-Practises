import json


def main() -> None:
    '''
    main function reading file in json format and sorting
    it depending from second el
    :return: None
    '''
    info_input = input()

    info = json.loads(info_input)

    info.sort(key=lambda x: x[1], reverse=True)

    print(info)
