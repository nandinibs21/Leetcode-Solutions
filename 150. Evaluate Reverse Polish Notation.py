from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st: List[int] = []

        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                st.append(int(t))
                continue

            b = st.pop()
            a = st.pop()

            if t == "+":
                st.append(a + b)
            elif t == "-":
                st.append(a - b)
            elif t == "*":
                st.append(a * b)
            else:  # "/"
                st.append(int(a / b))  # truncates toward 0

        return st[-1]
