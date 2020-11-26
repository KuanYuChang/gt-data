import pandas as pd

def get_stats(html_source):
  return html_source.xpath('//span[@class="elementor-progress-text"]/text()')

def get_atk(html_source):
  return get_stats(html_source)[0][len('ATK '):]

def get_hp(html_source):
  return get_stats(html_source)[1][len('HP '):]

def get_def(html_source):
  return get_stats(html_source)[2][len('DEF '):]

def get_crit(html_source):
  return get_stats(html_source)[3][len('Crit Chance '):]

def get_damage_reduction(html_source):
  return get_stats(html_source)[4][len('Damage Reduction '):]

def get_heal(html_source):
  return get_stats(html_source)[5][len('Heal '):]

def build_max_stats(names, htmls):
  print('Building {}...'.format('max_stats'), end=' ')
  max_stats = pd.DataFrame()
  
  atks = []
  hps = []
  defs = []
  crits = []
  damage_reductions = []
  heals = []
  
  for name in names:
    html = htmls[name]
    atks.append(get_atk(html))
    hps.append(get_hp(html))
    defs.append(get_def(html))
    crits.append(get_crit(html))
    damage_reductions.append(get_damage_reduction(html))
    heals.append(get_heal(html))
  
  max_stats['Name'] = names
  max_stats['ATK'] = atks
  max_stats['HP'] = hps
  max_stats['DEF'] = defs
  max_stats['Crit Chance'] = crits
  max_stats['Damage Reduction'] = damage_reductions
  max_stats['Heal'] = heals
  print('Done.')
  return max_stats

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://guardiantales.wiki/heroes/plitvice/'
  html_source = html.parse(ur.urlopen(url))
  print('Name: {}'.format(html_source.xpath('//h1/text()')[0][1:-1]))
  print('ATK: {}'.format(get_atk(html_source)))
  print('HP: {}'.format(get_hp(html_source)))
  print('DEF: {}'.format(get_def(html_source)))
  print('Crit Chance: {}'.format(get_crit(html_source)))
  print('Damage Reduction: {}'.format(get_damage_reduction(html_source)))
  print('Heal: {}'.format(get_heal(html_source)))
  
