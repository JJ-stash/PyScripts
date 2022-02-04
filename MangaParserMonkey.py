import os
import requests
from fpdf import FPDF
from bs4 import BeautifulSoup

print("Choice:\n1. One Punch Man\n2. Attack on Titan\n3. Berserk\n")

data = {
    '1': "https://read-one-punchman.com/comic/one-punch-man-chapter-{}/",
    '2': 'https://readshingekinokyojin.com/manga/shingeki-no-kyojin-chapter-{}/',
    '3': 'https://readberserk.com/chapter/berserk-chapter-{}/'
    }
    
    # Berserk has .jpg files that shouldn't be included in pdf, try a way to fix it

manga = str(input("Enter Number of Chosen One: "))
if manga not in data:
    print("You're not very bright are you ?\nTry again fool.")
    exit()

chapter = input("Enter Chapter Number: ")
try:
    int(chapter)
except(ValueError):
    print("I said Number!")
    exit()

startURL = data[manga]
endURL = startURL.format(chapter)

def imagedown(endURL, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(endURL)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    page = 0
    for image in images:
        page += 1
        name = f'Page {page}'
        link = image['src']
        with open(name + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)

def pdfmaker(folder):
    pdf = FPDF(unit='mm')
    pdf.set_auto_page_break(0)

    try:
        os.chdir(folder)
    except:
        pass
    all_files = os.listdir()
    all_images = [f for f in all_files if not f.endswith('.pdf')]
    
    all_images = sorted(all_images, key=lambda x: float(x[4:-4]))
    print(all_images)

    try:
        for img in all_images:
            pdf.add_page()
            pdf.image(img, 0, 0, w=210, h=297)
            os.remove(img)
    except:
        pass

    pdf.output(f"Chapter {chapter}.pdf")
    print("Done Sewing")


imagedown(endURL, 'Manga')
pdfmaker('Manga')

