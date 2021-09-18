def can_the_plants_be_potted(p:list, r:list):
    pots = p + r
    plants = p
    pots.sort()
    pots.reverse()
    plants.sort()
    plants.reverse()
    flag = True

    for i in range(len(plants)):
        if plants[i] >= pots[i]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")

def main():
    p = [4,3,3]
    r = [5,4,4]
    can_the_plants_be_potted(p,r)

if __name__ == "__main__":
    main()