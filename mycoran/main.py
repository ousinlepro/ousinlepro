
#import js
# https://hci-lab.github.io/PyQuran-Private/analysis_tools/
import pyquran as q
from time import sleep
import re

def mono_verset(*args, **kwargs):
    inp = Element('output')
    mysura = int(Element('sura').value)
    verset = int(Element('verse').value)
    verset = q.quran.get_verse(sura_number=mysura, verse_number=verset, with_tashkeel=True)
    inp.write(f"{verset}")

def multi_verset(*args, **kwargs):
    inp = Element('output')
    verset = Element('verse').value

    num_versets= verset

    num_versets1 = re.findall(r"\d+:", num_versets)
    num_versets1 = num_versets1[0]
    num_versets1 = num_versets1.replace(':','')
    num_versets1 = int(num_versets1)

    num_versets2 = re.findall(r":\d+", num_versets)
    num_versets2 = num_versets2[0]
    num_versets2 = num_versets2.replace(':','')
    num_versets2 = int(num_versets2)

    for i in range(num_versets1,num_versets2):
        sourate = int(Element('sura').value)
        versets = q.quran.get_verse(sura_number=sourate, verse_number=i, with_tashkeel=True)
    inp.write(versets)

def myverse(*args, **kwargs):
    verset = Element('verse').value
    if ':' in verset:
        multi_verset()
    else:
        mono_verset()





