def is_isomorphic(s, t)
return false if s.length != t.length
s_hash = {}
t_hash = {}
s.each_char.with_index do |char, index|
s_hash[char] = t[index] if ! s_hash.key?(char)
t_hash[t[index]] = char if ! t_hash.key?(t[index])
return false if s_hash[char] != t[index] | | t_hash[t[index]] != char
end
true
end
