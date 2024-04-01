def digitize(n)
  n.to_s.split('').reverse.map(&:to_i)
end