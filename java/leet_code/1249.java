class Solution {
  public String minRemoveToMakeValid(String s) {
    Stack<Integer> stack = new Stack<>();
    Set<Integer> remove = new HashSet<>();
    for (int i = 0; i < s.length(); i++) {
      if (s.charAt(i) == '(') {
        stack.add(i);
      } else if (s.charAt(i) == ')') {
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
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < s.length(); i++) {
      if (!remove.contains(i)) {
        sb.append(s.charAt(i));
      }
    }
    return sb.toString();
  }
}
