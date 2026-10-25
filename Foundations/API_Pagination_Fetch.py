import requests
import json
import time
from logger import logger

def fetch_Data(page: int, record: int):
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {
        "_page": page,
        "_limit": record
    }
    
    try:
        # Initial attempt
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
        
    except requests.RequestException as e:
        logger.warning(f"Initial request failed: {e}. Starting retries...")
        
        for attempt in range(1, 4): 
            time.sleep(attempt) 
            logger.info(f"Attempt {attempt} -> wait {attempt} sec")
            
            try:
                response = requests.get(url, params=params, timeout=10)
                response.raise_for_status()
                return response.json() 
            except requests.RequestException as e:
                logger.warning(f"Attempt {attempt} failed: {e}")
                
        logger.error("All retry attempts failed.")
        return None


# all_post=[]
# def fetch_5_page():
#     for i in range(1,6):
#         all_post.extend(fetch_Data(i,10))
#     return all_post

# print("Total posts:",len(fetch_5_page()))
# for item in all_post:
#     print(f"{item['id'] }-> {item['title']}")

def until_blank():
    i=0
    while True:
        i+=1
        data=fetch_Data(i,10)
        print(f"Page:{i}-> {len(data)}")
        if len(data)==0:
            break

# until_blank()

def refine_clean():
    i=0
    while True:
        i+=1
        data=fetch_Data(i,10)
        for post in data:
            # print(post)
            temp={
                "id": post["id"],
                "title": post["title"],
                "user_id": post["userId"]
            }
            print(temp)
            all_post.append(temp)
        if len(data)==0:
            break
    with open('Data/posts_clean.json','w') as file:
        # print(all_post)
        json.dump(all_post,file,indent=4)

# refine_clean()



# new things

def fetch_all_posts(limit=10):
    page = 1
    all_posts=[]
    while True:
        data = fetch_Data(page,limit)
        if data is None:
            logger.error(f"Failed to fetch page {page}. Stopping pipeline.")
            break

        if len(data) == 0:
            break
        logger.info(f"Fetched page {page}")
        page+=1
        all_posts.extend(data)
    return all_posts

logger.info("ETL pipeline started")
posts = fetch_all_posts()

# print("Total posts:", len(posts))
from Data_Validation import validate_title
import csv

def transform_posts(posts):
    filtered_data = []
    rejected_posts=[]
    for post in posts:
        post_id = post.get("id")
        title = post.get("title")
        user_id = post.get("userId")
        isValid , reason = validate_title(title)
        if isValid:
            temp_post = {
                "id": post_id,
                "user_id":user_id,
                "title": title
            }
            filtered_data.append(temp_post)
        else:
            temp_post = {
                "id": post_id,
                "reason": reason
            }
            rejected_posts.append(temp_post)
            logger.warning(f"Post {post_id} rejected -> {reason}")
    logger.info(
        f"Transformation completed: "
        f"clean={len(filtered_data)}, "
        f"rejected={len(rejected_posts)}"
    )
    return filtered_data,rejected_posts

def save_csv(filtered_data,rejected_post):
    with open("Data/clean_posts.csv", "w", newline="", encoding="utf-8") as file:
        fields_name = ['id','user_id','title']
        writer = csv.DictWriter(file,fields_name)
        writer.writeheader()
        writer.writerows(filtered_data)
        logger.info(f"Saved Filtered Data in {file.name}")
    with open("Data/rejected_posts.csv", "w", newline="", encoding="utf-8") as file:
        fields_name = ['id','reason']
        writer = csv.DictWriter(file,fields_name)
        writer.writeheader()
        writer.writerows(rejected_post)
        logger.info(f"Saved Rejected Data in {file.name}")

clean_data,rejected_data = transform_posts(posts)
save_csv(clean_data,rejected_data)


logger.info(
    f"ETL pipeline completed. "
    f"Raw={len(posts)}, "
    f"Clean={len(clean_data)}, "
    f"Rejected={len(rejected_data)}"
)