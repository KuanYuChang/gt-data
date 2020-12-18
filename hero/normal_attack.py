import pandas as pd

def get_normal_attack(html_source):
  return ''.join(html_source.xpath('//div[@class="hero-abilities section-box"]//table//tr[1]/td//text()')[1:])

def build_normal_attack(names, htmls):
  print('Building {}...'.format('normal_attack'), end=' ')
  normal_attack = pd.DataFrame()
  
  abilities = []
  
  for name in names:
    html = htmls[name]
    abilities.append(get_normal_attack(html))
  
  normal_attack['Name'] = names
  normal_attack['Normal Attack'] = abilities
  print('Done.')
  return normal_attack

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://heavenhold.com/heroes/future-princess/'
  html_source = html.parse(ur.urlopen(url))
  print('Name: {}'.format(html_source.xpath('//h1/text()')[0][1:-1]))
  print('Normal Attack: {}'.format(get_normal_attack(html_source)))

