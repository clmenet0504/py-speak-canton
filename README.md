# py-speak-canton

Cantonese Pinyin (常用字廣州話讀音表:拼音方案, also known as 教院式拼音方案) is a romanization system for Cantonese developed by Rev. Yu Ping Chiu (余秉昭)

This project is a little experiment on creating a Cantonese (廣東話) text-to-CantoPinyin.

## Usage (*.exe)


## Prerequisite
* Python 3.9.0
* [Chrome Driver](https://chromedriver.chromium.org/downloads) (Put in the same directory as scrapping.py)

### Libraries for Text to Cantonese Phonetic
```powershell
pip install selenium
pip install urllib
```

## Usage
### Text to Cantonese Phonetic
#### Input (Command line)
```powershell
python scrapping.py [sentence]
```
> **python scrapping.py 你好嗎**

#### Expected output
```powershell
Sentence(句子) : ['你', '好', '嗎']
==================
Word(字) : 你
Initial(聲母) : n
Final(韻母) : ei
Tone(音調) : 5
==================
Word(字) : 好
Initial(聲母) : h
Final(韻母) : ou
Tone(音調) : 2
==================
Word(字) : 嗎
Initial(聲母) : m
Final(韻母) : aa
Tone(音調) : 1
```
