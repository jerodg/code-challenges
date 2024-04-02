def identify_class(obj)
  # write your case control structure here
  case obj
  when Hacker, Submission, TestCase, Contest
    puts "It's a #{obj.class}!"
  else
    puts "It's an unknown model"
  end
end