import requests
from bs4 import BeautifulSoup
import re
import json
import pytest

class videoScraper:
    def __init__(self, link):
        self.soup = BeautifulSoup(requests.get(link).content, "html.parser")

    def get_title(self):
        try:
            return self.soup.find("meta", itemprop="name")['content']
        except TypeError:
            return "The title is not available"

    def get_date(self):
        try:
            return self.soup.find("meta", itemprop="datePublished")['content']
        except TypeError:
            return "The date is not available"

    def get_views(self):
        try:
            return self.soup.find("meta", itemprop="interactionCount")['content']
        except TypeError:
            return "Views are not available"

    def get_desc(self):
        try:
            pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
            return pattern.findall(str(self.soup))[0].replace('\\n', '\n')
        except TypeError:
            return "The description is not available"

    def get_links(self):
        try:
            description = self.get_desc()
            return re.findall(
                "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})",
                description)
        except TypeError:
            return "The links are not available"

    def get_channel_name(self):
        try:
            return self.soup.find("span", itemprop="author").next.next['content']
        except TypeError:
            return "The channel name is not available"

    def get_videoId(self):
        try:
            return self.soup.find("meta", itemprop="videoId")['content']
        except TypeError:
            return "The video id is not available"

    # def get_nb_likes(self):
    #   try:
    #       data = re.search(r"var ytInitialData = ({.*?});", self.soup.prettify()).group(1)
    #       data = json.loads(data) videoPrimaryInfoRenderer = data['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
    #

    #       likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
    #       return likes_label.split(' ')[0].replace(',', '')

    #    except TypeError:
    #        return "The number of likes is not available"

    def get_dict(self):
        return [self.get_title(), self.get_date(), self.get_views(), self.get_channel_name(),
                self.get_videoId(),  # self.get_nb_likes(),
                self.get_desc(), self.get_links()]


read_json = "input.json"
write_json = "output.json"

with open(read_json, "r") as json_file:
    data = json.loads(json_file.read())
    donnees = data['videos_id']
    lien = []
    videos = []
    for id in range(8):
        lien.append("https://www.youtube.com/watch?v={ids}".format(ids=str(donnees[id])))
        video = videoScraper(lien[id])
        videos.append(video)

with open(write_json, "w") as json_file2:
    for i in range(len(lien)):
        video = videos[i].get_dict()
        json.dump(video, json_file2)
