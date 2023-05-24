from PIL import Image

    
def miniatura(input_file, size, output_file):
    """ funkcja miniatura(input_file, size, output_file)
    tworzy miniatury obrazu w formacie jpg o różnych rozmiarach.
    Input:
    input_file (str): Nazwa/ścieżka do pliku wejściowego.
    sizes (list): Lista zawierająca porządne rozmiary miniatury (w pikselach).
    output_file (str): Nazwa/ścieżka do pliku wyjściowego (bez rozszerzenia)."""
    img=Image.open(input_file)
    img2=img.resize((size))
    img2=img2.save(output_file)
            
miniatura(r"C:\Users\dbjd2\Desktop\Piesek.jpg", [200, 200], r"C:\Users\dbjd2\Desktop\Piesek2.jpg")