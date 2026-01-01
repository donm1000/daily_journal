import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch

# Function to create a daily work log
def create_daily_work_log(filename="daily_work_log_2026.pdf"):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    margin = 0.5 * inch
    line_spacing = 0.35 * inch

    total_days = 365  # 2025 is not a leap year

    for day in range(1, total_days + 1):
        dt = datetime.date(2026, 1, 1) + datetime.timedelta(days=day - 1)
        day_of_week = dt.strftime("%A")
        date_str = dt.strftime("%B %d, %Y")

        # Top Date and Day
        c.setFont("Helvetica-Bold", 14)
        c.drawString(margin, height - margin, f"{day_of_week}, {date_str}")

        y_pos = height - margin - 1.0 * inch

        # Morning Planning
        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, y_pos, "Morning Planning:")
        y_pos -= 0.3 * inch
        c.setFont("Helvetica", 11)
        for _ in range(8):
            c.line(margin, y_pos, width - margin, y_pos)
            y_pos -= line_spacing

        y_pos -= 0.3 * inch

        # Evening Summary
        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, y_pos, "Evening Summary:")
        y_pos -= 0.3 * inch
        c.setFont("Helvetica", 11)
        for _ in range(8):
            c.line(margin, y_pos, width - margin, y_pos)
            y_pos -= line_spacing

        y_pos -= 0.3 * inch

        # Tomorrow Planning
        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, y_pos, "Tomorrow Planning:")
        y_pos -= 0.3 * inch
        c.setFont("Helvetica", 11)
        for _ in range(8):
            c.line(margin, y_pos, width - margin, y_pos)
            y_pos -= line_spacing

        c.showPage()

    c.save()

if __name__ == "__main__":
    create_daily_work_log()
