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
"""

import unittest
from copy import deepcopy

import pytest
from list_methods import (
    add_me_to_the_queue,
    add_me_with_my_friends,
    find_my_friend,
    how_many_namefellows,
    remove_the_last_person,
    remove_the_mean_person,
    sorted_names,
)


class ListMethodsTest(unittest.TestCase):
    """Test suite for the list methods implementation of Chaitana's Colossal Coaster project.

    This class contains test methods for all seven tasks in the project, with each task
    having one or more test methods to verify both correct output and proper list manipulation.
    """

    @pytest.mark.task(taskno=1)
    def test_add_me_to_the_queue(self) -> None:
        """Test that add_me_to_the_queue returns the correct queue after adding a person.

        Tests multiple variations of adding a person to either the express or normal queue
        based on their ticket type, and verifies the returned queue contains the expected values.
        """
        test_data = [
            ((["Tony", "Bruce"], ["RobotGuy", "WW"], 0, "HawkEye"), ["RobotGuy", "WW", "HawkEye"]),
            ((["Tony", "Bruce"], ["RobotGuy", "WW"], 1, "RichieRich"), ["Tony", "Bruce", "RichieRich"]),
            ((["Agatha", "Pepper", "Valkyrie"], ["Drax", "Nebula"], 1, "Okoye"), ["Agatha", "Pepper", "Valkyrie", "Okoye"]),
            ((["Agatha", "Pepper", "Valkyrie"], ["Drax", "Nebula"], 0, "Gamora"), ["Drax", "Nebula", "Gamora"]),
        ]

        for variant, (params, expected) in enumerate(test_data, start=1):
            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            express_queue, normal_queue, ticket_type, person_name = deepcopy(params)

            with self.subTest(f"variation #{variant}", params=params, expected=expected):
                actual_result = add_me_to_the_queue(*params)

                error_message = (
                    f"\nCalled add_me_to_the_queue{express_queue, normal_queue, ticket_type, person_name}.\n"
                    f"The function returned {actual_result},\n"
                    f" but the tests expected {expected} after {person_name} was added."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=1)
    def test_add_me_to_the_queue_validate_queue(self) -> None:
        """Test that add_me_to_the_queue modifies and returns the appropriate original queue.

        Verifies that the function not only returns the correct values but also modifies
        the original queue object (either express or normal) based on the ticket type.
        This ensures that object identity is maintained when returning the modified queue.
        """
        test_data = [
            ((["Tony", "Bruce"], ["RobotGuy", "WW"], 0, "HawkEye"), ["RobotGuy", "WW", "HawkEye"]),
            ((["Tony", "Bruce"], ["RobotGuy", "WW"], 1, "RichieRich"), ["Tony", "Bruce", "RichieRich"]),
            ((["Agatha", "Pepper", "Valkyrie"], ["Drax", "Nebula"], 1, "Okoye"), ["Agatha", "Pepper", "Valkyrie", "Okoye"]),
            ((["Agatha", "Pepper", "Valkyrie"], ["Drax", "Nebula"], 0, "Gamora"), ["Drax", "Nebula", "Gamora"]),
        ]

        for variant, (params, expected) in enumerate(test_data, start=1):
            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            express_queue, normal_queue, ticket_type, person_name = deepcopy(params)
            express, normal, ticket, name = params

            with self.subTest(f"variation #{variant}", express=express, normal=normal, ticket=ticket, name=name, expected=expected):
                actual_result = add_me_to_the_queue(express, normal, ticket, name)

                if type == 1:
                    error_message = (
                        f"\nCalled add_me_to_the_queue{express_queue, normal_queue, ticket_type, person_name}.\n"
                        f"The queue == {express}, but the tests expected\n"
                        f"queue == {expected} after {person_name} was added."
                    )

                    assert actual_result is express, error_message

                if type == 0:
                    error_message = (
                        f"\nCalled add_me_to_the_queue{express_queue, normal_queue, ticket_type, person_name}.\n"
                        f"The queue == {normal}, but the tests expected \n"
                        f"queue == {expected} after {person_name} was added."
                    )

                    assert actual_result is normal, error_message

    @pytest.mark.task(taskno=2)
    def test_find_my_friend(self) -> None:
        """Test that find_my_friend returns the correct index of a person's name in the queue.

        Tests various scenarios where a name is searched for in different positions within
        the queue, verifying that the function correctly returns the index of the name.
        """
        test_data = [
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Natasha"),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Steve"),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Rocket"),
        ]

        result_data = (0, 1, 4)

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", params=params, expected=expected):
                actual_result = find_my_friend(*params)
                error_message = (
                    f"\nCalled find_my_friend{params}.\n"
                    f"The function returned {actual_result}, but\n"
                    f"the tests expected {expected} when looking for\n"
                    f"{params[-1]} in the queue."
                )

                assert actual_result is expected, error_message

    @pytest.mark.task(taskno=3)
    def test_add_me_with_my_friends(self) -> None:
        """Test that add_me_with_my_friends correctly inserts a name at a specific index.

        Tests inserting a name at different positions (beginning, middle, end) of the queue
        and verifies that the function returns the queue with the name inserted at the proper position.
        """
        test_data = [
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 0, "Bucky"),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 1, "Bucky"),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 5, "Bucky"),
        ]

        result_data = [
            ["Bucky", "Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
            ["Natasha", "Bucky", "Steve", "Tchalla", "Wanda", "Rocket"],
            ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket", "Bucky"],
        ]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            queue, index, person_name = deepcopy(params)

            with self.subTest(f"variation #{variant}", params=params, expected=expected):
                actual_result = add_me_with_my_friends(*params)
                error_message = (
                    f"\nCalled add_me_with_my_friends{queue, index, person_name}.\n"
                    f"The function returned {actual_result}, but\n"
                    f"the tests expected {expected} when adding\n"
                    f"{person_name} to position {index} in the queue."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=3)
    def test_add_me_with_my_friends_validate_queue(self) -> None:
        """Test that add_me_with_my_friends modifies and returns the original queue.

        Verifies that the function not only returns the correct values but also modifies
        the original queue object, ensuring that object identity is maintained when returning
        the modified queue.
        """
        test_data = [
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 0, "Bucky"),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 1, "Bucky"),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 5, "Bucky"),
        ]

        result_data = [
            ["Bucky", "Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
            ["Natasha", "Bucky", "Steve", "Tchalla", "Wanda", "Rocket"],
            ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket", "Bucky"],
        ]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            start_queue, add_index, person_name = deepcopy(params)
            queue, _, _ = params

            with self.subTest(f"variation #{variant}", params=params, expected=expected):
                actual_result = add_me_with_my_friends(*params)
                error_message = (
                    f"\nCalled add_me_with_my_friends{start_queue, add_index, person_name}.\n"
                    f"The function returned {actual_result},\n"
                    "but the original queue was unmodified. The tests expected the \n"
                    f'*original* queue to be modified by adding "{person_name}".'
                )

                assert actual_result is queue, error_message

    @pytest.mark.task(taskno=4)
    def test_remove_the_mean_person(self) -> None:
        """Test that remove_the_mean_person correctly removes a specific name from the queue.

        Tests removing a name from different positions in the queue and verifies that
        the function returns the queue with that name removed.
        """
        test_data = [
            (["Natasha", "Steve", "Ultron", "Wanda", "Rocket"], "Ultron"),
            (["Natasha", "Steve", "Wanda", "Rocket", "Ultron"], "Rocket"),
            (["Ultron", "Natasha", "Steve", "Wanda", "Rocket"], "Steve"),
        ]

        result_data = [
            ["Natasha", "Steve", "Wanda", "Rocket"],
            ["Natasha", "Steve", "Wanda", "Ultron"],
            ["Ultron", "Natasha", "Wanda", "Rocket"],
        ]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            start_queue, person_name = deepcopy(params)

            with self.subTest(f"variation #{variant}", params=params, expected=expected):
                actual_result = remove_the_mean_person(*params)
                error_message = (
                    f"\nCalled remove_the_mean_person{start_queue, person_name}.\n"
                    f"The function returned {actual_result}, but\n"
                    f"the tests expected {expected} when removing\n"
                    f"{person_name} from the queue."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=4)
    def test_remove_the_mean_person_validate_queue(self) -> None:
        """Test that remove_the_mean_person modifies and returns the original queue.

        Verifies that the function not only returns the correct values but also modifies
        the original queue object, ensuring that object identity is maintained when returning
        the modified queue.
        """
        test_data = [
            (["Natasha", "Steve", "Ultron", "Wanda", "Rocket"], "Ultron"),
            (["Natasha", "Steve", "Wanda", "Rocket", "Ultron"], "Rocket"),
            (["Ultron", "Natasha", "Steve", "Wanda", "Rocket"], "Steve"),
        ]

        result_data = [
            ["Natasha", "Steve", "Wanda", "Rocket"],
            ["Natasha", "Steve", "Wanda", "Ultron"],
            ["Ultron", "Natasha", "Wanda", "Rocket"],
        ]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            start_queue, person_name = deepcopy(params)
            queue, _ = params

            with self.subTest(f"variation #{variant}", params=params, expected=expected):
                actual_result = remove_the_mean_person(*params)
                error_message = (
                    f"\nCalled remove_the_mean_person{start_queue, person_name}.\n"
                    f"The function returned {actual_result}, queue == {queue}.\n"
                    f"But the tests expected queue == {expected} when removing\n"
                    f"{person_name}."
                )

                assert actual_result is queue, error_message

    @pytest.mark.task(taskno=5)
    def test_how_many_namefellows(self) -> None:
        """Test that how_many_namefellows correctly counts occurrences of a name in the queue.

        Tests scenarios with zero, one, or multiple occurrences of a name in the queue
        and verifies that the function returns the correct count.
        """
        test_data = [
            (["Natasha", "Steve", "Ultron", "Natasha", "Rocket"], "Bucky"),
            (["Natasha", "Steve", "Ultron", "Rocket"], "Natasha"),
            (["Natasha", "Steve", "Ultron", "Natasha", "Rocket"], "Natasha"),
        ]

        result_data = (0, 1, 2)

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", params=params, expected=expected):
                actual_result = how_many_namefellows(*params)

                error_message = (
                    f"Called how_many_namefellows{params}. "
                    f"The function returned {actual_result}, but "
                    f"The tests expected {expected} when counting "
                    f"namefellows in the queue for {params[-1]}."
                )

                assert actual_result is expected, error_message

    @pytest.mark.task(taskno=6)
    def test_remove_the_last_person(self) -> None:
        """Test that remove_the_last_person removes and returns the last person from the queue.

        Verifies that the function correctly removes the last person from the queue,
        returns their name, and updates the queue appropriately.
        """
        test_data = [
            (["Natasha", "Steve", "Ultron", "Natasha", "Rocket"], ["Natasha", "Steve", "Ultron", "Natasha"], "Rocket"),
            (["Wanda", "Natasha", "Steve", "Rocket", "Ultron"], ["Wanda", "Natasha", "Steve", "Rocket"], "Ultron"),
            (["Steve", "Wanda", "Rocket", "Ultron", "Natasha"], ["Steve", "Wanda", "Rocket", "Ultron"], "Natasha"),
        ]
        for variant, (queue, modified, expected) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", queue=queue, modified=modified, expected=expected):
                # Deepcopy() is needed here because the task expects the input lists to be mutated.
                # That mutation wrecks havoc with the verification and error messaging.
                unmodified_queue = deepcopy(queue)
                expected_result = expected
                actual_result = remove_the_last_person(queue)
                expected_queue = modified

                error_message = (
                    f"\nCalled remove_the_last_person({unmodified_queue}).\n"
                    f'The function was expected to remove and return the name "{expected_result}" '
                    f"and change the queue to {expected_queue},\n"
                    f'but the name "{actual_result}" was returned and the queue == {queue}.'
                )

                assert (actual_result, queue) == (expected_result, expected_queue), error_message

    @pytest.mark.task(taskno=7)
    def test_sorted_names(self) -> None:
        """Test that sorted_names returns a sorted copy of the queue.

        Verifies that the function returns a new list with the names from the queue
        sorted in alphabetical order.
        """
        test_data = (
            (["Steve", "Ultron", "Natasha", "Rocket"], ["Natasha", "Rocket", "Steve", "Ultron"]),
            (["Agatha", "Pepper", "Valkyrie", "Drax", "Nebula"], ["Agatha", "Drax", "Nebula", "Pepper", "Valkyrie"]),
            (["Gamora", "Loki", "Tony", "Peggy", "Okoye"], ["Gamora", "Loki", "Okoye", "Peggy", "Tony"]),
        )

        for variant, (queue, expected) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", queue=queue, expected=expected):
                actual_result = sorted_names(queue)
                expected_result = expected

            error_message = (
                f"\nCalled sorted_names({queue}).\nThe function returned {actual_result}, but \nthe tests expect {expected_result}."
            )

            assert actual_result == expected_result, error_message

    @pytest.mark.task(taskno=7)
    def test_sorted_names_validate_queue(self) -> None:
        """Test that sorted_names does not modify the original queue.

        Verifies that the function returns a new list with the sorted names and does not
        modify the original queue, ensuring it remains unchanged after the function call.
        """
        test_data = (
            (["Steve", "Ultron", "Natasha", "Rocket"], ["Natasha", "Rocket", "Steve", "Ultron"]),
            (["Agatha", "Pepper", "Valkyrie", "Drax", "Nebula"], ["Agatha", "Drax", "Nebula", "Pepper", "Valkyrie"]),
            (["Gamora", "Loki", "Tony", "Peggy", "Okoye"], ["Gamora", "Loki", "Okoye", "Peggy", "Tony"]),
        )

        for variant, (queue, expected) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", queue=queue, expected=expected):
                # Deepcopy() is needed here because the input lists might be mutated.
                # That mutation wrecks havoc with the verification and error messaging.
                original_queue = deepcopy(queue)
                actual_result = sorted_names(queue)
                expected_result = expected

            error_message = (
                f"\nCalled sorted_names({original_queue}).\n"
                f"The function returned {actual_result}, \n"
                f"with a queue == {queue}.\n"
                f"The tests expect {expected_result}, \n"
                f"with a queue == {original_queue}."
            )

            assert actual_result is not queue, error_message
