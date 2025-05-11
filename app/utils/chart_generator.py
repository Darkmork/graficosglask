import matplotlib.pyplot as plt
from io import BytesIO


def generate_chart(chart_type, x_data, y_data, title, x_label, y_label):
    plt.figure(figsize=(10, 6))

    if chart_type == 'line':
        plt.plot(x_data, y_data)
    elif chart_type == 'bar':
        plt.bar(x_data, y_data)
    elif chart_type == 'pie':
        plt.pie(y_data, labels=x_data, autopct='%1.1f%%')
    else:
        raise ValueError("Tipo de gráfico no soportado")

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)

    # Guardar la imagen en un buffer
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return img