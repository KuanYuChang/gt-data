import pandas as pd

def get_ailment(html_source):
  return html_source.xpath('//span[@class="chain-text"]/text()')

def get_trigger(html_source):
  return get_ailment(html_source)[0]

def get_result(html_source):
  return get_ailment(html_source)[1]

def get_chain_skill(html_source):
  return html_source.xpath('//table[@class="hero-abilities-table"]//tr[3]/td//text()')[1]

def build_chain_ability(names, htmls):
  print('Building {}...'.format('chain_ability'), end=' ')
  chain_ability = pd.DataFrame()
  
  triggers = []
  results = []
  skills = []
  
  for name in names:
    html = htmls[name]
    triggers.append(get_trigger(html))
    results.append(get_result(html))
    skills.append(get_chain_skill(html))
  
  chain_ability['Name'] = names
  chain_ability['Trigger'] = triggers
  chain_ability['Result'] = results
  chain_ability['Chain Skill'] = skills
  print('Done.')
  return chain_ability

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://guardiantales.wiki/heroes/plitvice/'
  html_source = html.parse(ur.urlopen(url))
  print('Name: {}'.format(html_source.xpath('//h1/text()')[0][1:-1]))
  print('Trigger: {}'.format(get_trigger(html_source)))
  print('Result: {}'.format(get_result(html_source)))
  print('Chain Skill: {}'.format(get_chain_skill(html_source)))
