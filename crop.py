import cv2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("image_path", help='path of the image to open: ../test.jpg')
parser.add_argument("save_path", help = 'where to save cropped images')
parser.add_argument("height", help='height of crop area in pixels: int')
parser.add_argument("width", help='width of crop area in pixels: int')
args = parser.parse_args()

path = args.image_path
save = args.save_path
height, width = int(args.height), int(args.width)



def main(path, save, height, width):
    name = os.path.split(path)[1]
    name = name.split('.')[0]
    drawing = False
    def draw_rec(x, y, height, width, img):
        global sy, sx, ey, ex
        nimg = img.copy()
        sy = int(y - height/2)
        sx = int(x - width/2)
        ey = int(y + height/2)
        ex = int(x + width/2)
        cv2.rectangle(nimg, (sx, sy), (ex, ey), (255,0,0))
        cv2.imshow('image', nimg)

    def get_mouse(event,x,y,flags,param):    
        global mouseX, mouseY, drawing
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            mouseX, mouseY = x, y
            print(x, y)
            draw_rec(x, y, height, width, img)

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing is True:
                mouseX, mouseY = x, y
                print(x,y)
                draw_rec(x, y, height, width, img)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            mouseX, mouseY = x, y
            print(x,y)
            draw_rec(x, y, height, width, img)   

    cv2.namedWindow('image')
    cv2.setMouseCallback('image',get_mouse)
    img = cv2.imread(path)

    while True:         
        cv2.imshow('image', img)
        cv2.waitKey(0)

        if cv2.waitKey(0) == ord('c'):
            crop = img[sy:ey,sx:ex].copy()
            cv2.imwrite(save+'/'+name+str(height)+'x'+str(width)+'.jpg', crop)
            print('Saved!')

        # Wait for q key to exit    
        if cv2.waitKey(25):
            print('Exit')
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main(path, save, height, width)