
def observed_items():
    observations = []
    for i in range(7):
        print("What can you see?")
        user_input = input()
        observations.append(user_input)
    return observations


def run_task2():
    print("Counting observations...")
    observations = observed_items()
    observe = set()
    for item in observations:
        count = (item, observations.count(item))
        observe.add(count)
    for item in observe:
       print(f"{item[0]} observed {item[1]} times")

run_task2()






