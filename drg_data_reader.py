import json

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

timeline_data = json.load(open("timeline_data.json",'r'))

# print(pretty(timeline_data["data"]))

# FETCH ACTIVITY SET AND CREATE DICTIONARY
timeline_data_dict = {}
id = 0
for activity in timeline_data["activitySet"]["activities"]:
    timeline_data_dict[id] = {"name":timeline_data["activitySet"]["activities"][id]["name"], "duration":[], "total_time":0}
    id += 1

# print(timeline_data_dict)

# GO THROUGH DATA SET AND ADD DURATION VALUES TO DICTIONARY
for session in timeline_data["data"]:
    activity_id = 0
    for activity in session["data"]:
        # print(activity)
        # print(timeline_data["activitySet"]["activities"][activity_id]["name"])
        timeline_data_dict[activity_id]["duration"].append(activity)
        activity_id += 1

# print(pretty(timeline_data_dict))

for activity in timeline_data_dict:
    # print(timeline_data_dict[activity])
    for time_period in timeline_data_dict[activity]["duration"]:
        for timestamp in time_period:
            # print(timestamp[1] - timestamp[0])
            timeline_data_dict[activity]["total_time"] += timestamp[1] - timestamp[0]

# Converting milliseconds to minutes
for activity in timeline_data_dict:
    timeline_data_dict[activity]["total_time"] = timeline_data_dict[activity]["total_time"] / 60000

print(pretty(timeline_data_dict))
# ONE ACTIVITY
# print(pretty(timeline_data_dict[0]["duration"][0]))

# SET OF TWO
# print(pretty(timeline_data_dict[0]["duration"][0][0]))

    # print("\nBANANA AND TURTLE\n")
    # print(pretty(session))
    # print(pretty(session["data"][1]))
    # for activity in session["data"]:
    #     print(activity)
