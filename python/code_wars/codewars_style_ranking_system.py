"""CodeWars Style Ranking System.

This module implements a user ranking system similar to the one used by CodeWars.
It tracks a user's rank and progress through a custom ranking system with special rules.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""


class User:
    """A class representing a user in the CodeWars style ranking system.

    This class tracks a user's rank and progress. Users start at rank -8 and can
    progress to rank 8, with no rank 0. Progress is earned by completing activities,
    with the amount determined by the difference between the user's rank and the
    activity's rank.

    Attributes:
        _rank (int): The user's current rank, ranging from -8 to 8 (excluding 0).
        _progress (int): The user's current progress toward the next rank (0-99).
        valid_ranks (list[int]): Valid ranks in the system (-8 to -1 and 1 to 8).
    """

    def __init__(self) -> None:
        """Initialize a new user at the lowest rank with no progress."""
        self._rank = -8
        self._progress = 0
        self.valid_ranks = list(range(-8, 0)) + list(range(1, 9))

    @property
    def rank(self) -> int:
        """Get the user's current rank.

        Returns:
            int: The user's current rank.
        """
        return self._rank

    @property
    def progress(self) -> int:
        """Get the user's current progress.

        Returns:
            int: The user's current progress toward the next rank (0-99).
        """
        return self._progress

    def inc_progress(self, activity_rank: int) -> None:
        """Update the user's progress based on completing an activity.

        Progress earned depends on the difference between the user's rank and
        the activity's rank. Progress accumulates, and the user ranks up when
        progress reaches 100.

        Parameters:
            activity_rank (int): The rank of the completed activity.

        Raises:
            ValueError: If the activity rank is not a valid rank.

        Example:
            >>> user = User()
            >>> user.rank
            -8
            >>> user.inc_progress(-7)
            >>> user.progress
            10
        """
        # Validate activity rank
        if activity_rank not in self.valid_ranks:
            raise ValueError("Invalid rank value")

        # If already at max rank, do nothing
        if self._rank == 8:
            return

        # Calculate rank difference
        rank_diff = self._get_rank_difference(activity_rank)

        # Calculate progress points
        if rank_diff == 0:  # Same rank
            points = 3
        elif rank_diff == -1:  # One rank lower
            points = 1
        elif rank_diff <= -2:  # Two or more ranks lower
            points = 0
        else:  # Higher rank
            points = 10 * rank_diff * rank_diff

        # Update progress and handle rank upgrades
        self._update_progress(points)

    def _get_rank_difference(self, activity_rank: int) -> int:
        """Calculate the effective rank difference accounting for skipped zero rank.

        Converts ranks to continuous indices by mapping them to a zero-based scale,
        which allows for correct calculation of rank differences.

        Parameters:
            activity_rank (int): The rank of the completed activity.

        Returns:
            int: The effective difference between the activity rank and user rank.
        """
        # Convert ranks to continuous indices (skipping 0)
        current_idx = self._rank + 8 if self._rank < 0 else self._rank + 7
        activity_idx = activity_rank + 8 if activity_rank < 0 else activity_rank + 7

        return activity_idx - current_idx

    def _update_progress(self, points: int) -> None:
        """Update progress and handle rank upgrades.

        Adds points to progress and upgrades rank when progress reaches 100.
        Excess progress is carried over to the next rank.

        Parameters:
            points (int): Number of progress points to add.
        """
        self._progress += points

        while self._progress >= 100 and self._rank < 8:
            self._progress -= 100
            self._rank = self._get_next_rank()

        # Cap progress at 0 if max rank reached
        if self._rank == 8:
            self._progress = 0

    def _get_next_rank(self) -> int:
        """Return the next rank after the current one.

        Handles the special case where rank -1 is followed by rank 1 (skipping 0).

        Returns:
            int: The next rank in the progression.
        """
        if self._rank == -1:
            return 1

        return self._rank + 1