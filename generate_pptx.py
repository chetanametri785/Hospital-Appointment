"""
Generates MediCare_Plus_Presentation.pptx using Python's standard library (zipfile).
Zero external dependencies required.
"""

import zipfile
import io
import os

def create_pptx(output_filename="MediCare_Plus_Presentation.pptx"):
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
    <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
    <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
    <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
    <Override PartName="/ppt/slides/slide1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
    <Override PartName="/ppt/slides/slide2.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
    <Override PartName="/ppt/slides/slide3.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
    <Override PartName="/ppt/slides/slide4.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
    <Override PartName="/ppt/slides/slide5.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
    <Override PartName="/ppt/slides/slide6.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
</Types>"""

    root_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
</Relationships>"""

    presentation_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
    <p:sldMasterIdLst>
        <p:sldMasterId id="2147483648" r:id="rId1"/>
    </p:sldMasterIdLst>
    <p:sldIdLst>
        <p:sldId id="256" r:id="rId2"/>
        <p:sldId id="257" r:id="rId3"/>
        <p:sldId id="258" r:id="rId4"/>
        <p:sldId id="259" r:id="rId5"/>
        <p:sldId id="260" r:id="rId6"/>
        <p:sldId id="261" r:id="rId7"/>
    </p:sldIdLst>
    <p:sldSz cx="12192000" cy="6858000"/>
    <p:notesSz cx="6858000" cy="12192000"/>
</p:presentation>"""

    pres_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
    <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide1.xml"/>
    <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide2.xml"/>
    <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide3.xml"/>
    <Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide4.xml"/>
    <Relationship Id="rId6" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide5.xml"/>
    <Relationship Id="rId7" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide6.xml"/>
</Relationships>"""

    slide_master_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
    <p:cSld>
        <p:spTree>
            <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
            <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
        </p:spTree>
    </p:cSld>
    <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
    <p:sldLayoutIdLst>
        <p:sldLayoutId id="2147483649" r:id="rId1"/>
    </p:sldLayoutIdLst>
</p:sldMaster>"""

    slide_master_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
    <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>"""

    slide_layout_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank">
    <p:cSld>
        <p:spTree>
            <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
            <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
        </p:spTree>
    </p:cSld>
    <p:clrMapOvr><a:masterClrMap/></p:clrMapOvr>
</p:sldLayout>"""

    slide_layout_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>"""

    theme_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="MediCare Blue">
    <a:themeElements>
        <a:clrScheme name="MediCare">
            <a:dk1><a:srgbClr val="0C2F55"/></a:dk1>
            <a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>
            <a:dk2><a:srgbClr val="1E293B"/></a:dk2>
            <a:lt2><a:srgbClr val="F0F7FF"/></a:lt2>
            <a:accent1><a:srgbClr val="0284C7"/></a:accent1>
            <a:accent2><a:srgbClr val="0369A1"/></a:accent2>
            <a:accent3><a:srgbClr val="38BDF8"/></a:accent3>
            <a:accent4><a:srgbClr val="10B981"/></a:accent4>
            <a:accent5><a:srgbClr val="F59E0B"/></a:accent5>
            <a:accent6><a:srgbClr val="EF4444"/></a:accent6>
            <a:hlink><a:srgbClr val="0284C7"/></a:hlink>
            <a:folHlink><a:srgbClr val="0369A1"/></a:folHlink>
        </a:clrScheme>
        <a:fontScheme name="Modern Sans">
            <a:majorFont><a:latin typeface="Segoe UI"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont>
            <a:minorFont><a:latin typeface="Segoe UI"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont>
        </a:fontScheme>
        <a:fmtScheme name="Office">
            <a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst>
            <a:lnStyleLst><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst>
            <a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst>
            <a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst>
        </a:fmtScheme>
    </a:themeElements>
</a:theme>"""

    slide_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>"""

    # Helper to generate slide XML with a header and bullet items
    def make_slide_xml(title_text, subtitle_text, bullet_items, is_dark=False, is_closing=False):
        bg_color = "08213B" if is_dark else "F8FAFC"
        title_color = "FFFFFF" if is_dark else "0C2F55"
        sub_color = "BAE6FD" if is_dark else "0284C7"
        text_color = "F0F7FF" if is_dark else "334155"
        accent_color = "0284C7"

        # Generate paragraphs
        paras_xml = ""
        for item in bullet_items:
            paras_xml += f"""
                <a:p>
                    <a:pPr marL="288000" indent="-288000">
                        <a:buFont typeface="Arial"/>
                        <a:buChar char="•"/>
                    </a:pPr>
                    <a:r>
                        <a:rPr lang="en-US" sz="1800" b="1">
                            <a:solidFill><a:srgbClr val="{accent_color}"/></a:solidFill>
                        </a:rPr>
                        <a:t>{item[0]}: </a:t>
                    </a:r>
                    <a:r>
                        <a:rPr lang="en-US" sz="1800">
                            <a:solidFill><a:srgbClr val="{text_color}"/></a:solidFill>
                        </a:rPr>
                        <a:t>{item[1]}</a:t>
                    </a:r>
                </a:p>
                <a:p><a:endParaRPr sz="800"/></a:p>
            """

        closing_extra = ""
        if is_closing:
            closing_extra = f"""
            <p:sp>
                <p:nvSpPr><p:cNvPr id="5" name="ThankYouBanner"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
                <p:spPr>
                    <a:xfrm><a:off x="1000000" y="4800000"/><a:ext cx="10192000" cy="1400000"/></a:xfrm>
                    <a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val 20000"/></a:avLst></a:prstGeom>
                    <a:solidFill><a:srgbClr val="0C2F55"/></a:solidFill>
                    <a:ln w="25400"><a:solidFill><a:srgbClr val="0284C7"/></a:solidFill></a:ln>
                </p:spPr>
                <p:txBody>
                    <a:bodyPr anchor="ctr"/>
                    <a:p>
                        <a:pPr algn="ctr"/>
                        <a:r>
                            <a:rPr lang="en-US" sz="2400" b="1"><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill></a:rPr>
                            <a:t>🏥 MediCare Plus Hospital Network</a:t>
                        </a:r>
                    </a:p>
                    <a:p>
                        <a:pPr algn="ctr"/>
                        <a:r>
                            <a:rPr lang="en-US" sz="1600"><a:solidFill><a:srgbClr val="BAE6FD"/></a:solidFill></a:rPr>
                            <a:t>24/7 Helpline: +1 (800) 456-9111  |  Email: appointments@medicareplus.org</a:t>
                        </a:r>
                    </a:p>
                </p:txBody>
            </p:sp>
            """

        return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
    <p:cSld>
        <p:spTree>
            <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
            <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
            
            <!-- Slide Background Shape -->
            <p:sp>
                <p:nvSpPr><p:cNvPr id="2" name="Background"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
                <p:spPr>
                    <a:xfrm><a:off x="0" y="0"/><a:ext cx="12192000" cy="6858000"/></a:xfrm>
                    <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
                    <a:solidFill><a:srgbClr val="{bg_color}"/></a:solidFill>
                </p:spPr>
            </p:sp>

            <!-- Slide Title and Subtitle Box -->
            <p:sp>
                <p:nvSpPr><p:cNvPr id="3" name="TitleBox"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
                <p:spPr>
                    <a:xfrm><a:off x="1000000" y="600000"/><a:ext cx="10192000" cy="1400000"/></a:xfrm>
                    <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
                </p:spPr>
                <p:txBody>
                    <a:bodyPr/>
                    <a:p>
                        <a:r>
                            <a:rPr lang="en-US" sz="3600" b="1">
                                <a:solidFill><a:srgbClr val="{title_color}"/></a:solidFill>
                            </a:rPr>
                            <a:t>{title_text}</a:t>
                        </a:r>
                    </a:p>
                    <a:p>
                        <a:r>
                            <a:rPr lang="en-US" sz="1800" i="1">
                                <a:solidFill><a:srgbClr val="{sub_color}"/></a:solidFill>
                            </a:rPr>
                            <a:t>{subtitle_text}</a:t>
                        </a:r>
                    </a:p>
                </p:txBody>
            </p:sp>

            <!-- Content Body Box -->
            <p:sp>
                <p:nvSpPr><p:cNvPr id="4" name="ContentBox"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
                <p:spPr>
                    <a:xfrm><a:off x="1000000" y="2200000"/><a:ext cx="10192000" cy="4000000"/></a:xfrm>
                    <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
                </p:spPr>
                <p:txBody>
                    <a:bodyPr/>
                    {paras_xml}
                </p:txBody>
            </p:sp>

            {closing_extra}

        </p:spTree>
    </p:cSld>
    <p:clrMapOvr><a:masterClrMap/></p:clrMapOvr>
</p:sld>"""

    # Data for the 6 slides
    slides_data = [
        # Slide 1: Introduction
        (
            "MediCare Plus Hospital Portal",
            "Modern Healthcare Appointment Booking & Live Status Tracking System",
            [
                ("Overview", "A clinical web application designed for patients to seamlessly schedule specialist consultations and track real-time queue tokens."),
                ("Visual Theme", "Professional Blue & White healthcare palette promoting clinical calmness, hygiene, and patient trust."),
                ("Environment", "Engineered to run effortlessly inside VS Code via integrated terminal, F5 debugger, or Live Server.")
            ],
            True,
            False
        ),
        # Slide 2: Objectives
        (
            "Objectives of the Website",
            "Eliminating Healthcare Bottlenecks Through Digital Transparency",
            [
                ("Eliminate OPD Congestion", "Eliminates physical queue crowding with scheduled appointments and allocated time slots."),
                ("Real-Time Transparency", "Gives patients immediate visibility into verification status, queue token numbers, and cabin rooms."),
                ("Staff Efficiency", "Provides receptionist and nursing staff with a centralized OPD operations desk for smooth check-ins."),
                ("Patient Autonomy", "Empowers patients with self-service rescheduling, fee-free cancellation, and printable passes.")
            ],
            False,
            False
        ),
        # Slide 3: Architecture & Core Capabilities
        (
            "Core Architecture & Booking Engine",
            "3-Step Guided Scheduling & Automatic Token Generation",
            [
                ("Step 1 (Patient Intake)", "Captures patient demographics, blood group, symptoms description, and consultation mode."),
                ("Step 2 (Specialist Matching)", "Dynamic filtering across 8 medical departments and 8+ board-certified physician profiles."),
                ("Step 3 (Slot Scheduling)", "Calendar date picker with morning, afternoon, and evening slot pills and real-time fee summary."),
                ("Instant Token Pass", "Generates unique Reference ID (e.g. MC-1001), queue token (T-08), and assigned OPD room.")
            ],
            False,
            False
        ),
        # Slide 4: Real-Time Status Tracking
        (
            "Live Booking Status Tracker",
            "5-Stage Visual Stepper & Patient Action Suite",
            [
                ("Live Progress Stepper", "Visual progress bar tracking: Requested -> Desk Review -> Confirmed -> In-Consultation -> Completed."),
                ("Instant Search", "Look up booking records by Appointment ID (e.g. MC-1001), phone number, or email."),
                ("Self-Service Rescheduling", "Patients can dynamically pick new dates and time slots, updating queue records immediately."),
                ("Official Print Slip", "Dedicated clean print view that formats official patient passes without navbar clutter.")
            ],
            False,
            False
        ),
        # Slide 5: Technical Highlights
        (
            "Technical Highlights & Design System",
            "Dependable, Zero-Dependency Web Architecture for VS Code",
            [
                ("Blue & White Clinical UI", "Tailored color spectrum (Deep Navy #08213b, Medical Blue #0284c7, Soft Ice #e0f2fe, and Crisp White)."),
                ("Zero-Dependency Server", "Pure Node.js HTTP server (server.js) that starts instantly without complex npm installations."),
                ("LocalStorage Persistence", "Pre-seeded realistic appointment data (MC-1001 to MC-1005) that saves all updates locally."),
                ("Responsive & Accessible", "Mobile-first layout, custom SVG icons, and smooth transitions across all viewports.")
            ],
            False,
            False
        ),
        # Slide 6: Conclusion & Thank You
        (
            "Thank You for Your Time!",
            "MediCare Plus - Elevating Healthcare Delivery and Patient Experience",
            [
                ("Impact", "Reduces physical waiting times by over 60% while providing 100% booking transparency."),
                ("Readiness", "Fully tested and validated to run out-of-the-box in VS Code with modern web standards."),
                ("Questions & Next Steps", "We welcome feedback and questions regarding the system architecture and implementation.")
            ],
            True,
            True
        )
    ]

    # Assemble the PPTX zip archive
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', content_types)
        z.writestr('_rels/.rels', root_rels)
        z.writestr('ppt/presentation.xml', presentation_xml)
        z.writestr('ppt/_rels/presentation.xml.rels', pres_rels)
        z.writestr('ppt/slideMasters/slideMaster1.xml', slide_master_xml)
        z.writestr('ppt/slideMasters/_rels/slideMaster1.xml.rels', slide_master_rels)
        z.writestr('ppt/slideLayouts/slideLayout1.xml', slide_layout_xml)
        z.writestr('ppt/slideLayouts/_rels/slideLayout1.xml.rels', slide_layout_rels)
        z.writestr('ppt/theme/theme1.xml', theme_xml)

        for i, slide_info in enumerate(slides_data, start=1):
            slide_xml_content = make_slide_xml(
                slide_info[0], slide_info[1], slide_info[2], slide_info[3], slide_info[4]
            )
            z.writestr(f'ppt/slides/slide{i}.xml', slide_xml_content)
            z.writestr(f'ppt/slides/_rels/slide{i}.xml.rels', slide_rels)

    print(f"Successfully generated {output_filename}")

if __name__ == '__main__':
    create_pptx()
