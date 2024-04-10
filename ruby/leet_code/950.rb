# @param {Integer[]} deck
# @return {Integer[]}
def self.deck_revealed_increasing(deck)
  n = deck.size
  deck.sort!
  q = Array.new(n) { |i| i }
  ans = Array.new(n)
  (0...n).each do |i|
    idx = q.shift
    q.push(q.shift) unless q.empty?
    ans[idx] = deck[i]
  end
  ans
end
