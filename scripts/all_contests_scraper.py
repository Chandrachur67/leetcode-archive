import requests
import json

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
                cardImg 
                sponsors { 
                    name 
                    lightLogo 
                    darkLogo 
                } 
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


page_no = 0
while True:
    payload_template["variables"]["pageNo"] = page_no
    payload = json.dumps(payload_template)
    
    response = requests.post(reqUrl, data=payload, headers={"Content-Type": "application/json"})

    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        break
    
    contests = response.json().get('data').get('pastContests').get('data')
    print(len(contests))
    if len(contests) == 0:
        break

    for contest in contests:
        print(contest['titleSlug'])
        print(contest['originStartTime'])

    page_no += 1