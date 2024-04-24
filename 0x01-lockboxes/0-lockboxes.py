#!/usr/bin/python3
"""
Module for lockboxes
"""


def look_next_opened_box(opened_boxes):
    """Look for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Checks if all boxes can be opened
    Args:
        boxes (list): List which contains all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    aux = {}
    while True:
        if len(aux) == 0:
            aux[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = look_next_opened_box(aux)
        if keys:
            for key in keys:
                try:
                    if aux.get(key) and aux.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    aux[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        elif len(aux) == len(boxes):
            break
        else:
            return False

    return len(aux) == len(boxes)


def main():
    """Entry pointed"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
