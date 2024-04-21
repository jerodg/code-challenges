impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let (mut lo, mut hi) = (0, 0);
        for c in s.chars() {
            match c {
                '(' => {
                    lo += 1;
                    hi += 1;
                }
                ')' => {
                    if lo > 0 {
                        lo -= 1;
                    }
                    hi -= 1;
                }
                _ => {
                    if lo > 0 {
                        lo -= 1;
                    }
                    hi += 1;
                }
            }
            if hi < 0 {
                return false;
            }
        }
        lo == 0
    }
}
