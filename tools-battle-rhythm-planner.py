from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

F = '/tmp/claude-0/-home-user/75f577f6-91c6-5063-9579-3eba1a586c30/scratchpad/fonts'
pdfmetrics.registerFont(TTFont('Bebas',   f'{F}/BebasNeue.ttf'))
pdfmetrics.registerFont(TTFont('Inter',   f'{F}/Inter-400.ttf'))
pdfmetrics.registerFont(TTFont('InterSb', f'{F}/Inter-600.ttf'))

# Brand palette, inverted for print: navy ink and gold accents on white paper.
NAVY  = HexColor('#0d1220')
STEEL = HexColor('#1e2d45')
GOLD  = HexColor('#c9a84c')
GOLDD = HexColor('#9a7c35')
MUTED = HexColor('#5b6a7d')
RULE  = HexColor('#c3ccd8')
FAINT = HexColor('#e6eaf0')

W, H = letter
M  = 44.0
CW = W - 2 * M
OUT = '/home/user/ironbridgestrateygroup/assets/battle-rhythm-planner.pdf'

c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle('The Battle Rhythm Planner - Corporate Leaders Edition')
c.setAuthor('Kenyatta S. Williams - Ironbridge Strategy Group, LLC')
c.setSubject('A one-page daily planning framework for corporate leaders.')
c.setCreator('Ironbridge Strategy Group')

def tracked(x, y, text, font, size, color, track=0.0):
    """Letter-spaced text. Resets Tc to 0 afterwards: this reportlab build
    leaks char spacing into later draws, which silently widens every
    subsequent drawString and breaks right-aligned measurement."""
    t = c.beginText(x, y)
    t.setFont(font, size)
    t.setFillColor(color)
    t.setCharSpace(track)
    t.textOut(text)
    t.setCharSpace(0)
    c.drawText(t)

def twidth(text, font, size, track=0.0):
    return pdfmetrics.stringWidth(text, font, size) + track * max(0, len(text) - 1)

def rules(y, n, gap, x=M, width=CW):
    """n writing rules. Returns the y of the last one."""
    c.setStrokeColor(RULE); c.setLineWidth(0.6)
    for i in range(n):
        c.line(x, y - i * gap, x + width, y - i * gap)
    return y - (n - 1) * gap

def section(y, label, hint):
    """Gold tab, Bebas label, muted hint, hairline underline.
    Returns the y of the underline."""
    c.setFillColor(GOLD); c.rect(M, y - 1.5, 3, 13, stroke=0, fill=1)
    tracked(M + 10, y, label, 'Bebas', 13, NAVY, 2.2)
    if hint:
        tracked(M + 10 + twidth(label, 'Bebas', 13, 2.2) + 10, y + 1.2,
                hint, 'Inter', 7.6, MUTED, 0.9)
    c.setStrokeColor(FAINT); c.setLineWidth(0.8)
    c.line(M, y - 8, M + CW, y - 8)
    return y - 8

def two_col(y, left, right, split, rows, gap):
    """Labelled two-column ruled block. Returns y below the last rule."""
    tracked(M, y, left, 'Inter', 6.8, MUTED, 1.5)
    tracked(M + split + 14, y, right, 'Inter', 6.8, MUTED, 1.5)
    y -= 15
    c.setStrokeColor(RULE); c.setLineWidth(0.6)
    for _ in range(rows):
        c.line(M, y, M + split, y)
        c.line(M + split + 14, y, M + CW, y)
        y -= gap
    return y + gap

GAP = 30          # space between the end of one block and the next section head

# ── HEADER ───────────────────────────────────────────────────────────────
y = H - M - 20
tracked(M, y, 'BATTLE RHYTHM PLANNER', 'Bebas', 30, NAVY, 3.4)
c.setFillColor(GOLD); c.rect(M, y - 12, 132, 2.6, stroke=0, fill=1)

tracked(M, y - 27, 'CORPORATE LEADERS EDITION', 'Inter', 7.6, MUTED, 1.9)
sw = twidth('CORPORATE LEADERS EDITION', 'Inter', 7.6, 1.9)
tracked(M + sw + 8,  y - 27, '|', 'Inter', 7.6, RULE, 0)
tracked(M + sw + 16, y - 27, 'IRONBRIDGE STRATEGY GROUP', 'Inter', 7.6, GOLDD, 1.9)

for lbl, dy in (('DATE', -2), ('DAY OF WEEK', -20)):
    lx = W - M - 118
    tracked(lx, y + dy, lbl, 'Inter', 7.6, MUTED, 1.9)
    c.setStrokeColor(STEEL); c.setLineWidth(0.9)
    c.line(lx + twidth(lbl, 'Inter', 7.6, 1.9) + 8, y + dy - 2, W - M, y + dy - 2)

y -= 44
c.setStrokeColor(STEEL); c.setLineWidth(1.4); c.line(M, y, M + CW, y)

# ── 1. DAILY MISSION ─────────────────────────────────────────────────────
y = section(y - 26, 'DAILY MISSION', 'YOUR SINGLE FOCUS FOR THE DAY')
y = rules(y - 24, 2, 26)

# ── 2. TOP 3 PRIORITIES ──────────────────────────────────────────────────
y = section(y - GAP, 'TOP 3 PRIORITIES', 'RANKED BY IMPACT')
y -= 24
for n in ('1', '2', '3'):
    c.setStrokeColor(STEEL); c.setLineWidth(0.9)
    c.rect(M, y - 3.5, 9, 9, stroke=1, fill=0)
    tracked(M + 17, y - 1.5, n, 'Bebas', 12, GOLDD, 0)
    c.setStrokeColor(RULE); c.setLineWidth(0.6)
    c.line(M + 28, y - 4, M + CW, y - 4)
    y -= 27
y += 27 - 4

# ── 3. PEOPLE CHECK-IN ───────────────────────────────────────────────────
y = section(y - GAP, 'PEOPLE CHECK-IN', 'WHO NEEDS YOUR ATTENTION TODAY')
y = two_col(y - 16, 'NAME', 'WHAT THEY NEED FROM ME', 150, 4, 24)

# ── 4. DECISION LOG ──────────────────────────────────────────────────────
y = section(y - GAP, 'DECISION LOG', 'WHAT I DECIDED, AND WHY')
y = two_col(y - 16, 'DECISION', 'REASONING', 232, 3, 24)

# ── 5. AFTER-ACTION REVIEW ───────────────────────────────────────────────
y = section(y - GAP, 'AFTER-ACTION REVIEW', '3 QUESTIONS, 5 MINUTES')
y -= 20
for q in ('What went right today?',
          'What went wrong, and what caused it?',
          'What will I do differently tomorrow?'):
    c.setFillColor(GOLD); c.rect(M + 1, y + 1.5, 4, 4, stroke=0, fill=1)
    c.setFont('InterSb', 8.4); c.setFillColor(STEEL)
    c.drawString(M + 12, y, q)
    c.setStrokeColor(RULE); c.setLineWidth(0.6)
    c.line(M + 12, y - 15, M + CW, y - 15)
    y -= 30

# ── FOOTER ───────────────────────────────────────────────────────────────
fy = M + 6
c.setStrokeColor(FAINT); c.setLineWidth(0.8); c.line(M, fy + 20, M + CW, fy + 20)
tracked(M, fy + 6, 'IRONBRIDGE STRATEGY GROUP', 'Bebas', 10, GOLDD, 2.6)
c.setFont('Inter', 7.2); c.setFillColor(MUTED)
c.drawRightString(M + CW, fy + 6, 'Run the rhythm daily. Discipline compounds.')

print('content ends at y =', round(y), '| footer rule at y =', fy + 20)
c.showPage(); c.save()
print('wrote', OUT)
