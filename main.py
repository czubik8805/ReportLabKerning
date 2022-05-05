from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


pdfmetrics.registerFont(
    TTFont(
        'arial',
        'arial.ttf')
)

c = canvas.Canvas("hello.pdf")
c.setFont('arial', 32)
c.drawString(10, 450, "Toned Avenue")
c.showPage()
c.save()
