"""Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

Functions to manage and organize queues at Chaitana's roller coaster.
"""


def add_me_to_the_queue(express_queue: list[str], normal_queue: list[str], ticket_type: int, person_name: str) -> list[str]:
    """Add a person to the 'express' or 'normal' queue depending on the ticket type.

    Parameters:
        express_queue (list[str]): List of names in the express queue.
        normal_queue (list[str]): List of names in the normal queue.
        ticket_type (int): Type of ticket. 1 = express, 0 = normal.
        person_name (str): Name of person to add to a queue.

    Returns:
        list[str]: The updated queue the name was added to.

    Example:
        >>> add_me_to_the_queue(["Tony", "Bruce"], ["RobotGuy", "WW"], 1, "RichieRich")
        ['Tony', 'Bruce', 'RichieRich']
    """
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue

    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue: list[str], friend_name: str) -> int:
    """Search the queue for a name and return their queue position (index).

    Parameters:
        queue (list[str]): List of names in the queue.
        friend_name (str): Name of friend to find.

    Returns:
        int: Index at which the friend's name was found.

    Example:
        >>> find_my_friend(["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Steve")
        1
    """
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    """Insert a person's name at a specific index of the queue.

    Parameters:
        queue (list[str]): List of names in the queue.
        index (int): The index at which to add the new name.
        person_name (str): The name to add.

    Returns:
        list[str]: Queue updated with new name.

    Example:
        >>> add_me_with_my_friends(["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 1, "Bucky")
        ['Natasha', 'Bucky', 'Steve', 'Tchalla', 'Wanda', 'Rocket']
    """
    queue.insert(index, person_name)

    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    """Remove a specific person from the queue by name.

    Parameters:
        queue (list[str]): List of names in the queue.
        person_name (str): Name of person to remove.

    Returns:
        list[str]: Queue updated with the person's name removed.

    Example:
        >>> remove_the_mean_person(["Natasha", "Steve", "Ultron", "Wanda", "Rocket"], "Ultron")
        ['Natasha', 'Steve', 'Wanda', 'Rocket']
    """
    queue.remove(person_name)

    return queue


def how_many_namefellows(queue: list[str], person_name: str) -> int:
    """Count how many times the provided name appears in the queue.

    Parameters:
        queue (list[str]): List of names in the queue.
        person_name (str): Name to count occurrences of.

    Returns:
        int: The number of times the name appears in the queue.

    Example:
        >>> how_many_namefellows(["Natasha", "Steve", "Ultron", "Natasha", "Rocket"], "Natasha")
        2
    """
    return queue.count(person_name)


def remove_the_last_person(queue: list[str]) -> str:
    """Remove the person in the last index from the queue and return their name.

    Parameters:
        queue (list[str]): List of names in the queue.

    Returns:
        str: Name that has been removed from the end of the queue.

    Example:
        >>> remove_the_last_person(["Natasha", "Steve", "Ultron", "Rocket"])
        'Rocket'
    """
    return queue.pop()


def sorted_names(queue: list[str]) -> list[str]:
    """Sort the names in the queue in alphabetical order and return the result.

    The original queue remains unchanged as this function returns a new list.

    Parameters:
        queue (list[str]): List of names in the queue.

    Returns:
        list[str]: A new list containing queue names in alphabetical order.

    Example:
        >>> sorted_names(["Steve", "Ultron", "Natasha", "Rocket"])
        ['Natasha', 'Rocket', 'Steve', 'Ultron']
    """
    return sorted(queue)
