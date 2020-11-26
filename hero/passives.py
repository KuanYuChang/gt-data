import pandas as pd

def get_passives(html_source):
  return ''.join(html_source.xpath('//table[@class="hero-abilities-table"]//tr[5]/td//text()'))

def build_passives(names, htmls):
  print('Building {}...'.format('passivess'), end=' ')
  passivess = pd.DataFrame()
  
  passives = []
  
  for name in names:
    html = htmls[name]
    passives.append(get_passives(html))
  
  passivess['Name'] = names
  passivess['Passives'] = passives
  print('Done.')
  return passivess  

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://guardiantales.wiki/heroes/plitvice/'
  html_source = html.parse(ur.urlopen(url))
  print('Name: {}'.format(html_source.xpath('//h1/text()')[0][1:-1]))
  print('Passives: {}'.format(get_passives(html_source)))

