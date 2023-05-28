import requests
from locust import HttpUser, task, between, events
from os import getenv
import sys
import random

USER_TOKEN = getenv("SMARTBARD_TOKEN")  # token should have administrator privileges
CREATED_ANNOUNCEMENTS = []
BASE_URL = ""  # this will be set programmatically

@events.test_start.add_listener
def on_test_start():
    if USER_TOKEN is None or len(USER_TOKEN) == 0:
        print("Could not find token")
        sys.exit(1)

@events.test_stop.add_listener
def on_test_stop():
    for announcement_id in CREATED_ANNOUNCEMENTS:
        requests.delete(BASE_URL + "/announcements/" + str(announcement_id), headers={
            'Authorization': 'Bearer ' + USER_TOKEN
        })


class SmartBardUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        global BASE_URL
        BASE_URL = self.client.base_url
        self.client.headers = {'Authorization': 'Bearer ' + USER_TOKEN}

    @task
    def get_announcements(self):
        self.client.get(self.client.base_url + '/announcements')

    @task
    def get_user_info(self):
        self.client.get(self.client.base_url + '/users/self')

    @task
    def get_specific_announcement(self):
        if len(CREATED_ANNOUNCEMENTS) != 0:
            announcement_id = random.choice(CREATED_ANNOUNCEMENTS)
            self.client.get(self.client.base_url + '/announcements/' + str(announcement_id))

    @task
    def create_announcement(self):
        num = random.randint(0, 10000)
        result = self.client.post(self.client.base_url + '/announcements', json={
            'title': 'Load Testing Announcement ' + str(num),
            'body': 'This is the body of a load testing announcement',
            'media': '',
            'datefrom': '2023-01-01',
            'dateto': '2023-12-31',
            'priority': False
        }, headers={
            'Content-Type': 'application/json'
        })
        CREATED_ANNOUNCEMENTS.append(result.json()['announcementId'])