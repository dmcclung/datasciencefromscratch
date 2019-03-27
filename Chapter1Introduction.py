users = [
    {"id": 0, "name": "Teagan"},
    {"id": 1, "name": "Declan"},
    {"id": 2, "name": "Carl"},
    {"id": 3, "name": "Don"},
    {"id": 4, "name": "Susan"},
    {"id": 5, "name": "Liz"},
    {"id": 6, "name": "Bobby"}
]

friendships = [
    (0, 1), (0, 2), (0, 3), (0, 4), (4, 5), (4, 6)
]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


def number_of_friends(user):
    return len(user["friends"])


total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users

print(avg_connections)
