from PIL import Image, ImageFilter

img = Image.open('./history-in-hd-e5eDHbmHprg-unsplash.jpg')
img.thumbnail((200, 200))
img.save('thumbnail.jpg')