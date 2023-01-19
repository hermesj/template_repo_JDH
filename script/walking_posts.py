import json
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

filenames = os.listdir("comments_json_anonym")
filenames.sort()

last_date = 0
for file in filenames:
  with open(f"comments_json_anonym/{file}", "r",encoding="utf-8") as f:
    data = json.load(f)
  print(file)
  for comment in data:
    if comment['created_at'] > last_date:
      last_date = comment['created_at']
    if "answers" in comment:
      for answer in comment['answers']:
        if answer['created_at'] > last_date:
          last_date = answer['created_at']
  
last_date = datetime.fromtimestamp(last_date).date()
print(last_date)
post_lines = []

# Initialize the figure and the axis
fig, ax = plt.subplots(figsize=(20, 6))

# Function to update the plot for the next json file
def update(i):
  x = {datetime.strptime(filename.split("_")[0], "%Y-%m-%d"):0 for filename in filenames}
  x[last_date] = 0

  filename = filenames[i]
  if os.path.splitext(filename)[1].endswith("json"):
    with open(f"comments_json_anonym/{filename}", "r",encoding="utf-8") as f:
      comments = json.load(f)
  else:
    return

  post_date = datetime.strptime(filename.split("_")[0], "%Y-%m-%d")
  
  for comment in comments:
    comment_date = datetime.fromtimestamp(comment["created_at"]).date()
    if comment_date in x:
      x[comment_date] += 1
    else:
      x[comment_date] = 1
    if "answers" in comment:
      for answer in comment['answers']:
        answer_date = datetime.fromtimestamp(answer["created_at"]).date()
        if answer_date in x:
          x[answer_date] += 1
        else:
          x[answer_date] = 1

  ax.clear()

  ax.bar(x.keys(), x.values(),color="plum",width=0.8,label="Count of comments for post")
  ax.set_title('Comments over time per post')
  ax.axvline(x=post_date, color="purple",linewidth=0.4, linestyle="dashed",label="date of post")
  ax.set_ylim(0,1000)
  ax.legend()

# Create the animation using the `FuncAnimation` function
ani = animation.FuncAnimation(fig, update, frames=range(len(filenames)), repeat=True)
ani.save('Bilder/comments_per_post_over_time.gif',writer='imagemagick')
plt.show()

