def study_schedule(permanence_period, target_time):
    if target_time is None or not isinstance(
        permanence_period, (list, tuple, int)
    ):
        return None

    counter = 0
    for start_time, end_time in permanence_period:
        if not isinstance(start_time, int) or not isinstance(end_time, int):
            return None
        elif start_time <= target_time <= end_time:
            counter += 1

    return counter
