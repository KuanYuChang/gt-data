def get_ailment(html_source):
  return html_source.xpath('//span[@class="chain-text"]/text()')

def get_trigger(html_source):
  return get_ailment(html_source)[0]

def get_result(html_source):
  return get_ailment(html_source)[1]

def get_chain_skill(html_source):
  return html_source.xpath('//table[@class="hero-abilities-table"]//tr[3]/td//text()')[1]

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://guardiantales.wiki/heroes/plitvice/'
  html_source = html.parse(ur.urlopen(url))
  print('Name: {}'.format(html_source.xpath('//h1/text()')[0][1:-1]))
  print('Trigger: {}'.format(get_trigger(html_source)))
  print('Result: {}'.format(get_result(html_source)))
  print('Chain Skill: {}'.format(get_chain_skill(html_source)))
