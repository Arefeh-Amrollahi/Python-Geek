def maxEvents(arrival, duration):
    if not arrival:
        return 0

    max_events = 0
    current_arrival = 0
    min_duration = 0

    for process_arrival, process_duration in zip(arrival, duration):
        if current_arrival != process_arrival:
            if current_arrival + min_duration <= process_arrival:
                current_arrival = process_arrival
                min_duration = process_duration
                max_events += 1
        min_duration = min(min_duration, process_duration)

    return max_events
assert maxEvents([], []) == 0
assert maxEvents([1, 3, 3, 5, 7], [2, 2, 1, 2, 1]) == 4
assert maxEvents([1, 3, 3, 4, 7], [2, 2, 2, 3, 1]) == 3
assert maxEvents([1], [2]) == 1
assert maxEvents([1, 3, 4, 6], [4, 3, 3, 2]) == 2