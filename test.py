
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("local", help="local path to image")
parser.add_argument("-l","--local", action="store_true", help="path to local file")
args = parser.parse_args()





image_path = args.local

print (image_path)