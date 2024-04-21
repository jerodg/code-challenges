func digitize(_ num: Int) -> [Int] {
    var number = num
    var digits: [Int] = []

    while number >= 0 {
        let digit = number % 10
        digits.append(digit)
        number /= 10
        if number == 0 {
            break
        }
    }

    return digits
}
