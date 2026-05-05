from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def export_pdf(device, battery, storage):
    pdf = SimpleDocTemplate("device_report.pdf")
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("DroidInspect Report", styles['Title']))
    content.append(Spacer(1, 20))

    content.append(Paragraph("Device Info", styles['Heading2']))
    for k, v in device.items():
        content.append(Paragraph(f"{k}: {v}", styles['Normal']))

    content.append(Spacer(1, 20))
    content.append(Paragraph("Battery Info", styles['Heading2']))
    content.append(Paragraph(str(battery), styles['Normal']))

    content.append(Spacer(1, 20))
    content.append(Paragraph("Storage Info", styles['Heading2']))
    content.append(Paragraph(str(storage), styles['Normal']))

    pdf.build(content)

    return "PDF report saved"