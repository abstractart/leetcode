import kotlin.math.abs

class Solution {
    fun addStrings(num1: String, num2: String): String {
        val builder = StringBuilder()

        val head = "0".repeat(abs(num1.length - num2.length))
        val n1 :String
        val n2 :String

        if (num1.length < num2.length) {
            n1 = head + num1
            n2 = num2
        } else {
            n2 = head + num2
            n1 = num1
        }

        var remainder = 0

        var i = n1.length - 1
        var j = n2.length - 1

        while(i >= 0 && j >= 0) {
            val s = n1[i].toInt() - 48 + n2[j].toInt() - 48 + remainder
            builder.append((s % 10 + 48).toChar())
            remainder = s / 10

            i -= 1
            j -= 1
        }
        
        if (remainder != 0) {
            builder.append(remainder)
        }

        return builder.reverse().toString()
    }
}
