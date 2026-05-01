from selenium import webdriver
from bs4 import BeautifulSoup
import time

search = input()
def scrape_jobs():
    driver = webdriver.Chrome()

    driver.get(f"https://www.rozee.pk/job/jsearch/q/{search}/fpn/0")

    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    jobs = soup.find_all("div", class_="job")

    all_jobs = []

    for job in jobs:

        title_tag = job.find("h3", class_="s-18")
        if not title_tag:
            continue

        title = title_tag.get_text(strip=True)

        company_tag = job.find('div', class_='cname')
        if company_tag:
            company = company_tag.get_text(" ", strip=True)
        else:
            company = "N/A"

        desc_tag = job.find('div', class_='jbody')
        if desc_tag:
            description = desc_tag.get_text(strip=True)
        else:
            description = "N/A"

        posted_tag = job.find('span', {'data-original-title': 'Posted On'})
        if posted_tag:
            posted = posted_tag.get_text(strip=True)
        else:
            posted = "N/A"

        exp_tag = job.find('span', {'data-original-title': 'Experience'})
        if exp_tag:
            experience = exp_tag.get_text(strip=True)
        else:
            experience = "N/A"

        salary_tag = job.find('span', {'data-original-title': 'Offer Salary - PKR'})
        if salary_tag:
            salary = salary_tag.get_text(strip=True)
        else:
            salary = "N/A"

        link = "https:" + title_tag.a['href']

        all_jobs.append({
            "title": title,
            "company": company,
            "description": description,
            "posted": posted,
            "experience": experience,
            "salary": salary,
            "link": link
        })

    driver.quit()
    return all_jobs


# For testing only — remove this when using in API
if __name__ == "__main__":
    data = scrape_jobs()
    for job in data:
        print(job)
        print("-------------------------------------------------------")
