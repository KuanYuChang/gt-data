import pandas as pd

def get_weapon_name(html_source):
  try:
    return html_source.xpath('//span[@class="weapon-stat weapon-chain-title bold"]/text()')[0]
  except:
    return None

def get_weapon_ability(html_source):
  try:
    return html_source.xpath('//span[@class="exclusive"]/text()')[0]
  except:
    return None

def get_weapon_image_url(html_source):
  try:
    return html_source.xpath('//div[@class="item-single-picture"]/img/@src')[0]
  except:
    return None

def build_exclusive_weapon(names, htmls):
  print('Building {}...'.format('exclusive_weapon'), end=' ')
  exclusive_weapon = pd.DataFrame()
  
  weapon_names = []
  weapon_abilities = []
  weapon_image_urls = []
  
  for name in names:
    html = htmls[name]
    weapon_names.append(get_weapon_name(html))
    weapon_abilities.append(get_weapon_ability(html))
    weapon_image_urls.append(get_weapon_image_url(html))
  
  exclusive_weapon['Name'] = names
  exclusive_weapon['Exclusive weapon'] = weapon_names
  exclusive_weapon['Ability'] = weapon_abilities
  exclusive_weapon['URL of image'] = weapon_image_urls
  print('Done.')
  return exclusive_weapon

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://heavenhold.com/heroes/tinia/'
  html_source = html.parse(ur.urlopen(url))
  print('Name: {}'.format(html_source.xpath('//h1/text()')[0][1:-1]))
  print('Weapon: {}'.format(get_weapon_name(html_source)))
  print('Ability: {}'.format(get_weapon_ability(html_source)))
  print('URL of icon: {}'.format(get_weapon_image_url(html_source)))

