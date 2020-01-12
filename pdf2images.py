from pdf2image import convert_from_path, convert_from_bytes

images = convert_from_path('put_the_path')
i = 1
for image in images:
	image.save('name' + str(i) + '.jpg', 'JPEG')
	i = i + 1
