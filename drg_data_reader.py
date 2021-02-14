import json
import matplotlib.pyplot as plt

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

timeline_data = json.load(open("timeline_data.json",'r'))

# FETCH ACTIVITY SET AND CREATE DICTIONARY
timeline_data_dict = {}
id = 0
for activity in timeline_data["activitySet"]["activities"]:
    timeline_data_dict[id] = {"name":timeline_data["activitySet"]["activities"][id]["name"], "duration":[], "total_time":0}
    id += 1

total_project_time = 0

# GO THROUGH DATA SET AND ADD DURATION VALUES TO DICTIONARY
# AND CALCULATE TOTAL TIME SPENT ON PROJECT
for session in timeline_data["data"]:
    activity_id = 0
    total_project_time += session["duration"]
    for activity in session["data"]:
        timeline_data_dict[activity_id]["duration"].append(activity)
        activity_id += 1

# SUBTRACT START TIME FROM END TIME TO FIND TIME SPENT ON EACH ACTIVITY
for activity in timeline_data_dict:
    for time_period in timeline_data_dict[activity]["duration"]:
        for timestamp in time_period:
            timeline_data_dict[activity]["total_time"] += timestamp[1] - timestamp[0]

# Converting milliseconds to minutes
for activity in timeline_data_dict:
    timeline_data_dict[activity]["total_time"] = timeline_data_dict[activity]["total_time"] / 60000

print(pretty(timeline_data_dict))

# PLOTTING TIME
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Comparison of time spent on each design activity')
ax.set_xlabel('Activities')
ax.set_ylabel('Total time spent in minutes')
activity_list = []
time_spent = []
for activity in timeline_data_dict:
    activity_list.append(timeline_data_dict[activity]["name"])
    time_spent.append(timeline_data_dict[activity]["total_time"])

# adding bar for total time spent
activity_list.append("total project time")
time_spent.append(total_project_time/60000)

ax.bar(activity_list,time_spent)
plt.show()
