import sys, os
sys.path.append(os.pardir)
from mnist import load_mnist
import numpy as np
from PIL import Image

def img_show(img):
  pil_img = Image.fromarray(np.uint8(img))
  pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=False, flatten=True)

img = x_train[0]
label = t_train[0]
print(label)

img = img.reshape(28, 28)
img_show(img)
