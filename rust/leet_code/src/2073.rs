use std::collections::BinaryHeap;

impl Solution {
    pub fn time_required_to_buy(tickets: Vec<i32>, k: i32) -> i32 {
        let mut heap = BinaryHeap::from(tickets);
        let mut time = 0;
        let mut tickets_bought = 0;

        while tickets_bought < k && !heap.is_empty() {
            let current_ticket = heap.pop().unwrap();
            let new_ticket_value = current_ticket - 1;

            // Handle tickets with value 1
            if new_ticket_value > 0 {
                heap.push(new_ticket_value);
            }

            // Update time and bought tickets
            time += current_ticket; // Increment time by the value of the ticket
            tickets_bought += 1;
        }
        time
    }
}

// fixme: incorrect output
