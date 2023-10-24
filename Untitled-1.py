def maxEvents(arrival, duration):
    start_end_times = sorted([(a, a+d) for a,d in zip(arrival, duration)])
    events = [start_end_times[0]]
    for potential_event in start_end_times[1:]:
        prev_start_time, prev_end_time = events[-1]
        next_start_time, next_end_time = potential_event
        if next_start_time >= prev_end_time:
            events.append(potential_event)
        elif next_end_time < prev_end_time:
            # Found a better event that finishes sooner
            events.pop()
            events.append(potential_event)
    return len(events)