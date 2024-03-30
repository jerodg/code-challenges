object Kata {
    fun digitize(n: Long): IntArray {
        val str = n.toString().reversed()
        val result = IntArray(str.length)
        for (i in str.indices) {
            result[i] = Character.getNumericValue(str[i])
        }
        return result
    }
}