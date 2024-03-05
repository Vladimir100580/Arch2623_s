import matplotlib.pyplot as plt

# $|theta^2 = x_1$
def latex_to_png(latex_str):
    latex_str = r"\log_{3.1}^{2n}{(\frac{2}{t})}"
    fig = plt.figure(figsize=(0.2, 0.2), frameon=False)  # facecolor=(0.6, 0.4, 0.5) - цвет заливки

    plt.axis('off')
    plt.text(0.5, 0.5, f"${latex_str}$", alpha=1, size=50, ha="center", va="center")
    pdf_path = "C:/Users/vovar_h1dqlw1/IdeaProjects/Works/Paradigm_HW/GB_Python_Adv/result.png "

    plt.savefig(pdf_path, format="png", bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)

    return True

latex_formula = r"\log_{3.1}^{2n}{(\frac{2}{t})}"
# latex_formula = "\\theta^2 = x_1 + y_2"
a1s1 = latex_to_png(latex_formula)

# image = Image.open(png_path)
# image.show()
