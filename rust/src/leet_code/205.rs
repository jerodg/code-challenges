use std::collections::HashMap;

impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut s_hash: HashMap<char, char> = HashMap::new();
        let mut t_hash: HashMap<char, char> = HashMap::new();
        for (index, char) in s.chars().enumerate() {
            if !s_hash.contains_key(&char) {
                s_hash.insert(char, t.chars().nth(index).unwrap());
            }
            if !t_hash.contains_key(&t.chars().nth(index).unwrap()) {
                t_hash.insert(t.chars().nth(index).unwrap(), char);
            }
            if s_hash.get(&char).unwrap() != &t.chars().nth(index).unwrap() || t_hash.get(&t.chars().nth(index).unwrap()).unwrap() != &char {
                return false;
            }
        }
        true
    }
}
