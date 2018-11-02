import urllib.parse
import re

def cleanText(text):
  text = re.sub(r'\([^)]*\)', '', text)
  text = text.split('-')[0].strip()
  return text.strip()


def urlencode(text):
  return urllib.parse.quote_plus(text)
