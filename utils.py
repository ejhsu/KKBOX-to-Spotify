import urllib.parse
import re

def cleanText(text):
  text = re.sub(r'\([^)]*\)', '', text)
  text = re.sub(r'【[^】]*】', '', text)
  text = text.split('-')[0].strip()
  return text.strip()


def urlencode(text):
  return urllib.parse.quote_plus(text)


def chunks(list, n):
    for i in range(0, len(list), n):
        yield list[i:i + n]

