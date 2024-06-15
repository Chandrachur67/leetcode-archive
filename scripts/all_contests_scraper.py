import requests
import json
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

# Create a cursor object
cur = conn.cursor()

reqUrl = "https://leetcode.com/graphql/"

payload_template = {
    "query": """
    query pastContests($pageNo: Int, $numPerPage: Int) { 
        pastContests(pageNo: $pageNo, numPerPage: $numPerPage) { 
            pageNum 
            currentPage 
            totalNum 
            numPerPage 
            data { 
                title 
                titleSlug 
                startTime 
                originStartTime 
            } 
        } 
    } 
    """,
    "variables": {
        "pageNo": 0,
        "numPerPage": 10  
    },
    "operationName": "pastContests"
}


page_no = 1
done = False
while True:
    payload_template["variables"]["pageNo"] = page_no
    payload = json.dumps(payload_template)
    
    response = requests.post(reqUrl, data=payload, headers={"Content-Type": "application/json"})

    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        break
    
    contests = response.json().get('data').get('pastContests').get('data')
    print(contests)
    if len(contests) == 0:
        break

    for contest in contests:
        title_slug, title, start_time = contest['titleSlug'], contest['title'], contest['startTime']

        cur.execute("SELECT * FROM contest WHERE title_slug = %s", (title_slug,))
        existing_contest = cur.fetchall()

        if len(existing_contest) != 0:
            done = True
            break

        cur.execute("""
            INSERT INTO contest (title_slug, title, start_time)
            VALUES (%s, %s, %s)
        """, (title_slug, title, start_time))

        print(f'Added {title}')

    if done:
        break
    page_no += 1

conn.commit()
cur.close()
conn.close()