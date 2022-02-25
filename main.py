import requests
import json

TOKEN = '2619421814940190'


class Superhero():
    url = 'https://superheroapi.com/api/2619421814940190/'

    def __init__(self, token):
        self.token = token

    def search_hero(self, name):
        hero_url = self.url + 'search/' + name
        hero_id = requests.get(hero_url).json()['results'][0]['id']
        return str(hero_id)

    def get_stats(self, id):
        stats_url = self.url + '/' + id + '/powerstats'
        stats = requests.get(stats_url).json()['intelligence']
        return stats


if __name__ == '__main__':
    heroes = ['Hulk', 'Captain America', 'Thanos']
    heroes_compare = {}
    hero = Superhero(token=TOKEN)
    for cur_hero in heroes:
        cur_int = hero.get_stats(hero.search_hero(cur_hero))
        heroes_compare[cur_hero] = cur_int
    print(f'Most intelligent hero is {max(heroes_compare)}')
