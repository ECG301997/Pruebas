class FizzBuzz:
    
    def fizzBuzz(self,n):
        result = []
        for i in range(1,n+1):
            if i % 15==0:
                result.append('Fizz Buzz')
            elif i % 3 ==0:
                result.append('Fizz')
            elif i % 5 ==0:
                result.append('Buzz')
            else:
                result.append(i)
        return result