# AI-ebook-to-audiobook
- program uses [suno-ai/bark](https://github.com/suno-ai/bark) to convert ebook to audiobook
- simply put a text in the ebook.txt file and it will be converted to a wav file
- there is a choice of Polish and English voice
- if there is too much text in one line it will not be converted properly
- it is recommended to have one or two sentences per line
- if the program is stopped it will resume after restarting
- ffmpeg and ffprobe
- to run install:
```
pip install bark
pip install scipy
pip install ipython
pip install pydub
```
