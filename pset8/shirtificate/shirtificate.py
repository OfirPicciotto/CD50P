from fpdf import FPDF

class Shirtificate:
    def __init__(self, name):
        self.name = name
        self.make_shirt()

    @classmethod
    def get_name(cls):
        name = input("Name: ").strip()
        return cls(name)


    def make_shirt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font("helvetica", "B", 16)
        pdf.cell(0, 50, border=0, align="C", txt="CS50 Shirtificate")
        pdf.ln()
        pdf.image(
            "shirtificate.png",
            x=15,
            y=(297 / 4),
            w=180,
            alt_text=f"A Harvard shirt with the words: {self.name} took CS50",
        )
        pdf.set_font("helvetica", "B", size=28)
        pdf.set_text_color(255, 153, 255)
        pdf.cell(0, 150, border=0, align="C", txt=f"{self.name} took CS50")
        pdf.output("shirtificate.pdf")


def main():
    Shirtificate.get_name()


if __name__ == "__main__":
    main()