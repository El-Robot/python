def is_available(activity, person) -> bool:
    for busy in person:
        if busy[0] <= activity[0] < busy[1]:
            return False
        if busy[0] < activity[1] <= busy[1]:
            return False
        if activity[0] <= busy[0] and activity[1] >= busy[1]:
            return False
    return True


def main():
    total_cases = int(input())
    count = 1
    while count <= total_cases:

        impossible = False

        result = ""

        num_activities = int(input())

        jamie = []
        cameron = []

        activities = []

        for i in range(num_activities):
            time_range = input()
            activities.append(time_range.split(' '))
            for j in range(len(activities[i])):
                activities[i][j] = int(activities[i][j])

        for activity in activities:

            if is_available(activity, jamie):
                result += "J"
                jamie.append(activity)

            elif is_available(activity, cameron):
                result += "C"
                cameron.append(activity)

            else:
                impossible = True
                break

        if impossible:
            result = "IMPOSSIBLE"

        print("Case #%d: %s" % (count, result))

        count += 1


if __name__ == "__main__":
    main()
