class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        result = ""

        if (numerator < 0) != (denominator < 0):
            result += "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        result += str(numerator // denominator)

        remainder = numerator % denominator

        if remainder == 0:
            return result

        result += "."

        seen = {}

        while remainder != 0:
            if remainder in seen:
                index = seen[remainder]
                result = result[:index] + "(" + result[index:] + ")"
                break

            seen[remainder] = len(result)

            remainder *= 10
            result += str(remainder // denominator)
            remainder %= denominator

        return result
