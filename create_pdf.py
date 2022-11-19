from fpdf import FPDF
import fitz


def create_pdf(images, out):
    pdf = FPDF(orientation="landscape")
    pdf.add_page()
    for i in images:
        pdf.image(i, w=280, h=200)
    pdf.output(f"trash/{out}_tmp.pdf")
    pdf.close()
    a = fitz.open(f"trash/{out}_tmp.pdf")
    a.delete_page(0)
    a.save(f"{out}.pdf")


create_pdf(["pdf/Aleksey_0.png", "pdf/Aleksey_1.png", "pdf/Aleksey_2.png"], "test")
