def get_element(html_source):
  return html_source.xpath('//span[@class="element-text"]/text()')[0]

def get_role(html_source):
  return html_source.xpath('//span[@class="role-text"]/text()')[0]

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://guardiantales.wiki/heroes/plitvice/'
  html_source = html.parse(ur.urlopen(url))
  print('Name: {}'.format(html_source.xpath('//h1/text()')[0][1:-1]))
  print('Element: {}'.format(get_element(html_source)))
  print('Role: {}'.format(get_role(html_source)))

