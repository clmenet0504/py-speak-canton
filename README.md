# speak-canton

A little experiment on creating a Cantonese (廣東話) text-to-speech program using your own voice.



## Installation 
Prerequisite : Python 3.9.0
### Libraries for Sound Recording
```bash
pip install sounddevice
pip install wavio
pip install scipy
```
### Libraries for Text to Cantonese Phonetic
```bash
pip install selenium
pip install urllib
```

## Usage
### Text to Cantonese Phonetic
```bash
python scrapping.py [sentence]
```
i.e python scrapping.py 你好嗎
