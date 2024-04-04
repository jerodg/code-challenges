def digitize(n: Long): Seq[Int] = {
  var number = n
  var digits: Seq[Int] = Seq()

  while (number >= 0) {
    val digit = (number % 10).toInt
    digits = digits :+ digit
    number /= 10
    if (number == 0) {
      return digits
    }
  }
  digits
}