class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # 1. Handle sign
        if (numerator < 0) != (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        # 2. Integer part
        result.append(str(numerator // denominator))

        remainder = numerator % denominator

        # No decimal part
        if remainder == 0:
            return "".join(result)

        result.append(".")

        # remainder -> position in result
        seen = {}

        # 3. Long division
        while remainder != 0:
            if remainder in seen:
                index = seen[remainder]
                result.insert(index, "(")
                result.append(")")
                break

            seen[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)
