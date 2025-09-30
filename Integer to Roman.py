class Solution:
    mapper = {1000:'M', 900:'CM',
                500:'D', 400: 'CD',
                100:'C', 90:'XC',
                50:'L', 40:'XL',
                10:'X', 9:'IX',
                5:'V', 4:'IV',
                1:'I'}

    def intToRoman(self, num: int) -> str:
        ans = []
        for val in self.mapper.keys():
            while num > 0 and num >= val:
                ans.append(self.mapper[val]*(num//val))
                num = num%val
        return ''.join(ans) 
