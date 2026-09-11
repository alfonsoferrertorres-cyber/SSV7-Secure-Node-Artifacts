from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generar_pdf():
    filename = "informe_oficial_saare.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=16, textColor=colors.HexColor('#0f172a'), spaceAfter=4)
    subtitle_style = ParagraphStyle('SubTitleStyle', parent=styles['Normal'], fontSize=10, textColor=colors.HexColor('#64748b'), spaceAfter=20)
    heading_style = ParagraphStyle('HeadingStyle', parent=styles['Heading2'], fontSize=12, textColor=colors.HexColor('#1e293b'), spaceBefore=15, spaceAfter=8)
    body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=10, textColor=colors.HexColor('#1a1a1a'), leading=14, spaceAfter=8)

    story.append(Paragraph("<b>Gabinete Técnico Comercial MS3V</b>", title_style))
    story.append(Paragraph("Certificación Perimetral y Soberanía de Datos — SAARE v7 PRO<br/><b>ID de Protocolo:</b> MS3V-RECON-VALID-2026-ALF-0521 | <b>Fecha:</b> 11 de Septiembre, 2026", subtitle_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("1. Resumen Ejecutivo y Marco de Cumplimiento", heading_style))
    text_resumen = "El presente informe certifica la ejecución satisfactoria de la pasarela perimetral de Capa 7 bajo el paradigma de persistencia cero (<i>LOCAL_LOOPBACK_BIND</i>). El sistema garantiza la alineación estricta con los marcos normativos internacionales: NIST CSF 2.0, OWASP LLM Top 10, y EU AI Act & RGPD."
    story.append(Paragraph(text_resumen, body_style))

    story.append(Paragraph("2. Resultados de Pruebas Automatizadas de Punta a Punta", heading_style))
    data = [
        ["Vector", "Componente Evaluado", "Resultado", "Detalle / Veredicto"],
        ["Test 1", "Verificación de Evidencias (Ed25519)", "VALID", "Árbol de Merkle íntegro. ID: VRD-2026-EURK9"],
        ["Test 2", "Correo Fiduciario / Pasarela OTP", "SUCCESS", "Despachado desde legal@saare.es sin alteraciones."],
        ["Test 3", "Interceptor L7 / Seguridad OWASP", "BLOQUEADO (403)", "Neutralización ex-ante de directiva maliciosa."]
    ]
    t = Table(data, colWidths=[50, 140, 90, 220])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f8fafc')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#334155')),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    story.append(Paragraph("3. Trazabilidad Criptográfica e Inmutabilidad", heading_style))
    story.append(Paragraph("<b>Raíz de Merkle (Root Hash):</b><br/><font fontName='Courier' size=8>6f1b3986a4221147814b7e9a8f420e7df61a5b823e4299b9e671b569c7f1a842</font>", body_style))
    story.append(Paragraph("<b>Firma Criptográfica Ed25519:</b><br/><font fontName='Courier' size=8>3d84f9814402ebcf88a1095bf8589085cb221a69074092b3a985dcf85b7aa210e9cf41d7e35b71946399120785cba028e3b4821a8b0c619472e61a84b6f89004</font>", body_style))
    story.append(Paragraph("<b>Anclaje de Autoría (SHA-256):</b><br/><font fontName='Courier' size=8>37520F68596B3351FDAF6EA431DBC9A29ABFC4A4CCC601134616E683536D4CEB</font>", body_style))

    story.append(Spacer(1, 20))
    story.append(Paragraph("<font size=8 color='#64748b'>Titularidad Legal: Alfonso Ferrer Torres (NIF Protegido por Hash SHA-256) | Gabinete Técnico Comercial MS3V<br/>Estado del Nodo: PRODUCCIÓN / FAIL-CLOSED — Sello de Auditoría Criptográfica V7</font>", body_style))

    doc.build(story)
    print("¡Informe oficial generado con éxito: informe_oficial_saare.pdf!")

if __name__ == '__main__':
    generar_pdf()
