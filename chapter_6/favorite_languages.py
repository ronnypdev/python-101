favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'rust',
  'phil': 'python',
}

for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}")


# Looping Through all the keys in a dictionary
for name in favorite_languages.keys():
  print(name.title())

for language in favorite_languages.values():
  print(language.title())