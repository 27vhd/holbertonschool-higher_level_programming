#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Search and replace all occurrences of an element by another in a new list.

        Args:
            my_list (list): The initial list.
            search (int): The element to replace in the list.
            replace (int): The new element to replace the search element.
        Returns:
            A new list with all occurrences of search replaced by replace.
        """

    return [replace if i == search else i for i in my_list]
