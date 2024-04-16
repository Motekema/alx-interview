#!/usr/bin/python3
"""
Module for lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Args:
        boxes (list): A list of lists containing the keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or len(boxes) == 1:
        return True

    # Initialize a set to store the keys
    keys = set(boxes[0])

    # Initialize a set to store the opened boxes
    opened_boxes = {0}

    # Initialize a queue to store the indices of boxes to be checked
    queue = [0]

    # Iterate through the queue
    while queue:
        # Get the index of the box to be checked
        box_index = queue.pop(0)

        # Get the keys from the current box
        current_keys = boxes[box_index]

        # Add the keys to the set of keys
        keys.update(current_keys)

        # Add the index of the box to the set of opened boxes
        opened_boxes.add(box_index)

        # Iterate through the keys in the current box
        for key in current_keys:
            # Check if the key opens a new box and if the box is not already opened
            if key < len(boxes) and key not in opened_boxes:
                # Add the index of the new box to the queue
                queue.append(key)

    # Check if all boxes can be opened
    return len(opened_boxes) == len(boxes)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
