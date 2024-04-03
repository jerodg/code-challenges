# frozen_string_literal: true

def skip_animals(animals, skip)
  result = []
  animals.each_with_index do |animal, index|
    result << "#{index}:#{animal}" if index >= skip
  end
  result
end