class Solution {
  public String makeGood(final String s) {
    final Stack<Character> stack = new Stack<>();
    for (final char c : s.toCharArray()) {
      if (!stack.isEmpty() && 32 == Math.abs(stack.peek() - c)) {
        stack.pop();
      } else {
        stack.push(c);
      }
    }
    final StringBuilder sb = new StringBuilder();
    while (!stack.isEmpty()) {
      sb.append(stack.pop());
    }
    return sb.reverse().toString();
  }
}
