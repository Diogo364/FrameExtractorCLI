# Frame Extractor CLI

## Description
This CLI program extracts frames throughout a video length. 

## Table of contents
- [Frame Extractor CLI](#frame-extractor-cli)
  - [Description](#description)
  - [Table of contents](#table-of-contents)
  - [How to use](#how-to-use)
    - [Frame Extractor](#frame-extractor)
      - [Description:](#description-1)
      - [CLI Parameters:](#cli-parameters)
      - [Example of usage:](#example-of-usage)
    - [Instalation](#instalation)
  - [Technologies](#technologies)
  - [Autor](#autor)

---
## How to use
### Frame Extractor
#### Description:
CLI application to extract frames from all videos within a specific directory `A`, saving them as png images within a root directory  `B` following the same folder structure.

By calling the CLI application you will define the root directory for all videos, `A`, and the root directory for all frames to be saved, `B`. The same folder structure WILL be created within directory `B` if it is different from `A`

#### CLI Parameters:
- `-i` or `--input_dir`:
  - Root directory for video searching.
- `-o` or `--output-dir`:
  - Root directory for frame saving.
- `-n` or `--frames`:
  - Frame rate or number of frames to be taken from the video:
    - Int: Number of frames to be taken.
    - Float: Frame rate in which a frame will be taken.
- `-e` or `--extension`:
  - Extension of the video to be searched.
    - Default: MP4

#### Example of usage:
> ```$ python main.py -i ./videos -o ./frames -n 10 -e MP4```

### Instalation
All requirements are in the `requirements.txt` file. From pip, just run in the terminal the following command and you are ready to go.
> ```$ pip install -r requirements.txt```
## Technologies

- `Python>=3.8`
- `OpenCV>=4.5`

## Autor

<a href="https://github.com/Diogo364" >
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/44041957?s=400&u=44d208aa5d0b6df75c0bb60e2583fe6015cc0ed0&v=4" width="100px;" alt=""/>
</a>
<br>

[Diogo Nascimento](https://github.com/Diogo364)
[![Linkedin Badge](https://img.shields.io/badge/-Diogo-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/diogo-telheiro-do-nascimento/)](https://www.linkedin.com/in/diogo-telheiro-do-nascimento/) 
[![Gmail Badge](https://img.shields.io/badge/-diogotnascimento94@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:diogotnascimento94@gmail.com)](mailto:diogotnascimento94@gmail.com)