# @param {Integer[]} students
# @param {Integer[]} sandwiches
# @return {Integer}
def count_students(students, sandwiches)
  students_count = students.group_by(&:itself).transform_values(&:count)
  sandwiches_count = sandwiches.group_by(&:itself).transform_values(&:count)
  students_count.each do |key, value|
    if sandwiches_count[key].nil?
      return value
    end
    if value > sandwiches_count[key]
      return sandwiches_count[key]
    end
  end
  return 0
end