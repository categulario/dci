import unicodedata
import re

def strip_accents(s):
   s = s.strip().lower()
   s = '_'.join(re.split(r'\s+', s))
   return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

if __name__ == '__main__':
    assert strip_accents('á  viON') == 'a_vion'
