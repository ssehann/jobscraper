def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", mode="w")
    file.write("Title,Company,Location,Reward,URL\n")

    for job in jobs:
        file.write(f"{job['title']},{job['company']},{job['location']},{job['reward']},{job['url']}\n")

    file.close()