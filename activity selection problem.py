def activitySelection(start, finish):
    # Step 1: Pair and sort by finish times
    activities = list(zip(start, finish))
    activities.sort(key=lambda x: x[1])
    # Step 2: Select the first activity
    selected = [activities[0]]
    last_finish = activities[0][1]
    # Step 3: Iterate through remaining activities
    for i in range(1, len(activities)):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]
    return selected

start = [5, 6, 0, 4, 10]
finish = [8, 10, 5, 7, 12]
result = activitySelection(start, finish)
print("Selected Activities:", result)
print("Count:", len(result))
