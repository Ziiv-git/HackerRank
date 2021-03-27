'''
Objective
Today, we're learning about Interfaces. Check out the Tutorial tab for learning
materials and an instructional video!
Task
The AdvancedArithmetic interface and the method declaration for the abstract
divisorSum(n) method are provided for you in the editor below.
Complete the implementation of Calculator class, which implements the AdvancedArithmetic
interface. The implementation for the divisorSum(n) method must return the sum of
all divisors of
'''

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        result = 0
        for i in range(n+1):
            if i== 0:
                continue
            elif n % i == 0:
                result += i
        return result


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
