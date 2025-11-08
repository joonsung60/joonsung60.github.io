import csv

def save_to_file(keyword, jobs):
    with open(f"{keyword}.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Reward", "Link"])
        for job in jobs:
            writer.writerow([
                job.get("title", ""),
                job.get("company", ""),
                job.get("reward", ""),
                job.get("link", "")
            ])