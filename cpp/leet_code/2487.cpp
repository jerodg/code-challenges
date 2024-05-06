#pragma GCC optimize("O3", "unroll-loops")

#include <ios> // Provides the core input/output library

// ListNode is a struct that represents a node in a singly linked list.
// Each node contains an integer value and a pointer to the next node in the
// list.
struct ListNode {
  int val;        // The integer value stored in this node
  ListNode *next; // Pointer to the next node in the list

  // Default constructor initializes the node with a value of 0 and next pointer
  // as nullptr
  ListNode() : val(0), next(nullptr) {}

  // Constructor initializes the node with a given value and next pointer as
  // nullptr
  explicit ListNode(int x) : val(x), next(nullptr) {}

  // Constructor initializes the node with a given value and a given next node
  ListNode(const int x, ListNode *next) : val(x), next(next) {}
};

// Solution class encapsulates the method to solve the problem
class Solution {
public:
  // Method to remove nodes from a linked list based on a specific condition
  // Parameters:
  // - head: a pointer to the head node of the linked list
  // Returns: a pointer to the head node of the modified linked list
  static ListNode *removeNodes(ListNode *head) {
    std::ios_base::sync_with_stdio(
        false); // Speed up I/O operations by untieing cin from cout

    // If the list is empty, return the empty list
    if (head == nullptr)
      return head;

    // Recursively remove nodes from the rest of the list
    head->next = removeNodes(head->next);

    // If the list has only one node, return the single-node list
    if (head->next == nullptr)
      return head;

    // If the next node's value is greater than the current node's value, remove
    // the current node
    if (head->next->val > head->val)
      return head->next;

    // Otherwise, keep the current node
    return head;
  }
};
