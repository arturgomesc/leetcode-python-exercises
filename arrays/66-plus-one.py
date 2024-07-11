from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Percorre os dígitos de trás para frente
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # Se todos os dígitos eram 9, precisamos adicionar um dígito 1 à esquerda
        digits.insert(0, 1)
        return digits


solution = Solution()
print(solution.plusOne([1, 3, 9]))
