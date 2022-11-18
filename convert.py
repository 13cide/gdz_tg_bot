import pdfkit

path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)


def make_pdf(url, path):
    pdfkit.from_string(input=url, output_path=path, configuration=config)
