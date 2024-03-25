from fpdf import FPDF
pdf = FPDF()
# imagelist is the list with all image filenames
imagelist = ['image1.png', 'image2.png', 'image3.png']

for image in imagelist:
    pdf.add_page()
    pdf.image(image,0,0,210,297)
pdf.output("file1.pdf", "F")
