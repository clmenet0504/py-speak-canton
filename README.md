# speak-canton

A little experiment on creating a Cantonese (廣東話) text-to-speech program using your own voice.



## Installation 
* Prerequisite : Python 3.9.0
### Libraries for Sound Recording
```bash
pip install sounddevice
pip install wavio
pip install scipy
```
### Libraries for Text to Cantonese Phonetic
```powershell
pip install selenium
pip install urllib
```

## Usage
### Text to Cantonese Phonetic
#### Input
```bat
python scrapping.py [sentence]
```
i.e **python scrapping.py 你好嗎**

#### Expected output
```bat
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
