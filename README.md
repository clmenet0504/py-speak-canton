# py-speak-canton

Cantonese Pinyin (常用字廣州話讀音表:拼音方案, also known as 教院式拼音方案) is a romanization system for Cantonese developed by Rev. Yu Ping Chiu (余秉昭)

This project is aims to create a Cantonese (廣東話) text-to-CantoPinyin library.

## Usage for executable(main.exe)
### Prerequisite
* Download [Chrome Driver](https://chromedriver.chromium.org/downloads) according to your chrome version (Put in the same directory as main.py)

> [How to Find Your Internet Browser Version Number - Google Chrome](https://help.zenplanner.com/hc/en-us/articles/204253654-How-to-Find-Your-Internet-Browser-Version-Number-Google-Chrome)

### Usage
1. Run main.exe
2. Input Cantonese Characters (Character or Sentence)
3. Click "Go!"
4. Have fun!

## Usage for python (scrapping.py)
### Prerequisite
* Python 3.9.0
* Download [Chrome Driver](https://chromedriver.chromium.org/downloads) according to your chrome version (Put in the same directory as scrapping.py)

### Libraries for Text to Cantonese Phonetic
```powershell
pip install selenium
pip install urllib
```

### Usage
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
