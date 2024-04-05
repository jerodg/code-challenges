impl Solution {
    pub fn make_good(s: String) -> String {
        let mut stack = Vec::new();
        for c in s.chars() {
            if stack.is_empty() {
                stack.push(c);
            } else {
                let top = stack.last().unwrap();
                if top.is_lowercase() && top.to_ascii_uppercase() == c {
                    stack.pop();
                } else if top.is_uppercase() && top.to_ascii_lowercase() == c {
                    stack.pop();
                } else {
                    stack.push(c);
                }
            }
        }
        stack.into_iter().collect()
    }
}
