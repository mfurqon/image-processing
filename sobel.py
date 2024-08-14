# Meng-import library
import cv2

# Buat fungsi untuk menyesuaikan ukuran gambar
def show_resized_image(window_name, image, width, height):
    resized_image = cv2.resize(image, (width, height))
    cv2.imshow(window_name, resized_image)
    cv2.waitKey(0)

# Baca gambar asli
img = cv2.imread('img\gambar-gunung-dari-samping-3.jpg')
# Display original image
show_resized_image(' Gambar Original', img, 600, 400)
cv2.waitKey(0)

# Konversi ke skala abu-abu
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Mengaburkan gambar untuk deteksi tepi yang lebih baik
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

# Deteksi tepi Sobel
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Deteksi Tepi Sobel pada sumbu Y
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Deteksi Tepi Sobel pada sumbu X
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Deteksi Tepi Sobel kombinasi sumbu X dan Y
# Menampilkan gambar Deteksi Tepi Sobel
show_resized_image('Sobel X', sobelx, 600, 400)
cv2.waitKey(0)
show_resized_image('Sobel Y', sobely, 600, 400)
cv2.waitKey(0)
show_resized_image('Sobel X Y Dengan Sobel() function', sobelxy, 600, 400)
cv2.waitKey(0)