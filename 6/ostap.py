__author__ = 'Sergei.Ivanov'

def main():
    with open("input.txt") as f, open("output.txt", "w+") as g:
        lines = f.readlines()
        N, M = map(int, lines[0].split())
        sellers = sorted(map(int, lines[1].split()))
        buyers = sorted(map(int, lines[2].split()), reverse=True)

        S = 0
        for i in range(min(N,M)):
            if buyers[i] < sellers[i]:
                break
            else:
                S += buyers[i] - sellers[i]
        g.write(str(S))

main()