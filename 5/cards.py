__author__ = 'Sergei.Ivanov'

def main():
    with open("input.txt") as f, open("output.txt", "w") as g:
        line = next(f)
        N = int(line)
        line = next(f)
        sum1, sum2, sum3 = map(int, line.split())


        cards = range(1, N+1)
        S1 = sum(cards)
        S2 = sum(map(lambda x: x**2, cards))
        S3 = sum(map(lambda x: x**3, cards))

        A = S1 - sum1
        B = S2 - sum2
        C = S3 - sum3

        # for num1 in range(1, N):
        #     for num2 in range(num1, N+1):
        #         if (num1 + num2) >= A:
        #             break
        #         if (A - (num1+num2))**2 + num1**2 + num2**2 == B and (A - (num1+num2))**3 + num1**3 + num2**3 == C:
        #             print num1, num2, A - (num1+num2)
        #             g.write("%i %i %i" %(num1, num2, A - (num1+num2)))
        #             return

        for num1 in range(1, N+1):
            D = 4*(num1 - A)**2 - 8*(A**2 - B + 2*num1**2 - 2*A*num1)
            if D>=0:
                # case 1
                num2 = (-2*(num1 - A) + D**.5)/4
                if num2.is_integer() and (A - (num1+num2))**3 + num1**3 + num2**3 == C:
                        g.write("%i %i %i" %(num1, num2, A - (num1+num2)))
                        return

main()