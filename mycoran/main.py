
#import js
# https://hci-lab.github.io/PyQuran-Private/analysis_tools/
import pyquran as q
from time import sleep
"""from bs4 import BeautifulSoup

var = q.quran.get_verse(sura_number=31, verse_number=6)

def fix():
    page = './index.html'
    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find("span", {"id": "py-14dc108c-a2cb-4704-ddf0-444b92c01600-2"})
    content.string = ""

"""


def myverse(*args, **kwargs):
    inp = Element('output')
    mysura = int(Element('sura').value)
    myverse = int(Element('verse').value)
    verset = q.quran.get_verse(sura_number=mysura, verse_number=myverse, with_tashkeel=True)
    inp.write(f"{verset}")


def mysura(*args, **kwargs):
    inp = Element('output')
    mysura = int(Element('sura').value)
    sourate = q.quran.get_sura(mysura, with_tashkeel=True)
    inp.write(sourate)
