# frozen_string_literal: true

def group_by_marks(marks, pass_marks)
  # your code here
  marks.group_by { |key, value| value >= pass_marks ? "Passed" : "Failed" }
end