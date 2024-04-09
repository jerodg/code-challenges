# @param {Integer[]} tickets
# @param {Integer} k
# @return {Integer}
def time_required_to_buy(tickets, k)
  result = 0
  (0...tickets.length).each do |i|
    n = tickets[k]
    c = tickets[i]

    result += [i > k ? n - 1 : n, c].min
  end

  result
end