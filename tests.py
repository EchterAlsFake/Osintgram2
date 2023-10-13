
user = "nadyadorofeeva"

from instagrapi import Client
from tqdm import tqdm


cl = Client()

user_id = cl.user_id_from_username(user)
counter = 0
amount_per_request = 50  # Adjust as per your requirements
end_cursor = None
all_medias = []
user_info = cl.user_info_by_username('nadyadorofeeva')
total_posts = user_info.media_count

pbar = tqdm(total=total_posts, desc="Fetching media")

while True:
    medias, end_cursor = cl.user_medias_paginated(user_id, amount=amount_per_request, end_cursor=end_cursor)
    counter += len(medias)  # Increment counter by actual fetched count
    pbar.update(len(medias))  # Update progress bar by actual fetched count
    all_medias.extend(medias)

    if counter >= total_posts:
        break

for media in all_medias:
    print(media)