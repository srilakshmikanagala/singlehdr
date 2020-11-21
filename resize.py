from PIL import Image
import sys
import os
if __name__ == '__main__':
  if len(sys.argv) < 2:
        print("Usage:  python run.py [image_path]")
        sys.exit()
  runcase=int(sys.argv[1])
  if(runcase==1):
    image=Image.open(sys.argv[2])
    resized=image.resize((1000,1000))
    resized.save('resized.jpg')
  elif(runcase==2):
    original=Image.open(sys.argv[2])
    width, height = original.size
    final=Image.open(sys.argv[3])
    resized_3=final.resize((width,height))
    resized_3.save('final_output.jpg')
