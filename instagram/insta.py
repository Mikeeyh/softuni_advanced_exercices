# import instaloader
#
#
# def download_instagram_media(username):
#     # Create an Instaloader instance
#     L = instaloader.Instaloader()
#
#     try:
#         # Load the profile of the user
#         profile = instaloader.Profile.from_username(L.context, username)
#
#         # Create a directory for the user's media
#         user_dir = username
#         L.download_profile(profile, profile_pic_only=False)
#
#         # Iterate through the user's posts and download each post
#         for post in profile.get_posts():
#             L.download_post(post, target=user_dir)
#
#         print(f"Media downloaded to {user_dir} directory.")
#     except instaloader.exceptions.ProfileNotExistsException:
#         print(f"User {username} does not exist.")
#
#
# if __name__ == "__main__":
#     username = "zhaki.99"  # Replace with the Instagram username you want to download media from
#     download_instagram_media(username)

from instaloader import Instaloader, Profile

L = Instaloader()
PROFILE = ""
profile = Profile.from_username(L.context, PROFILE)

posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes,reverse=True)

for post in posts_sorted_by_likes:
    L.download_post(post, PROFILE)

