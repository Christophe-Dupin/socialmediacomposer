from django.db import models
from app.users.models import User

import os
import requests


class SocialMedia(models.Model):
    socialmedia = models.CharField(max_length=255)

    def __str__(self):
        return self.socialmedia


class PostManager(models.Manager):
    def get_all_post_on_queue(self, user):
        return self.filter(
            is_queue=True,
            author=user,
        )

    def get_all_post_history(self, user):
        return self.filter(
            is_send=True,
            author=user,
        )

    def get_all_post_on_queue_by_social_media(self, socialmedia, user):
        return self.filter(is_queue=True, socialmedia=socialmedia, author=user)

    def delete_a_selected_post(self, pk):
        return self.filter(id=pk).delete()


class Post(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    schedule_time = models.DateTimeField()
    is_queue = models.BooleanField(default=True)
    is_send = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    socialmedia = models.ManyToManyField(SocialMedia)
    objects = PostManager()

    def post_on_Linkedin(self):
        api_url = "https://api.linkedin.com/v2/ugcPosts"
        user = User.objects.get(username=self.author)
        social = user.social_auth.get(provider="linkedin-oauth2")
        access_token = social.extra_data["access_token"]
        headers = {
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        urn = social.extra_data["id"]
        author = f"urn:li:person:{urn}"
        post_data = {
            "author": author,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": self.body},
                    "shareMediaCategory": "NONE",
                },
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "CONNECTIONS"
            },
        }
        response = requests.post(api_url, headers=headers, json=post_data)

        if response.status_code == 201:
            print("Success")
        print(response.content)
