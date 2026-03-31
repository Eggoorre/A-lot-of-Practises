import xml.etree.ElementTree as ET
import json
import yaml


def to_format(func):
    '''
    decoratpr that changes format of return of function
    :param func: function fromat of which is changed
    :return: wrapper
    '''
    def wrapper(format_: str, *args, **kwargs):
        result = func(*args, **kwargs)

        match format_:
            case None:
                return json.dumps(
                    result,
                    ensure_ascii=False,
                    default=str
                )

            case 'YAML':
                return yaml.safe_dump(
                    result,
                    allow_unicode=True,
                    sort_keys=False
                )

            case 'XML':
                root = ET.Element('data')

                for item in result:
                    el = ET.SubElement(root, 'el')

                    if isinstance(item, dict):
                        for key, value in item.items():
                            child = ET.SubElement(el, key)
                            child.text = str(value)
                    else:
                        el.text = str(item)

                return ET.tostring(root, encoding='unicode')

            case _:
                raise ValueError("Unknown format")

    return wrapper


@to_format
def get_data() -> list:
    '''
    input data
    :return: data
    '''
    return [{"a": 1, "b": 2}, {"c": 3}]


if __name__ == '__main__':
    print(get_data(None))
    print(get_data("YAML"))
    print(get_data("XML"))
