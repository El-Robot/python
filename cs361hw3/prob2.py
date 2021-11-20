class weighted_time:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __repr__(self) -> str:
        return str([self.start, self.end, self.weight])

def prob2(times, weights):
    w_times = []
    for i in range(len(times)):
        w_times.append(weighted_time(times[i][0],times[i][1],weights[i]))
    w_times = sorted(w_times, key = lambda e:e.end)
    
    new_weights = [0] * len(w_times)

    for i in range(len(w_times)):
        possible_best = [0]
        for j in range(0, i + 1):
            if w_times[i].start >= w_times[j].end:
                possible_best.append(new_weights[j] + (w_times[i].start - w_times[j].end))
        new_weights[i] = w_times[i].weight + max(possible_best)

    return max(new_weights)

times = [[8,9],[1,2],[5,6]]
weights = [2,6,5]
print(prob2(times, weights))
