import pandas as pd
import urllib.request as ur
from lxml import html

from common import *
from hero.profile import *
from hero.normal_attack import *
from hero.max_stats import *
from hero.chain_ability import *
from hero.passives import *
from hero.special_ability import *
from hero.exclusive_weapon import *

# common variable
csv_dir = 'csv/hero'
url_source = 'https://heavenhold.com/heroes/'

# build and save hero name list
print('Requesting {}...'.format(url_source), end=' ')
html_source = html.parse(ur.urlopen(url_source))
print('Done.')
print('Building hero name list...', end=' ')
hero_names = html_source.xpath('//tbody[@id="hero-data"]//a/text()')
hero_stars = html_source.xpath('//tbody[@id="hero-data"]//tr/td[3]/text()')
hero_urls = html_source.xpath('//tbody[@id="hero-data"]//a/@href')
hero_image_urls = []
for style in html_source.xpath('//tbody[@id="hero-data"]//a/div/@style'):
  hero_image_urls.append(style.split('image:')[1][5:-3])
print('Done.')

print('Saveing hero name list...', end=' ')
heros = pd.DataFrame()
heros['Name'] = hero_names
heros['Star'] = hero_stars
heros['URL of image'] = hero_image_urls
heros['URL'] = hero_urls
heros = heros.drop(heros[(heros['Name'] != 'Male Knight') & (heros['Star'] == '1 Star')].index)
heros['Star'] = heros['Star'].replace(['1 Star'], '2 Star')
heros = heros.sort_values(by=['Star', 'Name'], ascending=[False, True])
heros.to_csv('{}/source.csv'.format(csv_dir), index=False)
print('Done.')

# build hero register
print('Building hero register...')
hero_pages = pd.Series(heros['URL'].values, index=heros['Name']).to_dict()
hero_names = list(hero_pages.keys())
htmls = {}
for name in hero_names:
  url = hero_pages[name]
  print('  Requesting {}...'.format(name), end=' ')
  htmls[name] = html.parse(ur.urlopen(url))
  print('Done.')
print('Done.')

# update profile
profile = build_profile(hero_names, htmls)
save_csv(csv_dir, 'profile', profile)

# update profile
normal_attack = build_normal_attack(hero_names, htmls)
save_csv(csv_dir, 'normal_attack', normal_attack)

# update max stats
max_stats = build_max_stats(hero_names, htmls)
save_csv(csv_dir, 'max_stats', max_stats)

# update chain ability
chain_ability = build_chain_ability(hero_names, htmls)
save_csv(csv_dir, 'chain_ability', chain_ability)

# update special ability
special_ability = build_special_ability(hero_names, htmls)
save_csv(csv_dir, 'special_ability', special_ability)

# update passives
passivess = build_passives(hero_names, htmls)
save_csv(csv_dir, 'passives', passivess)

# update exclusive weapon
exclusive_weapon = build_exclusive_weapon(hero_names, htmls)
save_csv(csv_dir, 'exclusive_weapon', exclusive_weapon)

