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

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://guardiantales.wiki/heroes/lavi/'
  html_source = html.parse(ur.urlopen(url))
  print('Name: {}'.format(html_source.xpath('//h1/text()')[0][1:-1]))
  print('Weapon: {}'.format(get_weapon_name(html_source)))
  print('Ability: {}'.format(get_weapon_ability(html_source)))

