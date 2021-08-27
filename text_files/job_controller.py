jobs_done = jobs_not_done = ""
with open('jobs_completed.txt') as file:
    jobs_done = file.read()

with open('upcoming_jobs.txt') as file:
    jobs_not_done = file.read()

jobs_done += "\n"
jobs_done += jobs_not_done

with open('full_job_directory.txt', 'w') as file:
    file.write(jobs_done)
