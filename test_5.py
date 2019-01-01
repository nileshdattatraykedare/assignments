from math import sqrt

max_val = 257


def aligncharacters(s):
    prime = [True] * (max_val + 1)

    # 0 and 1 are not primes
    prime[0] = False
    prime[1] = False
    for p in range(2, int(sqrt(max_val)) + 1):

        # If prime[p] is not changed, then
        # it is a prime

        if prime[p]:

            # Update all multiples of p
            for i in range(2 * p, max_val + 1, p):
                prime[i] = False

    part1 = []
    part2 = []
    # Traverse all the characters
    for i in range(len(s)):
        if prime[ord(s[i])]:
            part1 += [ord(s[i])]
        else:
            part2 += [ord(s[i])]

    part1.sort()
    part2.sort(reverse=True)
    mergedlist = []
    mergedlist.extend(part1)
    mergedlist.extend(part2)
    output = ""

    for i in mergedlist:
        output += chr(i)
    return output


if __name__ == "__main__":
    S = "abC5AB1";

    # print required answer
    print(aligncharacters(S))