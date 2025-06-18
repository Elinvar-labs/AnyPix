import engine as eng
import os
import argparse


def run():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    parser = argparse.ArgumentParser(
                        prog='AnyPix',
                        description='Convert .png or .jpg image to pixelated image',
                        epilog='Usage: anypix.py --pallete <SEGA/NES> --power <num> --colors <num> --in <input file> --out <output file>')

    parser.add_argument("--pallete")
    parser.add_argument("--power")
    parser.add_argument("--colors")
    parser.add_argument('--infile')
    parser.add_argument('--outfile')
    engine = eng.Engine()
    args = parser.parse_args()
    # if args.<5:
    #     print("Error: Too few arguments")
    #     exit()
    input_path = ""
    if not os.path.isabs(str(args.infile)):
        input_path = os.path.join(dir_path, str(args.infile))
    if not os.path.isfile(args.infile):
        print(input_path)
        
        print("Path of the input file is Invalid")
        exit()
    if str(args.pallete) != "NES" and str(args.pallete) != "SEGA":
        print("Error: Unknown palette. Try SEGA or NES")
        exit()
    if int(args.colors) > 66000 or int(args.colors) < 0:
        print("Error: Unknown colors number. Try 0 < x < 65536")
        exit()    
    engine.pixelize(args.infile, args.outfile, palette_name=args.pallete, power=int(args.power), colors=int(args.colors))
        
if __name__ == "__main__":
    run()