import pandas as pd
import urllib.request as ur
from lxml import html

from common import *
from hero.profile import *
from hero.max_stats import *
from hero.chain_ability import *
from hero.passives import *
from hero.special_ability import *
from hero.exclusive_weapon import *

# common variable
csv_dir = 'csv/hero'

# build hero name list
df = pd.read_csv('{}/source.csv'.format(csv_dir))
hero_page = pd.Series(df.URL.values, index=df.Name).to_dict()
names = list(hero_page.keys())

# build hero regitser
htmls = {}
for name in names:
  url = hero_page[name]
  print('Requesting {}...'.format(name), end=' ')
  htmls[name] = html.parse(ur.urlopen(url))
  print('Done.')

# update profile
profile = build_profile(names, htmls)
save_csv(csv_dir, 'profile', profile)

# update max stats
max_stats = build_max_stats(names, htmls)
save_csv(csv_dir, 'max_stats', max_stats)

# update chain ability
chain_ability = build_chain_ability(names, htmls)
save_csv(csv_dir, 'chain_ability', chain_ability)

# update special ability
special_ability = build_special_ability(names, htmls)
save_csv(csv_dir, 'special_ability', special_ability)

# update passives
passivess = build_passives(names, htmls)
save_csv(csv_dir, 'passives', passivess)

# update exclusive weapon
exclusive_weapon = build_exclusive_weapon(names, htmls)
save_csv(csv_dir, 'exclusive_weapon', exclusive_weapon)

