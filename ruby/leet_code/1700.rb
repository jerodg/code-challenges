# @param {Integer[]} students
# @param {Integer[]} sandwiches
# @return {Integer}
def count_students(students, sandwiches)
  students_queue = students.dup
  sandwiches_stack = sandwiches.dup

  while !sandwiches_stack.empty? && students_queue.include?(sandwiches_stack.first)
    if students_queue.first == sandwiches_stack.first
      students_queue.shift
      sandwiches_stack.shift
    else
      students_queue.rotate!
    end
  end

  students_queue.size
end