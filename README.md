# AnyPix - Pix anything!
## image pixelization tool working in console

Usage: python main.py --pallete [SEGA/NES] --power [num] --colors [num] --in [input file] --out [output file]

For example:

python main.py --pallete SEGA --power 8 --colors 256 --infile /path/to/image.png --outfile /path/to/pix_image.png

App is working good with *.png and *.jpg

For example, converting with power 8, pallete SEGA and 256 colors:

<image src="src/assets/test.jpg" height=128>Before</image>

<image src="src/assets/test_converted.jpg" height=128>After</image>


## Install
python -m venv venv
venv\Scripts\activate
pip install pillow
python main.py [arguments]

## Libraries
Pillow


## License
This project has MIT license. You can use it for any purpose, even commercially
