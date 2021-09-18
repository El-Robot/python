def is_splitable(necklace: list):
    people = 3
    length = len(necklace)

    sum = 0
    for weight in necklace:
        sum += weight
    split = sum/people
    print(str(split))

    success = False

    top = 0
    bot = 0
    first = -1
    curr_sum = necklace[0]
    for i in range(2*length):
        #print(str(curr_sum))

        if curr_sum > split:
            curr_sum -= necklace[bot]
            bot += 1
            bot %= length
            if first != -1:
                break
        elif curr_sum < split:
            top += 1
            top %= length
            curr_sum += necklace[top]

        elif curr_sum == split:
            if first == -1:
                first = bot
            top += 1
            top %= length
            bot = top
            curr_sum = necklace[top]
        if top == first:
            success = True
            break

    top = 0
    bot = 0
    first = -1
    curr_sum = necklace[0]
    for i in range(2*length):
        #print(str(curr_sum))

        if curr_sum > split:
            curr_sum += necklace[bot]
            bot -= 1
            bot %= length
            if first != -1:
                break
        elif curr_sum < split:
            top -= 1
            top %= length
            curr_sum += necklace[top]

        elif curr_sum == split:
            if first == -1:
                first = bot
            top -= 1
            top %= length
            bot = top
            curr_sum = necklace[top]
        if top == first:
            success = True
            break

    if success:
        print("YES")
    else:
        print("NO")


def main():
    is_splitable([2,1,1,1,1,1,1,1,1,2])


if __name__ == "__main__":
    main()
