from PIL import Image
import matplotlib.pyplot as plt

def agruparPixels(pixelsDesagrupados):
    agrupados = {}

    for i in range(0, 256, 1):
        agrupados[f'{i}'] = 0
    
    for pixel in pixelsDesagrupados:
        agrupados[f'{pixel}'] += 1

    return agrupados

def lerPixels():
    print('Iniciando leitura')
    
    lista = []
    for y in range(altura):
        for x in range(largura):
            pixel = imagem.getpixel((x, y))
            valor_r = pixel[0]
            valor_g = pixel[1]
            valor_b = pixel[2]

            pixel = (valor_r + valor_g + valor_b) // 3

            lista.append(pixel)
            
        if y == altura / 4:
            print('25%')
        elif y == altura / 2:
            print('50%')
        elif y == (altura * 3) / 4:
            print('75%')

    print('Concluído')
    
    return lista


# Transforma a imagem em um array de niveis de cinza
imagem = Image.open('imagem.jpg')
largura, altura = imagem.size
pixels = lerPixels()

# Gera um dicinário com a quantidade de pixels por valore de cinza da imagem (histograma)
pixelsAgrupados = agruparPixels(pixels)

# Gera o gráfico do histograma
eixoX = list(pixelsAgrupados.keys())
eixoY = list(pixelsAgrupados.values())

plt.bar(eixoX, eixoY, color='black')
plt.xlabel('Niveis de cinza')
plt.ylabel('Pixels')
plt.title('Histograma da imagem')
plt.show()


