import pandas as pd
import urllib.request as ur
from lxml import html

from hero.common import *
from hero.profile import *
from hero.max_stats import *
from hero.chain_ability import *
from hero.passives import *
from hero.special_ability import *

# common variable
csv_dir = 'csv/hero'

# build hero name list
df = pd.read_csv('{}/source.csv'.format(csv_dir))
hero_page = pd.Series(df.URL.values, index=df.Name).to_dict()
names = list(hero_page.keys())

# build hero regitser
html_source = {}
for name in names:
  url = hero_page[name]
  print('Requesting {}...'.format(name), end=' ')
  html_source[name] = html.parse(ur.urlopen(url))
  print('Done.')

# update profile
print('Building profile...', end=' ')
profile = pd.DataFrame()

elements = []
roles = []

for name in names:
  html = html_source[name]
  element = get_element(html)
  role = get_role(html)

  elements.append(element)
  roles.append(role)

profile['Name'] = names
profile['Element'] = elements
profile['Role'] = roles
print('Done.')

print('Saving out to csv format...', end=' ')
save_csv(csv_dir, 'profile', profile)
print('Done.')

# update max stats
print('Building max stats...', end=' ')
max_stats = pd.DataFrame()

atks = []
hps = []
defs = []
crits = []
damages = []
heals = []

for name in names:
  html = html_source[name]
  atk = get_atk(html)
  hp = get_hp(html)
  defence = get_def(html)
  crit = get_crit(html)
  damage = get_damage_reduction(html)
  heal = get_heal(html)

  atks.append(atk)
  hps.append(hp)
  defs.append(defence)
  crits.append(crit)
  damages.append(damage)
  heals.append(heal)

max_stats['Name'] = names
max_stats['ATK'] = atks
max_stats['HP'] = hps
max_stats['DEF'] = defs
max_stats['Crit Chance'] = crits
max_stats['Damage Reduction'] = damages
max_stats['Heal'] = heals
print('Done.')

print('Saving out to csv format...', end=' ')
save_csv(csv_dir, 'max_stats', max_stats)
print('Done.')

# update chain ability
print('Building chain ability...', end=' ')
chain_ability = pd.DataFrame()

triggers = []
results = []
skills = []

for name in names:
  html = html_source[name]
  trigger = get_trigger(html)
  result = get_result(html)
  skill = get_chain_skill(html)

  triggers.append(trigger)
  results.append(result)
  skills.append(skill)

chain_ability['Name'] = names
chain_ability['Trigger'] = triggers
chain_ability['Result'] = results
chain_ability['Chain Skill'] = skills
print('Done.')

print('Saving out to csv format...', end=' ')
save_csv(csv_dir, 'chain_ability', chain_ability)
print('Done.')

# update special ability
print('Building special ability...', end= ' ')
special_ability = pd.DataFrame()

specials = []

for name in names:
  html = html_source[name]
  special = get_special_ability(html)

  specials.append(special)

special_ability['Name'] = names
special_ability['Special Ability'] = specials
print('Done.')

print('Saving out to csv format...', end=' ')
save_csv(csv_dir, 'special_ability', special_ability)
print('Done.')

# update passives
print ('Building passives...', end=' ')
passivess = pd.DataFrame()

passives = []

for name in names:
  html = html_source[name]
  p = get_passives(html)

  passives.append(p)

passivess['Name'] = names
passivess['Passives'] = passives
print('Done.')

print('Saving out to csv format...', end=' ')
save_csv(csv_dir, 'passives', passivess)
print('Done.')

