from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

def extract_jobs(keyword: str):
    jobs_db = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")

        for x in range(5):
            time.sleep(1.5)
            page.keyboard.down("End")

        soup = BeautifulSoup(page.content(), "html.parser")
        cards = soup.find_all("div", class_="JobCard_container__zQcZs")

        for card in cards:
            link = f"https://www.wanted.co.kr{card.find('a')['href']}"
            title = card.find("strong", class_="JobCard_title___kfvj").text
            company_name = card.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu wds-nkj4w6").text
            reward = card.find("span", class_="JobCard_reward__oCSIQ").text
            jobs_db.append({
                "title": title,
                "company": company_name,
                "reward": reward,
                "link": link,
            })

        browser.close()
    return jobs_db

'''
page.wait_for_timeout(5000)

for frame in page.frames:
    try:
        close_btn = frame.locator("div.modal div.close")
        if close_btn.count() > 0:
            close_btn.click(force=True)
            break
    except:
        pass

page.click("button.Aside_searchButton__Ib5Dn.Aside_isNotMobileDevice__ko_mZ")

time.sleep(4)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(4)

page.keyboard.down("Enter")

time.sleep(5)

page.click("a#search_tab_position")
'''