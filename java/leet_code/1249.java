class Solution {
  public String minRemoveToMakeValid(final String s) {
    final Stack<Integer> stack = new Stack<>();
    final Set<Integer> remove = new HashSet<>();
    for (int i = 0; i < s.length(); i++) {
      if ('(' == s.charAt(i)) {
        stack.add(i);
      } else if (')' == s.charAt(i)) {
        if (stack.isEmpty()) {
          remove.add(i);
        } else {
          stack.pop();
        }
      }
    }
    while (!stack.isEmpty()) {
      remove.add(stack.pop());
    }
    final StringBuilder sb = new StringBuilder();
    for (int i = 0; i < s.length(); i++) {
      if (!remove.contains(i)) {
        sb.append(s.charAt(i));
      }
    }
    return sb.toString();
  }
}
