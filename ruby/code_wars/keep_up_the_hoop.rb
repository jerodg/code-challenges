# The `hoop_count` method takes an integer `n` as an argument.
# This method is used to determine the level of a hula hoop player.
#
# @param n [Integer] The number of hoops a player can hoop.
# @return [String] A motivational message based on the player's skill level.
def hoop_count n
  # If the player can hoop 10 or more hoops, they are considered skilled and are encouraged to learn tricks.
  # Otherwise, they are encouraged to keep practicing.
  n >= 10 ? "Great, now move on to tricks" : "Keep at it until you get it"
end