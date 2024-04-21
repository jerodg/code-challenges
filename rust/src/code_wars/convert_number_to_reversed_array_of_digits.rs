fn digitize(num: u64) -> Vec<u8> {
    let num_str = num.to_string();
    let mut digit_list = Vec::new();
    for char in num_str.chars().rev() {
        digit_list.push(char.to_digit(10).unwrap() as u8);
    }
    digit_list
}