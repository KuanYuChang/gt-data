import pandas as pd

def get_element(html_source):
  return html_source.xpath('//span[@class="element-text"]/text()')[0]

def get_role(html_source):
  return html_source.xpath('//span[@class="role-text"]/text()')[0]

def build_profile(names, htmls):
  print('Building {}...'.format('profile'), end=' ')
  profile = pd.DataFrame()
  
  elements = []
  roles = []
  
  for name in names:
    html = htmls[name]
    elements.append(get_element(html))
    roles.append(get_role(html))
  
  profile['Name'] = names
  profile['Element'] = elements
  profile['Role'] = roles
  print('Done.')
  return profile

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://guardiantales.wiki/heroes/plitvice/'
  html_source = html.parse(ur.urlopen(url))
  print('Name: {}'.format(html_source.xpath('//h1/text()')[0][1:-1]))
  print('Element: {}'.format(get_element(html_source)))
  print('Role: {}'.format(get_role(html_source)))

