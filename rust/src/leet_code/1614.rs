impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let mut max_depth = 0;
        let mut depth = 0;
        for c in s.chars() {
            match c {
                '(' => {
                    depth += 1;
                    max_depth = max_depth.max(depth);
                }
                ')' => {
                    depth -= 1;
                }
                _ => (),
            }
        }
        max_depth
    }
}
