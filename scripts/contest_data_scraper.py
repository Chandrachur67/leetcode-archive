import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from bs4 import BeautifulSoup
import psycopg2

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

# Create a cursor object
cur = conn.cursor()


# ----------------------- Getting all not scraped contests -----------------------
cur.execute("SELECT * FROM contest WHERE done = False")
contests = cur.fetchall()

formatted_contests = [{"title_slug": contest[0], "title": contest[1], "credit": contest[2], "done": contest[3]} for contest in contests]
contests = formatted_contests


# ----------------------- Getting problems for every contest -----------------------

driver = webdriver.Chrome()

for contest in contests:
    retry_count = 5
    for _ in range(retry_count):
        try:
            url = f"https://leetcode.com/contest/{contest['title_slug']}/"

            # Configure Selenium to use ChromeDriver
            driver.get(url)

            time.sleep(5)

            # Get the page source after the JavaScript has rendered
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, "lxml")

            problems = soup.find('ul', 'contest-question-list').findAll('li')[1:]


            for index, problem in enumerate(problems):
                title = problem.a.text
                link = problem.a['href']
                title_slug = link.split('/')[-2] if link.split('/')[-1] == '' else link.split('/')[-1]
                credit = int(problem.span.text)
                
                cur.execute("""
                    INSERT INTO problem (title_slug, title, credit, contest_title_slug)
                    VALUES (%s, %s, %s, %s)
                """, (title_slug, title, credit, contest['title_slug']))

            cur.execute("""
                UPDATE contest
                SET done = True 
                WHERE title_slug = %s
            """, (contest['title_slug'],))

            print(f"{contest['title']} done ✅")
            break
        except Exception as e:
            print(f"Error: {e}")

# Close the browser window
driver.quit()

conn.commit()
cur.close()
conn.close()