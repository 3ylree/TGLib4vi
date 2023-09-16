import extcolors
from PIL import Image

# 나중에 naver map api 변경
img = Image.open("mapimg_1.png")
colors, pixel_count = extcolors.extract_from_image(img)

# RGB 컬러 불러오고, 색깔별 퍼센트로 정렬
pixel_output = 0
for c in colors:
    pixel_output += c[1]
    print(f'{c[0]} : {round((c[1] / pixel_count) * 100, 2)}%({c[1]})')
print(f'Pixels in output: {pixel_output} of {pixel_count}')

# RGB -> HSV 컬러 변환
