def get_all_stats(html_source):
  all_stats = html_source.xpath('//div[@class="item-stats"]//span//text()')[6:]
  return [s for s in all_stats if not s.isspace()]

def get_stats_label():
  label = [
    'Atk',
    'Def',
    'HP',
    'Damage Reduction',
    'Skill Damage',
    'Weapon Skill Regen Speed',
    'Basic type Atk',
    'Dark type Atk',
    'Earth type Atk',
    'Fire type Atk',
    'Light type Atk',
    'Water type Atk',
    ' Atk increase on enemy kill',
    ' HP recovery on enemy kill',
    ' seconds of weapon skill Regen time on enemy kill',
    ' shield increase on battle start',
    ' shield increase on enemy kill',
  ]

  return label

