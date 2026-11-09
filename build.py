# -*- coding: utf-8 -*-
"""LipoSow 農翔誌 — 多頁靜態知識網站生成器"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
BRAND = "農翔誌"
BRAND_EN = "LipoSow"
SITE_URL = "https://www.agrisky.example"
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Crect width='40' height='40' rx='9' fill='%231E5A44'/%3E%3Cpath d='M9 22h22' stroke='%23E5EFE9' stroke-width='2.6' stroke-linecap='round'/%3E%3Ccircle cx='9.5' cy='18.5' r='3.6' fill='none' stroke='%23E5EFE9' stroke-width='2.2'/%3E%3Ccircle cx='9.5' cy='25.5' r='3.6' fill='none' stroke='%23E5EFE9' stroke-width='2.2'/%3E%3Ccircle cx='30.5' cy='18.5' r='3.6' fill='none' stroke='%23E5EFE9' stroke-width='2.2'/%3E%3Ccircle cx='30.5' cy='25.5' r='3.6' fill='none' stroke='%23E5EFE9' stroke-width='2.2'/%3E%3C/svg%3E"

def esc(s):
    return (s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"))

# ============================================================
# 導覽結構：六支柱 × (MegaMenu 欄位 / 側欄與目錄條目)
# ============================================================
PILLARS = [
  {"slug":"tech","name":"無人機技術","tag":"技術基礎","color":"sky",
   "menu":[["硬體設備",
      ("tech-drones","農用無人機機型怎麼選"),
      ("tech-starter","無人機技術怎麼入門"),
      ("tech-power","電池與動力系統"),
      ("tech-nav","定位、避障與導航")],
    ["感測與影像",
      ("tech-sensors","多光譜、熱影像拍攝"),
      ("tech-ai","AI 辨識病蟲與缺肥"),
      ("tech-cloud","雲端資料處理")],
    ["自動飛行",
      ("tech-autopilot","自動航線與任務規劃"),
      ("tech-variable","變量施作與處方圖"),
      ("tech-fleet","機隊與自動機巢")]],
   "topics":[
      ("tech-drones","農用無人機機型怎麼選","先分清楚植保、測繪與多功能三類，再依田塊與預算選機。"),
      ("tech-starter","無人機技術怎麼入門","從飛行原理、感測判讀到任務規劃，三層建立技術底子。"),
      ("tech-power","電池與動力系統","續航是農用機最主要的限制，換電與電池管理是作業核心。"),
      ("tech-nav","定位、避障與導航","RTK、慣性導航與避障感測，決定精準度與安全性。"),
      ("tech-sensors","多光譜、熱影像拍攝","把作物狀況「拍」成數據，是精準農業的第一步。"),
      ("tech-ai","AI 辨識病蟲與缺肥","用影像辨識找出雜草、病蟲與缺肥，輔助人工判讀。"),
      ("tech-cloud","雲端資料處理","拍攝資料上雲、生成處方圖，再回傳給機具作業。"),
      ("tech-autopilot","自動航線與任務規劃","從「手飛」走向「任務」，航線、返航與斷航續飛。"),
      ("tech-variable","變量施作與處方圖","依處方圖動態調整施藥施肥量，哪裡有問題才處理哪裡。"),
      ("tech-fleet","機隊與自動機巢","多機協同與自動機場，下一代省工農業的方向。")]},
  {"slug":"agri","name":"農業產業鏈","tag":"實務應用","color":"sky",
   "menu":[["種植前",
      ("agri-pre","田區勘測與面積量測"),
      ("agri-soil","土壤分區與種植規劃"),
      ("agri-slope","山坡地風險評估")],
    ["種植管理中",
      ("agri-monitor","作物生長與逆境監測"),
      ("agri-spray","植保噴灑與飄移防護"),
      ("agri-sow","播種、撒肥與粒劑"),
      ("agri-assist","驅鳥、授粉與山區運補")],
    ["收成後與下游",
      ("agri-post","產量預估與採收研判"),
      ("agri-disaster","災害勘災與損失評估"),
      ("agri-trace","農地履歷與品牌行銷")],
    ["服務生態系",
      ("agri-service","飛防與測繪服務隊"),
      ("agri-chain","機具維修供應鏈")]],
   "topics":[
      ("agri-pre","田區勘測與面積量測","用空拍把面積、地形與分區一次量清楚，省下踏田時間。"),
      ("agri-soil","土壤分區與種植規劃","結合土壤資料分區管理，種植方案更貼近每一塊田。"),
      ("agri-slope","山坡地風險評估","坡地與零碎農地風險高，空拍先評估開發與作業難度。"),
      ("agri-monitor","作物生長與逆境監測","定期空拍追蹤生長，提早發現缺水、缺肥與病蟲害。"),
      ("agri-spray","植保噴灑與飄移防護","噴灑標準流程、霧滴控制與藥劑飄移防護。"),
      ("agri-sow","播種、撒肥與粒劑","種子直播、粒肥與粒劑撒布，速度快且均勻。"),
      ("agri-assist","驅鳥、授粉與山區運補","驅鳥、輔助授粉與物資運補的輔助角色。"),
      ("agri-post","產量預估與採收研判","從產量預估到採收時機，把數據延伸到收成之後。"),
      ("agri-disaster","災害勘災與損失評估","颱風、淹水與火災後的空中勘災。"),
      ("agri-trace","農地履歷與品牌行銷","空拍影像做成履歷，是溯源與行銷好素材。"),
      ("agri-service","飛防與測繪服務隊","外包噴藥與測繪服務的商業模式與合作方式。"),
      ("agri-chain","機具維修供應鏈","機體、電池、維修與數據平台的服務供應鏈。")]},
  {"slug":"life","name":"無人機與生活","tag":"生活延伸","color":"amber",
   "menu":[["休閒空拍",
      ("life-record","旅行、風景空拍"),
      ("life-event","活動與婚禮紀錄")],
    ["生活服務",
      ("life-deliver","山區、偏鄉配送"),
      ("life-patrol","巡邏、搜救與勘查")],
    ["檢查與維運",
      ("life-inspect","屋頂、外牆與太陽能巡檢"),
      ("life-site","工地進度紀錄")],
    ["玩樂與學習",
      ("life-starter","新手空拍入門"),
      ("life-race","競速與花式飛行"),
      ("life-edu","親子科普課程")]],
   "topics":[
      ("life-record","旅行、風景空拍","用空拍記錄旅程與風景，最親民的入門用法。"),
      ("life-event","活動與婚禮紀錄","為重要時刻留下空中視角的獨特畫面。"),
      ("life-deliver","山區、偏鄉配送","偏鄉小件配送試驗，縮短最後一哩。"),
      ("life-patrol","巡邏、搜救與勘查","社區、河道與山坡巡邏，以及火災、搜救勘查。"),
      ("life-inspect","屋頂、外牆與太陽能巡檢","空中巡檢高處設施，安全又省力。"),
      ("life-site","工地進度紀錄","工地進度空拍，比地面紀錄更直觀、可追溯。"),
      ("life-starter","新手空拍入門","怎麼挑第一台機、怎麼安全飛、先練什麼。"),
      ("life-race","競速與花式飛行","無人機的另一種運動玩法。"),
      ("life-edu","親子科普課程","從玩樂中認識科技與安全。")]},
  {"slug":"reg","name":"法規安全成本","tag":"合規與風險","color":"sky",
   "menu":[["法規規範",
      ("reg-law","機體登記與飛手證照"),
      ("reg-no-fly","禁飛區與申請"),
      ("reg-env","噴藥的環境責任")],
    ["作業安全",
      ("reg-weather","天氣條件判斷"),
      ("reg-obstacle","避障與緊急處置"),
      ("reg-drift","藥劑飄移與鄰田爭議")],
    ["成本與經營",
      ("reg-cost","投入與維持成本"),
      ("reg-model","自購、合作社、外包")]],
   "topics":[
      ("reg-law","機體登記與飛手證照","台灣無人機法規重點：登記、證照與飛行紅線。"),
      ("reg-no-fly","禁飛區與申請","禁飛區、限制區與專案申請，起飛前必查。"),
      ("reg-env","噴藥的環境責任","藥劑管理、飄散與鄰田影響的責任議題。"),
      ("reg-weather","天氣條件判斷","風、雨、霧與溫度如何決定能不能出機。"),
      ("reg-obstacle","避障與緊急處置","避障、緊急處置與電池管理的安全守則。"),
      ("reg-drift","藥劑飄移與鄰田爭議","飄移傷鄰田的爭議怎麼預防與處理。"),
      ("reg-cost","投入與維持成本","買機、電池、維修、訓練與軟體的成本帳本。"),
      ("reg-model","自購、合作社、外包","三種經營方式怎麼選。")]},
  {"slug":"future","name":"未來永續","tag":"前瞻","color":"sky",
   "menu":[["發展趨勢",
      ("future-tech","技術與產業升級"),
      ("future-auto","全自動機場與機隊"),
      ("future-ai","AI 農業決策")],
    ["永續農業",
      ("future-sustain","減藥減水減碳"),
      ("future-organic","有機與坡地保育")]],
   "topics":[
      ("future-tech","技術與產業升級","自動化、多機協作與數據平台三條主線。"),
      ("future-auto","全自動機場與機隊","無人值守的農噴施肥，離我們多近。"),
      ("future-ai","AI 農業決策","用大模型自動生成田間管理方案的潛力。"),
      ("future-sustain","減藥減水減碳","無人機如何降低農業的環境足跡。"),
      ("future-organic","有機與坡地保育","有機、友善農業與坡地保育的應用潛力。")]},
  {"slug":"resources","name":"案例資源","tag":"參考","color":"amber",
   "menu":[["實務案例",
      ("resources-case","台灣農業案例"),
      ("resources-oversea","國外大型農場做法")],
    ["工具與資源",
      ("resources-tools","田間作業檢核表"),
      ("resources-training","飛手培訓資源"),
      ("resources-terms","名詞對照表")],
    ["站內索引",
      ("sitemap","知識庫目錄")]],
   "topics":[
      ("resources-case","台灣農業案例","茶園、果園與高山農業的實際應用案例。"),
      ("resources-oversea","國外大型農場做法","大型農場如何用機隊管理大面積農田。"),
      ("resources-tools","田間作業檢核表","出機前後逐項確認的工具。"),
      ("resources-training","飛手培訓資源","取得證照與技能的學習管道。"),
      ("resources-terms","名詞對照表","農用無人機常見名詞一次看懂。")]},
]

PILLAR = {p["slug"]:p for p in PILLARS}
ORDER = [p["slug"] for p in PILLARS]

PILLAR_SHORT = {
 "tech":"看懂農用無人機怎麼飛、怎麼看田、怎麼自動幹活，是一切應用的技術底子。",
 "agri":"沿產前、產中、產後看無人機如何補上人力、地形與資源缺口，並延伸至服務生態系。",
 "life":"把無人機帶進旅行、生活服務與居家檢查，是科技落地最親民的一條路。",
 "reg":"懂規定、知風險、算成本，無人機才用得長久、用得安心。",
 "future":"技術會怎麼長、農業會往哪去，以及無人機在永續路上的角色。",
 "resources":"看別人怎麼做、用工具動手做，還有名詞與培訓一次看懂。",
}

def pillar_of(slug):
    if slug in PILLAR: return PILLAR[slug]
    for p in PILLARS:
        for t,_,_ in p["topics"]:
            if t == slug: return p
    return None

# ============================================================
# 外殼（Head / Header / Drawer / Sidebar / Footer）
# ============================================================
LOGO = """<svg class="mark" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="9" fill="#1E5A44"/><path d="M9 22h22" stroke="#E5EFE9" stroke-width="2.4" stroke-linecap="round"/><circle cx="9.5" cy="19" r="3.4" fill="none" stroke="#E5EFE9" stroke-width="2"/><circle cx="9.5" cy="25" r="3.4" fill="none" stroke="#E5EFE9" stroke-width="2"/><circle cx="30.5" cy="19" r="3.4" fill="none" stroke="#E5EFE9" stroke-width="2"/><circle cx="30.5" cy="25" r="3.4" fill="none" stroke="#E5EFE9" stroke-width="2"/></svg>"""

def head(title, desc, page_slug):
    canon = SITE_URL + "/" + page_slug + ".html"
    site = BRAND + " " + BRAND_EN
    css = "https://miaoda.feishu.cn/fonts/css2?family=Noto+Serif+TC:wght@500;700;800&family=Noto+Sans+TC:wght@400;500;700&display=swap"
    lines = [
        "<!DOCTYPE html>",
        '<html lang="zh-Hant">',
        "<head>",
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>" + title + "</title>",
        '<meta name="description" content="' + desc + '">',
        '<meta name="robots" content="index, follow">',
        '<link rel="canonical" href="' + canon + '">',
        '<meta property="og:type" content="article">',
        '<meta property="og:site_name" content="' + site + '">',
        '<meta property="og:title" content="' + title + '">',
        '<meta property="og:description" content="' + desc + '">',
        '<meta property="og:locale" content="zh_TW">',
        '<link rel="icon" type="image/svg+xml" href="' + FAVICON + '">',
        '<link rel="stylesheet" href="assets/css/style.css">',
        '<link rel="preconnect" href="https://miaoda.feishu.cn">',
        '<link rel="stylesheet" href="' + css + '">',
        '<script type="application/ld+json">' + jsonld(page_slug) + '</script>',
        "</head>",
        "<body>",
    ]
    return "\n".join(lines) + "\n"

def jsonld(slug):
    import json
    base = {
      "@context":"https://schema.org",
      "@type":"WebPage",
      "name":BRAND+" "+BRAND_EN,
      "url":SITE_URL,
      "inLanguage":"zh-Hant",
      "publisher":{"@type":"Organization","name":BRAND,"url":SITE_URL}
    }
    p = pillar_of(slug)
    if p and slug not in PILLAR and slug in ART:
        base["@type"]="Article"
        base["headline"]=TITLE[slug]
        base["author"]={"@type":"Person","name":AUTHOR[ART[slug][3]].get("name","農翔誌編輯群")}
        base["dateModified"]="2026-11-02"
        base["mainEntityOfPage"]=SITE_URL+"/"+slug+".html"
    return json.dumps(base, ensure_ascii=False)

def top_link(slug, name):
    # 已撰寫的條目給真實連結；未撰寫的以純文字標註「撰寫中」，不造假連結
    # sitemap 為靜態頁（sitemap_page 產出），非 ART 文章，仍屬真實可連結頁面
    if slug in ART or slug in ("sitemap",):
        return '<a href="%s.html">%s</a>' % (slug, name)
    return '<span class="wip">%s（撰寫中）</span>' % name

def mega_html():
    out=['<nav class="main-nav" id="mainNav" aria-label="主要導覽">']
    for p in PILLARS:
        cols=[]
        for row in p["menu"]:
            group = row[0]
            items = row[1:]
            lis="".join(top_link(slug,name) for slug,name in items)
            cols.append('<div class="mcol"><span>%s</span>%s</div>'%(group,lis))
        out.append('<div class="nav-item" id="nv-%s"><a href="%s.html">%s<span class="caret">▾</span></a><div class="mega">%s</div></div>'%(p["slug"],p["slug"],p["name"],"".join(cols)))
    out.append('</nav>')
    return "".join(out)

def drawer_list():
    rows=""
    for p in PILLARS:
        kids="".join('<li>%s</li>'%top_link(t,n) for t,n,_ in p["topics"])
        rows+='<li><a href="%s.html">%s</a><ul class="sub">%s</ul></li>'%(p["slug"],p["name"],kids)
    rows+='<li><a href="about.html">關於我們</a></li><li><a href="contact.html">聯絡我們</a></li><li><a href="sitemap.html">知識庫目錄</a></li>'
    return rows

def header_html():
    return ('<header class="site-header" id="siteHeader">\n'
      '  <div class="nav-inner">\n'
      '    <a class="brand" href="index.html">' + LOGO + '<span class="bt"><b>' + BRAND + ' ' + BRAND_EN + '</b><span>農業與無人機知識庫</span></span></a>\n'
      '    ' + mega_html() + '\n'
      '    <a class="header-cta" href="contact.html">聯絡我們</a>\n'
      '    <button class="hamburger" id="hamburger" aria-label="開啟選單" aria-expanded="false"><span></span><span></span><span></span></button>\n'
      '  </div>\n'
      '</header>\n'
      '<div class="header-spacer"></div>\n'
      '<div class="drawer" id="drawer" aria-hidden="true">\n'
      '  <div class="scrim" data-close></div>\n'
      '  <div class="panel">\n'
      '    <div class="d-head"><span class="serif" style="font-weight:800">' + BRAND + '</span><button class="d-close" data-close aria-label="關閉">×</button></div>\n'
      '    <ul class="dl">' + drawer_list() + '</ul>\n'
      '  </div>\n'
      '</div>')

def sidebar_html(current):
    p = pillar_of(current)
    if not p: return '<aside class="sidebar"></aside>'
    items=[]
    for slug,name,_ in p["topics"]:
        if slug == current:
            items.append('<li class="here"><a class="side-top" href="%s.html">%s</a></li>'%(slug,name))
        elif slug in ART:
            items.append('<li><a class="side-top" href="%s.html">%s</a></li>'%(slug,name))
        else:
            items.append('<li><span class="side-top side-wip">%s（撰寫中）</span></li>'%name)
    return ('<aside class="sidebar">\n'
      '  <div class="side-head"><span class="bar"></span>本站分類 · ' + p["name"] + '</div>\n'
      '  <ul class="side-list">' + "".join(items) + '</ul>\n'
      '</aside>')

def footer_html():
    return ('<footer class="site-footer">\n'
      '  <div class="footer-in">\n'
      '    <div class="footer-brand">\n'
      '      ' + LOGO.replace('#1E5A44','#2E7A58') + '\n'
      '      <p>從田間到天空的繁體中文知識庫，專注農用無人機技術、農業產業鏈與日常應用。內容標示作者與更新日期，以可查證的公開資料為基礎，持續提升 E-E-A-T 可信度。</p>\n'
      '    </div>\n'
      '    <div><h4>認識本站</h4><ul>\n'
      '      <li><a href="about.html">關於我們</a></li>\n'
      '      <li><a href="contact.html">聯絡我們</a></li>\n'
      '      <li><a href="sitemap.html">知識庫目錄</a></li>\n'
      '    </ul></div>\n'
      '    <div><h4>重要文件</h4><ul>\n'
      '      <li><a href="privacy.html">隱私政策</a></li>\n'
      '      <li><a href="disclaimer.html">免責聲明</a></li>\n'
      '      <li><a href="terms.html">使用條款</a></li>\n'
      '    </ul></div>\n'
      '    <div><h4>六大支柱</h4><ul>\n'
      '      <li><a href="tech.html">無人機技術</a></li>\n'
      '      <li><a href="agri.html">農業產業鏈</a></li>\n'
      '      <li><a href="life.html">無人機與生活</a></li>\n'
      '      <li><a href="reg.html">法規安全成本</a></li>\n'
      '      <li><a href="future.html">未來永續</a></li>\n'
      '      <li><a href="resources.html">案例資源</a></li>\n'
      '    </ul></div>\n'
      '  </div>\n'
      '  <div class="footer-bottom">\n'
      '    <span>© <span id="yr">2026</span> ' + BRAND + ' ' + BRAND_EN + ' · 知識整理僅供參考，作業前請遵循主管機關法規</span>\n'
      '    <span>本網站為示範知識庫（Example Domain）</span>\n'
      '  </div>\n'
      '</footer>\n'
      '<script src="assets/js/site.js"></script>\n'
      '</body>\n'
      '</html>')

def article_layout(current, inner):
    crumb = pillar_of(current)
    bc = '<nav class="breadcrumb"><a href="index.html">首頁</a>'
    if crumb:
        if current != crumb["slug"]:
            bc += '<span class="sep">›</span><a href="%s.html">%s</a>'%(crumb["slug"], crumb["name"])
        bc += '<span class="sep">›</span><span>%s</span></nav>'%(TITLE.get(current,crumb["name"]))
    else:
        bc += '<span class="sep">›</span><span>%s</span></nav>'%(TITLE.get(current,current))
    return ('<main><div class="wrap page">' + sidebar_html(current) + '<div class="content">' + bc + inner + '</div></div></main>')

def hub_page(p):
    cards="".join(
      ('<a class="topic" href="%s.html"><b>%s</b><p>%s</p></a>'%(t,n,s) if t in ART
       else '<span class="topic wip"><b>%s</b><p>%s（撰寫中）</p></span>'%(n,s))
      for t,n,s in p["topics"])
    inner = ('<span class="eyebrow">支柱 · ' + p["tag"] + '</span>\n'
      '    <h1>' + p["name"] + '</h1>\n'
      '    <p class="lead">' + HUB_LEAD[p["slug"]] + '</p>\n'
      '    <div class="stat-row">' + hub_stats(p["slug"]) + '</div>\n'
      '    <h2>本章內容</h2>\n'
      '    <div class="topic-grid">' + cards + '</div>')
    return article_layout(p["slug"], inner)

def hub_stats(slug):
    return ''.join('<div class="stat"><div class="n">%s</div><div class="l">%s</div></div>'%(n,l) for n,l in STATS[slug])

def full_page(title, desc, slug, inner):
    return head(title, desc, slug) + header_html() + inner + footer_html()

def emit(slug, html):
    with open(os.path.join(ROOT, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("built", slug + ".html", len(html))

# ============================================================
# 內容資料：標題 / 作者 / 支柱導語 / 統計
# ============================================================
TITLE = {}
AUTHOR = {}
HUB_LEAD = {}
STATS = {}

def article_page(slug):
    t, summary, tags, author_key, toc, body, prev, next = ART[slug]
    a = AUTHOR[author_key]
    meta_chips = "".join('<span class="chip%s">%s</span>'%(" sky" if i%2 else "", "#"+tg) for i,tg in enumerate(tags))
    meta = ('<div class="article-meta">'
      '<span>作者：' + a["name"] + '</span>'
      '<span>分類：' + pillar_of(slug)["name"] + '</span>'
      '<span>更新：2026-11-02</span>'
      + meta_chips + '</div>')
    toc_html = ''
    if toc:
        items = "".join('<li><a href="#%s">%s</a></li>'%(tid,tname) for tid,tname in toc)
        toc_html = '<nav class="toc" aria-label="本文目錄"><b>本頁目錄</b><ol>' + items + '</ol></nav>'
    authorbox = ('<div class="author-box"><span class="av">' + a["abbr"] + '</span><div>'
      '<b>' + a["name"] + '</b><span class="role">' + a["role"] + '</span><p>' + a["bio"] + '</p></div></div>')
    pn = ''
    if prev or next:
        pl = '<a class="prev" href="%s.html"><span class="dir">← 上一篇</span><b>%s</b></a>'%(prev[0],prev[1]) if prev else '<span></span>'
        nl = '<a class="next" href="%s.html"><span class="dir">下一篇 →</span><b>%s</b></a>'%(next[0],next[1]) if next else '<span></span>'
        pn = '<div class="prevnext">%s%s</div>'%(pl,nl)
    inner = ('<span class="eyebrow">' + pillar_of(slug)["name"] + ' · 深度文章</span>\n'
      '  <h1>' + t + '</h1>\n'
      '  ' + meta + '\n'
      '  <p class="lead">' + summary + '</p>\n'
      '  ' + toc_html + '\n'
      '  <article class="article-body">' + body + '</article>\n'
      '  ' + authorbox + '\n'
      '  ' + pn)
    return article_layout(slug, inner)

def home_page():
    cards = ""
    for p in PILLARS:
        ic = 'sky' if p["color"]=="sky" else 'amber'
        cards += ('<a class="card" href="%s.html">'
          '<img class="card-img" loading="lazy" src="img/card-%s.webp" alt="%s">'
          '<span class="ic %s">%s</span>'
          '<span class="eyebrow">%s</span><h3>%s</h3><p>%s</p>'
          '<span class="more">進入%s<span class="tag">→</span></span></a>') % (
          p["slug"], p["slug"], p["name"], ic, HOME_ICON[p["slug"]], p["tag"], p["name"], PILLAR_SHORT[p["slug"]], p["name"])
    steps = "".join('<div class="step"><div class="no">%s</div><h3>%s</h3><p>%s</p></div>'%tuple(s) for s in HOME_STEPS)
    return """<section class="view">
<div class="hero"><div class="hero-in">
  <div>
    <span class="eyebrow">從田間到天空</span>
    <h1>農業遇上無人機，<br>把辛苦變成分寸。</h1>
    <p class="lede">""" + HERO_TEXT + """</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="tech.html">開始讀無人機技術</a>
      <a class="btn btn-ghost" href="agri.html">看農業產業鏈</a>
    </div>
  </div>
</div></div>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">六大主題支柱</span>
    <h2>你想先從哪裡認識無人機？</h2>
    <p>本站採「權重金字塔」的資訊架構：首頁只放六大支柱入口，深入內容由各支柱頁面與側邊欄承接，方便你沿著分類一步步往下讀。</p>
  </div>
  <div class="cards">""" + cards + """</div>
</div></section>

<section class="section section-tight"><div class="wrap">
  <div class="section-head"><span class="eyebrow">怎麼開始</span><h2>農用無人機上手四步</h2></div>
  <div class="steps">""" + steps + """</div>
</div></section>

<section class="section section-tight"><div class="wrap">
  <div class="band"><div style="flex:1;min-width:220px">
    <h2>需要協助導入或外包噴藥？</h2>
    <p>無論你是農民、飛手，還是想認識無人機的讀者，都可以與我們聯繫。本站不代購、不代飛，僅提供知識整理與諮詢指引。</p>
  </div>
  <a class="btn" href="contact.html">聯絡我們</a></div>
</div></section>
</section>"""

def sitemap_page():
    blocks=""
    for p in PILLARS:
        lis="".join('<li>%s</li>'%('<a href="%s.html">%s</a>'%(t,n) if t in ART else '<span class="wip">%s（撰寫中）</span>'%n) for t,n,_ in p["topics"])
        blocks+='<div class="smap"><h2>%s</h2><ul>%s</ul></div>'%(p["name"],lis)
    inner = """<span class="eyebrow">全站索引</span>
    <h1>知識庫目錄</h1>
    <p class="lead">以下是本站全部主題索引，以支柱分類排列。六支柱共 49 條目已全數上線，點擊連結即可直接閱讀。</p>
    <div class="sitemap-grid">""" + blocks + """</div>"""
    return full_page("知識庫目錄 ｜ 農翔誌 LipoSow", "農翔誌全站主題索引，六大支柱與所有條目一目了然。", "sitemap", article_layout("sitemap", inner))

def static_legal(title, desc, slug, paras):
    body = ""
    for item in paras:
        if item[0]=="h": body += '<h2>'+item[1]+'</h2>'
        elif item[0]=="p": body += '<p>'+item[1]+'</p>'
        elif item[0]=="ul": body += '<ul>'+''.join('<li>'+x+'</li>' for x in item[1])+'</ul>'
    inner = """<span class="eyebrow">Legal · 文件</span>
    <h1>""" + title + """</h1>
    <div class="article-body legal">""" + body + """</div>"""
    return full_page(title+" ｜ 農翔誌 LipoSow", desc, slug, article_layout(slug, inner))

def about_page():
    team = [("林","農業技術主編","農事服務與植保實務背景，負責技術與產業鏈內容架構。"),
            ("陳","法規與安全編輯","長期整理台灣無人機法規與現場作業風險。"),
            ("許","生活應用編輯","從休閒空拍到生活服務的入門內容撰寫。")]
    tg = "".join('<div class="team"><span class="av">%s</span><h3>%s</h3><span class="role">%s</span><p>%s</p></div>'%(n,n,r,b) for n,r,b in team)
    inner = """<span class="eyebrow">About · 關於本站</span>
    <h1>關於農翔誌</h1>
    <p class="lead">農翔誌是一份繁體中文的農業與無人機知識庫。我們相信：無人機不是遙遠的科技，而是能實際補上農業人力、地形與資源缺口的一雙手。</p>
    <article class="article-body">
      <h2>我們在做什麼</h2>
      <p>本站沿「無人機技術 → 農業生產產業鏈 → 日常生活延伸」三條主線整理內容，採權重金字塔的資訊架構。每一條目都標示作者與更新日期，正文以可查證的公開資料與實務經驗為基礎，拒絕無來源的誇大數據。</p>
      <h2>內容原則</h2>
      <ul>
        <li><strong>可查證來源：</strong>涉及法規、數據與規格時，盡量註明主管機關或來源方向。</li>
        <li><strong>人味與作者：</strong>每篇文章有署名與作者簡介，避免「無作者」的機器感。</li>
        <li><strong>以台灣實務為優先：</strong>法規、地形與產業案例多依台灣情境撰寫。</li>
        <li><strong>只整理知識、不代購代飛：</strong>實際作業請遵循主管機關規範並徵詢專業飛手。</li>
      </ul>
      <h2>編輯團隊</h2>
      <div class="team-grid">""" + tg + """</div>
    </article>"""
    return full_page("關於我們 ｜ 農翔誌 LipoSow", "認識農翔誌的定位、編輯團隊與內容原則。", "about", article_layout("about", inner))

def contact_page():
    inner = """<span class="eyebrow">Contact · 聯繫</span>
    <h1>聯絡我們</h1>
    <p class="lead">本站不代購、不代飛、不提供個別農田診斷。以下表單用於知識諮詢、合作提案與內容勘誤。</p>
    <div class="article-body">
      <form id="contactForm" novalidate>
        <div class="form-grid">
          <div class="field"><label for="cf-name">姓名</label><input id="cf-name" name="name" type="text" required placeholder="您的稱呼"></div>
          <div class="field"><label for="cf-mail">Email</label><input id="cf-mail" name="mail" type="email" required placeholder="name@example.com"></div>
        </div>
        <div class="field" style="margin-top:14px"><label for="cf-topic">主題</label>
          <select id="cf-topic" name="topic"><option>知識諮詢</option><option>合作提案</option><option>內容勘誤</option><option>其他</option></select></div>
        <div class="field" style="margin-top:14px"><label for="cf-msg">內容</label><textarea id="cf-msg" name="msg" required placeholder="請簡單說明你的需求或問題"></textarea></div>
        <button class="btn btn-primary" style="margin-top:18px" type="submit">送出諮詢</button>
        <p class="form-note">送出後本站將於 2 個工作天內回覆（示範站不實際寄送）。</p>
      </form>
    </div>"""
    return full_page("聯絡我們 ｜ 農翔誌 LipoSow", "與農翔誌編輯群聯繫，取得農用無人機與農業應用的諮詢指引。", "contact", article_layout("contact", inner))

# ============================================================
# 內容資料：首頁素材
# ============================================================
HERO_TEXT = "農翔誌是一個繁體中文的農業與無人機知識庫。我們把「無人機技術」與「農業生產產業鏈」接在一起，說明機器如何補上勞力、地形與資源的缺口——也延伸到日常生活，讓新手看得懂、用得起來。"

HOME_ICON = {
 "tech":"<svg viewBox='0 0 24 24' width='24' height='24' fill='none' stroke='currentColor' stroke-width='1.8'><path d='M3 18h18M4 18v-5a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v5M8 9V7a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2'/></svg>",
 "agri":"<svg viewBox='0 0 24 24' width='24' height='24' fill='none' stroke='currentColor' stroke-width='1.8'><path d='M4 20h16M6 20V11a6 6 0 0 1 12 0v9M9 20v-4M15 20v-4'/></svg>",
 "life":"<svg viewBox='0 0 24 24' width='24' height='24' fill='none' stroke='currentColor' stroke-width='1.8'><path d='M12 21c-4 0-7-3.5-7-8a7 7 0 0 1 14 0c0 4.5-3 8-7 8Z'/><path d='M12 21V11'/></svg>",
 "reg":"<svg viewBox='0 0 24 24' width='24' height='24' fill='none' stroke='currentColor' stroke-width='1.8'><path d='M12 3l7 3v5c0 4-3 7-7 10-4-3-7-6-7-10V6l7-3Z'/><path d='M9.5 12l2 2 3.5-4'/></svg>",
 "future":"<svg viewBox='0 0 24 24' width='24' height='24' fill='none' stroke='currentColor' stroke-width='1.8'><path d='M12 4a8 8 0 1 0 8 8'/><path d='M12 4v8l5 3'/></svg>",
 "resources":"<svg viewBox='0 0 24 24' width='24' height='24' fill='none' stroke='currentColor' stroke-width='1.8'><path d='M4 6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6Z'/><path d='M8 9h8M8 13h5M8 16h3'/></svg>",
}

HOME_STEPS = [
  ("01","看懂機型","先分清楚「植保噴灑型」與「測繪空拍型」的差異，再決定用途。"),
  ("02","查法規","確認機體重量、登記與證照門檻，以及你所在區域的禁飛範圍。"),
  ("03","練操作","先在空曠處練起降與航線，再依氣象與作物時序安排任務。"),
  ("04","看數據","把空拍影像接回田間管理，形成「拍攝→分析→施作」的閉環。"),
]

# ============================================================
# 標題 / 作者 / 支柱導語 / 統計
# ============================================================
TITLE.update({
  "index":"農翔誌 LipoSow｜農業與無人機專業知識庫",
  "tech":"無人機技術 ｜ 農翔誌 LipoSow",
  "agri":"農業產業鏈 ｜ 農翔誌 LipoSow",
  "life":"無人機與生活 ｜ 農翔誌 LipoSow",
  "reg":"法規安全成本 ｜ 農翔誌 LipoSow",
  "future":"未來永續 ｜ 農翔誌 LipoSow",
  "resources":"案例資源 ｜ 農翔誌 LipoSow",
  "tech-drones":"農用無人機機型怎麼選：植保、測繪與多功能一次看懂",
  "tech-starter":"無人機技術怎麼入門：先懂原理，再談操作",
  "tech-power":"電池與動力系統：續航、換電與保養實務",
  "agri-pre":"田區勘測與面積量測：用空拍一次把田摸清楚",
  "agri-spray":"植保噴灑作業流程：從準備到收工的完整步驟",
  "agri-monitor":"作物逆境監測：用空拍提早看見缺肥、缺水與病蟲害",
  "life-starter":"新手空拍入門：挑機、安全、先練什麼",
  "life-inspect":"屋頂、外牆與太陽能板巡檢：無人機的高處作業指南",
  "reg-law":"台灣無人機法規重點：登記、證照與飛行紅線",
  "reg-cost":"農用無人機成本全解析：買、租、外包怎麼算最划算",
  "future-auto":"從人工噴藥到全自動機場：農業無人機的下一步",
  "future-sustain":"無人機與永續農業：減藥、減水、減碳怎麼落地",
  "resources-tools":"田間作業檢核表：出機前後逐項確認",
  "resources-training":"飛手培訓與學習資源：從新手到能接案的管道",
  "about":"關於我們 ｜ 農翔誌 LipoSow",
  "contact":"聯絡我們 ｜ 農翔誌 LipoSow",
  "privacy":"隱私政策 ｜ 農翔誌 LipoSow",
  "disclaimer":"免責聲明 ｜ 農翔誌 LipoSow",
  "terms":"使用條款 ｜ 農翔誌 LipoSow",
  "sitemap":"知識庫目錄 ｜ 農翔誌 LipoSow",
})

AUTHOR = {
 "lin":{"name":"陳信旭","abbr":"陳","role":"農業技術主編","bio":"具農事服務與植保實務背景，負責技術與產業鏈內容的架構與審校，內容以可查證的公開資料與實務經驗為基礎。"},
 "chen":{"name":"陳信旭","abbr":"陳","role":"法規與安全編輯","bio":"長期整理台灣無人機法規與現場作業風險，協助讀者在不違規的前提下安全作業，並提醒讀者以主管機關現行公告為準。"},
 "xu":{"name":"陳信旭","abbr":"陳","role":"生活應用編輯","bio":"從休閒空拍到生活服務，負責面向一般讀者的入門與延伸內容。"},
 "team":{"name":"陳信旭","abbr":"陳","role":"內容編輯","bio":"由編者協作整理，內容以可查證的公開資料為基礎，持續以 E-E-A-T 原則提升可信度。"},
}

HUB_LEAD = {
 "tech":"建立農用無人機的技術底子：從機型、感測、AI 到自動飛行，是理解一切應用的起點。",
 "agri":"沿產前、產中、產後三大環節，看無人機如何補上人力、地形與資源的缺口，並延伸至服務生態系。",
 "life":"讓無人機走進旅行、生活服務與居家檢查，是科技落地最親民的一條路。",
 "reg":"懂規定、知風險、算成本，無人機才用得長久、用得安心。",
 "future":"技術會怎麼長、農業會往哪去，以及無人機在永續路上的角色。",
 "resources":"看別人怎麼做、用工具動手做，還有名詞與培訓一次看懂。",
}

STATS = {
 "tech":[("10","條技術條目"),("3","大知識面向"),("RTK","公分級定位")],
 "agri":[("12","條產業鏈條目"),("3","產前中後環節"),("1","套數據閉環")],
 "life":[("9","條生活應用"),("4","類應用場景"),("1","台入手機")],
 "reg":[("8","條合規條目"),("3","大風險面向"),("3","種經營模式")],
 "future":[("5","條前瞻條目"),("3","條升級主線"),("1","份永續藍圖")],
 "resources":[("5","條實用條目"),("1","張作業檢核表"),("3","種培訓管道")],
}

# ============================================================
# 文章內容（12 篇）
# 結構：(標題, 摘要, 標籤, 作者, [(目錄id,名稱)...], 正文HTML, 上一篇, 下一篇)
# ============================================================
ART = {}

ART["tech-drones"] = (
 "農用無人機機型怎麼選：植保、測繪與多功能一次看懂",
 "買農用機前最怕「買錯用途」。本文先幫你分清楚植保噴灑型、測繪空拍型與多功能型的差異，再依田塊大小與預算一步步縮小選擇。",
 ["選機","植保","測繪"], "lin",
 [("type","先搞清楚三種用途"),("compare","一張表看懂差異"),("how","依你的條件做選擇"),("budget","預算與成本思維"),("faq","常見問答")],
 """<h2 id="type">先搞清楚：你買的是「哪一種」農用機</h2>
<p>農用無人機不是「一台通用」，而是依用途分開設計。最常見的誤會是拿測繪機去噴藥、或拿植保機去精細測繪，結果不是效率差就是施作不均。</p>
<ul>
  <li><strong>植保噴灑型：</strong>大載重、快速度、大霧滴，任務是把藥、肥、粒劑均勻送到田裡。常見載重 10–50 公斤等級，作業效率以「畝/小時」計算。</li>
  <li><strong>測繪空拍型：</strong>高解析鏡頭、精準定位、可搭多光譜／熱影像，任務是「拍清楚」並還原成 2D／3D 資料。適合田區勘測、生長監測與產量估。</li>
  <li><strong>多功能／模組化：</strong>可換藥箱、播種器、測繪雲台或放物器，一台抵多種用途。適合自用農民與小規模飛手。</li>
</ul>
<div class="callout"><span class="ct">給你的第一個判斷</span>如果目的是「省工噴藥」，優先看載重與霧化；如果目的是「看懂田況」，優先看鏡頭與定位精度。兩者常是二選一，除非預算足夠買模組化機種。</div>

<h2 id="compare">一張表看懂三類機型</h2>
<div class="tablewrap"><table>
<caption>三類農用無人機的核心差異（依主流規格整理，實際以各家型錄為準）</caption>
<thead><tr><th>面向</th><th>植保噴灑型</th><th>測繪空拍型</th><th>多功能型</th></tr></thead>
<tbody>
<tr><td>主要任務</td><td>施藥、施肥、撒粒劑</td><td>田區測繪、生長監測</td><td>依模組切換多用途</td></tr>
<tr><td>載重/續航</td><td>載重高、續航中</td><td>續航長、載重低</td><td>居中可換配備</td></tr>
<tr><td>關鍵規格</td><td>藥箱容量、霧化、泵浦</td><td>感光元件、多光譜、RTK</td><td>模組接口、快拆</td></tr>
<tr><td>適合對象</td><td>專業飛防隊、大面積農場</td><td>測繪公司、研究單位</td><td>自用農民、新手</td></tr>
<tr><td>價格帶(約)</td><td>中高</td><td>中高</td><td>中低到中</td></tr>
</tbody></table></div>
<div class="procon">
  <div class="pc pro"><h4>選植保型的理由</h4><ul><li>噴藥效率最高、省工最有感</li><li>可替鄰里代噴、接案回本</li><li>噴藥是農用無人機最成熟的商業場景</li></ul></div>
  <div class="pc con"><h4>要留意的點</h4><ul><li>體積與重量大、存放與運送麻煩</li><li>載重續航受電池與天氣影響大</li><li>噴藥需取得適法飛手與藥劑管理</li></ul></div>
</div>

<h2 id="how">依你的條件，一步步縮小選擇</h2>
<ol>
  <li><strong>先定用途：</strong>噴藥為主？監測為主？還是都要？這一步決定機型方向。</li>
  <li><strong>量你的田：</strong>單次要覆蓋多大面積、地形是平原還是坡地，決定所需載重與航線能力。</li>
  <li><strong>看作業頻率：</strong>一年用幾次？偶爾自用選多功能，高頻作業才值得上專業植保機。</li>
  <li><strong>算總持有成本：</strong>不只機體，還有電池、維修、培訓與耗材，詳見「成本」支柱。</li>
</ol>
<div class="callout green"><span class="ct">重點提醒</span>若你「完全不打算考證照、也不想管藥劑」，從測繪／空拍型或委外服務起步，會比直接買植保機更務實。</div>

<h2 id="budget">預算之外的隱形成本</h2>
<p>購機只是開頭。多數人忽略的是電池汰換、馬達槳葉耗材、避障與圖傳升級、以及每年可能的保險與法規合規成本。建議把「兩年總持有成本」列為比較基準，而不是只看機體標價。</p>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>新手能直接買植保機嗎？</summary><div class="faq-a">不建議。植保機重量大、噴藥涉藥劑管理，建議先從測繪或小型多功能機練熟起降與航線，並取得對應證照後再升級。</div></details>
  <details><summary>測繪機可以拿來噴藥嗎？</summary><div class="faq-a">多數測繪機不具備噴灑機構，硬裝也不安全。兩者任務與載重設計不同，建議各司其職。</div></details>
  <details><summary>買不起專業機，有沒有替代？</summary><div class="faq-a">可以「外包」：委託飛防隊或測繪服務隊，依畝計費或專案報價，先試用再決定要不要自購。</div></details>
</div>""",
 ("tech","無人機技術"), ("tech-starter","無人機技術怎麼入門"))

ART["tech-starter"] = (
 "無人機技術怎麼入門：先懂原理，再談操作",
 "想把農用無人機學明白，不必先背規格。本文用三層框架——飛行原理、感測判讀、任務規劃——幫你把技術底子一次打好。",
 ["入門","原理","飛行"], "lin",
 [("fly","第一層：它怎麼飛起來"),("sense","第二層：它怎麼「看」田"),("plan","第三層：怎麼讓它自己去幹活"),("practice","該怎麼練"),("faq","常見問答")],
 """<h2 id="fly">第一層：它怎麼飛起來</h2>
<p>多旋翼無人機靠四個（以上）旋翼的推力差來控制姿態：上升靠總推力、前後左右靠個別馬達轉速差異。新手最容易忽略的是這三個物理約束：</p>
<ul>
  <li><strong>電量決定續航：</strong>載重越大、風越大，電池掉得越快，「剩餘電量」永遠是返航的紅線。</li>
  <li><strong>槳葉即耗材：</strong>碰撞、沙塵都會讓槳葉變形，是安全與效率的第一層風險。</li>
  <li><strong>GPS 只是參考：</strong>RTK 定位可到公分級，是精準農用的關鍵，但遮蔽處仍可能漂移。</li>
</ul>

<h2 id="sense">第二層：它怎麼「看」田</h2>
<p>測繪與監測靠的是鏡頭與感測器。常用的有三種：</p>
<div class="tablewrap"><table>
<thead><tr><th>感測類型</th><th>看什麼</th><th>典型用途</th></tr></thead>
<tbody>
<tr><td>可見光 (RGB)</td><td>人眼可見的顏色</td><td>地形、面積、生長狀態初步判斷</td></tr>
<tr><td>多光譜</td><td>紅邊、近紅外等波段</td><td>植被指數（NDVI）、缺肥、病害偵測</td></tr>
<tr><td>熱影像</td><td>表面溫度</td><td>缺水、灌溉不均、機械故障溫差</td></tr>
</tbody></table></div>
<div class="callout"><span class="ct">關鍵概念：NDVI</span>把紅光與近紅外波段算成一個指數，就能量化「這片葉子健康度」。健康植被反射近紅外多、病弱葉反射少——這就是把「長得如何」變成數字的起點。</div>

<h2 id="plan">第三層：怎麼讓它自己去幹活</h2>
<p>成熟作業不是「手飛」，而是「任務」：先在電腦或地面站圈出作業區塊與航線間距，無人機按規劃自主飛行、斷航續飛、自動返航。自動航線讓誤差與人為失誤大幅下降，是專業化的分水嶺。</p>

<h2 id="practice">該怎麼練</h2>
<ol>
  <li>先在空曠、無人、符合法規的地點練起降與手動方向感。</li>
  <li>再用模擬器與地面站練航線規劃與斷電返航。</li>
  <li>最後才進田區，從低高度、小面積逐步放大。</li>
</ol>
<div class="callout green"><span class="ct">安全底線</span>任何一次飛行前，都先確認電量、風速、遮蔽與當區法規。練習不是只練技術，更是練判斷力。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>完全沒碰過，多久能上手？</summary><div class="faq-a">起降與基本飛行幾個週末就能熟，但「精準農用」需要航線規劃、感測判讀與資料處理，建議以數週到數月的節奏投入。</div></details>
  <details><summary>要先學程式或資料處理嗎？</summary><div class="faq-a">不必。現在多數地面站與雲端平台已把航線與 NDVI 計算做成圖形介面，先從操作工具開始即可。</div></details>
  <details><summary>風大就完全不能飛？</summary><div class="faq-a">每台機有抗風等級與作業風速上限，超過會影響穩定性與噴藥霧滴落點，建議以機型規格與氣象預報為準。</div></details>
</div>""",
 ("tech-drones","農用無人機機型怎麼選"), ("agri","農業產業鏈"))

ART["agri-spray"] = (
 "植保噴灑作業流程：從準備到收工的完整步驟",
 "噴藥看似「飛過去就好」，其實牽涉藥劑、天氣、航線與安全四件事。本文把植保噴灑拆成可執行的標準流程，讓你每一趟都穩定、合規、不傷鄰田。",
 ["植保","噴灑","作業流程"], "lin",
 [("pre","作業前：五件事先確認"),("plan","航線與施藥規劃"),("fly","飛行施作要點"),("post","收工與善後"),("safety","安全與飄移防護"),("faq","常見問答")],
 """<h2 id="pre">作業前：五件事先確認</h2>
<ol>
  <li><strong>天候：</strong>風速、降雨、高溫。噴藥對風速最敏感，超過作業上限就要停。</li>
  <li><strong>機況：</strong>電池滿電、槳葉無傷、泵浦與噴嘴暢通、RTK 訊號正常。</li>
  <li><strong>藥劑：</strong>確認藥種、濃度、稀釋倍數與安全間隔期，並依規定管理。</li>
  <li><strong>範圍：</strong>圈定作業區、避開人群與敏感設施，確認無禁飛限制。</li>
  <li><strong>鄰田：</strong>留意風向會把霧滴帶到哪裡，預先溝通或留緩衝。</li>
</ol>

<h2 id="plan">航線與施藥規劃</h2>
<p>好的航線決定噴灑是否均勻。重點參數包括：航線間距（與噴幅相關）、飛行高度（影響霧滴落點）、作業速度（影響單位面積施藥量）。透過地面站設定好自動航線，能大幅降低重噴與漏噴。</p>
<div class="callout"><span class="ct">施藥量怎麼算</span>「畝施藥量」= 每株/單位面積的目標藥量 ÷ 實際噴出的藥量。規劃時把藥液流速與飛行速度對上，才能讓每畝都吃到正確劑量。</div>

<h2 id="fly">飛行施作要點</h2>
<ul>
  <li>沿主風向安排航線，讓霧滴自然下壓、減少飄移。</li>
  <li>轉彎處先爬升再轉向，避免重噴。</li>
  <li>全程盯緊電量與圖傳，任何異常先返航再排查。</li>
  <li>若風向或風速驟變，立即停止，別硬噴。</li>
</ul>

<h2 id="post">收工與善後</h2>
<ol>
  <li>清洗藥箱與噴嘴，避免藥液殘留與交叉污染。</li>
  <li>記錄施藥時間、藥劑、用量與天氣，留存為履歷。</li>
  <li>檢查電池溫度與槳葉，做基本保養。</li>
</ol>

<h2 id="safety">安全與飄移防護</h2>
<p>植保噴藥的風險不只機體，更在「藥劑到哪去」。減輕飄移的實務手段包括：使用抗飄移噴嘴、降低飛行高度、挑無風或風小窗口、與鄰田留緩衝帶。任何一次飄移都可能造成鄰田藥害，寧可少噴也不冒險。</p>
<div class="procon">
  <div class="pc pro"><h4>植保機噴藥的優勢</h4><ul><li>省工、速度快，適合大面積</li><li>人員不必進入田間，降低暴露</li><li>配合變量技術可精準施藥</li></ul></div>
  <div class="pc con"><h4>需要留意的風險</h4><ul><li>霧滴飄移風險高</li><li>藥劑與法規管理較繁瑣</li><li>天氣窗口窄、不確定性高</li></ul></div>
</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>噴藥一定要專業飛手嗎？</summary><div class="faq-a">植保噴藥涉及藥劑與安全，建議由取得對應證照、經驗充足的飛手或飛防隊執行，以降低風險與爭議。</div></details>
  <details><summary>一天能噴多大面積？</summary><div class="faq-a">依機型、電池與天候差異很大，從幾十畝到數百畝都有。先用小區塊試噴測出單位效率，再排當日作業量。</div></details>
  <details><summary>噴完要不要清洗機身？</summary><div class="faq-a">藥箱、噴嘴與管路務必清洗，機身可依藥劑殘留情況擦拭，避免腐蝕與交叉污染。</div></details>
</div>""",
 ("agri","農業產業鏈"), ("agri-monitor","作物逆境監測：用空拍提早看見缺肥、缺水與病蟲害"))

ART["agri-monitor"] = (
 "作物逆境監測：用空拍提早看見缺肥、缺水與病蟲害",
 "等葉子黃了才處理，往往已經晚了。本文說明如何用多光譜與熱影像定期空拍，在肉眼看到之前，就先一步發現缺肥、缺水與病蟲害的早期訊號。",
 ["監測","多光譜","逆境"], "lin",
 [("why","為什麼要提早發現"),("tech","用什麼感測器"),("ndvi","怎麼讀出問題"),("plan","多久拍一次、怎麼拍"),("faq","常見問答")],
 """<h2 id="why">為什麼要提早發現</h2>
<p>作物「肉眼可見的症狀」出現時，光合作用早已受損。逆境的早期訊號往往出現在光譜層面——葉片含水量、葉綠素密度與健康度的細微變化，人眼看不出來，但多光譜與熱影像感測器看得出來。提早一週發現，處理成本可能差好幾倍。</p>

<h2 id="tech">用什麼感測器</h2>
<div class="tablewrap"><table>
<thead><tr><th>訊號</th><th>感測方式</th><th>能提早發現的逆境</th></tr></thead>
<tbody>
<tr><td>葉綠素密度下降</td><td>多光譜（紅邊/NDVI）</td><td>缺氮等缺肥、葉片老化</td></tr>
<tr><td>冠層溫度上升</td><td>熱影像</td><td>缺水、灌溉不均、根系受損</td></tr>
<tr><td>光譜異常斑塊</td><td>多光譜 高解析拼接</td><td>病斑、蟲害、草害初發</td></tr>
</tbody></table></div>

<h2 id="ndvi">怎麼讀出問題</h2>
<p>最常見的讀法是 NDVI（植被指數）：把紅光與近紅外波段算成 0–1 的值，健康植被通常較高，受脅與稀疏植被較低。重點不是「絕對值」，而是「相對差異」——同一田區、前後幾次拍攝的變化，最能揪出正在惡化的區塊。</p>
<div class="callout"><span class="ct">讀圖的陷阱</span>天候、拍攝角度與時間都會影響指數。務必固定拍攝條件（同高度、同時間帶），並用「同一田區比較」而非跨田絕對值判斷。</div>

<h2 id="plan">多久拍一次、怎麼拍</h2>
<ul>
  <li><strong>生長關鍵期加密：</strong>分蘗、開花、灌漿等關鍵階段，建議每 7–14 天一次。</li>
  <li><strong>固定航線與高度：</strong>重複同一航線，前後影像才可比。</li>
  <li><strong>補地面取樣：</strong>空拍標出的異常區，到田間實地確認，兩者互相印證。</li>
</ul>
<div class="callout green"><span class="ct">落地做法</span>不需一次買高階感測器。可以先用手邊可見光空拍確認地形與長勢，再逐步加入多光譜；監測的價值在「持續、可比」，不在「一次很貴」。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>NDVI 高就代表一定健康？</summary><div class="faq-a">不盡然。植被指數反映的是光譜訊號，可能受品種、物候與拍攝條件影響，需配合地面觀察與其他感測器交叉判讀。</div></details>
  <details><summary>一定要會算指數嗎？</summary><div class="faq-a">不必手算。多數地面站與雲端平台會自動生成 NDVI 與熱影像圖層，你只需學會「怎麼讀、怎麼比」。</div></details>
  <details><summary>小農田塊值得做嗎？</summary><div class="faq-a">面積小可採「重點區定期拍」或委外單次監測，花費可控且能掌握長勢；重點是養成紀錄習慣，而非一次砸錢。</div></details>
</div>""",
 ("agri-spray","植保噴灑作業流程"), ("life","無人機與生活"))

ART["life-starter"] = (
 "新手空拍入門：挑機、安全、先練什麼",
 "想開始玩空拍，不必被複雜規格嚇到。本文從挑第一台機、查法規到安全練飛，帶你順順走出新手村。",
 ["空拍","新手","入門"], "xu",
 [("pick","第一台機怎麼挑"),("law","先查法規再起飛"),("safe","安全練飛三步"),("next","下一步能玩什麼")],
 """<h2 id="pick">第一台機怎麼挑</h2>
<p>第一台空拍機不用追旗艦。以「好操作、圖傳穩、重量合規」優先，規格上留意：</p>
<ul>
  <li><strong>重量門檻：</strong>先確認你所在國家/地區的重量級別，重量影響登記與飛行限制。</li>
  <li><strong>圖傳距離與穩定性：</strong>比解析度更影響體驗，安全返航依賴穩定圖傳。</li>
  <li><strong>避障與返航：</strong>入門機的避障與自動返航能省下不少新手失誤成本。</li>
  <li><strong>電池與備件：</strong>多備一顆電池與一套槳葉，是基本教養。</li>
</ul>

<h2 id="law">先查法規再起飛</h2>
<p>無人機不是「想飛就飛」。起飛前務必確認三件事：機體是否需要登記、操作者是否需要證照、所在位置是否屬禁飛或限制區。機場、人群、政府機關與敏感設施周邊多半有限制。詳細請見本站「法規安全成本」支柱。</p>
<div class="callout"><span class="ct">最常踩的雷</span>在「看起來空曠」的地方飛，其實可能就在禁飛區內。起飛前用官方或合規的飛行區域工具查一次，幾秒鐘的事。</div>

<h2 id="safe">安全練飛三步</h2>
<ol>
  <li><strong>找合法空曠場地：</strong>遠離人群、車流、電線與樹木，確認不在禁飛區。</li>
  <li><strong>先練基本功：</strong>定點懸停、直線來回、低空轉向，不急著拍片。</li>
  <li><strong>設好返航：</strong>起飛前設定返航點與高度，養成「起飛前檢查清單」的習慣。</li>
</ol>
<div class="callout green"><span class="ct">天氣紅線</span>大風、雨、霧與低溫都不適合新手練習。風速超過機型抗風等級就收機，別硬飛。</div>

<h2 id="next">下一步能玩什麼</h2>
<p>基本功熟了，可以往三個方向延伸：<strong>風景空拍</strong>（旅行與創作）、<strong>生活服務</strong>（屋頂巡檢、活動紀錄），或<strong>精進技術</strong>（測繪、競速）。本站「生活支柱」的每一條都能當你的下一步。</p>""",
 ("life","無人機與生活"), ("life-inspect","屋頂、外牆與太陽能板巡檢"))

ART["life-inspect"] = (
 "屋頂、外牆與太陽能板巡檢：無人機的高處作業指南",
 "爬上屋頂檢查太陽能板又累又危險。用無人機做高處巡檢，既安全又省力。本文說明怎麼拍、怎麼看出問題，以及該注意的安全與法規。",
 ["巡檢","屋頂","太陽能"], "xu",
 [("why","為什麼用空拍做巡檢"),("how","怎麼拍才有效"),("read","怎麼看出問題"),("safe","安全與法規"),("faq","常見問答")],
 """<h2 id="why">為什麼用空拍做巡檢</h2>
<p>太陽能板、屋頂與外牆巡檢，傳統靠人工攀爬，有墜落風險、耗時且難全面。無人機能以固定距離、固定角度快速繞場拍攝，把「危險高處」變成「安全桌面作業」。對屋主、機電包商與物業都是成本有感的正解。</p>

<h2 id="how">怎麼拍才有效</h2>
<ul>
  <li><strong>定距定角：</strong>垂直或斜向俯拍，固定高度與角度，前後才可比。</li>
  <li><strong>熱影像優先：</strong>太陽能板用熱影像最有效，異常升溫的 cell 常是故障熱點。</li>
  <li><strong>重疊拼接：</strong>飛行路徑留有重疊，後製才能拼成完整全景。</li>
</ul>

<h2 id="read">怎麼看出問題</h2>
<div class="tablewrap"><table>
<thead><tr><th>畫面現象</th><th>可能問題</th><th>建議</th></tr></thead>
<tbody>
<tr><td>熱影像局部升溫</td><td>電池/逆變器熱點、遮蔭不均</td><td>實地檢查並維修</td></tr>
<tr><td>板面髒污、積塵</td><td>發電效率下降</td><td>安排清洗</td></tr>
<tr><td>外牆裂縫、漏水跡</td><td>結構或防水問題</td><td>請專業人員評估</td></tr>
<tr><td>螺絲鬆動、變形</td><td>安裝或風損</td><td>盡快處理</td></tr>
</tbody></table></div>

<h2 id="safe">安全與法規</h2>
<p>高處巡檢靠近建築與設備，重點確認：<strong>不在禁飛區</strong>（機場、敏感設施周邊）、<strong>避開人群與下方行人</strong>、<strong>與屋頂及電線保持安全距離</strong>。涉及電氣設備時保持安全間距，巡檢僅做「看」，維修交給專業。</p>
<div class="callout"><span class="ct">重要界線</span>空拍只是「檢查工具」，不會修理。發現任何疑似結構或電氣問題，交由具備資格的專業人員評估處置。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>需要很貴的機才能做太陽能巡檢？</summary><div class="faq-a">看得清楚只需一般空拍機；要看「升溫熱點」才需要熱影像雲台。可先租借或委外熱影像巡檢再決定要不要投資。</div></details>
  <details><summary>自家屋頂能自己飛嗎？</summary><div class="faq-a">只要不在禁飛區、符合重量與操作規定，自家範圍空拍通常可行，但務必確認當區法規與鄰里安全。</div></details>
  <details><summary>多久巡一次？</summary><div class="faq-a">太陽能板建議至少每季一次熱影像巡檢，風災後、異常發電時立即加巡。</div></details>
</div>""",
 ("life-starter","新手空拍入門"), ("reg","法規安全成本"))

ART["reg-law"] = (
 "台灣無人機法規重點：登記、證照與飛行紅線",
 "在台灣飛無人機，先懂規定才不會踩雷。本文整理機體登記、操作證照與飛行區域的紅線，並提醒你以民航局現行公告為準。",
 ["法規","登記","證照"], "chen",
 [("rule","先掌握三個層級"),("reg","機體登記"),("lic","操作證照"),("zone","飛行區域紅線"),("note","重要提醒")],
 """<h2 id="rule">先掌握三個層級</h2>
<p>台灣無人機管理以《民用航空法》遙控無人機專章為核心，主要分三個層級：<strong>機體管理</strong>（登記與標誌）、<strong>操作者管理</strong>（證照與操作限制）、<strong>飛行區域管理</strong>（禁飛區與活動申請）。</p>
<div class="callout"><span class="ct">提醒</span>法規會不定期更新、且與重量級別相關。本文為重點整理，實際作業請以交通部民用航空局現行公告與規範為準。</div>

<h2 id="reg">機體登記</h2>
<p>達一定重量以上的遙控無人機需辦理「註冊／登記」，機體應標註辨識資訊，並可能需向主管機關申報。重量是分級的第一把尺：不同級別對應不同的登記義務與操作限制。</p>

<h2 id="lic">操作證照</h2>
<p>操作達一定級別的無人機需取得操作證，並可能區分「基本級／高級」等不同測驗等級。商用與學術等特定用途、以及特定操作情境，證照與限制更嚴格。考照需通過學科（法規與原理）與術科測驗。</p>

<h2 id="zone">飛行區域紅線</h2>
<ul>
  <li><strong>禁飛區：</strong>機場周邊、政府機關、軍事與敏感設施等，未經許可禁止飛行。</li>
  <li><strong>限制區：</strong>部分區域需申請或條件性飛行（如人群活動、夜航）。</li>
  <li><strong>人群上空：</strong>人潮密集處飛行通常有更嚴格限制或需申請。</li>
</ul>
<div class="callout green"><span class="ct">起飛前必做</span>使用官方或合規的飛行區域查詢工具確認當前位置，並留意夜間、人群與高度限制。</div>

<h2 id="note">重要提醒</h2>
<p>無人機管理橫跨民航、電信（頻率）與農業用藥（噴藥時的藥劑管理）。農用噴藥除了飛行法規，還涉及農藥管理與安全間隔期。建議：作業前逐項確認，必要時諮詢主管機關或專業飛防業者，確保合規再上機。</p>""",
 ("reg","法規安全成本"), ("reg-cost","農用無人機成本全解析"))

ART["reg-cost"] = (
 "農用無人機成本全解析：買、租、外包怎麼算最划算",
 "買農用機要花多少？多久回本？本文把購機、電池、維修與委外的成本拆開算，幫你用「兩年總成本」做務實決定，而不是只看機體標價。",
 ["成本","經營","購機"], "chen",
 [("total","別只看機體價"),("buy","自購的成本帳"),("out","租賃與外包"),("model","三種方式怎麼選"),("faq","常見問答")],
 """<h2 id="total">別只看機體價</h2>
<p>農用無人機的「真成本」是持有與使用成本的總和。把下面幾項都列入，你才算得出回本與否：</p>
<ul>
  <li><strong>購機與周邊：</strong>機體、電池組、地面站、備用槳葉與維修工具。</li>
  <li><strong>電池汰換：</strong>電池循環壽命有限，是最被低估的開銷。</li>
  <li><strong>維修耗材：</strong>槳葉、馬達、圖傳與感測器故障的維修。</li>
  <li><strong>培訓與證照：</strong>考照、進修與每年的合規成本。</li>
  <li><strong>軟體與數據：</strong>地面站、雲端處理與測繪軟體授權。</li>
</ul>

<h2 id="buy">自購的成本帳</h2>
<div class="tablewrap"><table>
<caption>自購農用無人機的成本面向（示意，實際以機型與行情為準）</caption>
<thead><tr><th>項目</th><th>性質</th><th>說明</th></tr></thead>
<tbody>
<tr><td>機體</td><td>一次性</td><td>依用途與等級差異很大</td></tr>
<tr><td>電池</td><td>循環耗材</td><td>視使用頻率數季到數年汰換</td></tr>
<tr><td>維修</td><td>變動</td><td>依飛行環境與保養習慣而異</td></tr>
<tr><td>培訓證照</td><td>一次性+週期</td><td>證照效期與複訓要計入</td></tr>
</tbody></table></div>
<p>自購的好處是掌控力與單位成本低，壞處是閒置與維護成本要自己扛。一年只噴幾次的話，機體放著也是成本。</p>

<h2 id="out">租賃與外包</h2>
<p><strong>租賃/共享：</strong>按次付費使用機體，適合低頻與試用。**外包飛防/測繪**：直接把作業委給飛防隊，依畝計費或專案報價，省下投資與維護，也把藥劑與安全風險交給專業。</p>

<h2 id="model">三種方式怎麼選</h2>
<div class="procon">
  <div class="pc pro"><h4>自購最適合</h4><ul><li>高頻作業、大面積自有田</li><li>願意投入時間練技術與維護</li><li>想建立自有數據與品牌</li></ul></div>
  <div class="pc pro"><h4>外包最適合</h4><ul><li>作業頻率低、不熟技術</li><li>想把風險與藥劑管理交出去</li><li>先用外包驗證效果再決定</li></ul></div>
  <div class="pc pro"><h4>租賃/合作最適合</h4><ul><li>季節性高峰期補產能</li><li>試用不同機型</li><li>合作社共同採購分攤成本</li></ul></div>
</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>多久能回本？</summary><div class="faq-a">看作業量與收費。先算出「每畝省下的工時與藥量」與「接案收入」，再把兩年總成本攤平，才能估計回本週期。</div></details>
  <details><summary>電池是最貴的隱形成本？</summary><div class="faq-a">是。電池循環壽命與天氣都會影響壽命，多數人的總成本低估來自這裡，務必單獨列帳。</div></details>
  <details><summary>一開始可以只租或外包嗎？</summary><div class="faq-a">可以。先外包或租賃驗證作業價值，再依使用頻率決定是否自購，是降低決策風險的好策略。</div></details>
</div>""",
 ("reg-law","台灣無人機法規重點"), ("future","未來永續"))

ART["future-auto"] = (
 "從人工噴藥到全自動機場：農業無人機的下一步",
 "如果無人機自己會充電、換電池、自己起飛巡田，農業會變成什麼樣？本文談自動機場與機隊技術的現況、想像與現實門檻。",
 ["自動化","機場","機隊"], "lin",
 [("today","今天做到哪一步"),("dock","自動機場是什麼"),("fleet","從單機到機隊"),("gate","現實門檻與機會"),("faq","常見問答")],
 """<h2 id="today">今天做到哪一步</h2>
<p>今天的農用無人機已經能「自動航線 + 斷航續飛 + 自動返航」，但換電池、充電與資料回傳仍多靠人工。下一個升級是「自動機場（機巢）+ 機隊調度」：機子降落後自動換電、充電、上傳資料，並依任務自動出勤。</p>

<h2 id="dock">自動機場是什麼</h2>
<p>自動機場是一個放無人機的「小房子」：無人機降落在機場上，自動充電或換電池、回收任務資料、依雲端排程再次起飛。它讓「巡田」可以定時、定點、無人值守地反覆進行——尤其適合需要高頻監測的大面積農場。</p>
<div class="callout"><span class="ct">它能帶來什麼</span>監測頻率從「人想到才拍」變成「固定每天拍」；資料自動上雲，形成真正連續的生長紀錄。對病蟲害、缺水與災害的掌握度，是人工巡田比不上的。</div>

<h2 id="fleet">從單機到機隊</h2>
<p>單台機覆蓋面積有限。機隊與調度平台能同時排程多台機、分工覆蓋大田區或不同任務（一台測繪、一台噴藥）。真正的價值不在「多幾台」，而在「調度與資料自動化」——這需要地面站、雲端平台與感測器串成一套閉環。</p>

<h2 id="gate">現實門檻與機會</h2>
<div class="procon">
  <div class="pc pro"><h4>機會</h4><ul><li>省人力、監測更即時</li><li>數據自動化、決策更準</li><li>適合大面積與果園等高頻需求</li></ul></div>
  <div class="pc con"><h4>門檻</h4><ul><li>機場與平台投資高</li><li>場地、供電與網路建置</li><li>法規與維運成熟度仍在成長</li></ul></div>
</div>
<div class="callout green"><span class="ct">務實看法</span>對多數小農，自動機場還不是必備；對大型農場與專業服務隊，它是「省工＋數據」的下一個價值點。先從自動航線與雲端資料做起，再視需求投資機巢，是更穩的路。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>自動機場現在成熟嗎？</summary><div class="faq-a">已有多家廠商推出商用機巢，但維運、供電與法規仍在快速演進，導入前建議先實證、再規模化。</div></details>
  <details><summary>小農用得著嗎？</summary><div class="faq-a">單一小農需求通常不高；透過合作社或服務隊共享機場，才是攤平成本、讓小農也受益的方式。</div></details>
</div>""",
 ("reg-cost","農用無人機成本全解析"), ("future-sustain","無人機與永續農業"))

ART["future-sustain"] = (
 "無人機與永續農業：減藥、減水、減碳怎麼落地",
 "無人機常被視為「效率工具」，但它更大的價值在於降低農業的環境足跡。本文談減藥、減水、減碳三個角度，以及友善農業中的實際角色。",
 ["永續","減藥","ESG"], "lin",
 [("pest","減藥：變量施藥"),("water","減水：精準灌溉"),("carbon","減碳：省工與數據"),("org","友善與坡地保育"),("faq","常見問答")],
 """<h2 id="pest">減藥：變量施藥</h2>
<p>傳統施藥「整片同量」，其實很多藥噴在不需施藥的地方。無人機結合監測影像與處方圖，能<strong>依田區健康度動態調整施藥量</strong>——該噴的區塊足量、不需處理的區塊少噴或不噴。這是「減藥」最直接的一條路，也能降低藥劑殘留與鄰田風險。</p>

<h2 id="water">減水：精準灌溉</h2>
<p>熱影像能看出哪裡缺水、哪裡灌溉不均。把「哪裡缺水」的地圖接回灌溉系統，就能只補該補的區塊，避免整田大水漫灌。省水之外，也省抽水耗能與肥料流失。</p>

<h2 id="carbon">減碳：省工與數據</h2>
<p>無人機省下大量往返與人工，間接降低油料與人力碳排；更重要的是，<strong>數據讓決策更準</strong>——減少不必要的用藥、用肥與灌溉，本身就是減碳。未來若搭配電動機隊與綠電，單位作業碳排會更低。</p>

<h2 id="org">友善與坡地保育</h2>
<p>在有機與友善農業中，雜草與病蟲管理不靠化學藥劑，改靠「早期發現、精準處理」。無人機的空拍監測正好補上這個需求。對陡峭坡地與零碎農地，無人機也能在不破壞地形的前提下巡視與補資材，是坡地保育的輔助好幫手。</p>
<div class="callout green"><span class="ct">永續不是口號</span>永續農業的關鍵是「以更少投入，維持產量與品質」。無人機把「看得見田況」變成低成本常態，正是往這個方向走。從變量施藥與監測做起，效果最快、也最可量測。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>減藥一定省成本嗎？</summary><div class="faq-a">多數情況下能省藥與省工，但需投入監測與設備。建議先在小區塊實證，量到「省下的藥量與工時」再擴大。</div></details>
  <details><summary>友善農場適合嗎？</summary><div class="faq-a">適合。早期病蟲草害偵測對無藥農場尤其有價值，配合人工或局部物理防治，能顯著降低損失。</div></details>
</div>""",
 ("future-auto","從人工噴藥到全自動機場"), ("resources","案例資源"))

ART["resources-tools"] = (
 "田間作業檢核表：出機前後逐項確認",
 "飛行前後最怕漏東漏西。這張檢核表把出機、施作與收工的重點列成可勾選清單，幫你建立穩定、安全、合規的作業習慣。",
 ["檢核表","作業","安全"], "team",
 [("pre","出機前"),("during","飛行中"),("post","收工後"),("how","怎麼用這張表")],
 """<p>這張檢核表是給「有基礎的飛手」用的實務工具，涵蓋機況、法規、安全與記錄四面向。可印出或在地面站旁對照，逐項勾選。</p>
<h2 id="pre">出機前</h2>
<ul class="check">
  <li>確認飛行區域不在禁飛／限制區，符合當區法規</li>
  <li>機體已完成登記（若適用），標誌清楚</li>
  <li>操作者具對應證照（若適用）</li>
  <li>天候：風速、降雨、溫度符合作業上限</li>
  <li>電池滿電、無膨脹、電量夠任務加返航餘裕</li>
  <li>槳葉無缺損、馬達與機體無異狀</li>
  <li>藥箱（若噴藥）清洗、噴嘴暢通、藥劑與濃度確認</li>
  <li>RTK/GPS 訊號正常，返航點與高度已設定</li>
  <li>作業區無人群、牲畜與敏感設施，鄰田已溝通</li>
</ul>
<h2 id="during">飛行中</h2>
<ul class="check">
  <li>全程盯圖傳與電量，異常即返航</li>
  <li>風向風速驟變時暫停或調整</li>
  <li>航線與施藥量如規劃執行，不臨時亂改</li>
  <li>保持與障礙物、人群的安全距離</li>
</ul>
<h2 id="post">收工後</h2>
<ul class="check">
  <li>清洗藥箱、噴嘴與機身，避免殘留與腐蝕</li>
  <li>電池低溫充電保養，記錄循環次數</li>
  <li>檢查槳葉與機體，發現損傷即處置</li>
  <li>記錄作業時間、藥劑、用量、天氣與影像路徑</li>
  <li>資料已備份或上雲，作為履歷與追溯</li>
</ul>
<div class="callout"><span class="ct">怎麼用</span>把「出機前」固化成固定流程，就能大幅降低失誤。檢核表不是叫你慢慢勾，而是幫你養成「起飛前想一遍」的肌肉記憶。</div>""",
 ("resources","案例資源"), ("resources-training","飛手培訓與學習資源"))

ART["resources-training"] = (
 "飛手培訓與學習資源：從新手到能接案的管道",
 "想當農用無人機飛手，考證照、練技術、接案，分別該走哪些管道？本文整理從新手到可接案的學習路徑與資源類型。",
 ["培訓","證照","接案"], "chen",
 [("path","先想清楚目標"),("cert","考證照"),("skill","練技術的管道"),("job","從練到接案")],
 """<h2 id="path">先想清楚目標</h2>
<p>「學無人機」有三種不同目標，管道也不同：想<strong>休閒空拍</strong>、想<strong>做農用作業</strong>、想<strong>接案當職業</strong>。先定位，才不會學了一堆用不到的東西。</p>
<h2 id="cert">考證照</h2>
<p>從事特定級別與用途的飛行需取得操作證，測驗含學科（法規、原理）與術科。建議：先讀主管機關的測驗範圍，再報考對應級別。證照是接商用案的基本門票。</p>
<h2 id="skill">練技術的管道</h2>
<ul>
  <li><strong>官方/合規課程：</strong>主管機關或受認可單位的培訓，兼顧法規與術科。</li>
  <li><strong>模擬器與地面站：</strong>低成本練航線與返航，是成本最低的練習。</li>
  <li><strong>業者/飛防隊實習：</strong>跟有經驗的飛手出機，學真實作業與風險處理。</li>
  <li><strong>資料處理課：</strong>若走測繪/監測，補上拼圖、NDVI 與雲端處理技能。</li>
</ul>
<h2 id="job">從練到接案</h2>
<div class="callout green"><span class="ct">務實建議</span>接案前先以小範圍、低風險案子累積經驗與口碑；備好保險、證照與作業記錄。農用噴藥涉及藥劑，務必由具備資格的飛手執行，並對客戶講清楚合規與風險。</div>
<p>接案的養成不是「上完課就會」，而是「考照 → 實習 → 小案 → 大案」的累積。比起急著接單，先讓自己的機況與判斷力無懈可擊，口碑才是接案的護城河。</p>""",
 ("resources-tools","田間作業檢核表"), ("resources","案例資源"))

# ============================================================
# 新增條目（37 篇補齊計畫：種子 2 篇 + 子代理產出 35 篇）
# ============================================================
# ---- 種子文章（模式樣本）：tech-power、agri-pre ----
ART["tech-power"] = (
 "電池與動力系統：續航、換電與保養實務",
 "續航是農用無人機最主要的限制，也是作業排程的起點。本文從電池規格、動力匹配到保養汰換，一次看懂怎麼讓機子飛得久、飛得穩。",
 ["電池","動力","續航"], "lin",
 [("bat","先看懂電池與續航"),("power","動力系統怎麼匹配"),("ops","作業現場的電量管理"),("care","電池保養與汰換"),("faq","常見問答")],
 """<h2 id="bat">先看懂電池與續航</h2>
<p>農用無人機的續航由「電池能量 × 動力效率 ÷ 任務耗能」決定。能量看電池容量與放電能力，耗能看載重、風速與飛行模式。相同電池，空機巡田與滿載噴藥的續航可以差到一半以上。</p>
<figure style="margin:18px 0"><img src="img/drone_electronics_detail.webp" alt="無人機電子與動力元件特寫" style="width:100%;max-width:760px;margin:0 auto;border-radius:10px" loading="lazy"><figcaption style="margin-top:8px;font-size:14px;color:#667;text-align:center">動力與電子元件是續航與穩定的關鍵，作業前值得逐一檢查。</figcaption></figure>
<div class="callout"><span class="ct">核心原則</span>「剩餘電量＝返航紅線」。任務耗電要預留返航與意外繞行餘裕，寧可少飛一趟，也不要低電量硬撐回程。</div>
<ul>
  <li><strong>容量：</strong>以安時（Ah）或瓦時（Wh）標示，決定「能裝多少能量」。</li>
  <li><strong>放電倍率（C 數）：</strong>決定瞬間能吐出多少電流，滿載爬升最吃這個。</li>
  <li><strong>重量：</strong>電池越重續航越長，但會擠壓載重空間，兩者要取捨。</li>
</ul>

<h2 id="power">動力系統怎麼匹配</h2>
<p>動力系統由馬達、電變（ESC）與槳葉組成。農用機追求的不是「快」，而是「載重下的穩定推力」。挑選重點：</p>
<div class="tablewrap"><table>
<caption>動力系統三大件的角色（依主流規格整理，實際以機型為準）</caption>
<thead><tr><th>元件</th><th>角色</th><th>挑選／保養重點</th></tr></thead>
<tbody>
<tr><td>馬達</td><td>把電能轉成轉速與推力</td><td>KV 值與槳葉搭配、散熱與防塵</td></tr>
<tr><td>電變 ESC</td><td>控制馬達轉速與煞車</td><td>電流上限要留餘裕，過熱即檢查</td></tr>
<tr><td>槳葉</td><td>把轉速變成升力</td><td>變形、缺角即換，是首要耗材</td></tr>
</tbody></table></div>
<p>動力匹配錯誤的常見後果：馬達過熱、電變燒毀、槳葉共振。原廠動力組合最穩，改裝前先確認規格相容。</p>

<h2 id="ops">作業現場的電量管理</h2>
<ol>
  <li><strong>備足電池組：</strong>依當日作業量準備可輪替的電池組數，規劃「飛行—換電」節奏。</li>
  <li><strong>起飛前看電壓與溫度：</strong>電壓過低、溫度異常都不應起飛。</li>
  <li><strong>設定低電量返航：</strong>在地面站設好剩餘電量／電壓觸發值，讓系統代你守住紅線。</li>
  <li><strong>記錄每趟耗電：</strong>用歷史數據推算後續航次，比憑感覺可靠。</li>
</ol>
<figure style="margin:18px 0"><img src="img/drone_tools_parts_table.webp" alt="無人機工具與備用零件" style="width:100%;max-width:760px;margin:0 auto;border-radius:10px" loading="lazy"><figcaption style="margin-top:8px;font-size:14px;color:#667;text-align:center">電池、工具與備料隨車備妥，換電與臨時檢修才不耽誤作業。</figcaption></figure>

<h2 id="care">電池保養與汰換</h2>
<p>電池是農用機成本中被低估最多的部分，保養得當能延壽不少：</p>
<ul class="check">
  <li>存放於陰涼乾燥處，避免高溫與陽光直射</li>
  <li>長期存放保持適度電量（約一半上下），不過充不過放</li>
  <li>充電時有人看顧，避免過充與充電器異常</li>
  <li>膨脹、漏液、電壓異常的電池立即停用並依規範回收</li>
  <li>記錄循環次數，接近壽命末期就汰換，別硬撐</li>
</ul>
<div class="callout green"><span class="ct">汰換判斷</span>「還能飛」不代表安全。循環次數高、內阻上升、續航明顯縮水的電池，就該退役——省一顆電池的錢，可能賠上一整趟作業與機體。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>多帶電池就能解決續航嗎？</summary><div class="faq-a">可以提升「總作業量」，但單趟續航仍受載重與天氣限制；換電節奏與作業排程配合得好，效率才高。</div></details>
  <details><summary>可以用更大容量電池延長續航？</summary><div class="faq-a">電池規格須與機體、電變相容，容量升級同時增加重量，未必划算。請以原廠支援的規格為準。</div></details>
  <details><summary>電池冬天是不是掉電特別快？</summary><div class="faq-a">低溫會降低電池可用容量與放電能力，冬天作業前先讓電池回暖，並縮短單趟任務規劃。</div></details>
</div>""",
 ("tech-starter","無人機技術怎麼入門"), ("tech-nav","定位、避障與導航"))

ART["agri-pre"] = (
 "田區勘測與面積量測：用空拍一次把田摸清楚",
 "用空拍把面積、地形與分區一次量清楚，省下踏田時間。本文說明勘測飛行怎麼規劃、資料怎麼處理，以及面積與地形量測的實務要點。",
 ["勘測","面積","測繪"], "lin",
 [("why","為什麼用空拍勘田"),("plan","勘測飛行怎麼規劃"),("data","面積與地形怎麼量"),("use","量完之後怎麼用"),("faq","常見問答")],
 """<h2 id="why">為什麼用空拍勘田</h2>
<p>傳統勘田靠捲尺與雙腳，大面積田要走到腿軟，坡地與零碎田更難量。空拍一次飛完，後續用軟體量面積、看地形、劃分區，速度快且可重複——同一塊田可以年年比對，看出界線與使用變化。</p>
<div class="callout"><span class="ct">第一步的價值</span>面積與地形是後續所有決策的底圖：買藥量、排航線、算成本、申請補助，全都從「這塊田到底多大、長什麼樣」開始。</div>

<h2 id="plan">勘測飛行怎麼規劃</h2>
<ul>
  <li><strong>高度與重疊：</strong>依需要的解析度定高度，航線留足前後／左右重疊，後製拼接才不破圖。</li>
  <li><strong>固定航線：</strong>把勘測航線存檔，日後重飛同一航線，資料才可比。</li>
  <li><strong>地面控制點：</strong>要更精準的面積與地形，可布設地面控制點校正定位。</li>
  <li><strong>天候：</strong>無風或微風、光線穩定時拍攝，畫面品質最好。</li>
</ul>

<h2 id="data">面積與地形怎麼量</h2>
<p>空拍影像經拼接與地理校正後，就能在測繪軟體裡圈出田界、量出面積，並產出地形等高線與坡度圖。量測精度與定位方式（GPS／RTK）、飛行高度及控制點有關，需高精度用途請採用 RTK 與地面控制點。</p>
<div class="tablewrap"><table>
<caption>不同用途建議的量測方式（示意，精度以實際設備與作業為準）</caption>
<thead><tr><th>用途</th><th>建議方式</th><th>精度取向</th></tr></thead>
<tbody>
<tr><td>面積概算、買藥量估</td><td>空拍拼接 + 一般定位</td><td>夠用即可</td></tr>
<tr><td>申請補助、界址疑義</td><td>RTK + 地面控制點</td><td>高精度</td></tr>
<tr><td>坡度與排水規劃</td><td>空拍建模 + 等高線</td><td>地形還原度</td></tr>
</tbody></table></div>

<h2 id="use">量完之後怎麼用</h2>
<ol>
  <li>把面積、地形與分區存成田區基本資料，接續種植規劃。</li>
  <li>依坡度與地界規劃噴藥、撒肥航線，避開風險區。</li>
  <li>逐年重測，追蹤田區變化，作為履歷與決策依據。</li>
</ol>
<div class="callout green"><span class="ct">務實提醒</span>量測結果用於正式用途（如補助申請）前，請先確認主管機關對測量方式與精度的要求，必要時委託具備測量專業的單位。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>小田塊值得空拍勘測嗎？</summary><div class="faq-a">值得。一次空拍就能留下面積與地形底圖，日後規劃與履歷都用得到；面積小就飛一兩趟，成本很低。</div></details>
  <details><summary>量出來的面積和地籍資料不同？</summary><div class="faq-a">空拍量的是「實際耕作邊界」，與地籍登記面積可能不同（田埂、溝渠、道路等）。以用途為準：作業規劃用實測，正式申報以主管機關認定為準。</div></details>
  <details><summary>一定要買測繪軟體嗎？</summary><div class="faq-a">不必。多數地面站與雲端平台已內建拼接與量測功能，先用手邊工具跑一次流程，再決定要不要投資專業軟體。</div></details>
</div>""",
 ("agri","農業產業鏈"), ("agri-soil","土壤分區與種植規劃"))

# ==== 外部內容插入點（子代理產出的 part_*.py 內容將整合於此） ====

# agri 與 life 支柱新增條目（agri_life）
TITLE.update({
  "agri-chain": "機具維修供應鏈：從採購、耗材到保養，把農用機的後勤接起來",
  "life-record": "旅行、風景空拍：把旅程與風景拍出不一樣的視角",
  "life-event": "活動與婚禮紀錄：為重要時刻留下空中視角",
  "life-deliver": "山區、偏鄉配送：無人機小件運送的最後一哩試驗",
})

ART.update({
  "agri-chain": (
    "機具維修供應鏈：從採購、耗材到保養，把農用機的後勤接起來",
    "機體、電池、維修與數據平台的服務供應鏈。",
    ["供應鏈", "維修", "售服"], "lin",
    [("buy", "機體採購：先看後勤再看標價"),
     ("consumable", "電池與耗材：最日常的供應鏈"),
     ("repair", "維修保養：找服務商還是自修"),
     ("data", "數據平台與保險"),
     ("skill", "建立自有維護能力"),
     ("faq", "常見問答")],
    """<h2 id="buy">機體採購：先看後勤再看標價</h2>
<p>農用無人機是「買一次、用好幾年」的生產工具，採購時最容易被忽略的不是規格，而是後勤：這台機子的零件好不好叫？壞了多久能修？原廠或代理商在你所在的區域有沒有據點？一台再強的機，只要零件缺貨、送修要等上很久，農忙季一停擺就是直接損失。</p>
<ul>
  <li><strong>原廠保固範圍：</strong>確認保固涵蓋哪些元件、人為碰撞是否給付，送修流程與聯絡窗口要先問清楚。</li>
  <li><strong>代理商與服務據點：</strong>在地有據點或簽約維修站，臨場支援速度差很多。</li>
  <li><strong>零件供應穩定度：</strong>熱門耗材與常用備件是否常備供貨，避免「停產等料」。</li>
  <li><strong>韌體與技術更新：</strong>能否持續更新韌體、取得航線與感測功能的新版本。</li>
</ul>
<figure style="margin:18px 0"><img src="img/drone_frame_showcase.webp" alt="農用無人機機架結構展示" style="width:100%;max-width:760px;margin:0 auto;border-radius:10px" loading="lazy"><figcaption style="margin-top:8px;font-size:14px;color:#667;text-align:center">機架是所有維修與改裝的基底，採購時一併了解它的拆解與備件方式。</figcaption></figure>
<div class="callout"><span class="ct">選購原則</span>同一級別裡，寧可選「後勤好、零件好叫」的機種，也不要只看標價便宜。農忙季的停機成本，往往比機體本身的差價更可觀。</div>

<h2 id="consumable">電池與耗材：最日常的供應鏈</h2>
<p>真正決定出勤率的，不是機體本身，而是耗材。槳葉、電池、噴嘴、濾網、泵浦墊圈這些東西會持續消耗，備料斷貨就等於停機。把它們當成「農資」來管理，固定備安全庫存。</p>
<div class="tablewrap"><table>
<caption>常見耗材的供應與備料觀念（依主流作業經驗整理，實際以機型為準）</caption>
<thead><tr><th>耗材項目</th><th>消耗特性</th><th>備料建議</th></tr></thead>
<tbody>
<tr><td>槳葉</td><td>碰撞、沙塵即損，最常更換</td><td>隨車常備一整組</td></tr>
<tr><td>電池</td><td>循環壽命有限，屬漸進汰換</td><td>依作業量準備可輪替組數</td></tr>
<tr><td>噴嘴／濾網</td><td>藥劑殘易堵塞</td><td>每次作業後清理，備數個備品</td></tr>
<tr><td>泵浦墊圈、管路</td><td>老化、漏液</td><td>季節性檢查更換</td></tr>
<tr><td>馬達／電變</td><td>屬故障件、非常備</td><td>找原廠或服務商叫料</td></tr>
</tbody></table></div>
<figure style="margin:18px 0"><img src="img/drone_parts_closeup_hands.webp" alt="雙手檢查無人機備用零件" style="width:100%;max-width:760px;margin:0 auto;border-radius:10px" loading="lazy"><figcaption style="margin-top:8px;font-size:14px;color:#667;text-align:center">每次出工前過一遍備料，耗材齊全才不會在田邊停擺。</figcaption></figure>

<h2 id="repair">維修保養：找服務商還是自修</h2>
<p>維修可以分成兩層：<strong>日常檢查與耗材更換</strong>多數飛手自己就能做；<strong>涉及電子、飛控與動力的故障</strong>則建議交給原廠或合格服務商。問題在於怎麼判斷「自己能修到哪」。</p>
<div class="procon">
  <div class="pc pro"><h4>委外維修的好處</h4><ul><li>原廠有檢測儀器與技術資訊，判斷準</li><li>保固期內送修較有保障</li><li>複雜電子故障免自行冒險</li></ul></div>
  <div class="pc con"><h4>自修的條件</h4><ul><li>耗材更換、外觀與螺絲緊固可自行處理</li><li>需有工具、料件與基本電子常識</li><li>飛控、電變等進度故障不建議自修</li></ul></div>
</div>
<figure style="margin:18px 0"><img src="img/drone_wiring_soldering.webp" alt="無人機線路焊接維修" style="width:100%;max-width:760px;margin:0 auto;border-radius:10px" loading="lazy"><figcaption style="margin-top:8px;font-size:14px;color:#667;text-align:center">焊接與走線屬於進階維修，建議在有師傅指導下操作。</figcaption></figure>
<p>實務上常見的分工是：飛手負責「收工清洗、槳葉更換、外觀與螺絲檢查、電池保養」；原廠或服務站負責「動力、飛控、圖傳等電子件故障」。把這條界線先畫清楚，故障時才不會手忙腳亂。</p>

<h2 id="data">數據平台與保險</h2>
<p>供應鏈不只硬體。農用機越來越依賴地面站、雲端處理與航線管理平台，這些軟體是否持續維護、資料能不能順利匯出、中斷後能不能切換替代工具，都會影響長期使用。另外，機體登記、責任險與第三方責任規劃，也是營運前應該一併處理的環節。</p>
<ul class="check">
  <li>確認使用的地面站與雲端平台仍持續更新與維運</li>
  <li>定期備份航線、作業紀錄與影像，避免平台綁架</li>
  <li>機體完成登記，操作符合證照要求（以主管機關現行公告為準）</li>
  <li>評估適當的機體保險與第三人責任規劃</li>
</ul>
<div class="callout"><span class="ct">軟體也是供應鏈</span>當你依賴某個平台排航線、看數據，就要留意它的存續與資料可攜性。隨時保留匯出能力，才不會在服務收掉時一籌莫展。</div>

<h2 id="skill">建立自有維護能力</h2>
<p>長期下來，與其每次小毛病都等服務商，不如逐步建立基本的自修能力。可以從跟原廠或合格修護站一次完整的季檢開始，請師傅當面說明機架拆解、走線、螺絲鎖付與日常檢查重點；有需要再進修組裝與電子基礎課程。懂得基本判斷，送修時也能講清楚問題、避免被報價灌水。</p>
<figure style="margin:18px 0"><img src="img/drone_instructor_guidance.webp" alt="師傅指導學員進行無人機維修" style="width:100%;max-width:760px;margin:0 auto;border-radius:10px" loading="lazy"><figcaption style="margin-top:8px;font-size:14px;color:#667;text-align:center">跟著資深師傅實地學一次季檢，勝過自己摸索好幾遍。</figcaption></figure>
<div class="callout green"><span class="ct">務實建議</span>把「原廠／服務商」與「自己」的分工白紙黑字寫下來：哪些自己處理、哪些送修、備料庫存放哪、誰負責聯絡窗口。這套後勤 SOP，才是農用機長期穩定出勤的真正底盤。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>買農用機時，後勤要怎麼問原廠？</summary><div class="faq-a">直接問三件事：保固範圍與送修流程、常用備件是否常備供貨、你所在地有沒有簽約服務站。把這些答案寫進比選條件，比只比標價更實在。</div></details>
  <details><summary>什麼故障絕對不要自己修？</summary><div class="faq-a">飛控、電變、馬達繞線與電池相關的電子故障，牽涉安全與除膠焊接，建議交給原廠或合格服務商；自修只建議做耗材更換與外觀檢查。</div></details>
  <details><summary>一定要保險嗎？</summary><div class="faq-a">植保噴藥與高空作業有第三方風險，商業用途建議評估適當的機體與責任保險。實際投保內容以保險公司商品與法規要求為準。</div></details>
</div>""",
    ("agri-service", "飛防與測繪服務隊"), ("agri", "農業產業鏈")),

  "life-record": (
    "旅行、風景空拍：把旅程與風景拍出不一樣的視角",
    "用空拍記錄旅程與風景，最親民的入門用法。",
    ["空拍", "旅行", "風景"], "xu",
    [("subject", "旅行空拍拍什麼題材"),
     ("light", "抓住好光線與構圖"),
     ("law", "法規與禁飛區：出門前必查"),
     ("safe", "安全與場景紀律"),
     ("faq", "常見問答")],
    """<h2 id="subject">旅行空拍拍什麼題材</h2>
<p>旅行帶空拍機最大的好處，是把「走不到、爬不上」的角度一次收進畫面。但空拍不是「起飛就有好畫面」，要先想好你想記錄什麼。旅行中最耐看的題材通常是這幾類：</p>
<ul>
  <li><strong>地標與空景：</strong>廟宇、海岸、湖泊、梯田這類從地面看就有限、從空中才有規模感的場景。</li>
  <li><strong>旅程動線：</strong>用空拍把「你在路上」這件事拍出來——車軌、步道、海岸線上的行進。</li>
  <li><strong>人與環境的比例：</strong>把旅人放進大景觀裡，一個小小的身影對比遼闊風景，往往最有故事感。</li>
  <li><strong>時間性場景：</strong>日出、日落、雲瀑、海面反光等可遇不可求的畫面。</li>
</ul>

<h2 id="light">抓住好光線與構圖</h2>
<p>同一個地點，清晨黃昏與正午看起來完全是兩個世界。旅行空拍最值得等的就是「好光」，而不是硬拍。</p>
<div class="tablewrap"><table>
<caption>不同時段的空拍表現（依主流拍攝經驗整理）</caption>
<thead><tr><th>時段</th><th>光線特色</th><th>適合題材</th></tr></thead>
<tbody>
<tr><td>清晨破晓</td><td>光線柔和、人少、易有薄霧</td><td>山景、田園、海面</td></tr>
<tr><td>正午</td><td>光線平、陰影硬</td><td>地形紋理、建築細節</td></tr>
<tr><td>黃昏</td><td>暖色調、影子長</td><td>海岸、城市天際線剪影</td></tr>
<tr><td>入夜</td><td>光源多但需注意夜航規定</td><td>城市夜景（需確認可飛）</td></tr>
</tbody></table></div>
<p>構圖上記得「留白」：空拍畫面很容易塞滿，適度把主題放在邊角、留出大面積的海或天，反而更耐看。先定鏡頭動線（前進、拉升、環繞）再起飛，不要邊飛邊想。</p>

<h2 id="law">法規與禁飛區：出門前必查</h2>
<p>旅行最容易踩雷的就是「到了現場才發現不能飛」。風景漂亮的地方，往往正好在禁飛或限制區內——機場周邊、國家公園部分區域、政府機關、軍事設施、熱門觀光據點的人潮上空，都可能有限制。</p>
<div class="callout"><span class="ct">起飛前必做</span>用官方或合規的飛行區域查詢工具，確認當前位置是否禁飛、是否需要申請；並確認機體登記與操作者資格符合當區規定。法規會調整，一切以主管機關現行公告為準。</div>
<ul>
  <li><strong>觀光熱點：</strong>人潮多、視線複雜，常設額外限制或需申請。</li>
  <li><strong>國家公園與保護區：</strong>部分區域全面禁飛，不要僥倖。</li>
  <li><strong>跨縣市移動：</strong>每到一個新縣市，習慣性重查一次，別用上一站的經驗直接套用。</li>
</ul>

<h2 id="safe">安全與場景紀律</h2>
<p>旅行空拍的風險往往來自「環境陌生」：突然起風、訊號被山壁擋、腳邊就是懸崖或海浪。建立基本紀律比拍得炫更重要。</p>
<ul class="check">
  <li>起飛前設好返航點與返航高度，確認高過周圍山壁與樹梢</li>
  <li>隨時留足返航電量，不在低電量下貪拍</li>
  <li>風速超過機型抗風等級就收機，山區風況變化快</li>
  <li>不在人群上方、道路上方貼飛，保持安全距離</li>
  <li>海邊與沙地做好防鹽、防沙，落地後清潔機體</li>
</ul>
<div class="callout green"><span class="ct">旅行心法</span>空拍機是旅行的加分項，不是主角。別為了一個畫面在懸崖邊或強風裡硬飛——拍不到可以下次再來，機子摔了或傷到人就是一整趟旅程的終點。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>旅行帶哪種空拍機最適合？</summary><div class="faq-a">以輕、穩、好攜帶為主。旅行走動多，機體越輕越願意帶出門；重量與登記限制也要一併考慮，避免到現場不能飛。</div></details>
  <details><summary>風景區一定可以自由飛嗎？</summary><div class="faq-a">不一定。很多熱門風景點正好在禁飛或限制區。出發前先查飛行區域，並留意人潮上空的額外規範。</div></details>
  <details><summary>幾顆電池才夠用一天？</summary><div class="faq-a">依景點數量與單趟拍攝長度彈性準備，建議至少備足可全天輪替的數量，並把握黃金光線時段集中拍攝。</div></details>
</div>""",
    ("life", "無人機與生活"), ("life-event", "活動與婚禮紀錄")),

  "life-event": (
    "活動與婚禮紀錄：為重要時刻留下空中視角",
    "為重要時刻留下空中視角的獨特畫面。",
    ["活動", "婚禮", "紀錄"], "xu",
    [("plan", "事前規劃與場勘"),
     ("shoot", "當天怎麼拍"),
     ("audio", "收音與現場配合"),
     ("privacy", "肖像權與人群上空的紅線"),
     ("faq", "常見問答")],
    """<h2 id="plan">事前規劃與場勘</h2>
<p>婚禮與活動空拍和一般風景拍攝最大的不同，是「現場不能重來」。賓客進場、儀式時刻、雙方親友的反應都是一次過，所以事前規劃比當天臨場反應更重要。</p>
<ol>
  <li><strong>先場勘：</strong>確認場地能不能飛、四周有沒有電線與建築、風況與光線狀況。</li>
  <li><strong>抓關鍵時刻：</strong>和新人或主辦方對照流程表，標出一定要從空中記錄的環節（進場、進場式、敬酒、送客）。</li>
  <li><strong>定鏡頭清單：</strong>事先想好每個環節要什麼空拍畫面，當天照表操作，不要現場臨時想。</li>
  <li><strong>準備備援：</strong>備用電池、備用機或至少備用槳葉與手機，避免現場臨時故障。</li>
</ol>

<h2 id="shoot">當天怎麼拍</h2>
<p>活動現場人多、聲音雜、時程壓力大，空拍的角色是「補一個地面攝影師拍不到的角度」，而不是搶鏡頭。</p>
<ul>
  <li><strong>先空景後人物：</strong>在賓客還沒到滿前，先把場地全景、空廊與空景拍完。</li>
  <li><strong>環繞與拉升為主：</strong>穩定的環繞、爬升拉遠這類鏡頭最適合婚禮，不要做激烈翻滾。</li>
  <li><strong>保持安靜與距離：</strong>螺旋槳噪音大，飛行位置避開儀式進行的核心區，寧可遠一點用變焦。</li>
  <li><strong>與地面攝影師分工：</strong>先溝通好誰拍什麼，避免空拍機干擾地面團隊作業。</li>
</ul>
<div class="tablewrap"><table>
<caption>婚禮／活動空拍的環節與建議鏡頭（依主流拍攝經驗整理）</caption>
<thead><tr><th>環節</th><th>建議空拍畫面</th></tr></thead>
<tbody>
<tr><td>賓客進場前</td><td>場地全景、空廊、空桌布置</td></tr>
<tr><td>儀式進行中</td><td>遠距高空全景，不干擾現場</td></tr>
<tr><td>敬酒、送客</td><td>人群鳥瞰、氣氛空景</td></tr>
<tr><td>活動尾聲</td><td>拉升拉遠的收場大景</td></tr>
</tbody></table></div>

<h2 id="audio">收音與現場配合</h2>
<p>無人機本身收音品質有限、螺旋槳噪音又大，<strong>重要場合的聲音不要靠空拍機收</strong>。誓詞、致詞這類關鍵音軌，應由地面的收音設備或錄音團隊處理，空拍影像事後再配上正確音軌。</p>
<div class="callout"><span class="ct">分工原則</span>空拍負責「畫面」，聲音與現場主持由地面團隊處理。事後把空拍畫面與地面音軌剪在一起，才是完整的紀錄，不要指望一台機子包辦全部。</div>

<h2 id="privacy">肖像權與人群上空的紅線</h2>
<p>活動空拍最容易被忽略的是「人」的問題。你拍的不只是風景，還有上百位賓客的臉與私人場合。這幾條界線要先守住：</p>
<ul class="check">
  <li>於企劃階段向主辦方確認空拍拍攝與公開使用的授權範圍</li>
  <li>避免特寫單一賓客的清楚臉部，全景為主</li>
  <li>不在人群正上方低空飛行，保持安全距離與高度</li>
  <li>確認場地不在禁飛區，人潮聚集處的飛行限制以主管機關現行公告為準</li>
  <li>後製對外發布前，再次確認露出畫面的授權</li>
</ul>
<div class="callout green"><span class="ct">隱私優先</span>婚禮是當事人的私人場合。事前白紙黑字講清楚「會不會有空拍、影像未來會不會對外曝光」，比事後賠償或爭議划算得多。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>婚禮空拍一定要找專業嗎？</summary><div class="faq-a">重要場合一次過、風險高，建議交由熟悉活動節奏的空拍／錄影團隊。業餘練手容易錯過關鍵畫面或在人群上空出狀況。</div></details>
  <details><summary>會場室內可以飛嗎？</summary><div class="faq-a">室內場館空間、訊號與人群條件都不同，多數婚宴會館不適合一般空拍機。空拍主要戶外進行，室內由地面攝影處理。</div></details>
  <details><summary>拍到賓客可以直接放社群嗎？</summary><div class="faq-a">務必先取得主辦方與當事人的授權，敏感或清楚特寫的畫面建議後製處理或不對外曝光。</div></details>
</div>""",
    ("life-record", "旅行、風景空拍"), ("life-deliver", "山區、偏鄉配送")),

  "life-deliver": (
    "山區、偏鄉配送：無人機小件運送的最後一哩試驗",
    "偏鄉小件配送試驗，縮短最後一哩。",
    ["配送", "偏鄉", "物流"], "xu",
    [("why", "偏鄉配送想解決什麼"),
     ("limit", "載重與續航的現實限制"),
     ("case", "常見的試驗場景"),
     ("reg", "法規與營運挑戰"),
     ("faq", "常見問答")],
    """<h2 id="why">偏鄉配送想解決什麼</h2>
<p>台灣偏遠山區、離島與沿海小聚落，面臨的不是「沒有物流」，而是「最後一哩成本太高」：一趟送藥、送文件，山路曲折、時效差，對醫療與緊急需求尤其不便。無人機配送的構想，就是繞過蜿蜒山路，用直線飛行把小件貨物快速送到定點，縮短這最後一哩。</p>
<div class="callout"><span class="ct">它解決的不是「大宗物流」</span>無人機配送目前最有意義的場景，是「高時效、小體積、重量輕」的東西——例如急件、藥品、樣本與小零件，而不是一般網購大宗包裹。</div>

<h2 id="limit">載重與續航的現實限制</h2>
<p>偏鄉配送的可行性，取決於兩個硬體現實：能載多重、能飛多遠。兩者都直接決定了「能送什麼、送到哪」。</p>
<div class="tablewrap"><table>
<caption>無人機配送的主要限制面向（依主流規格整理，實際以機型與任務為準）</caption>
<thead><tr><th>限制面向</th><th>影響</th><th>因應方式</th></tr></thead>
<tbody>
<tr><td>載重</td><td>只能送小件、輕量貨品</td><td>把貨品體積重量控制在掛載上限內</td></tr>
<tr><td>續航</td><td>山區來回距離受限</td><td>規劃中繼點、換電或預留返航電量</td></tr>
<tr><td>天候</td><td>風、雨、低能見度即停飛</td><td>挑天氣窗口、設停飛標準</td></tr>
<tr><td>地形遮蔽</td><td>山壁阻擋訊號與定位</td><td>預先勘航線、設中繼與備降點</td></tr>
</tbody></table></div>
<p>因為載重與續航有限，配送試驗多採「定點定線」的方式：在起飛站與定點降落站之間固定航線來回，而不是隨處起降。貨物多以專用吊掛或貨艙固定，落地後再由定點人員簽收。</p>

<h2 id="case">常見的試驗場景</h2>
<p>目前偏鄉無人機配送仍以「試驗與專案」為主，常見的場景包括：</p>
<ul>
  <li><strong>醫療物資：</strong>把急診所需藥品、檢體或血液製品快速送到偏遠診所，講求時效與低溫維持。</li>
  <li><strong>離島與沿岸：</strong>小島之間、海上與陸地之間的小件往來，繞過船班時間限制。</li>
  <li><strong>山區農資與樣本：</strong>把種子、農藥包裝或採檢樣本在山區定點間快速運送。</li>
  <li><strong>救災應變：</strong>道路中斷時，把緊急物資先送進受困區域。</li>
</ul>
<div class="procon">
  <div class="pc pro"><h4>潛在價值</h4><ul><li>縮短偏鄉時效、補上醫療缺口</li><li>山區不繞路、不受道路中斷影響</li><li>小量高時效場景成本有感</li></ul></div>
  <div class="pc con"><h4>現實限制</h4><ul><li>載重與續航限制大、貨種受限</li><li>天候與地形影響出勤率</li><li>定點設施與人力仍需配套</li></ul></div>
</div>

<h2 id="reg">法規與營運挑戰</h2>
<p>把「送東西」飛上天，牽涉的不只是飛行技術。物流用途屬於特定商業與操作情境，登記、證照、飛行申請與責任歸屬都比休閒空拍更嚴格；貨物本身的安全、落地簽收、丟損責任與保險，也都要先定清楚。</p>
<ul class="check">
  <li>確認商業配送用途的登記、證照與操作限制（以主管機關現行公告為準）</li>
  <li>劃定起飛站與降落站的合法區域，必要時提出專案申請</li>
  <li>貨物固定與吊掛安全，避免落地脫落或偏離</li>
  <li>建立落地簽收、異常通報與責任界定流程</li>
  <li>評估適當的保險，涵蓋第三方與貨物風險</li>
</ul>
<div class="callout green"><span class="ct">現階段定位</span>偏鄉無人機配送仍處於專案試驗與特定需求階段，不是「一般快遞」。它最有價值的地方，是在「山路很遠、時間很急、貨品很輕」的縫隙裡，補上傳統物流到不了的那一段。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>一般包裹能叫無人機送嗎？</summary><div class="faq-a">目前無人機配送仍以小量、高時效、輕量貨品為主，受載重與法規限制，尚未發展成一般大眾快遞的常態服務。</div></details>
  <details><summary>山區風大、訊號差，能穩定配送嗎？</summary><div class="faq-a">需要先勘查航線、設中繼與備降點，並把風況列為停飛條件。穩定度取決於事前規劃，而非硬飛。</div></details>
  <details><summary>貨物掉了誰負責？</summary><div class="faq-a">商業配送應先以合約與保險界定責任，涵蓋貨物安全與第三方風險，並建立落地簽收與異常通報流程。</div></details>
</div>""",
    ("life-event", "活動與婚禮紀錄"), ("life-patrol", "巡邏、搜救與勘查")),
})

# 農業產業鏈 支柱新增條目（part_agri_post）
# 收成後與下游／服務生態系：agri-post / agri-disaster / agri-trace / agri-service
TITLE.update({
  "agri-post": "產量預估與採收研判：把空拍數據延伸到收成之後",
  "agri-disaster": "災害勘災與損失評估：颱風、淹水與火災後的空中證據",
  "agri-trace": "農地履歷與品牌行銷：空拍影像做成溯源與行銷素材",
  "agri-service": "飛防與測繪服務隊：外包噴藥與測繪的商業模式與合作",
})

ART.update({
  "agri-post": (
    "產量預估與採收研判：把空拍數據延伸到收成之後",
    "從產量預估到採收時機，把數據延伸到收成之後。",
    ["產量預估","採收","測繪"], "lin",
    [("why","為什麼要在收成前先估產"),("how","空拍怎麼估產：影像、株數與果實計數"),("timing","採收時機怎麼研判"),("limit","估產的誤差與務實用法"),("faq","常見問答")],
    """<h2 id="why">為什麼要在收成前先估產</h2>
<p>產量預估不是為了報一個漂亮數字，而是讓後端接得住：什麼時候要請採工人、要預留多少收購與倉儲、行銷與契約要不要調整，都繞不過「這一季大概會收多少」。過去果農與稻農多靠經驗「看樹頭估」，大面積或分散田塊很容易估偏差。空拍把整片田一次性拍進來，提供了一個可重複、可逐年對照的估產起點。</p>
<div class="callout"><span class="ct">定位要清楚</span>空拍估產是「協助研判」，不是「磅秤」。它給的是趨勢與相對量，實際採收仍以田間抽樣與經驗為準——兩者互補，而非互相取代。</div>

<h2 id="how">空拍怎麼估產：影像、株數與果實計數</h2>
<p>主流做法大致分三條路，依作物與設備條件選擇，常互相搭配使用：</p>
<ul>
  <li><strong>影像長勢推估：</strong>用可見光或多光譜影像看冠層密度與植被指數的分佈，把「長得好、長得普通、長得差」的區塊量化成面積比例，再對照往年實際收量推估今年。</li>
  <li><strong>株數／穗數計算：</strong>水稻等高稈或條播作物，可用高解析影像估算有效植株數或分佈密度，作為穗數與產量推估的輸入。</li>
  <li><strong>果實計數：</strong>果樹類在掛果期以高解析影像搭配辨識模型，數出可見果實的相對數量與分佈，作為結果量的參考。</li>
</ul>
<div class="tablewrap"><table>
<caption>常見作物的空拍估產切入點（依主流做法整理，實際成效視品種與設備而定）</caption>
<thead><tr><th>作物類型</th><th>主要切入點</th><th>估產角色</th></tr></thead>
<tbody>
<tr><td>果樹（高接梨、荔枝、柑橘等）</td><td>冠層長勢 + 果實計數</td><td>判斷結果量與分佈，估總產</td></tr>
<tr><td>水稻</td><td>植株密度 + 植被指數動態</td><td>看長勢均勻度與潛在產量區</td></tr>
<tr><td>葉菜／雜糧</td><td>冠層覆蓋與長勢分區</td><td>預估可收面積與成熟進度</td></tr>
</tbody></table></div>
<div class="callout"><span class="ct">關鍵在「 ground truth 」</span>任何模型都要靠地面實際抽樣校正：選幾個代表性區塊，數真實果數或秤實收，再回頭調整影像推估的係數。沒有地面校正的空中數字，只是圖。</div>

<h2 id="timing">採收時機怎麼研判</h2>
<p>估產之外，空拍還能幫忙判斷「何時開始採收」。重點不是單張照片，而是<strong>時間序列</strong>：</p>
<ol>
  <li><strong>固定航線重複拍：</strong>從果實膨大到著色期，每隔一段時間拍一次，觀察長勢與色澤變化的區域差異。</li>
  <li><strong>找成熟先後：</strong>影像裡色差較大的區塊，常意味成熟度不一致，可據此規劃「分區、分批」採收。</li>
  <li><strong>接地面判斷：</strong>空拍標出的成熟先後，到田間用糖度、色澤、果梗狀態等指標確認，再定實際開採日。</li>
</ol>
<div class="callout green"><span class="ct">對後端的好處</span>把「哪塊田先熟、哪塊後熟」排出順序，採工人、貨車與收購點就能錯峰安排，避免果實一次集中成熟卻無人可收。</div>

<h2 id="limit">估產的誤差與務實用法</h2>
<p>務實看待空拍估產：冠層會遮擋果實、不同品種辨識難度不同、天候與光照也會影響影像。因此它的最佳用法是：</p>
<ul class="check">
  <li>當作「相對比較」工具——這塊比去年好還是差，比絕對數字更可靠</li>
  <li>當作「分區管理」依據——把田分成幾區分別估、分批收</li>
  <li>當作「預先規劃」參考——提早訂工人、談收購、安排倉儲</li>
  <li>絕對產量仍以實際採收與秤量為最終依據</li>
</ul>
<div class="callout"><span class="ct">一句話</span>空拍估產讓你「心裡有底、手上有計畫」，但不要把它當成對收購商拍胸脯的保證數字。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>果實計數能直接算出實際產量嗎？</summary><div class="faq-a">不能直接。影像只看得到外露果實，且需經地面抽樣校正。它比較適合用來判斷結果量的豐歉與分佈，實際產量仍要靠田間抽樣與歷年收量推估。</div></details>
  <details><summary>水稻用空拍估產準嗎？</summary><div class="faq-a">水稻空拍估產多用於看長勢均勻度與潛在豐歉區，屬於趨勢研判。要更準確仍需搭配分蘗、穗數等田間調查，兩者互相印證。</div></details>
  <details><summary>一定要買很貴的測繪機才能估產嗎？</summary><div class="faq-a">不必。先以可見光空拍做長勢分區與重複比對，就能得到初步參考；要更高階的果實計數與指數分析，再逐步升級設備或委外。</div></details>
</div>""",
    ("agri-assist","驅鳥、授粉與山區運補"), ("agri-disaster","災害勘災與損失評估")),

  "agri-disaster": (
    "災害勘災與損失評估：颱風、淹水與火災後的空中證據",
    "颱風、淹水與火災後的空中勘災。",
    ["勘災","災損","補助"], "lin",
    [("why","災後為什麼要趕快空拍"),("flow","空拍勘災的標準流程"),("assess","災損怎麼分級評估"),("evidence","照片證據與補助申請"),("faq","常見問答")],
    """<h2 id="why">災後為什麼要趕快空拍</h2>
<p>災後現場變動很快：傾倒植株被扶正、淹水退去、土壤乾了、清理人員進場，證據一旦消失就很難重建。空拍的價值在於「趁現場還原封不動時，從空中留下完整記錄」——整片受害範圍、淹水線、倒伏分佈，一兩趟空拍就能掌握，比逐塊走查快得多，也更有說服力。</p>
<div class="callout"><span class="ct">時效最關鍵</span>災後幾天內是勘災黃金期。既為自己留存證據，也方便後續向主管機關申請災損救助時佐證受災範圍。</div>

<h2 id="flow">空拍勘災的標準流程</h2>
<ol>
  <li><strong>先看天氣與法規：</strong>風勢穩定、無雨再飛；確認當區不在禁飛或臨時管制範圍，必要時依規定向主管機關申請。</li>
  <li><strong>先拍全景、再拍特寫：</strong>先以較大範圍、固定高度拍下整體受害分佈，再針對嚴重區塊低空拍特寫。</li>
  <li><strong>固定航線留檔：</strong>把勘災航線存下，日後重飛同一航線，可前後比對災後恢復進度。</li>
  <li><strong>記錄時間與位置：</strong>每段影像都要帶拍攝日期與坐標，證據力才完整。</li>
</ol>
<div class="tablewrap"><table>
<caption>常見災害類型的空拍重點（依主流勘災做法整理）</caption>
<thead><tr><th>災害類型</th><th>空拍重點</th><th>想留下的證據</th></tr></thead>
<tbody>
<tr><td>颱風風害</td><td>植株傾倒、折损分佈</td><td>倒伏範圍與嚴重區塊</td></tr>
<tr><td>淹水</td><td>淹水面積與水位線</td><td>被淹範圍、退水時間點</td></tr>
<tr><td>火災</td><td>焚燒邊界與过火面積</td><td>受損邊界、焚損程度</td></tr>
</tbody></table></div>

<h2 id="assess">災損怎麼分級評估</h2>
<p>空中影像適合判「面」，地面核查適合判「點」。實務上兩者分工：</p>
<ul>
  <li><strong>空拍看面：</strong>哪幾塊田受害、各自範圍多大、嚴重程度如何分佈，一次看清。</li>
  <li><strong>地面看點：</strong>到田間實際數折損株數、看果實與枝條損傷、評估後續恢復或復耕需求。</li>
</ul>
<div class="procon">
  <div class="pc pro"><h4>空拍勘災的好處</h4><ul><li>快速掌握整體受災範圍</li><li>證據即時、可重複比對</li><li>人員不必在危險現場久留</li></ul></div>
  <div class="pc con"><h4>要留意的限制</h4><ul><li>風雨未息時不宜起飛</li><li>樹冠遮擋，地下損傷看不完全</li><li>損失金額仍需地面與資料佐證</li></ul></div>
</div>

<h2 id="evidence">照片證據與補助申請</h2>
<p>空拍影像最大的下游用途，是做為農業災害救助與保險理賠的佐證材料。要讓證據站得住腳，留意幾個原則：</p>
<ul class="check">
  <li>影像帶有拍攝日期、時間與地理坐標</li>
  <li>先拍整體、後拍特寫，範圍與細節都有</li>
  <li>保留原始檔，不要只留經過裁切或編修的版本</li>
  <li>與田間照片、收貨紀錄等資料交叉佐證</li>
</ul>
<div class="callout green"><span class="ct">重要提醒</span>災害救助與保險的認定標準、應備文件與申請期限，各年度與各縣市可能不同，請以主管機關與保險公司的現行規定為準；空拍只是佐證，不能替代正式申請程序。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>颱風一過就能馬上飛嗎？</summary><div class="faq-a">不行。務必等風勢穩定、無殘留雨勢，且確認不在臨時管制範圍內再飛。安全永遠排在勘災之前。</div></details>
  <details><summary>空拍照片可以直接當補助證明嗎？</summary><div class="faq-a">空拍是很有說服力的佐證，但正式災損認定仍依主管機關規定的程序與文件。建議把空拍與田間照片、資料一起備齊。</div></details>
  <details><summary>自己沒有空拍機怎麼辦？</summary><div class="faq-a">可以委託當地的測繪或飛防服務隊協助災後空拍，重點是「趁現場還在時拍到」，越快越好。</div></details>
</div>""",
    ("agri-post","產量預估與採收研判"), ("agri-trace","農地履歷與品牌行銷")),

  "agri-trace": (
    "農地履歷與品牌行銷：空拍影像做成溯源與行銷素材",
    "空拍影像做成履歷，是溯源與行銷好素材。",
    ["履歷","溯源","品牌"], "lin",
    [("what","履歷為什麼需要空拍影像"),("build","怎麼把影像做成農地履歷"),("market","履歷素材怎麼變成行銷"),("care","資訊揭露與個資界線"),("faq","常見問答")],
    """<h2 id="what">履歷為什麼需要空拍影像</h2>
<p>產銷履歷的核心是「可追溯」：消費者或通路想知道這塊地在哪、長期怎麼種。過去履歷多靠文字紀錄與填表，空拍影像讓它多了一層「看得見」的證據——整片農地的位置、環境、週邊條件，以及一季下來的生長變化，都可以用影像記錄下來，比單純文字更有說服力。</p>
<div class="callout"><span class="ct">它解決什麼</span>空拍把「這塊田在哪、長什麼樣、週邊是什麼環境」變成客觀視覺紀錄，讓履歷從「自己說」走向「有畫面可查」。</div>

<h2 id="build">怎麼把影像做成農地履歷</h2>
<p>實務上不必一次做到很複雜，從固定動作開始累積就好：</p>
<ul>
  <li><strong>定期留底：</strong>在種植、生長關鍵期、採收等節點各空拍一次，形成時間序列。</li>
  <li><strong>固定航線：</strong>同一塊田每次用相近航線拍，前後影像才接得起來。</li>
  <li><strong>對應紀錄：</strong>把影像當季的施藥、施肥、灌溉等作業紀錄對照存放，影像與文字互相連結。</li>
  <li><strong>長期累積：</strong>連續幾季留下，就是一份完整、可追溯的農地履歷。</li>
</ul>
<div class="tablewrap"><table>
<caption>履歷影像可對應的資訊面向（示意，依各驗證制度要求調整）</caption>
<thead><tr><th>面向</th><th>空拍能呈現</th><th>搭配的文字紀錄</th></tr></thead>
<tbody>
<tr><td>農地位置與環境</td><td>地界、週邊設施、地形</td><td>地址、面積、土地基本資料</td></tr>
<tr><td>生長歷程</td><td>長勢變化的時間序列</td><td>作業日誌、施藥施肥紀錄</td></tr>
<tr><td>採收狀態</td><td>成熟分佈、採收範圍</td><td>採收量、出貨紀錄</td></tr>
</tbody></table></div>

<h2 id="market">履歷素材怎麼變成行銷</h2>
<p>同一份空拍素材，除了溯源，也是很好的品牌行銷材料：</p>
<ol>
  <li><strong>說故事：</strong>一張空拍全景，就是「我的田在山腳下、週邊沒有工廠」最直觀的證明。</li>
  <li><strong>做透明：</strong>把關鍵期影像放在品牌頁或包裝 QR 碼背後，讓消費者掃了就看得到農地。</li>
  <li><strong>做差異：</strong>有連續影像履歷的產品，在講究溯源與產地故事的通路裡更容易被記住。</li>
</ol>
<div class="callout green"><span class="ct">務實提醒</span>行銷用的影像要真實、如實呈現，不為了好看而過度後製。履歷的價值在「可信」，一旦誇大反而傷品牌。</div>

<h2 id="care">資訊揭露與個資界線</h2>
<p>把農地影像對外公開前，留意幾條界線：</p>
<ul class="check">
  <li>鏡頭裡避免帶到鄰居隱私、他人住家或可識別個人的資訊</li>
  <li>不隨意外流過於精確的坐標與界線，避免無端暴露</li>
  <li>涉及產銷履歷驗證時，依該驗證制度的文件規定提供素材</li>
  <li>對外發布的影像與說法，要與實際作業一致</li>
</ul>
<div class="callout"><span class="ct">一句話</span>空拍履歷是「讓人放心」的工具，不是「自我宣傳」的海報——真實、克制、可追溯，它才有用。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>空拍影像一定要通過正式驗才算履歷嗎？</summary><div class="faq-a">正式產銷履歷有其驗證制度與文件要求，空拍可作為佐證素材；要不要納入正式驗證，依你申請的制度規定為準。</div></details>
  <details><summary>小面積農地值得做影像履歷嗎？</summary><div class="faq-a">值得。面積小固定拍幾次成本不高，卻能累積出獨特的產地故事，對直銷與品牌加分明顯。</div></details>
  <details><summary>影像可以直接放網路上嗎？</summary><div class="faq-a">可以，但先檢查是否帶入他人隱私或過度精確的敏感資訊，並確認內容與實際作業一致再對外發布。</div></details>
</div>""",
    ("agri-disaster","災害勘災與損失評估"), ("agri-service","飛防與測繪服務隊")),

  "agri-service": (
    "飛防與測繪服務隊：外包噴藥與測繪的商業模式與合作",
    "外包噴藥與測繪服務的商業模式與合作方式。",
    ["飛防隊","測繪","外包"], "lin",
    [("who","飛防隊與測繪服務隊在做什麼"),("price","怎麼計費：依畝或專案"),("contract","契約與合作重點"),("choose","怎麼挑適合的服務隊"),("faq","常見問答")],
    """<h2 id="who">飛防隊與測繪服務隊在做什麼</h2>
<p>不是每個農家都需要自己買機、考證照。多數人更實惠的做法，是把作業「外包」給專業服務隊。市場上常見兩類：</p>
<ul>
  <li><strong>飛防（植保）服務隊：</strong>主要做空中噴藥、施肥、撒粒劑，載重大、速度快，替大面積或無力自行施作的農家省工。</li>
  <li><strong>測繪／空拍服務隊：</strong>主要做田區勘測、面積量測、生長監測、災後空拍與履歷影像，輸出的是資料與報告。</li>
</ul>
<div class="callout"><span class="ct">為什麼外包划算</span>把機體、電池、維修、證照與藥劑管理的風險都交給專業隊，農家只為「這次作業」付費，不用扛長期閒置與維護成本。</div>

<h2 id="price">怎麼計費：依畝或專案</h2>
<p>服務隊的收費方式大致兩種，依作業性質選擇，實際金額視作物、地形、距離與行情而定，這裡只談方式：</p>
<div class="tablewrap"><table>
<caption>兩種常見計費方式比較（方式說明，非費用表）</caption>
<thead><tr><th>方式</th><th>適合什麼</th><th>特點</th></tr></thead>
<tbody>
<tr><td>依面積（每畝計費）</td><td>大面積、常態噴藥</td><td>單純透明，面積越大越好估</td></tr>
<tr><td>依專案報價</td><td>測繪、災勘、履歷等一次性任務</td><td>依範圍、精度與後製需求議價</td></tr>
</tbody></table></div>
<p>報價前通常要先確認作業範圍、地形難度、距離與時程。坡地、偏遠田區、緊急加開的任務，成本結構和平原常態噴藥不同，這些都應在議價時講清楚。</p>
<div class="callout"><span class="ct">不要只比單價</span>只問「一畝多少」容易漏掉後勤、時程與品質。要一起看：是否含藥劑管理、能不能固定排程、資料要不要交付，這些都影響總體划算與否。</div>

<h2 id="contract">契約與合作重點</h2>
<p>外包不是「現場說好就飛」。正式合作前，把幾件事白紙黑字講清楚，日後才不會爭議：</p>
<ul class="check">
  <li>作業範圍與實際面積如何認定</li>
  <li>計費方式、計價單位與付款時點</li>
  <li>施作內容：噴什麼劑、要不要含材料，還是農家自備</li>
  <li>時程安排與氣象不適合作業時的處理</li>
  <li>影像、資料要不要交付，交付什麼格式</li>
  <li>藥劑飄移、鄰田影響等責任如何界定</li>
</ul>
<div class="callout green"><span class="ct">合規底線</span>植保噴藥涉及藥劑與飛行法規，合作時確認服務隊的飛手資格與機體合規，不把自己的法規風險外包出去。</div>

<h2 id="choose">怎麼挑適合的服務隊</h2>
<div class="procon">
  <div class="pc pro"><h4>好服務隊的線索</h4><ul><li>有穩定的在地口碑與可參考案例</li><li>飛手具合規資格、機體登記清楚</li><li>作業前願意先看田、說明流程</li><li>願意交付影像與作業紀錄</li></ul></div>
  <div class="pc con"><h4>要避免的紅旗</h4><ul><li>只報低價、不談範圍與責任</li><li>不願意說明飛行與藥劑合規</li><li>作業後不留任何紀錄</li><li>對鄰田飄移風險輕描淡寫</li></ul></div>
</div>
<p>建議先以小範圍、低風險的任務試作一次，看品質、配合度與紀錄習慣，再決定要不要長期合作。</p>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>外包噴藥和自己買機，哪個划算？</summary><div class="faq-a">看使用頻率。高頻、大面積自有田，自購單位成本低；作業次數少、不想管維修與藥劑，外包通常更務實。</div></details>
  <details><summary>測繪服務隊會交付什麼？</summary><div class="faq-a">依專案而定，常見是空拍影像拼接圖、面積與地形資料、或監測報告。合作前先講清楚要交付哪些成果與格式。</div></details>
  <details><summary>服務隊只接大面積嗎？</summary><div class="faq-a">不一定。很多服務隊接受小面積或重點田塊的委託，也可結合鄰里共同作業來分攤，直接詢問業者最準。</div></details>
</div>""",
    ("agri-trace","農地履歷與品牌行銷"), ("agri-chain","機具維修供應鏈")),
})

# 農業產業鏈 支柱新增條目（agri-sow）
TITLE.update({
  "agri-soil": "土壤分區與種植規劃：把土壤圖疊上空拍，分區安排每塊田",
  "agri-slope": "山坡地風險評估：梯田與零碎田的開發及作業難度先評估",
  "agri-sow": "播種、撒肥與粒劑：水稻直播與粒肥粒劑的均勻撒布",
  "agri-assist": "驅鳥、授粉與山區運補：無人機的輔助角色與限制",
})

ART.update({
  "agri-soil": (
    "土壤分區與種植規劃：把土壤圖疊上空拍，分區安排每塊田",
    "結合土壤資料分區管理，種植方案更貼近每一塊田。本文說明怎麼把田間取樣的土壤資料與空拍影像疊合，劃出管理分區，讓施肥、灌水與選種對準田的真實差異。",
    ["土壤", "分區管理", "種植規劃"], "lin",
    [("why", "為什麼要分區管理"), ("sample", "田間土壤怎麼取樣"), ("overlay", "空拍影像怎麼疊合土壤圖"), ("plan", "分區之後怎麼下種與施肥"), ("faq", "常見問答")],
    """<h2 id="why">為什麼要分區管理</h2>
<p>一塊田看起來整片連在一起，實際上土壤往往東邊偏砂、西邊偏黏，低處容易積水、高處常態乾旱。若用同一個配方施肥、同一個水量灌溉，不是某區肥傷、就是某區吃不飽。土壤分區管理的概念，就是把「田」依土壤條件切成幾個管理單元，讓施肥、灌水與選種對準每區的真實需求。</p>
<div class="callout"><span class="ct">核心觀念</span>分區不是把田愈切愈細，而是把「條件相近」的區塊歸在一起。目標是用少數幾個管理單元涵蓋田裡的主要差異，讓後續作業好執行。</div>
<ul>
  <li><strong>為什麼靠空拍：</strong>土壤差異往往連帶反映在作物長勢上，空拍的長勢圖與地形圖，能協助你把取樣點放得更有代表性。</li>
  <li><strong>與勘測接軌：</strong>先有田區勘測的面積與地形底圖，再疊上土壤資料，分區才站得住腳。</li>
</ul>

<h2 id="sample">田間土壤怎麼取樣</h2>
<p>空拍不能直接測出土壤酸鹼與養分，它需要「田間取樣＋化驗」當基礎。取樣的重點在代表性，而不是取幾個點：</p>
<ol>
  <li><strong>先看地形與長勢：</strong>用空拍的長勢圖與地形圖，把明顯不同的區塊標出來，分別取樣。</li>
  <li><strong>分層取表土：</strong>依主流做法，於耕作層深度範圍內採集，多點混合成一組樣品，降低單點誤差。</li>
  <li><strong>記錄座標：</strong>每個取樣點用 GPS／RTK 記下位置，事後才能疊回空拍圖上。</li>
  <li><strong>送驗常規項目：</strong>酸鹼值、有機質、主要養分與微量元素等，依實驗室提供的標準項目為準。</li>
</ol>
<div class="callout"><span class="ct">取樣點怎麼配置</span>面積大可採「分區取樣」，每一管理單元一組混合樣品；面積小可整田混合成少數幾組。重點是同一區前後次取樣位置一致，資料才可比。</div>

<h2 id="overlay">空拍影像怎麼疊合土壤圖</h2>
<p>把取樣化驗的結果標在座標上，再疊上空拍拼接圖、地形圖與長勢圖，就能在同一張底圖上看出「土壤條件相近、長勢也相近」的區塊，進而描出管理分區界線。</p>
<div class="tablewrap"><table>
<caption>常見分區依據與對應意義（依主流做法整理，實際以田間狀況為準）</caption>
<thead><tr><th>分區依據</th><th>資料來源</th><th>管理意義</th></tr></thead>
<tbody>
<tr><td>土壤質地與酸鹼</td><td>田間取樣化驗</td><td>決定基肥種類與用量</td></tr>
<tr><td>地形與排水</td><td>空拍地形建模</td><td>決定灌溉與排水配置</td></tr>
<tr><td>長勢差異</td><td>多光譜／可見光空拍</td><td>驗證分區、找隱藏問題</td></tr>
<tr><td>前作與歷史</td><td>田間紀錄</td><td>銜接輪作與肥培習慣</td></tr>
</tbody></table></div>
<div class="procon">
  <div class="pc pro"><h4>分區管理的好處</h4><ul><li>施肥對準需求，減少盲目重施</li><li>長勢不均的區塊容易被看見</li><li>逐年可比，累積自己田的知識</li></ul></div>
  <div class="pc con"><h4>要留意的點</h4><ul><li>取樣與化驗需要時間與成本</li><li>分區太細會讓作業難以執行</li><li>空拍是輔助，不能取代化驗</li></ul></div>
</div>

<h2 id="plan">分區之後怎麼下種與施肥</h2>
<ol>
  <li><strong>選種與輪作：</strong>依各區排水與土壤條件，決定適合的作物或品種，低窪易積水區與高燥區不硬種同樣東西。</li>
  <li><strong>分區施肥：</strong>把化驗結果換成各區的基肥與追肥建議，再搭配後續變量施作。</li>
  <li><strong>灌溉配置：</strong>依地形與土壤保水性，安排灌排水量與頻次。</li>
  <li><strong>逐年更新：</strong>每季或每年重取樣、重空拍，看分區界線是否隨耕作改變。</li>
</ol>
<div class="callout green"><span class="ct">務實起步</span>不必一次做到全田精細分區。先在一塊田做「取樣＋空拍疊圖」試點，跑通一次流程，再決定要不要擴大到整個農場。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>空拍可以直接測出土壤養分嗎？</summary><div class="faq-a">不行。空拍看的是長勢與地形，土壤酸鹼、有機質與養分仍需田間取樣送驗。空拍的角色是幫你把取樣點放對位置、並驗證長勢差異。</div></details>
  <details><summary>分區要切幾塊才好？</summary><div class="faq-a">沒有定數。原則是「用最少的區塊涵蓋主要差異」，通常一塊田切成數個管理單元就夠，切太細反而不好執行。</div></details>
  <details><summary>小農田也要做嗎？</summary><div class="faq-a">面積小可整田取一兩組樣品、配一次空拍，重點是養成「紀錄＋比對」的習慣，而不是追求精細分區。</div></details>
</div>""",
    ("agri-pre", "田區勘測與面積量測：用空拍一次把田摸清楚"), ("agri-slope", "山坡地風險評估")),

  "agri-slope": (
    "山坡地風險評估：梯田與零碎田的開發及作業難度先評估",
    "坡地與零碎農地風險高，空拍先評估開發與作業難度。本文整理坡地、梯田與零散田塊在航線規劃與人工作業上的風險點，以及空拍能先幫你看清楚什麼。",
    ["山坡地", "風險評估", "航線規劃"], "lin",
    [("why", "坡地為什麼要先評估"), ("terrain", "空拍能看出哪些地形風險"), ("flight", "航線與飛行的限制"), ("decision", "評估後怎麼決定做不做"), ("faq", "常見問答")],
    """<h2 id="why">坡地為什麼要先評估</h2>
<p>台灣很多茶園、果園與高冷農地位在山坡地與梯田，田塊小、坡度大、上下坡落差明顯。這類地塊不論是人工作業或無人機作業，風險都比平原田高：人容易滑倒、機體容易受風與地形干擾、資材搬運也費工。空拍的價值，是在投入開發或大規模作業之前，先從空中把地形、界線與障礙看清楚。</p>
<div class="callout"><span class="ct">先評估再投入</span>坡地開發或引入無人機作業前，先做一次空拍評估，能幫你判斷「這塊地適合怎麼做、風險在哪、哪些區塊根本不建議硬上」，避免事後才發現難以作業。</div>

<h2 id="terrain">空拍能看出哪些地形風險</h2>
<p>透過空拍拼接與地形建模，可以先掌握幾項對作業影響很大的地形因子：</p>
<div class="tablewrap"><table>
<caption>坡地常見地形風險與空拍可見線索（依主流做法整理）</caption>
<thead><tr><th>風險類型</th><th>空拍可見的線索</th><th>對作業的影響</th></tr></thead>
<tbody>
<tr><td>坡度陡</td><td>等高線密集、梯田落差大</td><td>人工作業危險、機體航線受限</td></tr>
<tr><td>零散田塊</td><td>田界破碎、被道路或林地切開</td><td>航線需分段、起降點難找</td></tr>
<tr><td>障礙物</td><td>電線、電桿、高大喬木、設施</td><td>避障風險高、需留安全距離</td></tr>
<tr><td>排水與沖蝕</td><td>徑流路徑、裸地與崩溝</td><td>影響水土保持與作業安全</td></tr>
</tbody></table></div>

<h2 id="flight">航線與飛行的限制</h2>
<ul>
  <li><strong>地形跟隨：</strong>成熟機種可依地形起伏調整飛行高度，但坡地落差大時，要隨時留意機體與坡面、樹冠的距離。</li>
  <li><strong>起降點選擇：</strong>坡地平坦處少，起降場地要事先用空拍與現場確認，避免在斜坡或臨近電線起降。</li>
  <li><strong>風的放大效應：</strong>山谷風、坡道風往往比平原強，風速上限要比平地更保守。</li>
  <li><strong>RTK 遮蔽：</strong>兩側高樹或山壁可能遮蔽定位訊號，影響精度與穩定。</li>
</ul>
<div class="callout"><span class="ct">航線不是愈滿愈好</span>坡地作業寧可把航線排寬、把障礙距離留大，也不要貪圖一次飛完。轉彎與臨界區是事故熱點，預留反應空間。</div>

<h2 id="decision">評估後怎麼決定做不做</h2>
<div class="procon">
  <div class="pc pro"><h4>適合導入無人機輔助</h4><ul><li>坡度尚可、田塊雖小但集中</li><li>有可用的平坦起降與充電點</li><li>主要任務是巡視、測繪與局部施作</li></ul></div>
  <div class="pc con"><h4>建議保守或改人工</h4><ul><li>坡度过陡、緊鄰懸崖或崩溝</li><li>電線喬木密布、定位長期遮蔽</li><li>純粹為大面積噴灑而硬上</li></ul></div>
</div>
<p>評估的目的不是「全部都用無人機」，而是把適合的區塊交給機器、高風險區塊保留人工或局部處理。涉及水土保持、山坡地開發與農業設施的規範，請以主管機關現行公告為準，必要時委請專業單位會勘。</p>
<div class="callout green"><span class="ct">界線提醒</span>空拍風險評估是「作業規劃的參考」，不是工程安全鑑定。真正涉及邊坡穩定、水土保持的決定，一定要由具資格的專業人員判斷。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>梯田果園能直接用無人機噴藥嗎？</summary><div class="faq-a">要先評估。梯田落差、樹冠與電線都可能讓噴灑變得侷促，建議先空拍掌握地形、找出起降點與風況，再決定用無人機還是局部人工。</div></details>
  <details><summary>空拍能取代現場會勘嗎？</summary><div class="faq-a">不能。空拍適合「先看全貌、標重點」，但障礙物淨空、起降場地與邊坡實況仍需現場確認。</div></details>
  <details><summary>坡地作業風險怎麼排優先？</summary><div class="faq-a">先看「坡度與落差」，再看「障礙與定位遮蔽」，最後看「風況與起降點」。三者任一項過高，就降低自動化作業的期待。</div></details>
</div>""",
    ("agri-soil", "土壤分區與種植規劃"), ("agri-sow", "播種、撒肥與粒劑")),

  "agri-sow": (
    "播種、撒肥與粒劑：水稻直播與粒肥粒劑的均勻撒布",
    "種子直播、粒肥與粒劑撒布，速度快且均勻。本文說明無人機撒布粒狀資材的運作方式、換裝模組與均勻性控制，以及哪些作物與時機適合。",
    ["直播", "撒肥", "粒劑"], "lin",
    [("what", "無人機撒的是哪些粒狀資材"), ("rice", "水稻直播怎麼做"), ("evenness", "均勻性怎麼控制"), ("module", "換裝模組與作業節奏"), ("faq", "常見問答")],
    """<h2 id="what">無人機撒的是哪些粒狀資材</h2>
<p>除了噴液態藥劑，植保無人機換上撒布模組後，也能撒粒狀資材。常見的包括水稻種子（直播）、粒狀肥料（粒肥）與粒劑（如粒狀藥劑或餌劑）。它們共同的好處是速度快、人員不必下田踩踏，尤其適合泥濘水田或大面積田塊。</p>
<div class="tablewrap"><table>
<caption>常見粒狀撒布項目與用途（依主流做法整理，實際以資材與機型為準）</caption>
<thead><tr><th>項目</th><th>撒布時機</th><th>重點要求</th></tr></thead>
<tbody>
<tr><td>水稻種子直播</td><td>整地後、播種期</td><td>均勻落粒、深度一致</td></tr>
<tr><td>粒肥</td><td>基肥或追肥期</td><td>避免局部重施造成肥傷</td></tr>
<tr><td>粒劑／餌劑</td><td>病蟲或鼠害管理期</td><td>依規定使用、留意非目標生物</td></tr>
</tbody></table></div>

<h2 id="rice">水稻直播怎麼做</h2>
<p>水稻直播省去育秧與插秧的勞力，是人力短缺下很受關注的做法。無人機直播的流程大致是：整地與整平→測定目標播量→設定撒布模組流速與航線→均勻撒播→後續灌溉與管理。</p>
<ol>
  <li><strong>種子預措：</strong>依主流做法做發芽率篩選與適當的播種前處理，確保落粒後整齊萌芽。</li>
  <li><strong>整地品質：</strong>田面平整、泥漿狀態適中，落粒才容易固定，不隨水流聚集或流失。</li>
  <li><strong>播量先試：</strong>先小面積試撒，確認單位面積落粒量與均勻度，再放大到全田。</li>
</ol>
<div class="callout"><span class="ct">直播不是萬靈丹</span>直播省了插秧工，但後續雜草管理與初期水層管理要求更高。是否採用，要看品種、期作與當地栽培習慣，建議先小區試作。</div>

<h2 id="evenness">均勻性怎麼控制</h2>
<p>撒布最容易出問題的就是「東多西少」。均勻度主要由幾個參數共同決定：</p>
<ul>
  <li><strong>撒布寬度：</strong>航線間距要與實際撒幅對齊，避免重疊漏接。</li>
  <li><strong>飛行速度與流速：</strong>兩者要搭配，速度快時流速跟著調，單位面積用量才一致。</li>
  <li><strong>轉彎處：</strong>轉彎容易堆料或漏撒，通常先爬升、減速或事後補撒。</li>
  <li><strong>風：</strong>粒狀資材比霧滴重，但側風仍會讓落點偏移，風大時要調整或停手。</li>
</ul>
<div class="callout green"><span class="ct">先驗證再放大</span>每次換資材、換模組，都先小區試撒，目視或簡單量測落粒分布。確認均勻度可接受，再排大面積作業。</div>

<h2 id="module">換裝模組與作業節奏</h2>
<p>同一台機，從噴藥切到撒粒，主要是換上撒布倉與轉盤／風送模組，並在地面站改設定。作業現場的節奏大致是：裝料→起飛→沿航線撒布→返航補料或換電→續飛。粒狀資材的裝卸與機體清潔也要做足，避免殘料卡料。</p>
<div class="procon">
  <div class="pc pro"><h4>無人機撒布的優勢</h4><ul><li>省工、速度快，泥水田不必下田</li><li>換模組後一台機多功能</li><li>均勻度可控，比人工踩踏更平</li></ul></div>
  <div class="pc con"><h4>要留意的點</h4><ul><li>均勻度需事前試算與驗證</li><li>粒劑使用要符合農藥管理規範</li><li>風與地形仍會影響落點</li></ul></div>
</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>無人機直播可以完全取代插秧嗎？</summary><div class="faq-a">在人力短缺與大面積水田是可行選項之一，但直播對整地、雜草與水層管理要求更高，建議先小區試作、累積經驗再放大。</div></details>
  <details><summary>一台噴藥機能直接拿來撒肥嗎？</summary><div class="faq-a">需要換上對應的撒布模組與倉體，並在地面站重新設定。硬改不相容模組有安全與均勻度風險，請以原廠或合格配備為準。</div></details>
  <details><summary>撒粒肥會不會局部肥傷？</summary><div class="faq-a">會，若流速與速度不匹配、轉彎堆料，就可能局部用量過高。先小區試撒、確認均勻度，是預防肥傷的基本動作。</div></details>
</div>""",
    ("agri-slope", "山坡地風險評估"), ("agri-assist", "驅鳥、授粉與山區運補")),

  "agri-assist": (
    "驅鳥、授粉與山區運補：無人機的輔助角色與限制",
    "驅鳥、輔助授粉與物資運補的輔助角色。本文談這三類常被討論的應用，各自適用什麼情境、能做到什麼程度，以及現階段的限制。",
    ["驅鳥", "授粉", "運補"], "lin",
    [("bird", "驅鳥：嚇趕不是常態防治"), ("pollinate", "輔助授粉：試驗階段的角色"), ("supply", "山區運補：小件物資的點到點"), ("limit", "輔助角色的界線"), ("faq", "常見問答")],
    """<h2 id="bird">驅鳥：嚇趕不是常態防治</h2>
<p>鳥害在稻田、果園與酪農鄰近區域都常見。無人機低空空飛或搭配音響，可以短暫驚嚇鳥群、迫其離開作為區域。但它比較像「嚇趕工具」，而不是一勞永逸的防治。</p>
<ul>
  <li><strong>效果短暫：</strong>鳥類很快適應聲音與身影，固定時間飛、固定路線飛，效果會遞減。</li>
  <li><strong>要穿插變化：</strong>不規則時間、變化航線與高度，維持「不確定性」，效果才較持久。</li>
  <li><strong>綜合搭配：</strong>驅鳥通常要與網室、細繩或其他物理方法搭配，單靠無人機不夠。</li>
</ul>
<div class="callout"><span class="ct">安全優先</span>驅鳥飛行靠近果園與設施時，更要留意電線、樹冠與人群；也避免在非目標物種的重要活動區域造成干擾。</div>

<h2 id="pollinate">輔助授粉：試驗階段的角色</h2>
<p>像網室蔬菜、部分果樹在昆蟲授粉不足時，會討論「用無人機擾動空氣、帶動花粉飄散」的輔助授粉方式。這類做法目前多屬試驗與局部應用，還不是成熟的常規作業。</p>
<div class="tablewrap"><table>
<caption>輔助授粉的現況與定位（依主流試驗做法整理）</caption>
<thead><tr><th>面向</th><th>現況</th><th>備註</th></tr></thead>
<tbody>
<tr><td>原理</td><td>機身下洗氣流擾動花冠、帶動花粉</td><td>與作物花型關係很大</td></tr>
<tr><td>適用</td><td>網室、昆蟲不足或特定試驗情境</td><td>依作物與設施條件而異</td></tr>
<tr><td>定位</td><td>輔助授粉，非取代蜜蜂等昆蟲</td><td>效果仍需逐作物驗證</td></tr>
</tbody></table></div>
<p>若你在考慮這類應用，建議先以小面積試驗、與自然授粉或昆蟲授粉對照，觀察著果差異，再決定是否擴大，不要直接當常規流程。</p>

<h2 id="supply">山區運補：小件物資的點到點</h2>
<p>高山茶園、果園常面臨物資搬運貴、路陡難走的問題。無人機可以把種子、肥料小包、藥劑或工具，從山腳定點運到作業區，減少人力肩扛。但它有清楚的天花板：</p>
<ul>
  <li><strong>載重有限：</strong>每次能運的量不大，適合「輕、急、小」的東西，不是大宗物資。</li>
  <li><strong>航線固定：</strong>山區起降落點與路線要事先勘察，不能隨意改線。</li>
  <li><strong>風與天候敏感：</strong>山谷風與午後對流常讓山區作業窗口很短。</li>
</ul>
<div class="callout"><span class="ct">運補的真正價值</span>不是取代搬運工，而是「關鍵小件、臨時補給」——例如現場發現少帶了一包藥劑或工具，用無人機送上去，省下來回一段山路的時間。</div>

<h2 id="limit">輔助角色的界線</h2>
<p>這三類應用共通的特色，是「輔助」而非「主力」。它們補的是人力難以到、或常規方法效果不彰的小缺口，而不是全面取代現有農法。</p>
<div class="procon">
  <div class="pc pro"><h4>適合當輔助工具</h4><ul><li>臨時性、季節性的需求</li><li>地形或設施讓人工作業吃緊</li><li>已有常規方法、無人機再加把勁</li></ul></div>
  <div class="pc con"><h4>不要過度期待</h4><ul><li>單靠無人機解決長期病蟲鳥害</li><li>把它當成熟的常規授粉作業</li><li>期待大宗物資靠它全天候運</li></ul></div>
</div>
<div class="callout green"><span class="ct">務實定位</span>把驅鳥、輔助授粉與山區運補想成「農場工具箱裡的新工具」，在對的情境、小範圍先用，累積自己田的經驗，再決定常態化與否。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>每天固定飛去驅鳥有效嗎？</summary><div class="faq-a">效果會遞減。鳥類容易適應規律的聲影，建議不規則時間、變化航線，並搭配其他物理防治，不要把它當單一解方。</div></details>
  <details><summary>無人機授粉能取代蜜蜂嗎？</summary><div class="faq-a">現階段仍屬輔助與試驗性質，效果依作物而異，不適合直接取代昆蟲授粉。建議以對照試驗驗證後再採用。</div></details>
  <details><summary>山區能用無人機大量運肥料嗎？</summary><div class="faq-a">不適合。載重與天候窗口都有限，它適合輕量緊急補給，大宗肥料仍以傳統搬運或軌道車等為主。</div></details>
</div>""",
    ("agri-sow", "播種、撒肥與粒劑"), ("agri-post", "產量預估與採收研判")),
})

# 未來永續 支柱新增條目（future）：future-tech / future-ai / future-organic
TITLE.update({
  "future-tech": "技術與產業升級：自動化、多機協作與數據平台的三條主線",
  "future-ai": "AI 農業決策：大模型能幫農場做哪些決定",
  "future-organic": "有機與坡地保育：無人機在友善農業與坡地的角色",
})

ART.update({
  # ============================================================
  # future-tech — 技術與產業升級
  # ============================================================
  "future-tech": (
    "技術與產業升級：自動化、多機協作與數據平台的三條主線",
    "自動化、多機協作與數據平台，是農業無人機往產業化升級的三條主線。本文用趨勢觀察的角度，看這三條路徑如何彼此接軌，以及農民、飛手與服務業的分工會怎麼演變。",
    ["自動化", "多機協作", "數據平台"], "lin",
    [("why", "三條主線怎麼來的"),
     ("auto", "自動化：從手飛到任務"),
     ("fleet", "多機協作與機隊分工"),
     ("platform", "數據平台才是真正核心"),
     ("industry", "產業分工會怎麼變"),
     ("faq", "常見問答")],
    """<h2 id="why">三條升級主線怎麼來的</h2>
<p>農用無人機這幾年走過的路，大致是「先能飛、再拍得準、接著讓它自己飛」。當單機操作逐漸成熟，接下來的升級不會只停在「一台更好的機子」，而是沿著三條路徑往前：<strong>自動化</strong>把人從操作裡抽出來、<strong>多機協作</strong>把作業規模放大、<strong>數據平台</strong>把一次次飛行累積成可重用的判斷依據。三者不是三條獨立的路，而是一條鏈——自動化產生穩定數據，數據餵給平台，平台再回頭調度更多機。</p>
<div class="callout"><span class="ct">怎麼看這三條主線</span>與其問「哪條最重要」，不如問「你的農場現在卡在哪一環」。多數人真正的瓶頸不是飛不好，而是飛完之後沒有把資料留下來、接不上下一次決策。</div>

<h2 id="auto">自動化：從手飛到任務</h2>
<p>今天多數農用機已經能依地面站規劃的航線自主飛行、斷航續飛、低電量返航。下一步的自動化不在「飛得更炫」，而在把<strong>換電、充電、上傳資料、再出勤</strong>這一串人工環節也交給系統，也就是常見的自動機場（機巢）方向。它帶來的改變是：監測可以從「人想到才拍」變成「固定、可預期地拍」，資料才連得起來。</p>
<ul>
  <li><strong>航線自動化：</strong>固定航線與重飛機制，讓前後影像可比，是所有後續分析的前提。</li>
  <li><strong>換電與充電自動化：</strong>把人從現場綁住的時間解放出來，作業排程更順。</li>
  <li><strong>任務排程自動化：</strong>依田區狀況、天氣窗口自動決定「今天該飛哪幾塊」。</li>
</ul>

<h2 id="fleet">多機協作與機隊分工</h2>
<p>單台機覆蓋面積有限，也只能做一種任務。多機協作的真正價值不是「多幾台機」，而是<strong>分工</strong>：一台負責測繪監測、一台負責噴灑、一台專跑高頻巡田，由調度平台統一排程。對大面積農場或專業飛防隊而言，機隊的意義在於把「錯峰作業」與「即時補位」變成常態。</p>
<div class="tablewrap"><table>
<caption>多機協作常見的分工型態（依現有服務型態整理，實際以現場需求為準）</caption>
<thead><tr><th>角色</th><th>主要任務</th><th>搭配的資料流</th></tr></thead>
<tbody>
<tr><td>測繪監測機</td><td>定期空拍、產生長勢圖層</td><td>影像上雲 → 形成處方依據</td></tr>
<tr><td>植保噴灑機</td><td>依處方圖變量施藥施肥</td><td>讀取平台處方 → 回報作業紀錄</td></tr>
<tr><td>高頻巡田機</td><td>定點巡視、災後快速勘災</td><td>異常即時回傳 → 通知現場確認</td></tr>
</tbody></table></div>

<h2 id="platform">數據平台才是真正核心</h2>
<p>如果說自動化與多機協作是「手腳」，數據平台就是「大腦」。它把每次空拍的影像、NDVI 等植被指數、熱影像、施藥施肥紀錄與天氣資料收斂到同一處，讓同一块田的歷史能被前後比對。平台成熟與否，決定了無人機究竟只是「一次性工具」，還是「會越用越懂這塊田的系統」。</p>
<div class="callout green"><span class="ct">務實看法</span>多數小農不需要一步到位買自動機場。真正值得先做的，是把「固定航線＋影像上雲＋逐年比對」這件小事做起來——它是後面一切升級的地基。</div>

<h2 id="industry">產業分工會怎麼變</h2>
<p>技術升級往往伴隨分工改組。當作業自動化、數據平台化，單一角色很難包辦「飛、拍、分析、開處方、執行」全部環節，產業可能往幾類角色集中：</p>
<div class="procon">
  <div class="pc pro"><h4>可能被放大的角色</h4><ul><li>飛防與測繪服務隊：承接高頻、大面積作業</li><li>數據處理與顧問：把影像轉成可行的田間建議</li><li>設備與機巢維運：負責機體、電池與平台穩定</li></ul></div>
  <div class="pc con"><h4>需要被提醒的界線</h4><ul><li>數據平台不是買了就有用，要靠持續輸入與判讀</li><li>自動化不等於無人值守，法規與安全仍要人把關</li><li>小農宜透過合作社或共享服務，避免重複投資</li></ul></div>
</div>
<p>對多數農民而言，最務實的路徑不是「自己建一套系統」，而是先加入或選用成熟的服務與平台，把自己的田納進去，再視需要逐步自購。</p>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>三條主線一定要一起上嗎？</summary><div class="faq-a">不必。它們是彼此接軌的鏈，但可以分階段：先固定航線與資料留存，再視作業量決定是否走向多機與自動機場。</div></details>
  <details><summary>小農需要跟得上這波升級嗎？</summary><div class="faq-a">與其「跟著投資」，不如「善用服務」。透過飛防隊、測繪服務或合作社共享，小農也能享受到自動化與數據平台的好處，而不必一次買齊。</div></details>
  <details><summary>數據平台會不會很難用？</summary><div class="faq-a">現在多數平台已把拼圖、指數計算做成圖形介面，門檻在於「固定拍、持續留」的習慣，而不是技術本身。</div></details>
</div>""",
    ("future", "未來永續"), ("future-ai", "AI 農業決策")),

  # ============================================================
  # future-ai — AI 農業決策
  # ============================================================
  "future-ai": (
    "AI 農業決策：大模型能幫農場做哪些決定",
    "用大模型自動生成田間管理方案的潛力，正在快速逼近。本文務實看待 AI 在病蟲辨識、處方建議與田間管理方案上的角色，以及「AI 輔助、人做決定」這條界線該畫在哪裡。",
    ["AI", "大模型", "決策"], "lin",
    [("where", "AI 現在走到哪一步"),
     ("identify", "病蟲與逆境辨識"),
     ("prescript", "處方建議與田間方案"),
     ("boundary", "AI 輔助、人做決定"),
     ("trust", "誤判、數據與信任"),
     ("faq", "常見問答")],
    """<h2 id="where">AI 現在走到哪一步</h2>
<p>過去幾年，AI 在農業裡的角色從「被動的影像分類」慢慢往「主動給建議」靠近。一路的演進大致是：先用模型把空拍影像自動分成健康、缺肥、病蟲、草害等類別；再進一步把這些分類疊上空間位置，生成「哪裡有問題」的地圖；最新的一步，則是讓模型結合田區資料與知識，<strong>自動產出初步的田間管理建議</strong>。這是大模型進入農業決策的起點，而不是終點。</p>
<div class="callout"><span class="ct">一句話定位</span>AI 擅長「從大量影像與資料裡找規律、出草擬稿」，但農業決策還涉及天氣、土壤、品種與市場——這些最終仍要懂田的人來判斷。</div>

<h2 id="identify">病蟲與逆境辨識</h2>
<p>辨識是 AI 在農業裡最成熟、也最值得信賴的一環。結合多光譜與可見光影像，模型可以在肉眼察覺之前，標出長勢異常、局部缺水、疑似病斑或草害初發的區塊。它的價值在於<strong>把「整片田巡一遍」的工時壓縮成「只看被標出來的幾塊」</strong>。</p>
<div class="tablewrap"><table>
<caption>AI 辨識常見的輸出類型（依現有平台功能整理，實際效果因地而異）</caption>
<thead><tr><th>輸出</th><th>看的是什麼</th><th>對應的田間動作</th></tr></thead>
<tbody>
<tr><td>長勢分區圖</td><td>整體健康度的空間分布</td><td>規劃重點巡查與施肥區</td></tr>
<tr><td>病蟲熱點</td><td>疑似病斑、蟲害的聚集區</td><td>安排人工到田確認與局部處理</td></tr>
<tr><td>水分異常區</td><td>熱影像顯示的區域性溫差</td><td>檢查灌溉管路與排水</td></tr>
</tbody></table></div>

<h2 id="prescript">處方建議與田間方案</h2>
<p>當辨識接上處方圖，AI 就能更進一步：依健康度分區，給出「哪裡該加量、哪裡可以少噴或不噴」的初步施作建議。有了大模型之後，這種建議開始出現「敘述版」的樣子——不只給地圖，還能用白話說明為何這樣建議、需要哪些條件配合。對缺乏專人判讀的農場，這相當於一個隨時在線的初步顧問。</p>
<div class="callout green"><span class="ct">務實期待</span>把 AI 產出的方案當「草擬稿」而非「處方箋」。它能省下你從零開始想的時間，但落實前一定要套進自己這塊田的實際狀況。</div>

<h2 id="boundary">AI 輔助、人做決定</h2>
<p>這是最重要的一條界線。AI 模型的建議來自「既有資料的歸納」，而農業現場充滿模型沒見過的例外：罕見的病害組合、異常天氣、特殊品種、鄰田與成本的現實考量。把決策權完全交給模型，等於把這些例外一起交出去。</p>
<ul>
  <li><strong>AI 適合做：</strong>快速過濾、標出重點、整理歷史、擬定初步方案。</li>
  <li><strong>人應該保留：</strong>用藥與用肥的最終決定、何時下田、何時停損、以及對成本與風險的判斷。</li>
  <li><strong>兩者交接點：</strong>AI 給建議與依據，人決定「這次要不要、怎麼做」，並把結果回頭餵給系統。</li>
</ul>

<h2 id="trust">誤判、數據與信任</h2>
<p>模型一定會誤判，差別只在誤判被不被發現。降低誤判風險的方式不是「相信更高階的模型」，而是<strong>建立交叉驗證的習慣</strong>：空拍標出的異常，到田間實地看一眼；模型建議的處方，先在小區塊試作。當人工不斷確認與修正，系統也會越來越貼近你這塊田的真實規律。</p>
<div class="callout"><span class="ct">信任是養出來的</span>AI 建議的可信度，取決於你給它的資料夠不夠連續、夠不夠貼近你的田。持續、固定、可比的輸入，才換得到可用的建議。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>AI 建議可以直接照著噴藥嗎？</summary><div class="faq-a">不建議。用藥用肥涉及藥劑管理與安全間隔，應由具備專業知識者依田間實況確認後執行，AI 的輸出僅供擬定方向參考。</div></details>
  <details><summary>需要很懂電腦才能用嗎？</summary><div class="faq-a">不需要。多數平台已把辨識與建議做成圖形介面，重點是固定拍攝、持續留資料，而非理解模型原理。</div></details>
  <details><summary>模型會不會一直給錯答案？</summary><div class="faq-a">初期一定會有誤判，這很正常。靠小區試作與人工確認逐步校正，系統會越用越準；若長期偏差大，代表資料或方法需要檢討。</div></details>
</div>""",
    ("future-tech", "技術與產業升級"), ("future-organic", "有機與坡地保育")),

  # ============================================================
  # future-organic — 有機與坡地保育
  # ============================================================
  "future-organic": (
    "有機與坡地保育：無人機在友善農業與坡地的角色",
    "有機、友善農業與坡地保育，是無人機過去較少被談到的一條線。本文談它在雜草管理、早期偵測、局部處理，以及坡地巡視與運補上的應用潛力——重點是「少用一點、少動一點」。",
    ["有機", "友善農業", "坡地保育"], "lin",
    [("why", "有機農場為何更需要空拍"),
     ("weed", "雜草與病蟲早期偵測"),
     ("local", "局部處理與物理輔助"),
     ("slope", "坡地巡視與物資運補"),
     ("ground", "減少地表干擾"),
     ("faq", "常見問答")],
    """<h2 id="why">有機農場為何更需要空拍</h2>
<p>有機與友善農業的核心，是「不靠化學藥劑壓倒性地處理問題」，而靠<strong>更早發現、更小範圍處理</strong>。這正好撞上一個現實：雜草與病蟲在大面積田裡，靠雙腳巡視很難即時發現。無人機的價值於此浮現——它讓有機農場用較低成本，把「常態巡視」這件事做起來，把問題消滅在小規模階段。</p>
<div class="callout"><span class="ct">與慣行農法的差異</span>一般農法是「發現問題再整片噴」；有機思路是「在問題變大之前就找到它」。空拍監測讓後者第一次變得可行。</div>

<h2 id="weed">雜草與病蟲早期偵測</h2>
<p>沒有除草劑與廣效農藥，有機農場對雜草與病蟲的策略，完全建立在「早」與「準」。空拍把雜草群落、病斑初發與長勢異常提早標出來，讓農友可以在還小的時候用人工或物理方式處理掉，避免演變成需要大動作剷除的局面。</p>
<ul>
  <li><strong>雜草分布：</strong>高解析空拍可辨草相聚集區，做為人工除草或覆蓋的優先名單。</li>
  <li><strong>病蟲初發：</strong>熱影像與多光譜能在肉眼病徵出現前，抓到冠層的異常訊號。</li>
  <li><strong>長勢起伏：</strong>前後幾次影像比對，看出哪一區正在惡化，不必整片都緊張。</li>
</ul>

<h2 id="local">局部處理與物理輔助</h2>
<p>有機農法強調「對的地方、用對的方式、用剛剛好的量」。無人機配合處方圖，可以把有機資材（如認可的肥材、驅避性物資）<strong>只送到需要的局部區塊</strong>，而不是全田均勻撒。這對小規模、高價值的有機作物尤其有感：資材成本與環境衝擊都壓在最小範圍。</p>
<div class="tablewrap"><table>
<caption>無人機在友善農業中的常見輔助定位（依現有應用整理，實施方式以田況為準）</caption>
<thead><tr><th>環節</th><th>無人機角色</th><th>對應的保育價值</th></tr></thead>
<tbody>
<tr><td>雜草管理</td><td>標出草相聚集區，引導人工或局部處理</td><td>減少全區除草與土壤擾動</td></tr>
<tr><td>病蟲偵測</td><td>熱影像與多光譜提早抓異常</td><td>縮小處理規模、避免全面用藥</td></tr>
<tr><td>資材局部投撒</td><td>依處方圖只投必要區塊</td><td>降低資材用量與殘留風險</td></tr>
</tbody></table></div>

<h2 id="slope">坡地巡視與物資運補</h2>
<p>台灣許多農地在山坡地，地形陡峭、田塊零碎，人走上去又慢又危險。無人機在這裡的角色不是「大噴灑」，而是<strong>巡視與輕量運補</strong>：定期飛一趟看坡面沖蝕、邊界與排水，把肥料、資材或小工具運到難以到達的高處，省下來回爬坡的工時與風險。對坡地保育而言，這代表「不用為了巡田而反覆踐踏坡面」。</p>
<div class="callout green"><span class="ct">保育思維</span>坡地最怕的是為了作業而反覆開路、壓實土壤。空中巡視與運補，正是讓人「少上去一點」的技術答案。</div>

<h2 id="ground">減少地表干擾</h2>
<p>永續農業的一條隱性原則，是「盡量少動土壤、少壓實地表」。傳統機具進田作業會留下壓痕、翻動表土，在敏感的坡地與有機田裡尤其要小心。無人機從空中完成監測與輕量施作，把「機具下田」的次數與範圍壓到最小，本身就是一種保育手段——這也是它在有機與坡地場景最容易被忽略、卻最扎實的價值。</p>
<ul class="check">
  <li>以空拍巡視取代部分實地開路，減少坡面踐踏</li>
  <li>局部投撒取代全區均勻作業，縮小干擾範圍</li>
  <li>固定航線重飛比對，逐年掌握田區變化而不必年年重測</li>
</ul>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>有機農場可以用無人機噴資材嗎？</summary><div class="faq-a">端視使用的資材是否符合有機規範與主管機關公告，以及作業方式是否符合當地法規。建議先確認適用資材與飛行規定，再委由具經驗者執行。</div></details>
  <details><summary>坡地飛行安全嗎？</summary><div class="faq-a">坡地風場與遮蔽較複雜，風速、亂流與起降點都要比平地更保守規劃，建議由熟悉地形的飛手評估後再作業。</div></details>
  <details><summary>小規模有機田值得上空拍嗎？</summary><div class="faq-a">值得，但不必自購。先以委外單次或定期監測起步，把雜草與病蟲的「早期名單」做出來，再決定是否進一步導入。</div></details>
</div>""",
    ("future-ai", "AI 農業決策"), ("future", "未來永續")),
})

# 無人機與生活（life）支柱新增條目
TITLE.update({
  "life-patrol": "巡邏、搜救與勘查：社區巡視、熱影像勘災怎麼做",
  "life-site": "工地進度紀錄：固定航線空拍讓進度看得見、查得到",
  "life-race": "競速與花式飛行：FPV 運動無人機的玩法、設備與場地",
  "life-edu": "親子科普課程：從組裝與飛行中玩出科技與安全素養",
})

ART.update({
  "life-patrol": (
    "巡邏、搜救與勘查：社區巡視、熱影像勘災怎麼做",
    "社區、河道與山坡巡邏，以及火災、搜救勘查。空拍把「看不到的死角」一次拍下來，是觀察與佐證的好工具。",
    ["巡邏", "搜救", "勘查"], "xu",
    [("why", "為什麼空拍適合巡邏與勘查"),
     ("patrol", "社區、河道與山坡巡邏"),
     ("fire", "火災與搜救勘查：熱影像與夜視"),
     ("ethics", "作業倫理與法規界線"),
     ("faq", "常見問答")],
    """<h2 id="why">為什麼空拍適合巡邏與勘查</h2>
<p>巡邏與勘查的共同痛點是「人走到的地方有限」。社區巷弄、河道兩岸與山坡邊坡，靠雙腳繞一圈要花上好一段時間，視角還常被樹木、圍牆與地形擋住。無人機用幾分鐘就能升到高處、飛到死角上空，把原本看不到的地方一次拍下來，做為紀錄比口頭描述客觀得多。</p>
<div class="callout"><span class="ct">它擅長的是「看」與「記錄」</span>空拍在巡邏與勘查裡是一種觀察與佐證工具：先幫你掌握全貌、標出重點，真正的處置與救援仍要交給專業單位。</div>

<h2 id="patrol">社區、河道與山坡巡邏</h2>
<ul>
  <li><strong>社區巡邏：</strong>里辦公處、管委會或志工團隊用空拍檢視巷弄堆置、違建、夜間照明死角與環境髒亂，做成整改前後的比對資料。</li>
  <li><strong>河道巡檢：</strong>汛期前後沿兩岸飛一趟，掌握排水溝淤積、河岸沖刷與淹水潛勢區，比沿堤防步行更全面。</li>
  <li><strong>山坡與道路勘查：</strong>降雨後巡視邊坡裂縫、崩塌與落石路段，做為搶修與封路評估的第一手空中資料。</li>
</ul>
<div class="tablewrap"><table>
<caption>三類巡邏場景的空拍重點（依主流做法整理，實際作業現場狀況為準）</caption>
<thead><tr><th>場景</th><th>主要看什麼</th><th>產出用途</th></tr></thead>
<tbody>
<tr><td>社區</td><td>巷弄環境、違建、照明死角</td><td>整改前後比對、環境改善佐證</td></tr>
<tr><td>河道</td><td>淤積、沖刷、淹水潛勢</td><td>汛期巡查、排水檢視</td></tr>
<tr><td>山坡道路</td><td>邊坡裂縫、崩塌、落石</td><td>搶修評估、封路建議</td></tr>
</tbody></table></div>

<h2 id="fire">火災與搜救勘查：熱影像與夜視</h2>
<p>火災現場最怕「看不到火勢從哪延燒」。搭載熱影像的空拍機可在濃煙中分辨溫度分布，協助指揮端掌握火勢蔓延方向與複燃熱點；夜間搜救則靠低光／夜視攝影機與照明，縮小協尋範圍。</p>
<ul>
  <li><strong>熱影像：</strong>在搜救中用於辨識人體熱源，在勘災中用於找冒煙點與結構高溫。</li>
  <li><strong>夜視／低光：</strong>協助夜間山域、水域與道路事故的現場掌握。</li>
  <li><strong>照明與臨時支援：</strong>部分機型可掛載照明或拋投器，做為夜間現場的輔助光源。</li>
</ul>
<div class="callout"><span class="ct">身分要對</span>火災與搜救屬消防與搜救單位職權。民間空拍只能在指揮體系同意、且不阻礙救災的前提下旁觀或協助提供畫面，不可自行闖入現場上空。</div>

<h2 id="ethics">作業倫理與法規界線</h2>
<p>巡邏與勘查經常拍到他人住家、門牌與活動現場，比一般空拍更需要自我約束。以下是起飛前後都該守住的基本界線：</p>
<ul class="check">
  <li>不在禁飛區、機場與敏感設施周邊起飛</li>
  <li>不於人群與救災現場上空任意飛行，夜航依規定申請</li>
  <li>不拍攝他人住家內部、門牌與可辨識個人的畫面做為公開用途</li>
  <li>現場畫面僅供公務或佐證使用，不隨意外流轉傳</li>
  <li>發現即時危險，第一時間通報消防、警察或權責單位</li>
</ul>
<div class="callout green"><span class="ct">法規隨時更新</span>無人機登記、證照與夜航、人群上空的限制，請以主管機關現行公告為準；救災場域另依消防指揮體系的現場管制辦理。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>一般人可以自己飛去參加搜救嗎？</summary><div class="faq-a">不建議自行出動。搜救由消防與搜救單位主導，民間空拍應在單位邀請或同意下配合提供畫面，避免干擾救災航線與通訊。</div></details>
  <details><summary>熱影像一定要很貴的機才有？</summary><div class="faq-a">高階熱影像雲台確實較貴，但一般空拍可見光先掌握全貌已很有幫助；需要辨識熱源時，再租賃或委外熱影像機更務實。</div></details>
  <details><summary>空拍畫面可以直接放上网路嗎？</summary><div class="faq-a">涉及他人、住家或現場當事人的畫面，公開前應確認隱私與個資，並注意是否屬管制現場；公務用途的資料建議依權責單位規定留存。</div></details>
</div>""",
    ("life-deliver", "山區、偏鄉配送"),
    ("life-site", "工地進度紀錄")),

  "life-site": (
    "工地進度紀錄：固定航線空拍讓進度看得見、查得到",
    "工地進度空拍，比地面紀錄更直觀、可追溯。把同一片工地在不同時間拍成可疊合的畫面，進度一目了然。",
    ["工地", "進度", "空拍"], "xu",
    [("why", "為什麼要空拍記工地進度"),
     ("route", "固定航線與時間序列"),
     ("compare", "時間序列比對怎麼做"),
     ("manage", "對業主與營建管理的價值"),
     ("faq", "常見問答")],
    """<h2 id="why">為什麼要空拍記工地進度</h2>
<p>工地進度最難的不是「做了什麼」，而是「怎麼讓不在現場的人也看得懂」。地面紀錄受限於鷹架、圍籬與死角，業主、監造與營造之間常因各說各話，在估驗與履約上產生爭議。固定角度的空拍，把同一片工地在不同時間拍成可疊合的畫面，進度一目了然，也留下可追溯的證據。</p>
<div class="callout"><span class="ct">重點不是拍美，而是拍得一致</span>進度空拍的價值在「前後可比」：同一角度、同一範圍，才看得出時間推進。漂亮的鏡頭反而是其次。</div>

<h2 id="route">固定航線與時間序列</h2>
<p>進度空拍的關鍵不是「拍得漂亮」，而是「每次都一樣」。同一起降點、相近高度航線、相同光線時段，前後畫面才有意義。實務上的做法包括：</p>
<ul>
  <li><strong>固定航線：</strong>把航線與高度存檔，每次重飛同一路徑，避免每次角度不同。</li>
  <li><strong>定位校正：</strong>需要精準疊圖時採用 RTK，降低前後拍攝的位置誤差。</li>
  <li><strong>固定頻率：</strong>依工程階段決定每週、每月或重要節點拍一次，並記錄拍攝日期。</li>
</ul>

<h2 id="compare">時間序列比對怎麼做</h2>
<p>把每次空拍依日期排序，就能形成一條「時間軸」。前後同角度疊圖，地基從無到有、樓層逐層拉高、外牆漸次完工，進度推進一目了然。</p>
<div class="tablewrap"><table>
<caption>進度空拍的常見頻率與用途（依主流做法整理，依工程規模調整）</caption>
<thead><tr><th>工程階段</th><th>建議紀錄頻率</th><th>主要用途</th></tr></thead>
<tbody>
<tr><td>開挖與基礎期</td><td>每週或重要節點</td><td>基礎深度、高程與排水佐證</td></tr>
<tr><td>結構體施工期</td><td>每週至每月</td><td>樓層進度、混凝土進場比對</td></tr>
<tr><td>裝修與外觀期</td><td>每月</td><td>外牆、門窗與設備安裝進度</td></tr>
<tr><td>完工驗收期</td><td>完工前後各一次</td><td>前後比對、移交履歷</td></tr>
</tbody></table></div>
<p>這條時間軸做為月報、估驗與履約佐證都站得住；萬一日後對進度有爭議，同角度的前後畫面是最客觀的依據。</p>

<h2 id="manage">對業主與營建管理的價值</h2>
<div class="procon">
  <div class="pc pro"><h4>帶來的好處</h4><ul><li>進度對業主透明，減少資訊不對稱</li><li>做為履約與估驗的客觀佐證</li><li>可順便巡視鷹架、圍籬與料堆配置</li></ul></div>
  <div class="pc con"><h4>要注意</h4><ul><li>工地靠近道路與工安區，須維持安全距離</li><li>影像可能涉及營建機密，應管控存取權限</li><li>高樓與鋼筋會干擾訊號，留意失控風險</li></ul></div>
</div>
<div class="callout green"><span class="ct">由誰來飛</span>工地進度空拍可由營造團隊自飛，或委託空拍服務業者定期到場。重點是把航線、頻率與歸檔流程固定下來，形成可長期累積的進度履歷。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>一定要買很貴的測繪機嗎？</summary><div class="faq-a">若只求進度紀錄與同角度比對，一般空拍機搭配固定航線即可；需要精準疊圖與高程，才考慮 RTK 等進階配備。</div></details>
  <details><summary>空拍畫面能當作估驗依據嗎？</summary><div class="faq-a">同角度的時間序列畫面可做為進度佐證，但金錢與數量認定仍需配合監造簽證與合約約定，空拍是輔助而非最終認定。</div></details>
  <details><summary>工地在市區，能直接飛嗎？</summary><div class="faq-a">市區工地常鄰道路、建築與人群，起飛前務必確認法規與禁飛限制，並與工地主任確認工安動線，避免干擾作業。</div></details>
</div>""",
    ("life-patrol", "巡邏、搜救與勘查"),
    ("life-race", "競速與花式飛行")),

  "life-race": (
    "競速與花式飛行：FPV 運動無人機的玩法、設備與場地",
    "無人機的另一種運動玩法。FPV 第一視角把空拍變成貼身的飛行體驗，本文說明它的玩法、設備與安全場地。",
    ["FPV", "競速", "花式"], "xu",
    [("what", "認識 FPV 與花式飛行"),
     ("gear", "設備長什麼樣"),
     ("field", "安全場地怎麼選"),
     ("start", "新手怎麼入門"),
     ("faq", "常見問答")],
    """<h2 id="what">認識 FPV 與花式飛行</h2>
<p>一般空拍機追求穩與遠，FPV（第一視角）與花式飛行追求的是快與靈活。飛手戴著 FPV 眼鏡，看到的是機頭攝影機即時傳回的畫面，像自己坐在機上一起飛。</p>
<ul>
  <li><strong>競速（Racing）：</strong>穿越設定好的門框與旗門，計時排名，強調反應與軌道精準。</li>
  <li><strong>花式（Freestyle）：</strong>沒有固定軌道，在空曠場地做大角度翻滾、貼地急轉與自創動作。</li>
</ul>
<p>兩者都不是「拍風景」，而是把無人機當成一項需要練習與反應的運動。</p>

<h2 id="gear">設備長什麼樣</h2>
<p>FPV 競速機和一般空拍機的設計思維完全不同：它們小、快、不強調自動避障，靠的是飛手即時反應。</p>
<div class="tablewrap"><table>
<caption>FPV 競速機與一般空拍機的差異（依主流規格整理，實際以機型為準）</caption>
<thead><tr><th>面向</th><th>FPV 競速機</th><th>一般空拍機</th></tr></thead>
<tbody>
<tr><td>體型重量</td><td>小而輕、強調靈活</td><td>較大、搭載雲台與電池</td></tr>
<tr><td>飛行特性</td><td>快、反應直接、可特技</td><td>穩、緩、適合拍攝</td></tr>
<tr><td>主要用途</td><td>競速、花式、第一視角</td><td>風景、紀錄、巡檢</td></tr>
<tr><td>入門難度</td><td>高，需反應與體感</td><td>低，有自動輔助</td></tr>
<tr><td>安全要求</td><td>專用場地、護具為必備</td><td>一般法規與安全距離</td></tr>
</tbody></table></div>
<p>典型 FPV 系統包括小尺寸機架、無刷馬達、即時圖傳、FPV 眼鏡與遙控器，動力用鋰聚電池；它不像空拍機那樣有自動避障，因此更依賴飛手反應與場地控管。</p>

<h2 id="field">安全場地怎麼選</h2>
<p>FPV 飛行速度快、慣性大，場地選擇的重要性不亞於技術。以下是基本底線：</p>
<ul class="check">
  <li>遠離人群、道路、電線與建築的空曠場地</li>
  <li>優先使用專用賽道或室內場館，設定明確飛行邊界</li>
  <li>飛手佩戴護目鏡，觀眾與飛行區保持安全距離</li>
  <li>鋰聚電池單獨存放、充電時有人看顧</li>
  <li>起飛前確認不在禁飛區，並設好失控返航</li>
</ul>

<h2 id="start">新手怎麼入門</h2>
<ol>
  <li><strong>先上模擬器：</strong>在電腦上練打桿與緊急處置，成本最低、也最安全。</li>
  <li><strong>室內小機起步：</strong>用耐撞的小機在室內或防護網內找手感，不怕摔。</li>
  <li><strong>再進戶外場地：</strong>熟悉後到專用場地，從慢飛與直線開始，不急著鑽門。</li>
</ol>
<div class="callout green"><span class="ct">安全優先</span>FPV 反應快、慣性大，初學者最容易因為「貼地飛」或「貼人飛」而受傷。把場地與護具做對，比追速度更重要。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>玩 FPV 一定要從競速機開始嗎？</summary><div class="faq-a">不建議。新手先靠模擬器與室內小機建立體感，再依興趣選擇走競速或花式，直接上高階競速機風險很高。</div></details>
  <details><summary>FPV 眼鏡很貴，有沒有替代？</summary><div class="faq-a">入門可先用螢幕即時畫面體驗第一視角，確認喜歡後再投資眼鏡；周邊配備可依預算逐步升級。</div></details>
  <details><summary>一般空拍機不能玩花式嗎？</summary><div class="faq-a">多數空拍機強調穩定與續航，不適合激烈特技；花式與競速請使用專為靈活性設計的 FPV 機型。</div></details>
</div>""",
    ("life-site", "工地進度紀錄"),
    ("life-edu", "親子科普課程")),

  "life-edu": (
    "親子科普課程：從組裝與飛行中玩出科技與安全素養",
    "從玩樂中認識科技與安全。成熟的無人機科普課程把組裝、調校與飛行拆成親子共學的體驗，玩中學出科技素養。",
    ["親子", "科普", "組裝"], "xu",
    [("value", "為什麼適合親子一起參與"),
     ("design", "課程怎麼設計"),
     ("safety", "安全規範是課程的核心"),
     ("learn", "「玩中學」的真正價值"),
     ("faq", "常見問答")],
    """<h2 id="value">為什麼適合親子一起參與</h2>
<p>無人機科普課程最吸引人的地方，是把「遙控玩具」變成「看得懂原理的科技」。對孩子來說，組裝與飛行像玩樂；對家長來說，這是一次和孩子一起動手、一起除錯的難得經驗。課程不只教怎麼飛，更把飛行安全與電器素養一起放進去。</p>
<figure style="margin:18px 0"><img src="img/drone_classroom_overview.webp" alt="無人機科普課程的教室全景" style="width:100%;max-width:760px;margin:0 auto;border-radius:10px" loading="lazy"><figcaption style="margin-top:8px;font-size:14px;color:#667;text-align:center">整齊的教室與分組座位，是親子科普課程動手實作的基本場景。</figcaption></figure>
<div class="callout"><span class="ct">重點是「共學」</span>好的親子課程不是大人在旁划手機，而是家長和孩子一起鎖螺絲、一起校正、一起為起飛成功歡呼——這才是課程的核心價值。</div>

<h2 id="design">課程怎麼設計</h2>
<p>成熟的科普課程多採「原理 → 組裝 → 調校 → 首飛」的節奏：先講升力與馬達，再動手鎖機架、接無刷馬達與電調、裝飛控，最後做羅盤與加速度計校正，在講師帶領下完成第一次飛行。深度會依參加者年齡調整，不求一次講完全部。</p>
<ul>
  <li><strong>原理層：</strong>多旋翼怎麼靠馬達轉速差控制前後左右與升降。</li>
  <li><strong>動手層：</strong>每人一套零件，從第一根螺絲開始親手組裝。</li>
  <li><strong>飛行層：</strong>低高度、小空間的教學飛行，講師在旁隨時指點。</li>
</ul>
<figure style="margin:18px 0"><img src="img/drone_student_learning.webp" alt="學員在課程中專注學習無人機" style="width:100%;max-width:760px;margin:0 auto;border-radius:10px" loading="lazy"><figcaption style="margin-top:8px;font-size:14px;color:#667;text-align:center">學員專注跟著講師的步驟操作，動手做比聽講更記得住。</figcaption></figure>

<h2 id="safety">安全規範是課程的核心</h2>
<p>親子課程有孩子參與，安全規範不是點綴，而是課程設計的一部分。下列是家長與單位都該要求的基本底線：</p>
<ul class="check">
  <li>全程成人或講師陪同，孩子不單獨操作鋰聚電池</li>
  <li>電池由大人負責充電與保管，避免擠壓、高溫與短路</li>
  <li>飛行區與觀察區分開，參加者佩戴護具</li>
  <li>選擇合法、空曠的場地，避開禁飛區與人群</li>
  <li>先在地面確認機體與訊號正常，再低飛試飛</li>
</ul>
<div class="callout green"><span class="ct">安全素養就是學習重點</span>讓孩子在課程中學會「起飛前要檢查、電池要小心、場地要合法」，本身就是一條帶得走的科技素養。</div>

<h2 id="learn">「玩中學」的真正價值</h2>
<p>孩子在組裝過程中學到的不是某個零件叫什麼名字，而是「想法 → 動手 → 失敗 → 除錯」的循環。一台飛不起來的機器，往往比一次順利起飛更有教育意義：它逼著孩子檢查接線、重新校正，並理解科技背後需要的耐心。這正是科普課程相對於一般遙控玩具的價值。</p>
<figure style="margin:18px 0"><img src="img/drone_workshop_student_assembly.webp" alt="學員在工作坊中動手組裝無人機" style="width:100%;max-width:760px;margin:0 auto;border-radius:10px" loading="lazy"><figcaption style="margin-top:8px;font-size:14px;color:#667;text-align:center">動手組裝的過程，讓孩子在除錯中理解飛行原理與電器安全。</figcaption></figure>
<div class="callout"><span class="ct">選課小提醒</span>評估一門親子課程，可先看它是否強調分齡、安全與動手比例，而不是只強調「成品帶回家」。穩健的流程與負責任的講師，比設備多昂貴更重要。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>小朋友需要什麼程度才能上課？</summary><div class="faq-a">多數科普課程會依年齡分級，重點是有成人陪同與專注力，不必先有電子或程式基礎，講師會帶著做。</div></details>
  <details><summary>課程組裝的無人機可以直接帶回家飛嗎？</summary><div class="faq-a">成品可帶回，但應在合法場地、家長陪同下低飛，並注意電池安全與當區法規，不要在人群或禁飛區起降。</div></details>
  <details><summary>在家自己帶孩子組裝不行嗎？</summary><div class="faq-a">可以入門，但鋰聚電池與飛控校正有一定風險，課程的價值在於講師把關安全與除錯經驗，適合第一次接觸的親子。</div></details>
</div>""",
    ("life-race", "競速與花式飛行"),
    ("life", "無人機與生活")),
})

# 法規安全成本 支柱新增條目（reg-biz）
TITLE.update({
  "reg-drift": "藥劑飄移與鄰田爭議：成因、預防與處理",
  "reg-model": "自購、合作社、外包：農用無人機三種經營方式怎麼選",
})
ART.update({
  "reg-drift": (
    "藥劑飄移與鄰田爭議：成因、預防與處理",
    "飄移傷鄰田的爭議怎麼預防與處理。",
    ["藥劑飄移","鄰田爭議","噴藥安全"], "chen",
    [("cause","飄移是怎麼發生的"),("nozzle","噴嘴與霧滴的關鍵"),("weather","風向、高度與緩衝帶"),("dispute","鄰田爭議怎麼處理"),("faq","常見問答")],
    """<h2 id="cause">飄移是怎麼發生的</h2>
<p>無人機噴藥最怕的不是「噴不到」，而是「噴到不該噴的地方」。藥劑飄移（drift）指的是噴出的藥滴隨風與氣流飄離目標田區，落到鄰田、水溝、道路或設施上。一旦鄰田作物出現藥害或養蜂戶通報蜜蜂受影響，爭議往往就從這裡開始。</p>
<p>飄移不是單一因素造成，而是三個條件同時成立的結果：</p>
<ul>
  <li><strong>風：</strong>側風與陣風把細霧滴直接帶出田外；無人機旋翼下洗氣流也會攪動地表空氣，加劇細霧的擴散。</li>
  <li><strong>高度：</strong>機體離冠層越高，霧滴在空气中停留越久，被風帶走的機會越大。</li>
  <li><strong>噴嘴與霧滴：</strong>霧滴越細、越輕，沉降越慢、越容易隨風漂移；粒徑分佈是飄移量最直接的控制點。</li>
</ul>
<div class="callout"><span class="ct">觀念</span>飄移無法百分之百消除，但可以「壓低到合理範圍」。多數爭議並非來自故意，而是現場天氣、高度與噴嘴設定沒抓緊。</div>

<h2 id="nozzle">噴嘴與霧滴的關鍵</h2>
<p>噴嘴是最容易被忽略、卻最有效的防飄移工具。同一台機、同一片田，換一支噴嘴，飄移量可以差很多。實務上的方向：</p>
<div class="tablewrap"><table>
<caption>常見噴嘴取向與適用情境（依主流規格整理，實際以原廠說明為準）</caption>
<thead><tr><th>噴嘴取向</th><th>霧滴特性</th><th>適用情境</th></tr></thead>
<tbody>
<tr><td>抗飄移（減飄）噴嘴</td><td>較粗、較均，細滴比例低</td><td>鄰近設施、養蜂區、水溝與村落</td></tr>
<tr><td>標準噴嘴</td><td>粒徑中等</td><td>大面積、四周開闊的常規田區</td></tr>
<tr><td>細霧（穿透取向）噴嘴</td><td>較細、附著與穿透佳</td><td>需穿透冠層的密集作物，但要更嚴格控風</td></tr>
</tbody></table></div>
<ul>
  <li><strong>依田畔環境選噴嘴：</strong>田的外側邊帶、鄰設施與鄰居側，優先用抗飄移噴嘴；內部再依需要切換。</li>
  <li><strong>固定霧滴觀念：</strong>不要為了「看起來霧很細、很均勻」而一味追求細滴，那正是飄移最愛的條件。</li>
  <li><strong>定期檢查噴嘴：</strong>磨損、阻塞會讓粒徑分佈變差，出機前目檢、作業後清理是基本動作。</li>
</ul>

<h2 id="weather">風向、高度與緩衝帶</h2>
<p>天候與飛行參數是現場能立刻控制的變數，也是預防飄移最有效的一關。</p>
<ul>
  <li><strong>先看風向再決定起飛：</strong>作業前先觀察當下風向（煙囪、落葉、旗幟都能判斷），把「下風側」當成敏感側——那正是鄰田、水溝、養蜂設施最需要避開的方向。</li>
  <li><strong>順風邊帶與逆風起點：</strong>實務上常把田的下風側保留一段不噴或減量噴，做為「緩衝帶」，避免最後一趟把藥帶進鄰田。</li>
  <li><strong>降低飛行高度：</strong>在安全與避障前提下，讓機體貼近冠層飛，能縮短霧滴飄浮路徑、降低被風帶走的距離。</li>
  <li><strong>風大即停：</strong>風速明顯超過經驗可接受的程度，或出現不穩定陣風、逆溫、清晨濃霧剛散等條件，寧可收工改期，不要硬飛。</li>
</ul>
<div class="callout green"><span class="ct">現場檢核</span>起飛前自問三句話：現在風往哪吹？鄰田與敏感設施在哪一側？這一趟下風邊帶預留了多遠？三個答案都能講清楚，才起飛。</div>

<h2 id="dispute">鄰田爭議怎麼處理</h2>
<p>就算做足預防，還是可能遇上鄰田反映「我的菜葉有斑點／果實掉了／蜜蜂不歸巢」。這類爭議處理的重點不是立刻認賠或立刻否認，而是先把事實攤開。</p>
<ul>
  <li><strong>先留紀錄：</strong>每次噴藥都記下日期、時間、藥劑種類與稀釋、飛行航線圖、當時風向與天氣、操作人員。出事時這些就是最關鍵的證據，事後再補往往補不齊。</li>
  <li><strong>主動到場瞭解：</strong>鄰居反應時先到現場看，不要在電話裡爭論。拍對方田的症狀、拍自己田的狀況、看兩田的相對方位與當時風向，再決定下一步。</li>
  <li><strong>不要急著認錯或推諉：</strong>藥害成因可能是病害、肥害、其他田區的飄移、或設施漏藥，單憑目測很難立刻定論。</li>
  <li><strong>尋求主管機關與專業協助：</strong>農藥施用與藥害的認定有其技術與法定程序，可循地方農政單位、農業試驗改良場或病蟲害診斷系統協助判斷；必要時也可由鄉鎮市調解委員會進行調處。</li>
  <li><strong>事先鄰里溝通：</strong>最好的爭議處理是「爭議根本沒發生」。噴藥前幾天主動跟左右鄰居打聲招呼——哪天要噴、噴什麼方向、請他們把蜂箱或敏感設施暫時做好防護，往往能避免九成的摩擦。</li>
</ul>
<div class="callout"><span class="ct">責任觀念</span>無人機噴藥涉及農藥管理與環境安全，實際施用應由具備資格的人員執行；一旦發生爭議，責任認定以主管機關與專業診斷為準，本文僅提供現場處置的思考框架。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>風多大就不能噴？</summary><div class="faq-a">沒有一個絕對數字適用所有田。重點是「風向穩不穩、下風側有沒有敏感目標」。只要側風或陣風明顯讓你擔心藥會帶出田外，就寧可改期，不要硬上。</div></details>
  <details><summary>抗飄移噴嘴會不會影響效果？</summary><div class="faq-a">霧滴變粗的代價是附著與穿透可能略減，因此實務上常見的做法是「內田用標準噴嘴、田邊與下風側用抗飄移噴嘴」，在效果與安全之間取平衡。</div></details>
  <details><summary>鄰居來抗議時，第一件事該做什麼？</summary><div class="faq-a">不是爭論對錯，而是先到現場、先拍照、先把當日的施藥紀錄與航線圖調出來。把證據備齊之後再談責任與賠償，會比在現場對嗆有效得多。</div></details>
  <details><summary>養蜂戶在附近，是不是就不能噴？</summary><div class="faq-a">並非絕對不能噴，但要更嚴格：避開蜜蜂活動時段、選擇合適藥劑、加強緩衝帶、並事前主動與養蜂戶溝通。具體藥劑與安全間隔期以農藥標示與主管機關規定為準。</div></details>
</div>""",
    ("reg-obstacle","避障與緊急處置"), ("reg-model","自購、合作社、外包")),

  "reg-model": (
    "自購、合作社、外包：農用無人機三種經營方式怎麼選",
    "三種經營方式怎麼選。",
    ["經營模式","自購","外包"], "chen",
    [("overview","三種模式先看全貌"),("self","自購：掌控度最高"),("coop","合作社共同採購"),("out","外包：把作業交出去"),("choose","怎麼依自己的情況選"),("faq","常見問答")],
    """<h2 id="overview">三種模式先看全貌</h2>
<p>農用無人機不是只有「買一台回來自己飛」一條路。實務上常見三種經營方式：<strong>自購</strong>（自己買機、自己養人）、<strong>合作社共同採購</strong>（一群農友合資、分攤使用）、<strong>外包飛防</strong>（直接請專業隊來噴）。三者沒有絕對好壞，重點是匹配你的作業量、技術門檻與風險承受度。</p>
<div class="tablewrap"><table>
<caption>三種經營方式的比較（面向取向，實際數字依行情與報價為準）</caption>
<thead><tr><th>面向</th><th>自購</th><th>合作社共同採購</th><th>外包飛防</th></tr></thead>
<tbody>
<tr><td>掌控度</td><td>最高，自己排時程</td><td>中等，需協調使用順序</td><td>低，配合對方行程</td></tr>
<tr><td>前置投入</td><td>高（機體＋電池＋訓練）</td><td>中等（按比例分攤）</td><td>幾乎沒有</td></tr>
<tr><td>單位成本</td><td>高頻使用下最低</td><td>分攤後比自購低</td><td>依次／面積計費</td></tr>
<tr><td>技術與維護</td><td>全部自己扛</td><td>共同分擔、可分工</td><td>對方負責</td></tr>
<tr><td>藥劑與安全責任</td><td>自己承擔</td><td>依合作社約定</td><td>多由飛防隊處理</td></tr>
<tr><td>適合作業量</td><td>高頻、大面積</td><td>中頻、區域性</td><td>低頻或季節性</td></tr>
</tbody></table></div>
<div class="callout"><span class="ct">語先註明</span>本文不給具體金額。無人機、電池、飛防報價隨機型、季節與地區差異很大，任何費用請以實際詢價與行情為準。</div>

<h2 id="self">自購：掌控度最高</h2>
<p>自購的核心價值是「時程自己說了算」——蟲害爆發當天想噴就噴、想幾點飛就幾點飛，不用排別人的行程。對高頻、大面積、或需要依田況彈性處方的農場，這份掌控力本身就是價值。</p>
<div class="procon">
  <div class="pc pro"><h4>自購的優勢</h4><ul><li>作業時程完全自主，應變快</li><li>長期高頻使用下，單位成本最攤得薄</li><li>累積自己田區的飛行與施藥數據</li><li>可對外接案，成為額外收入來源</li></ul></div>
  <div class="pc con"><h4>自購的代價</h4><ul><li>前置投入高（機體、電池、地面站、備件）</li><li>操作者要自行訓練、考照、定期複訓</li><li>維修、保養、閒置成本都要自己扛</li><li>藥劑飄移與安全責任由自己承擔</li></ul></div>
</div>
<p>自購適合的人：一年下來噴藥、撒肥、巡田的次數夠多，且願意把「操作無人機」當成一門要長期學的技藝，而不是買回來就一勞永逸。</p>

<h2 id="coop">合作社共同採購</h2>
<p>合作社（或產銷班、區域農友共購）是許多中小農最務實的中間路線：一群人合資買機、共同分擔電池與維修、輪流使用，並由其中一兩位受過訓練的人擔任主要操作員。</p>
<ul>
  <li><strong>分攤成本：</strong>機體、電池、保養、備件的壓力被多人分攤，比單獨自購輕。</li>
  <li><strong>分攤技術：</strong>不必每個農友都考照、都精通維修，由少數人專責操作，其他人預約使用。</li>
  <li><strong>區域協調：</strong>合作社正好可以把「鄰田噴藥時段、風向、緩衝帶」一起溝通，反而比單戶更能避免飄移爭議。</li>
</ul>
<div class="callout green"><span class="ct">重點</span>共同採購成敗的關鍵不在「買哪台機」，而在「使用規則怎麼訂」：誰先約、壞了誰修、電池誰出錢、出意外誰負責。這些寫在紙上，比買好機更重要。</div>

<h2 id="out">外包：把作業交出去</h2>
<p>外包（請飛防隊、測繪服務隊）是門檻最低的切入方式：你不用買機、不用考照、不用修電池，只要預約、報面積、指定藥劑處方，其餘由對方處理。</p>
<div class="procon">
  <div class="pc pro"><h4>外包的優勢</h4><ul><li>幾乎零前置投入，依實際報價為準</li><li>技術、機體、證照都由專業隊處理</li><li>適合作業頻率低、只想處理特定時期</li><li>可先外包驗證效果，再決定要不要自購</li></ul></div>
  <div class="pc con"><h4>外包的限制</h4><ul><li>要配合對方的行程與排程</li><li>高峰期可能排不到機</li><li>對田區的長期掌握度不如自己飛</li><li>藥劑與處方的細節要雙方充分溝通</li></ul></div>
</div>
<p>外包的常見計費方式依面積、依次或依專案，實際報價視行情與地區而定；簽約前務必把「噴哪些田、用什麼藥、安全間隔期、出問題怎麼處理」白紙黑字寫清楚。</p>

<h2 id="choose">怎麼依自己的情況選</h2>
<ul class="check">
  <li>先估自己一年的實際作業天數與面積，不要用「理想狀況」算</li>
  <li>看周遭有沒有合適的飛防隊或合作社，不要假設一定找得到</li>
  <li>評估自己或班員有沒有人願意長期投入訓練與維護</li>
  <li>把「藥劑飄移與鄰田責任」當成一項成本，而不是事後才想到的問題</li>
  <li>建議先用外包或合作社試一季，再決定要不要走向自購</li>
</ul>
<div class="callout"><span class="ct">一個常見的混搭做法</span>多數成熟農場不是「純自購」或「純外包」，而是「自己的常規噴藥自己飛、大面積一次性撒肥或測繪外包」。先想清楚哪些事自己做最划算、哪些事交出去比較好，再決定設備投資，比一次到位更穩。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>剛開始接觸無人機，建議從哪一種模式開始？</summary><div class="faq-a">多數情況建議先外包或加入合作社試一季。實際走過一次噴藥、撒肥與田區監測，再來判斷自己的作業量與技術意願，會比憑想像買機準確得多。</div></details>
  <details><summary>合作社共同採購，最容易爭論的是什麼？</summary><div class="faq-a">通常是使用順序與維修分攤。建議在買機之前就先把預約規則、耗材分攤、損壞責任寫成白紙黑字，並推一位專責管理人，避免事後吵。</div></details>
  <details><summary>外包飛防隊，要不要自己懂藥劑？</summary><div class="faq-a">要。飛防隊負責飛行，但「噴什麼藥、濃度多少、安全間隔期」的最終責任仍在農友自己。簽約前把處方確認清楚，並保留施藥紀錄。</div></details>
  <details><summary>自購之後，閒置的風險怎麼控制？</summary><div class="faq-a">一開始就把「一年預期作業天數」估保守一點；設備閒置不代表成本歸零，電池還是會隨時間老化。若有機會對外接案或共享給合作社，閒置壓力會小很多。</div></details>
</div>""",
    ("reg-drift","藥劑飄移與鄰田爭議"), ("reg","法規安全成本")),
})

# 法規安全成本 支柱新增條目（part_reg_safe）：禁飛區、環境責任、天氣判斷、避障與緊急處置
TITLE.update({
  "reg-no-fly": "禁飛區與申請：起飛前必查的區域紅線",
  "reg-env": "噴藥的環境責任：藥劑、飄散與鄰田影響",
  "reg-weather": "天氣條件判斷：風、雨、霧與溫度如何決定能不能出機",
  "reg-obstacle": "避障與緊急處置：避障極限、失控斷鏈與電池安全守則",
})

ART.update({
  "reg-no-fly": (
    "禁飛區與申請：起飛前必查的區域紅線",
    "禁飛區、限制區與專案申請，起飛前必查。本文整理台灣常見的禁飛與限制區類型、查詢工具方向，以及需要申請時的準備要點，並提醒一切以主管機關現行公告為準。",
    ["法規", "禁飛區", "申請"], "chen",
    [("why","為什麼起飛前一定要查"),("types","常見的禁飛與限制區類型"),("query","起飛前怎麼查"),("apply","需要申請時怎麼準備"),("farm","農用噴藥的特別提醒"),("faq","常見問答")],
    """<h2 id="why">為什麼起飛前一定要查</h2>
<p>無人機的飛行權利不是「在哪裡都可以」。台灣對無人機的飛行區域有明確規範，未經許可進入禁飛或限制區，可能影響航安、公共安全，也會讓飛手自身面臨法規責任。對農用噴藥與測繪來說，田區旁邊可能就有機場航道、政府設施或軍事敏感設施，「看起來是田」不代表「可以飛」。</p>
<div class="callout"><span class="ct">第一條原則</span>起飛前先查區域，再談機況與天氣。區域查詢是所有作業的第一道關卡，幾秒鐘的事，卻是最容易被忽略的一關。</div>

<h2 id="types">常見的禁飛與限制區類型</h2>
<p>以下是實務上最常遇到的幾類區域型態，僅供你建立地圖概念，<strong>實際範圍與限制一律以主管機關現行公告為準</strong>：</p>
<div class="tablewrap"><table>
<caption>常見禁飛／限制區型態（概念整理，範圍與規定以主管機關公告為準）</caption>
<thead><tr><th>類型</th><th>為什麼被管制</th><th>農用作業常見情境</th></tr></thead>
<tbody>
<tr><td>機場周邊與航道</td><td>維航安，避免與有人機接近</td><td>西部平原、台東縱谷等機場附近農田</td></tr>
<tr><td>政府機關與重要設施</td><td>維安考量</td><td>田區旁有縣市機關、醫院、電廠</td></tr>
<tr><td>軍事與敏感設施</td><td>國防與機密</td><td>特定營區、雷達站、彈藥庫周邊</td></tr>
<tr><td>人群聚集場所</td><td>公共安全</td><td>廟會、活動、市集、學校上方</td></tr>
<tr><td>重大公共建設</td><td>維安與設施安全</td><td>重要橋梁、水庫、電塔周邊</td></tr>
</tbody></table></div>
<p>除了「完全不能飛」的禁飛區，還有一類是「條件式可以飛」的限制區——需要申請、或限縮高度、限縮時間、限縮用途。同一片田，平日作業與節慶活動期間的限制可能不同。</p>

<h2 id="query">起飛前怎麼查</h2>
<ul>
  <li><strong>用官方或合規的飛行區域查詢工具：</strong>主管機關提供的遙控無人機相關查詢平台，是最直接的第一站。</li>
  <li><strong>同時對照地圖：</strong>把起飛點與作業範圍標在地圖上，看是否鄰近機場、設施或活動場所。</li>
  <li><strong>問當地：</strong>里長、社區、農會或鄰近飛手，常能補上官方地圖未即時反映的臨時管制（如演習、活動）。</li>
  <li><strong>出機當天再查一次：</strong>區域狀態可能因臨時活動、演習而改變，前一天查過不代表當天一樣。</li>
</ul>
<div class="callout green"><span class="ct">務實做法</span>把「起飛點 + 作業範圍 + 起降備援點」三個座標都查過。只查起飛點、沒查作業中途航線，是最常見的疏漏。</div>

<h2 id="apply">需要申請時怎麼準備</h2>
<p>若作業範圍位於限制區，或涉及人群、夜航、特定用途，依規範可能需要事先申請。準備方向如下（<strong>實際應備文件與流程以主管機關現行公告為準</strong>）：</p>
<ol>
  <li><strong>確認申請門檻：</strong>用途、重量級別、飛行區域與高度，先判斷自己屬於哪一類。</li>
  <li><strong>備妥基本資料：</strong>機體辨識資訊、操作者證照資訊、作業期間與地點、航線概要。</li>
  <li><strong>講明作業目的：</strong>農用噴藥、測繪、監測等，用途越清楚，審查越順。</li>
  <li><strong>預留作業時間：</strong>申請需要作業等候時間，不要當天要飛才臨時送件。</li>
  <li><strong>保留核准證明：</strong>通過後的核准資訊留在地面站或手機，現場可備查。</li>
</ol>

<h2 id="farm">農用噴藥的特別提醒</h2>
<p>農用作業有幾個容易踩雷的情境：<strong>山坡地</strong>可能鄰近軍事設施或雷達站；<strong>都會邊緣農地</strong>可能在政府設施或學校上方；<strong>河川地與水庫周邊</strong>常屬於特定管理區。噴藥航線拉得長，很容易「起飛點合法、中途飄進管制區」。建議把整段航線都納入查詢範圍，並與客戶（田主）確認過去有無類似作業的申請紀錄。</p>
<div class="callout"><span class="ct">責任意識</span>查區域、申請許可不是「形式」，而是你對航安、鄰里與自身執業的基本責任。一次未查就飛，省下的是幾分鐘，賠上的可能是整年度的執業權利。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>我只是在自己家的田飛，也要查嗎？</summary><div class="faq-a">要。農地是否自有與是否在禁飛區無關。起飛前查一次區域，是每次飛行的固定動作。</div></details>
  <details><summary>禁飛區的範圍會不會常常改？</summary><div class="faq-a">會。重大活動、演習或新建設都可能調整。建議每次作業當天重新確認，並把官方查詢工具設為常用書籤。</div></details>
  <details><summary>申請被駁回怎麼辦？</summary><div class="faq-a">先對照核准條件，常見原因包括用途說明不足、航線穿過敏感設施、時間與活動衝突。依補件說明修正後重新送件，或調整作業區域與時段。</div></details>
</div>""",
    ("reg", "法規安全成本"), ("reg-env", "噴藥的環境責任")),

  "reg-env": (
    "噴藥的環境責任：藥劑、飄散與鄰田影響",
    "藥劑管理、飄散與鄰田影響的責任議題。本文從合法藥劑、安全間隔期到飄散防護，說明農用噴藥背後的環境責任，並提醒一切以主管機關現行公告為準。",
    ["農藥", "環境", "責任"], "chen",
    [("why","噴藥不是只把藥噴出去"),("legal","合法藥劑與使用紀錄"),("interval","安全間隔期與採收"),("drift","飄散與鄰田影響"),("record","作業紀錄與責任"),("faq","常見問答")],
    """<h2 id="why">噴藥不是只把藥噴出去</h2>
<p>農用無人機噴藥看起來是「飛過田就好」，但實際上它同時是一項<strong>農業施藥行為</strong>與一項<strong>空中作業行為</strong>。空中飛行受民航法規規範，田間施藥則受農藥管理相關規範約束。飛手與田主面對的不只是「有沒有把藥噴到田裡」，還有「藥到了哪裡、留下什麼、對誰負責」。</p>
<div class="callout"><span class="ct">責任的起點</span>在按下噴灑開關之前，先問自己三個問題：用的藥合法嗎？噴的時間對嗎？風把藥帶去哪裡？</div>

<h2 id="legal">合法藥劑與使用紀錄</h2>
<ul>
  <li><strong>使用合法登記藥劑：</strong>選用經主管機關核可、標示完整的農藥，不用來路不明、標示不全或逾期藥劑。</li>
  <li><strong>對症用藥：</strong>依病蟲草害種類選藥，不任意混用、不任意提高劑量。</li>
  <li><strong>稀釋與配藥：</strong>依標示倍數與田區面積計算用量，並做好個人防護。</li>
  <li><strong>藥劑紀錄：</strong>紀錄藥名、劑量、稀釋倍數、施藥日期與作業人員，做為日後追溯依據。</li>
</ul>
<div class="callout green"><span class="ct">重要觀念</span>農用無人機噴的藥，和地面噴藥機噴的藥，在農藥管理上是同一回事。不能因為「飛得快、看起來自動」就省略用藥紀錄與合法藥劑的把關。</div>

<h2 id="interval">安全間隔期與採收</h2>
<p>每一種農藥都有建議的安全採收間隔期，意思是「最後一次施藥到可以實際採收之間，需要間隔多久」。這段期間是為了讓藥劑在作物上降到安全容許量以下。無人機噴藥速度快，很容易「一天噴完好幾分田」，也很容易因此把間隔期算錯。</p>
<div class="tablewrap"><table>
<caption>安全間隔期的實務重點（概念整理，數值以農藥標示與主管機關公告為準）</caption>
<thead><tr><th>面向</th><th>實務做法</th><th>常見疏忽</th></tr></thead>
<tbody>
<tr><td>間隔天數</td><td>依藥劑標示與作物別查表</td><td>多種藥混用時只看其中一種</td></tr>
<tr><td>採收時機</td><td>間隔期滿後再安排採收</td><td>趕著出貨提前採收</td></tr>
<tr><td>作業紀錄</td><td>記錄施藥日期與藥名</td><td>沒記錄、事後對不上</td></tr>
<tr><td>供應鏈溝通</td><td>把施藥紀錄提供給收購端</td><td>履歷資料不完整</td></tr>
</tbody></table></div>

<h2 id="drift">飄散與鄰田影響</h2>
<p>無人機噴藥最大的環境風險，是<strong>霧滴飄散</strong>。風速稍大、飛行高度偏高、霧滴偏細，藥霧就可能被帶到隔壁田、鄰路、甚至社區。鄰田若是有機農場、蜜蜂養殖區、魚塭或果園，一次飄移就可能造成可觀損失。</p>
<ul>
  <li><strong>看風向：</strong>把鄰田敏感作物放在風下側的相反方向，或主動留緩衝。</li>
  <li><strong>控高度與速度：</strong>依機型與噴嘴特性，把飛行高度與作業速度壓在合理範圍。</li>
  <li><strong>選噴嘴：</strong>霧滴不要過細，減少長距離飄散。</li>
  <li><strong>與鄰里溝通：</strong>噴藥前主動告知相鄰農戶，必要時約定作業時段。</li>
</ul>
<div class="procon">
  <div class="pc pro"><h4>做好飄散防護的好處</h4><ul><li>降低鄰田藥害爭議</li><li>提高藥劑實際利用率</li><li>累積友善鄰里的執業口碑</li></ul></div>
  <div class="pc con"><h4>忽略飄散的代價</h4><ul><li>鄰田損害求償與爭議</li><li>有機認證或友善耕作受影響</li><li>公共形象與執業信譽受損</li></ul></div>
</div>

<h2 id="record">作業紀錄與責任</h2>
<p>完整的施藥紀錄，在出事時是保護自己的最佳證據。建議至少留存：日期時間、田區位置、作物別、藥名與劑量、作業飛手、天氣概況、以及鄰田溝通情形。一旦鄰田發生疑似藥害，這份紀錄就是你與田主、鄰居、甚至主管機關之間對話的基礎。</p>
<div class="callout"><span class="ct">責任不是事後</span>環境責任不是「出事再處理」，而是事前就把用藥、天氣與鄰里關係都管好。寧可當天少噴幾分田，也不要讓藥霧飄到不該去的地方。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>我是幫別人噴藥，責任在誰？</summary><div class="faq-a">飛手與田主都有各自的責任：飛手對飛行安全與施作技術負責，田主對用藥種類與田間管理負責。雙方最好在事前書面確認藥劑、劑量與作業方式。</div></details>
  <details><summary>鄰田說被我的藥飄到了，怎麼辦？</summary><div class="faq-a">先保留現場與作業紀錄，主動與對方溝通，必要時通知農業相關主管機關協助判斷。不要在未確認前直接認賠，也不要回避溝通。</div></details>
  <details><summary>有機田旁邊可以噴藥嗎？</summary><div class="faq-a">風險很高。有機田對農藥殘留極度敏感，即使是合法藥劑，飄散過去也可能影響對方認證。建議主動留更大緩衝帶、避開風向，或與對方協調作業時段。</div></details>
</div>""",
    ("reg-no-fly", "禁飛區與申請"), ("reg-weather", "天氣條件判斷")),

  "reg-weather": (
    "天氣條件判斷：風、雨、霧與溫度如何決定能不能出機",
    "風、雨、霧與溫度如何決定能不能出機。本文把農用無人機最常遇到的四類天氣因子拆開講，提供一張可執行的出機判斷邏輯，並提醒以氣象預報與機型規格為準。",
    ["天氣", "作業判斷", "安全"], "chen",
    [("why","天氣是出機的第一道關卡"),("wind","風：最敏感的因子"),("rain","雨與高濕"),("fog","霧與能見度"),("temp","高溫與低溫"),("decide","一張出機判斷流程"),("faq","常見問答")],
    """<h2 id="why">天氣是出機的第一道關卡</h2>
<p>農用無人機的安全性與作業品質，很大程度由天氣決定。同一台機、同一塊田，微風晴天與午後對流天氣下，是兩種完全不同的作業情境。對植保噴藥來說，天氣不只關係飛得穩不穩，更關係<strong>藥霧會不會飄、落在哪裡</strong>。</p>
<div class="callout"><span class="ct">核心觀念</span>天氣判斷不是「看一下天空」，而是「看風、看雨、看能見度、看溫度」的綜合決策。任何一項達到紅線，就不出機。</div>

<h2 id="wind">風：最敏感的因子</h2>
<p>風是農用無人機最敏感的天氣因子，原因有二：風大會讓機體飄移、耗電增加；更重要的是，<strong>風大會讓藥霧飄到不該去的地方</strong>。</p>
<ul>
  <li><strong>風速：</strong>超過機型抗風等級或作業上限就不應起飛，具體數值以原廠規格與作業手冊為準。</li>
  <li><strong>風向：</strong>噴藥作業要把鄰田、道路、村落放在風下側的相反方向。</li>
  <li><strong>風的突發性：</strong>午後對流、地形峽谷風、沿海陣風，都可能在十幾分鐘內改變風況。</li>
  <li><strong>熱氣流與風切：</strong>晴天正午的上升氣流與低高度風切，會讓機體在低高度作業時突然飄移。</li>
</ul>
<div class="callout green"><span class="ct">實務經驗</span>噴藥作業最好的時段往往是清晨或傍晚：風小、氣流穩、露水未乾有助霧滴附著。正午大太陽下的熱氣流，其實是最不適合噴藥的時段。</div>

<h2 id="rain">雨與高濕</h2>
<p>雨對噴藥的影響最直接：雨水會把葉面上的藥液沖掉，等於白噴；未來數小時內可能降雨，也會讓剛噴的藥流失。除了下雨本身，<strong>高濕與露水</strong>也要判斷：</p>
<ul>
  <li><strong>雨中不作業：</strong>雨會改變藥液濃度、沖刷葉面，也影響電子系統。</li>
  <li><strong>雨後待葉面乾：</strong>葉面還濕時噴藥，藥液會順著水滴流失或聚集成珠。</li>
  <li><strong>降雨機率：</strong>出機前查短時天氣預報，預報降雨機率高就避開。</li>
</ul>

<h2 id="fog">霧與能見度</h2>
<p>能見度不足對無人機的威脅是雙重的：飛手看不到機體、機上的光學避障與圖傳也容易受影響。霧、薄霧、晨間低雲與濃濕氣，都會讓本來「看起來很近」的距離變得模糊。</p>
<div class="tablewrap"><table>
<caption>能見度條件與作業建議（概念整理，實際以現場與預報為準）</caption>
<thead><tr><th>能見度狀況</th><th>飛行風險</th><th>作業建議</th></tr></thead>
<tbody>
<tr><td>清晰、視野廣</td><td>低</td><td>可依規劃作業</td></tr>
<tr><td>薄霧、晨霧</td><td>中</td><td>縮短作業距離、加強目視</td></tr>
<tr><td>濃霧、低雲</td><td>高</td><td>暫停作業，待能見度恢復</td></tr>
<tr><td>雨後水氣瀰漫</td><td>中</td><td>確認光學感測與圖傳後再決定</td></tr>
</tbody></table></div>

<h2 id="temp">高溫與低溫</h2>
<p>溫度對電池與藥劑都有影響。<strong>高溫</strong>會讓電池放電更快、機體散熱負擔變大，也容易引發午後對流；<strong>低溫</strong>會讓電池可用容量下降，飛行前若沒讓電池回暖，單趟續航會明顯縮短。</p>
<ul>
  <li><strong>高溫：</strong>避免電池在陽光下曝曬過久，作業中注意馬達與電變溫度。</li>
  <li><strong>低溫：</strong>起飛前讓電池回到適溫，縮短單趟任務，預留更多返航餘裕。</li>
  <li><strong>大溫差：</strong>清晨與正午溫差大，電池表現與氣流都會變化，要分開評估。</li>
</ul>

<h2 id="decide">一張出機判斷流程</h2>
<ol>
  <li><strong>看短時預報：</strong>風速風向、降雨機率、溫度、濕度。</li>
  <li><strong>看現場：</strong>實際站在田邊感受風、看雲、看鄰田與樹梢擺動。</li>
  <li><strong>對紅線：</strong>任一項超過機型規格或作業上限，就停。</li>
  <li><strong>留餘裕：</strong>即使看似可以飛，也把返航餘裕與備援場地想好。</li>
  <li><strong>作業中持續觀察：</strong>風向風速改變就暫停，不要硬噴完。</li>
</ol>
<div class="callout green"><span class="ct">判斷的底線</span>「今天看起來還可以飛」不是標準，「今天每一項都在安全範圍內」才是。寧可延後半天，也不要在邊緣天氣硬上。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>預報沒下雨，下午突然飄雨怎麼辦？</summary><div class="faq-a">立即結束當趟作業，優先返航降落。噴藥作業遇到降雨，霧滴會被雨水沖刷、效果打折，繼續飛反而增加風險。</div></details>
  <details><summary>風速看哪個數字比較準？</summary><div class="faq-a">除了都會區氣象站數據，更要看田區現場。地形與海風會讓實際風況與氣象站有落差，站在田邊感受最準。</div></details>
  <details><summary>清晨有薄霧可以噴藥嗎？</summary><div class="faq-a">薄霧風小、露水重，其實是噴藥條件好的時段，但要留意能見度與圖傳。若霧開始變濃、目視不穩，就先停。</div></details>
</div>""",
    ("reg-env", "噴藥的環境責任"), ("reg-obstacle", "避障與緊急處置")),

  "reg-obstacle": (
    "避障與緊急處置：避障極限、失控斷鏈與電池安全守則",
    "避障、緊急處置與電池管理的安全守則。本文說明避障感測的能力邊界、失控與斷鏈時的處置原則，以及電池管理上最容易被忽略的安全細節。",
    ["安全", "避障", "緊急處置"], "chen",
    [("why","先認識風險邊界"),("limit","避障感測的極限"),("fail","失控與斷鏈處置"),("lowbat","低電量與緊急降落"),("battery","電池管理安全守則"),("faq","常見問答")],
    """<h2 id="why">先認識風險邊界</h2>
<p>現代農用無人機配備了多方向避障、RTK 定位、斷航續飛與低電量返航，聽起來很安全。但越依賴自動化，越要清楚：<strong>這些系統都有邊界</strong>。避障看不到的東西、斷鏈後的數十秒、電池突然掉壓，都是現場作業真正的風險點。認識這些邊界，才知道什麼時候要靠自己的判斷接管。</p>
<div class="callout"><span class="ct">安全觀念</span>自動化是「輔助」，不是「替代判斷」。飛手永遠要準備好隨時接手，並知道每一項自動功能的極限在哪裡。</div>

<h2 id="limit">避障感測的極限</h2>
<p>避障系統多靠光學、雷射或視覺感測偵測障礙物，但它們不是萬靈丹：</p>
<ul>
  <li><strong>細小線狀物：</strong>電線、纜線、細樹枝，常是避障最弱的一環。</li>
  <li><strong>透明或低對比物：</strong>玻璃、塑膠布、特定材質圍籬，感測器不容易辨識。</li>
  <li><strong>低高度作物與地形：</strong>稻田水面、樹冠下緣、起伏地，光學判讀容易誤差。</li>
  <li><strong>夜間與強逆光：</strong>光學避障在光線不足或強逆光下性能下降。</li>
  <li><strong>動態障礙：</strong>突然闖入的人、車、牲畜，反應時間永遠不夠。</li>
</ul>
<div class="tablewrap"><table>
<caption>常見障礙情境與避障表現（概念整理，實際表現以機型規格為準）</caption>
<thead><tr><th>障礙類型</th><th>避障可信度</th><th>飛手應對</th></tr></thead>
<tbody>
<tr><td>大型建物、樹幹</td><td>高</td><td>仍保持目視</td></tr>
<tr><td>電線、纜線</td><td>低</td><td>航線主動避開，不依賴避障</td></tr>
<tr><td>低高度作物、水面</td><td>中</td><td>壓低飛行高度時格外小心</td></tr>
<tr><td>夜間、強逆光</td><td>下降</td><td>避免在此條件下作業</td></tr>
<tr><td>突發人車牲畜</td><td>反應有限</td><td>作業前清空區域、設警戒</td></tr>
</tbody></table></div>

<h2 id="fail">失控與斷鏈處置</h2>
<p>「失控」不是電影裡那種突然狂飆，比較常見的是<strong>圖傳或遙控訊號中斷</strong>，機體依設定進入返航或懸停。成熟的飛手不會等系統幫你處理，而是事前就把預設行為設好：</p>
<ol>
  <li><strong>斷鏈返航：</strong>設定訊號中斷後自動返航到起飛點，並確認返航高度高於沿途障礙。</li>
  <li><strong>返航點設定：</strong>起飛前設定明確返航點，不要讓機體用「最後定位」隨便選一個降落點。</li>
  <li><strong>返航高度：</strong>高於作業區內最高障礙（樹冠、電塔、電線），避免返航途中碰撞。</li>
  <li><strong>現場處置：</strong>訊號中斷時不要慌亂亂打遙控，先等系統反應，必要時切入手動接管。</li>
  <li><strong>紀錄與回報：</strong>事後留下事件經過，做為保險與日後檢討依據。</li>
</ol>
<div class="callout"><span class="ct">失控的常見誤解</span>以為「有自動返航就安全了」。若返航高度不夠、途中有電線，自動返航反而會把機體送上碰撞路徑。返航高度是要你依田區環境手動設的，不是出廠預設就好。</div>

<h2 id="lowbat">低電量與緊急降落</h2>
<p>低電量是最常見的緊急狀況。作業中電量下降速度若比預期快（風大、載重、低溫都會讓耗電增加），要提早返航，而不是等到系統警告才動作。</p>
<ul>
  <li><strong>設兩層警戒：</strong>第一層提醒返航、第二層強制返航，數值依機型與任務設定。</li>
  <li><strong>預備迫降點：</strong>作業前想好「萬一現在要緊急降落，要降在哪裡」。</li>
  <li><strong>不要硬飛回程：</strong>低電量硬撐是最常見的墜毀原因。寧可迫降在安全田區，再去把機子撿回來。</li>
</ul>

<h2 id="battery">電池管理安全守則</h2>
<p>農用無人機的許多安全事件，源頭不是飛行技術，而是<strong>電池</strong>。以下守則建議逐條建立習慣：</p>
<ul class="check">
  <li>起飛前確認每顆電池電壓一致、無膨脹、無破損</li>
  <li>電池在適溫下使用，冬天先回暖、夏天避免曝曬</li>
  <li>充電時有人看顧，不在無人狀況下充電</li>
  <li>充電區遠離可燃物與作業現場，備有合適的滅火器材</li>
  <li>損傷、異常發熱、鼓脹的電池立即停用</li>
  <li>電池運送與存放做好隔絕，避免金屬接觸與擠壓</li>
  <li>依規範回收廢電池，不任意丟棄</li>
</ul>
<div class="callout green"><span class="ct">底線</span>電池事故的代價往往是整台機、整個車，甚至人員安全。省電池的錢不值得；把電池管理當成作業流程的一部分，才是長遠做法。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>避障全開是不是就可以放心手動飛？</summary><div class="faq-a">不可以。避障對電線、細枝、低高度作物的偵測有限，且動態物體反應時間不足。航線規劃與現場清空，仍是第一道防線。</div></details>
  <details><summary>斷鏈時應該立刻搶遙控嗎？</summary><div class="faq-a">先讓系統依設定反應（通常是返航或懸停），過幾秒再依畫面與訊號狀況決定接管。慌亂連打遙控反而可能觸發更多動作。</div></details>
  <details><summary>電池循環次數到了就一定要換？</summary><div class="faq-a">循環次數是參考，不是絕對紅線。若續航明顯縮水、電壓不一致、外觀膨脹，即使次數未到也應汰換；反之狀況良好可與原廠確認後繼續使用。</div></details>
</div>""",
    ("reg-weather", "天氣條件判斷"), ("reg-drift", "藥劑飄移與鄰田爭議")),
})

# 案例資源 支柱新增條目（part_resources）
# 實務案例／工具與資源：resources-case / resources-oversea / resources-terms
TITLE.update({
  "resources-case": "台灣農業案例：茶園、果園與高山農業的常見應用情境",
  "resources-oversea": "國外大型農場做法：用機隊、自動機場與數據平台管理大面積農田",
  "resources-terms": "農用無人機名詞對照表：機體、定位、感測、作業與法規一次看懂",
})

ART.update({
  "resources-case": (
    "台灣農業案例：茶園、果園與高山農業的常見應用情境",
    "茶園、果園與高山農業的實際應用案例。",
    ["案例","台灣","茶園果園"], "team",
    [("why","為什麼先看本土案例"),("tea","茶園的常見應用情境"),("orchard","果園的常見應用情境"),("rice","稻田的常見應用情境"),("high","高山與坡地農業的常見應用情境"),("take","從案例裡能學到什麼"),("faq","常見問答")],
    """<p>台灣農業地形多樣、田塊零碎、山區比例高，無人機的價值往往不在「快」，而在「人不容易走到、走到也危險」的地方。本文不綁特定農場名稱，而是把田間常見的應用情境歸納出來，讓你對號入座、判斷自己的田有沒有類似需求。</p>

<h2 id="why">為什麼先看本土案例</h2>
<p>國外大農場的做法很吸引人，但台灣的田地小、地形陡、勞力老齡化，直接套用未必合用。本土案例的意義在於：它們面對的是和你類似的限制——<strong>面積零碎、坡地作業、人力不足、天災頻繁</strong>。看這些情境怎麼被處理，比看規格表更能幫你判斷「無人機對我到底有沒有用」。</p>
<div class="callout"><span class="ct">閱讀方式</span>下面每個情境都只描述「常見應用方式」，不指名特定農場、不寫具體產量與金額。把它當作「這類田地通常會遇到什麼、無人機補上哪一段」的地圖即可。</div>

<h2 id="tea">茶園的常見應用情境</h2>
<p>茶園多位於丘陵與山坡，田壟沿等高線分布，人工作業要爬上爬下。無人機在茶園的切入點集中在巡視與施作：</p>
<ul>
  <li><strong>長勢與病害巡視：</strong>沿茶行固定航線定期空拍，比對茶叢長勢與冠層色澤變化，提早看見疑似病斑或樹勢衰弱區。</li>
  <li><strong>病蟲害用藥：</strong>在適合作業的天氣窗口，以植保機沿茶行噴施，減少人員長時間暴露於藥劑與陡坡環境。</li>
  <li><strong>區塊登錄與地形底圖：</strong>把分散的茶區一次空拍下來，做為日後施肥、修剪與勞力調度的參考底圖。</li>
</ul>
<div class="callout"><span class="ct">茶園特別注意</span>坡地與茶行密度高，航線規劃要避開陡峭落差與臨邊區，風速上限也比平地更保守；噴藥時務必留意下坡方向的霧滴飄散。</div>

<h2 id="orchard">果園的常見應用情境</h2>
<p>果園（柑橘、荔枝、芒果、高接梨等）樹冠高低參差，地面巡視死角多。無人機在果園常扮演「從上面看」的角色：</p>
<ul>
  <li><strong>冠層長勢與結果分布：</strong>掛果期以高解析空拍看樹冠密度與結果狀況，協助判斷結果均勻度與需要疏果或營養調節的區塊。</li>
  <li><strong>病蟲與逆境早期偵測：</strong>搭配多光譜或熱影像，在黃化、落葉明顯之前，先看見冠層的光譜與溫度異常。</li>
  <li><strong>樹冠噴施：</strong>對高大果樹，地面噴藥噴不高、噴不透時，由空中由上往下施作，覆蓋到樹冠上緣。</li>
</ul>
<div class="tablewrap"><table>
<caption>果園常見應用情境與切入點（依主流做法整理，實際成效視品種與設備而定）</caption>
<thead><tr><th>情境</th><th>主要用途</th><th>常用感測／機型</th></tr></thead>
<tbody>
<tr><td>樹冠長勢巡視</td><td>看結果分布與樹勢</td><td>可見光空拍</td></tr>
<tr><td>病蟲逆境早期偵測</td><td>黃化、缺水、病斑早期訊號</td><td>多光譜／熱影像</td></tr>
<tr><td>樹冠上緣噴施</td><td>地面噴不到的高處施藥</td><td>植保噴灑型</td></tr>
</tbody></table></div>

<h2 id="rice">稻田的常見應用情境</h2>
<p>稻田是相對平整、面積集中的作物，也是無人機最容易發揮效率的場域：</p>
<ul>
  <li><strong>病蟲與除草用藥：</strong>水稻分蘗至抽穗期的病蟲害防治，由植保機大面積均勻噴施，省工且覆蓋快。</li>
  <li><strong>撒肥與穗肥：</strong>以撒布模組施肥、播種，代替人工均勻撒布。</li>
  <li><strong>長勢與產前監測：</strong>固定航線定期拍攝，看長勢均勻度與可能的缺水、病害區。</li>
</ul>
<div class="callout green"><span class="ct">稻田的優勢</span>稻田地形平坦、障礙少，是新手飛防服務隊最常接案、也最容易建立穩定 SOP 的場景；對稻農來說，外包噴藥的起點往往也是從稻田開始。</div>

<h2 id="high">高山與坡地農業的常見應用情境</h2>
<p>高冷蔬菜、高山果樹與坡地作物，最大的痛點是「人進不去、進去也危險」。無人機在這裡的價值特別明顯：</p>
<ul>
  <li><strong>勘災與災後復勘：</strong>颱風、豪雨後道路中斷時，由空拍先看坡地作物倒伏、土石影響與田損範圍，做為復耕與損失研判的空中佐證。</li>
  <li><strong>地形與風險評估：</strong>空拍還原坡度、排水路徑與邊界，協助判斷哪些區塊適合作業、哪些有滑落風險。</li>
  <li><strong>資材與藥劑輸送：</strong>在人員不便往返的高處，以放物或噴灑方式補上局部資材需求（實際可行程度視法規與設備而定）。</li>
</ul>

<h2 id="take">從案例裡能學到什麼</h2>
<p>把上面幾個場景放在一起看，會發現無人機在台灣農業的價值不是單一功能，而是三條共通的線：</p>
<ol>
  <li><strong>補人力：</strong>噴藥、撒肥、巡視這些重複費力的工作，交給機器。</li>
  <li><strong>補視角：</strong>從人走不到、看不清的上空，把田整體看進來。</li>
  <li><strong>補紀錄：</strong>固定航線重複拍攝，留下可逐年比對的田區資料。</li>
</ol>
<ul class="check">
  <li>你的田地是「坡地、分散、人力不足」這三項占越多，無人機的相對價值越高</li>
  <li>先從「外包服務隊」試一個季，比直接買機更能驗證需求</li>
  <li>不論自購或外包，固定航線與拍攝條件都要一致，資料才有意義</li>
</ul>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>這些案例是真實農場嗎？</summary><div class="faq-a">本文描述的是「常見應用情境」，刻意不指名特定農場，也不引用未經查證的產量與金額。重點在說明這類田地通常怎麼用無人機，而非宣傳單一案例成效。</div></details>
  <details><summary>我家只有幾分地，用得起嗎？</summary><div class="faq-a">面積小不一定要自購機器。可以用外包飛防或測繪服務，依面積計費；重點是先確認你的痛點是噴藥、巡視還是勘測，再選對應服務。</div></details>
  <details><summary>高山農業最大的限制是什麼？</summary><div class="faq-a">多半不是技術，而是天候、風速與起降場地。坡地起飛空間小、風況不穩，作業窗口比平地短，務必把安全與法規放在前面。</div></details>
</div>""",
    ("resources","案例資源"), ("resources-oversea","國外大型農場做法")),

  "resources-oversea": (
    "國外大型農場做法：用機隊、自動機場與數據平台管理大面積農田",
    "大型農場如何用機隊管理大面積農田。",
    ["國外案例","機隊","大面積"], "team",
    [("scale","大農場面對的問題不同"),("fleet","機隊與調度怎麼運作"),("dock","自動機場（機巢）的角色"),("data","數據平台怎麼串起整場"),("borrow","台灣農場可以借鏡什麼"),("faq","常見問答")],
    """<p>國外尤其是大面積平整農區的農場，單一田塊動輒遼闊、作業季節高度集中，靠人工單機飛行根本應付不過來。它們發展出的一套做法——<strong>機隊調度、自動機場、數據平台</strong>——值得台灣大農場、農企業與飛防服務隊參考，但不能直接照搬。</p>

<h2 id="scale">大農場面對的問題不同</h2>
<p>台灣常見的小塊梯田，和國外的大面積連片農田，本來就是兩種問題。大農場的痛點不是「飛不飛得到」，而是「時間窗口太短」：</p>
<ul>
  <li><strong>作業季集中：</strong>病蟲防治、施肥往往只有短短幾天的有效窗口，單機來不及完成大面積。</li>
  <li><strong>田塊眾多：</strong>一個農場可能同時管理不同生長階段的多個區塊，要同時排不同任務。</li>
  <li><strong>人力稀缺：</strong>靠人逐台起飛、逐台換電，人力成本與失誤都會放大。</li>
</ul>
<div class="callout"><span class="ct">核心差異</span>小農追求「一台機、一個人，把自己的田做好」；大農場追求「一套系統，讓多台機自動把整片田做完」。問題層次不同，解法自然不同。</div>

<h2 id="fleet">機隊與調度怎麼運作</h2>
<p>所謂「機隊管理」不是多買幾台機，而是把<strong>多台機體放在同一個調度平台下分工</strong>：</p>
<ol>
  <li><strong>任務拆分：</strong>把大面積田區切成數個作業區，分配給不同機體，平行作業。</li>
  <li><strong>即時排程：</strong>依電量、位置、剩餘任務與天氣，動態決定下一趟誰飛、飛哪一區。</li>
  <li><strong>分工配備：</strong>有的機體專門測繪監測、有的專門噴灑施肥，平台把兩類任務接成「拍攝→分析→施作」的循環。</li>
</ol>
<div class="tablewrap"><table>
<caption>單機 vs 機隊管理的差異（依主流做法整理，實際規模視場域而定）</caption>
<thead><tr><th>面向</th><th>單機作業</th><th>機隊調度</th></tr></thead>
<tbody>
<tr><td>適合面積</td><td>小至中、田塊集中</td><td>大面積、多區塊</td></tr>
<tr><td>人力配置</td><td>一機一人</td><td>一人監控多機</td></tr>
<tr><td>作業節奏</td><td>飛完一趟再換電</td><td>多機輪替、不中斷</td></tr>
<tr><td>資料流程</td><td>人工整理</td><td>平台自動彙整</td></tr>
</tbody></table></div>

<h2 id="dock">自動機場（機巢）的角色</h2>
<p>機隊要真正省人，關鍵是配上「自動機場」——一個讓無人機降落後自動充電（或換電）、回收資料、再依排程自動起飛的小站。它讓大農場能做到：<strong>定時、定點、無人值守地巡田與作業</strong>，例如每天固定時間自動飛一圈監測長勢，把影像自動送上雲端。對需要高頻掌握整片田狀況的大型農場，這是把「定期監測」變成常態的關鍵設施。</p>

<h2 id="data">數據平台怎麼串起整場</h2>
<p>機體與機場只是硬體，真正讓大農場有效率的是<strong>串在背後的數據平台</strong>：</p>
<ul>
  <li><strong>資料集中：</strong>多台機、多次飛行的影像與施作記錄集中在同一平台，不再散落在各人手機。</li>
  <li><strong>處方圖銜接：</strong>監測影像產生的病蟲或缺肥分區，直接轉成噴灑與施肥的處方圖，再派機執行。</li>
  <li><strong>履歷可追溯：</strong>哪塊田、什麼時候、用了什麼藥肥，都留得到紀錄，供查驗與改善。</li>
</ul>
<div class="callout green"><span class="ct">閉環才是重點</span>國外大農場的價值不在「飛得炫」，而在「拍攝→分析→處方→施作→記錄」形成自動閉環。單獨買機或單獨買平台都不夠，要的是接起來。</div>

<h2 id="borrow">台灣農場可以借鏡什麼</h2>
<p>大面積平整農田的條件，台灣多數農場並不具備，但觀念仍然可以局部借鑑：</p>
<div class="procon">
  <div class="pc pro"><h4>值得借鏡的觀念</h4><ul><li>把資料集中管理，而非各自散落</li><li>建立「監測→施作」的固定循環</li><li>以合作社或服務隊共享機隊與機場，攤平成本</li></ul></div>
  <div class="pc con"><h4>不能直接照搬的部分</h4><ul><li>大面積自動機場的硬體投資高</li><li>台灣地形零碎，大規模航線規劃難度高</li><li>法規與天候窗口仍需就地配合</li></ul></div>
</div>
<div class="callout"><span class="ct">務實結論</span>對台灣的大農場或飛防服務隊，合理的路徑是：先從自動航線與資料集中管理做起，再視業務量逐步加入多機協同，最後才考慮自動機場。不必一步到位。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>台灣也能導入自動機場嗎？</summary><div class="faq-a">技術上可行，但大面積平整農田的條件較少。實務上多由飛防服務隊或大型農企業先行試點，小農可透過共享或外包間接受益。</div></details>
  <details><summary>機隊一定要很多台機才叫機隊？</summary><div class="faq-a">重點不是數量，而是「是否在同一調度與資料平台下分工」。兩三台機若能共享排程與數據，就已經有機隊管理的雛形。</div></details>
  <details><summary>數據平台一定要自己買嗎？</summary><div class="faq-a">不必。多數商用機體與飛防服務已附帶雲端平台，先把既有飛行資料導入集中管理，再評估是否升級。</div></details>
</div>""",
    ("resources-case","台灣農業案例"), ("resources-terms","名詞對照表")),

  "resources-terms": (
    "農用無人機名詞對照表：機體、定位、感測、作業與法規一次看懂",
    "農用無人機常見名詞一次看懂。",
    ["名詞","對照表","術語"], "team",
    [("body","機體類型"),("pos","定位技術"),("sensor","感測與影像"),("ops","作業用語"),("reg","法規用語"),("faq","常見問答")],
    """<p>看農用無人機文章時，常被一堆縮寫與術語卡到：RTK、NDVI、處方圖、變量……這張對照表把最常見的名詞依主題分類，每個用一句話講清楚，供你隨時回頭查。</p>

<h2 id="body">機體類型</h2>
<div class="tablewrap"><table>
<caption>依「機翼構型」分類的常見名詞</caption>
<thead><tr><th>名詞</th><th>一句話解釋</th></tr></thead>
<tbody>
<tr><td>多旋翼</td><td>靠多組旋翼提供升力，可垂直起降、懸停，是農用植保與空拍最常見的構型。</td></tr>
<tr><td>固定翼</td><td>靠機翼產生升力、需跑道或彈射起飛，續航與覆蓋面積大，適合大面積測繪。</td></tr>
<tr><td>垂起複合（VTOL）</td><td>兼具多旋翼的垂直起降與固定翼的長續航，起飛後轉換翼飛，適合大面積巡查。</td></tr>
<tr><td>植保機</td><td>專為噴藥、撒肥設計，大載重、配藥箱與噴灑模組。</td></tr>
<tr><td>測繪機</td><td>搭高解析與光譜感測器，以「拍清楚、量準」為主要任務。</td></tr>
</tbody></table></div>

<h2 id="pos">定位技術</h2>
<div class="tablewrap"><table>
<caption>決定「飛多準、定位多準」的常見名詞</caption>
<thead><tr><th>名詞</th><th>一句話解釋</th></tr></thead>
<tbody>
<tr><td>GPS</td><td>衛星定位，一般空拍與導航的基本定位方式，精度約公尺級。</td></tr>
<tr><td>RTK</td><td>即時動態定位，搭配基地站把定位精度提升到公分等級，是精準農用的關鍵。</td></tr>
<tr><td>PPK</td><td>事後動態定位，飛行後再以基地站資料事後解算定位，適合測繪後處理。</td></tr>
<tr><td>慣性導航（INS）</td><td>在衛星訊號遮蔽時，靠慣性感測器短暫維持姿態與位置推估。</td></tr>
<tr><td>地面控制點（GCP）</td><td>布設於地面、座標已知的標靶，用來校正空拍影像的定位精度。</td></tr>
</tbody></table></div>

<h2 id="sensor">感測與影像</h2>
<div class="tablewrap"><table>
<caption>把作物狀況「拍」成數據的常見名詞</caption>
<thead><tr><th>名詞</th><th>一句話解釋</th></tr></thead>
<tbody>
<tr><td>RGB（可見光）</td><td>一般彩色畫面，看得到的地形、長勢與果實狀況。</td></tr>
<tr><td>多光譜</td><td>拍攝紅外、紅邊等多個波段，用來算植被指數、看缺肥與病害。</td></tr>
<tr><td>熱影像</td><td>感測表面溫度，用來看缺水、灌溉不均與異常升溫。</td></tr>
<tr><td>NDVI</td><td>植被指數，綜合紅光與近紅外訊號，量化植被健康與茂密程度。</td></tr>
<tr><td>正射影像（Orthomosaic）</td><td>把多張空拍拼接、校正後的完整平面影像，是田區的「空拍地圖」。</td></tr>
<tr><td>DSM / 地形建模</td><td>由空拍重建的數字地表模型，可看坡度與高程變化。</td></tr>
</tbody></table></div>

<h2 id="ops">作業用語</h2>
<div class="tablewrap"><table>
<caption>現場作業與任務規劃的常見名詞</caption>
<thead><tr><th>名詞</th><th>一句話解釋</th></tr></thead>
<tbody>
<tr><td>航線</td><td>預先規劃好的飛行路徑，讓無人機按計畫自主飛行。</td></tr>
<tr><td>噴幅</td><td>一次噴灑能涵蓋的有效寬度，決定航線間距與效率。</td></tr>
<tr><td>變量施作</td><td>依田區狀況動態調整用藥、用肥量，而非整片同量。</td></tr>
<tr><td>處方圖</td><td>標示「哪裡該多施、哪裡少施或不施」的分區地圖，指引變量作業。</td></tr>
<tr><td>斷航續飛</td><td>因電量或其他中斷返航後，回到中斷處接續完成任務。</td></tr>
<tr><td>返航點 / RTL</td><td>低電量或訊號異常時自動返回的預設位置與高度。</td></tr>
</tbody></table></div>

<h2 id="reg">法規用語</h2>
<div class="tablewrap"><table>
<caption>飛行合規相關的常見名詞（實務請以主管機關現行公告為準）</caption>
<thead><tr><th>名詞</th><th>一句話解釋</th></tr></thead>
<tbody>
<tr><td>機體登記</td><td>達一定重量以上的無人機需向主管機關辦理註冊登記並標示辨識資訊。</td></tr>
<tr><td>操作證照</td><td>操作達一定級別或商用用途無人機所需的合格證明，含學科與術科。</td></tr>
<tr><td>禁飛區</td><td>如機場周邊、政府與敏感設施等，未經許可禁止飛行的區域。</td></tr>
<tr><td>限制區</td><td>需申請或符合條件（如人群、夜航）才能飛行的區域。</td></tr>
<tr><td>最大起飛重量（MTOW）</td><td>含電池與載重在內的起飛總重，是法規分級的重要依據。</td></tr>
</tbody></table></div>
<div class="callout"><span class="ct">提醒</span>法規名詞對應的具體門檻、級別與罰則會隨主管機關公告調整，本文只解釋「這個詞是什麼」，實際合規請以交通部民用航空局現行規定為準。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>一定要把這些名詞都背起來嗎？</summary><div class="faq-a">不必死背。遇到不懂的詞再回來查這張表即可；實際作業時，機體說明書與地面站介面才是你最常看到的名詞。</div></details>
  <details><summary>RTK 和 PPK 差在哪？</summary><div class="faq-a">兩者都靠基地站提升定位精度，差別在「即時」與「事後」：RTK 飛行當下就給高精定位，PPK 飛完後再事後解算。測繪後處理常用 PPK，即時作業常用 RTK。</div></details>
  <details><summary>NDVI 數字越高越好嗎？</summary><div class="faq-a">不盡然。它反映光譜健康度，須配合物候、品種與拍攝條件解讀，重點是「同田前後比對」而非單看絕對值。</div></details>
</div>""",
    ("resources-oversea","國外大型農場做法"), ("resources","案例資源")),
})

# 無人機技術 支柱新增條目（tech）
TITLE.update({
  "tech-nav": "定位、避障與導航：RTK 公分級定位與飛行安全的底子",
  "tech-sensors": "多光譜、熱影像拍攝：把作物狀況「拍」成數據的第一步",
  "tech-ai": "AI 辨識病蟲與缺肥：讓影像輔助人工判讀",
  "tech-cloud": "雲端資料處理：上雲、生成處方圖、回傳機具",
  "tech-autopilot": "自動航線與任務規劃：從手飛走向任務",
  "tech-variable": "變量施作與處方圖：哪裡有問題才處理哪裡",
  "tech-fleet": "機隊與自動機巢：多機協同與無人值守的下一步",
})

ART.update({
  "tech-nav": (
    "定位、避障與導航：RTK 公分級定位與飛行安全的底子",
    "RTK、慣性導航與避障感測，決定精準度與安全性。",
    ["定位","RTK","避障"], "lin",
    [("pos","先搞清楚定位怎麼來"),("rtk","RTK 與慣性導航"),("avoid","避障感測怎麼分工"),("shield","訊號遮蔽與實務風險"),("faq","常見問答")],
    """<h2 id="pos">先搞清楚：定位怎麼來</h2>
<p>無人機在天上「知道自己在哪」，靠的是衛星定位加上機上的慣性測量元件。一般消費級 GPS 只能做到數公尺等級，對噴藥來說夠用，但對測繪、變量施作與重複航線來說就太粗。農用講求「每一條航線都飛在同一條線上」，定位精度直接決定資料能不能比對、施作會不會重疊或漏區。</p>
<div class="callout"><span class="ct">為什麼精度這麼關鍵</span>重複拍攝要前後疊圖、變量施作要對準處方圖、勘測要量準面積——這些都要求飛機「每次都回到同一個座標」。差一兩公尺，資料就對不上。</div>

<h2 id="rtk">RTK 與慣性導航</h2>
<p>RTK（即時動態定位）透過基地台與流動站之間的差分修正，把一般 GPS 的誤差壓到公分等級。農用常見做法是在田邊架設基地台，或使用網路 RTK 服務。它不是「更準的 GPS」，而是「一邊飛一邊修正」的定位模式。</p>
<ul>
  <li><strong>基地台模式：</strong>在已知位置架設基地台，飛機與它對差，精度穩定但需攜帶基地台設備。</li>
  <li><strong>網路 RTK：</strong>透過電信網路接收差分訊號，免去架台，適合機動出勤，需行動訊號涵蓋。</li>
  <li><strong>慣性導航（IMU）：</strong>在訊號短暫中斷時靠陀螺儀與加速度計推算姿態與位置，是定位的「備胎」，但誤差會隨時間累積，不能長時間單靠它。</li>
</ul>
<div class="tablewrap"><table>
<caption>常見定位方式比較（依主流規格整理，實際以設備與訊號環境為準）</caption>
<thead><tr><th>定位方式</th><th>精度等級</th><th>典型用途</th><th>限制</th></tr></thead>
<tbody>
<tr><td>一般 GPS</td><td>數公尺</td><td>休閒空拍、概略飛行</td><td>不適合測繪與重複航線</td></tr>
<tr><td>RTK 差分</td><td>公分级</td><td>測繪、變量施作、重複監測</td><td>需基地台或網路訊號</td></tr>
<tr><td>慣性導航</td><td>短期推算</td><td>訊號暫時遮蔽時的備援</td><td>長時間誤差累積</td></tr>
</tbody></table></div>

<h2 id="avoid">避障感測怎麼分工</h2>
<p>避障不是單一感測器，而是多種感測器分工看不同方向與距離。農用機常在樹梢、電線、棚架之間飛，單靠人眼看圖傳不夠。</p>
<div class="tablewrap"><table>
<caption>常見避障感測方式（依主流規格整理）</caption>
<thead><tr><th>感測方式</th><th>原理</th><th>擅長</th><th>弱點</th></tr></thead>
<tbody>
<tr><td>視覺（立體相機）</td><td>比對兩眼畫面算距離</td><td>辨認物體形狀、近距離</td><td>光線不足或純色表面判讀差</td></tr>
<tr><td>雷射測距（LiDAR）</td><td>發射雷射量反射時間</td><td>精準距離、夜間與地形</td><td>成本高、細小物體易漏</td></tr>
<tr><td>超音波</td><td>聲波測距</td><td>貼地高度、低空作業</td><td>距離短、遇草叢散射</td></tr>
</tbody></table></div>
<p>實際機種常把「前後下」多方向組合：下方感測器顧貼地高度，前後方顧樹與電線，上方顧高壓電線與棚架。重點是：避障是「降風險」不是「零風險」，細電線、細鐵絲仍可能漏判。</p>

<h2 id="shield">訊號遮蔽與實務風險</h2>
<p>台灣農地常在山坡、果園、大樹與建物旁，RTK 與 GPS 訊號容易被擋。遮蔽後飛機會轉靠慣性導航撐一下，但撐不久。實務上要預先處理：</p>
<ul class="check">
  <li>起飛前確認定位收訊星數與 RTK 固定解狀態，未達定位不硬飛</li>
  <li>果園、林帶、建物夾縫等遮蔽區，先觀察訊號再決定航線</li>
  <li>基地台架在空曠高點，避免被樹與屋頂遮</li>
  <li>設定安全返航高度，高於沿途障礙物再返程</li>
  <li>訊號異常時以人為操控為主，不自動進入遮蔽區深處</li>
</ul>
<div class="callout green"><span class="ct">務實提醒</span>避障與定位都會受環境影響。與其買最貴的感測器，不如先摸清你的田有哪些遮蔽與障礙，把航線與返航路線規劃在訊號好、看得清楚的地方。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>一定要上 RTK 嗎？</summary><div class="faq-a">如果只是偶爾空拍風景，一般 GPS 可能夠；但要做測繪、重複監測或變量施作，RTK 的公分級定位是基本要求。</div></details>
  <details><summary>訊號被樹擋到會怎樣？</summary><div class="faq-a">短暫遮蔽靠慣性導航撐，但誤差會逐漸放大；長時間遮蔽可能定位漂移、偏離航線，應避免讓飛機鑽進長期遮蔽區。</div></details>
  <details><summary>有避障就不會撞到電線？</summary><div class="faq-a">不能這麼說。多方向避障能大幅降低撞擊機率，但細電線、細鐵絲仍可能漏判，航線規劃與人為監看不能省。</div></details>
</div>""",
    ("tech-power","電池與動力系統：續航、換電與保養實務"), ("tech-sensors","多光譜、熱影像拍攝")),

  "tech-sensors": (
    "多光譜、熱影像拍攝：把作物狀況「拍」成數據的第一步",
    "把作物狀況「拍」成數據，是精準農業的第一步。",
    ["感測","多光譜","熱影像"], "lin",
    [("three","RGB、多光譜、熱影像差在哪"),("how","多光譜怎麼讀"),("thermal","熱影像看什麼"),("tips","拍攝要點"),("faq","常見問答")],
    """<h2 id="three">RGB、多光譜、熱影像差在哪</h2>
<p>「拍照」在農業裡不是只拍好看的畫面，而是拍不同波段的光線訊號。人眼看到的可見光（RGB）只是其中一種；多光譜拍肉眼看不到的紅外光，熱影像拍物體散發的熱。三種各看一件事，不能互相取代。</p>
<div class="tablewrap"><table>
<caption>三類拍攝方式比較（依主流規格整理，實際以感測器規格為準）</caption>
<thead><tr><th>方式</th><th>拍的是</th><th>能看出</th><th>典型用途</th></tr></thead>
<tbody>
<tr><td>可見光 RGB</td><td>人眼可見顏色</td><td>地形、長勢外觀、明顯病斑</td><td>勘測、面積、一般監測</td></tr>
<tr><td>多光譜</td><td>紅外等特定波段</td><td>植被指數、葉綠素變化、早期缺肥</td><td>生長監測、病蟲早期偵測</td></tr>
<tr><td>熱影像</td><td>表面溫度</td><td>缺水、灌溉不均、設備熱點</td><td>灌溉管理、逆境監測</td></tr>
</tbody></table></div>

<h2 id="how">多光譜怎麼讀</h2>
<p>多光譜的關鍵，是把不同波段組合成一個「植被指數」。最常見的是 NDVI：用近紅外與紅光的反射差，算出一個 0 到 1 之間的值。健康植被反射近紅外多，值偏高；受脅、稀疏或枯損的植被值偏低。</p>
<div class="callout"><span class="ct">重點不是絕對值</span>NDVI 的價值在「同一塊田、前後幾次」的相對變化，而不是跨田比高低。先把固定航線拍下來，圖層之間才能比。</div>
<p>另一個常見波段是「紅邊」，對葉綠素變化很敏感，常用來提早判讀缺肥與老化。多光譜相機通常一次拍出多個波段，後製時再疊算指數。</p>

<h2 id="thermal">熱影像看什麼</h2>
<p>熱影像量的是冠層表面溫度。作物缺水時氣孔關閉、散熱變差，葉面溫度會上升；灌溉不均的田，溫度圖會一塊一塊。熱影像因此特別適合「找哪裡缺水」，而不是「數長得好不好」。</p>
<ul>
  <li><strong>缺水判讀：</strong>局部溫度偏高，往往是水分供應不足的訊號。</li>
  <li><strong>灌溉均勻度：</strong>整片溫度參差，可能是澆灌設施不均或堵塞。</li>
  <li><strong>設備熱點：</strong>套用在太陽能或馬達巡檢時，異常升溫代表故障。</li>
</ul>
<div class="callout"><span class="ct">熱影像的季節限制</span>溫度受日照、風速與時間影響很大，最好固定在相似天候與時段拍攝，並避免正午過熱造成判讀失真。</div>

<h2 id="tips">拍攝要點</h2>
<ul class="check">
  <li>固定飛行高度與航線，前後資料才可比</li>
  <li>挑光線穩定、雲層少的時段，避免陰影干擾</li>
  <li>留足前後、左右重疊，後製拼接才不破圖</li>
  <li>多光譜與熱影像拍攝前先做白場／溫度校準（依設備說明）</li>
  <li>空拍標出的異常區，務必到田間實地確認</li>
</ul>
<div class="callout green"><span class="ct">起步建議</span>不必一次上全套。可先從可見光空拍建立地形與長勢底圖，有明確監測需求再加入多光譜或熱影像；工具要貼問題，而不是為了買而買。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>多光譜跟一般空拍差多少錢？</summary><div class="faq-a">多光譜與熱影像雲台通常比一般空拍昂貴，且需對應後製軟體。建議先評估自己的監測頻率與問題，再決定是自購還是委外拍攝。</div></details>
  <details><summary>NDVI 圖一片紅就是有病？</summary><div class="faq-a">不是。顏色圖只是指數的視覺化，可能受品種、物候、裸土與陰影影響。務必對照田間實況，把指數當「線索」而非「診斷書」。</div></details>
  <details><summary>熱影像可以晚上拍嗎？</summary><div class="faq-a">夜間溫差小、訊號弱，多數作物監測仍以白天相似條件拍攝為宜；具體時機依感測器規格與監測目的調整。</div></details>
</div>""",
    ("tech-nav","定位、避障與導航"), ("tech-ai","AI 辨識病蟲與缺肥")),

  "tech-ai": (
    "AI 辨識病蟲與缺肥：讓影像輔助人工判讀",
    "用影像辨識找出雜草、病蟲與缺肥，輔助人工判讀。",
    ["AI","影像辨識","病蟲害"], "lin",
    [("what","AI 在農業做什麼"),("scope","病蟲、雜草、缺肥怎麼分"),("line","AI 與人工的界線"),("flow","導入步驟"),("faq","常見問答")],
    """<h2 id="what">AI 在農業影像裡做什麼</h2>
<p>AI 影像辨識的核心，是把「一張張照片」變成「標記好位置與類別的圖層」：哪裡有雜草、哪裡有疑似病斑、哪裡長勢偏弱。它不直接幫你決定怎麼噴藥，而是先把大面積影像裡「值得人看一眼」的地方圈出來，縮小人工判讀的範圍。</p>
<div class="callout"><span class="ct">它本質是「分類與定位」</span>常見兩種任務：分類（這片長得健不健康）與偵測（這一叢是不是某種病蟲或雜草）。後者對田間處置更實用，因為它標了位置。</div>

<h2 id="scope">病蟲、雜草、缺肥怎麼分</h2>
<div class="tablewrap"><table>
<caption>常見 AI 辨識應用面向（依主流技術整理，實際成效依訓練資料而異）</caption>
<thead><tr><th>面向</th><th>輸入</th><th>AI 產出</th><th>價值</th></tr></thead>
<tbody>
<tr><td>病蟲害</td><td>高解析 RGB／多光譜影像</td><td>疑似病斑、蟲害位置標記</td><td>縮小人工巡查範圍</td></tr>
<tr><td>雜草</td><td>苗期 RGB 影像</td><td>作物與雜草分離、位置圖</td><td>輔助局部除草或點噴</td></tr>
<tr><td>缺肥／逆境</td><td>多光譜植被指數</td><td>長勢分區圖</td><td>提示可能缺肥區塊</td></tr>
</tbody></table></div>
<p>這三類的難度不同：雜草與作物在苗期顏色接近、病蟲種類繁多，訓練資料是否貼近當地品種與病蟲，決定準確度。</p>

<h2 id="line">AI 與人工的界線</h2>
<p>這是最需要講清楚的一環。AI 是「輔助判讀」，不是「自動開藥」：</p>
<div class="procon">
  <div class="pc pro"><h4>AI 擅長</h4><ul><li>快速掃過大面積影像、圈出可疑區</li><li>把重複性的目視工作自動化</li><li>留下可追溯的數位紀錄</li></ul></div>
  <div class="pc con"><h4>仍需人工</h4><ul><li>確認疑似病蟲是否真的是該病蟲</li><li>決定用藥、用肥與處置方式</li><li>對新型、罕見狀況下判斷</li></ul></div>
</div>
<div class="callout"><span class="ct">為什麼不能全交給 AI</span>田間環境複雜：品種、時期、天候與鏡頭都會干擾辨識。把 AI 圈出的可疑區直接拿去噴藥，可能噴錯、噴多。正確流程是「AI 初篩 → 人工確認 → 再決定處置」。</div>

<h2 id="flow">導入步驟</h2>
<ol>
  <li><strong>先有乾淨影像：</strong>固定航線、解析度夠、重疊充足，辨識才有原料。</li>
  <li><strong>選對平台或模型：</strong>多數雲端平台已內建病蟲、雜草判讀，不必從零訓練。</li>
  <li><strong>人工抽驗：</strong>拿 AI 標記結果與田間實況比對，了解誤判型態。</li>
  <li><strong>閉環修正：</strong>把錯判案例回饋，持續提升對當地田塊的適配。</li>
</ol>
<div class="callout green"><span class="ct">務實看法</span>對多數農友，最務實的起點不是「自己訓練 AI」，而是用成熟雲端平台做影像初篩，再由有經驗的人或農改場人員確認。AI 省下的是「找」的力氣，不是「判斷」的責任。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>AI 抓出來的病就一定是病？</summary><div class="faq-a">不盡然。辨識結果是「高度疑似」，可能把損傷、蔭影或雜草誤判為病斑。一定要到現場確認，再決定處置。</div></details>
  <details><summary>一定要自己蒐集照片訓練模型？</summary><div class="faq-a">多數使用者不需要。現成平台已整合常見病蟲與雜草模型，先拿現成的跑，有特殊需求再談客製訓練。</div></details>
  <details><summary>AI 能直接告訴我噴什麼藥？</summary><div class="faq-a">不建議這樣用。用藥選擇牽涉病蟲種類、作物時期與法規安全，應由人工與專家把關，AI 只負責標位置。</div></details>
</div>""",
    ("tech-sensors","多光譜、熱影像拍攝"), ("tech-cloud","雲端資料處理")),

  "tech-cloud": (
    "雲端資料處理：上雲、生成處方圖、回傳機具",
    "拍攝資料上雲、生成處方圖，再回傳給機具作業。",
    ["雲端","資料流","處方圖"], "lin",
    [("flow","一次完整的資料流"),("upload","上雲與拼接"),("prescription","處方圖怎麼生成"),("back","回傳機具作業"),("faq","常見問答")],
    """<h2 id="flow">一次完整的資料流</h2>
<p>精準農業不是「拍了照片就結束」，而是一條從天上回到田裡的資料流：飛機拍下影像 → 資料上雲 → 後製拼接與指數計算 → 生成處方圖 → 回傳給地面站 → 機具依圖施作。每一環接得上，資料才有意義。</p>
<div class="callout"><span class="ct">閉環的概念</span>「拍攝 → 分析 → 處置 → 再拍攝」形成循環：這次噴了什麼、效果如何，下次影像再驗證。斷在任何一環，都只是存檔，不是管理。</div>

<h2 id="upload">上雲與拼接</h2>
<p>空拍回來的是幾百上千張重疊照片，不能直接看。雲端平台的第一個工作是「拼接」：把重疊影像算成一張完整田區正射影像，並套上空間座標。</p>
<ul>
  <li><strong>拼接：</strong>比對相鄰照片的共同特徵，縫成連續底圖。</li>
  <li><strong>地理校正：</strong>把影像對上真實座標，後續量測與疊圖才有意義。</li>
  <li><strong>指數圖層：</strong>多光譜資料在此算成 NDVI 等圖層，疊在底圖上。</li>
</ul>
<p>上雲的好處是運算不必在自己電腦跑，且資料集中、隨手可查。缺點是需要網路與平台費用，且要注意資料歸屬與隱私。</p>

<h2 id="prescription">處方圖怎麼生成</h2>
<p>處方圖（也叫變量地圖）是把「哪裡該噴多少」畫成一張圖：不同分區對應不同施作量。它通常由植被指數或診斷結果分區而來，而不是整張田同一個數字。</p>
<div class="tablewrap"><table>
<caption>資料處理常見環節（依主流雲端平台整理，實際介面以廠商為準）</caption>
<thead><tr><th>環節</th><th>做什麼</th><th>產出</th></tr></thead>
<tbody>
<tr><td>拼接校正</td><td>把照片縫成完整底圖</td><td>正射影像</td></tr>
<tr><td>指數計算</td><td>多光譜轉成植被指數</td><td>NDVI 等圖層</td></tr>
<tr><td>分區</td><td>依指數把田切成數個等級</td><td>管理分區</td></tr>
<tr><td>處方圖</td><td>把分區對應到施作量</td><td>可下載的處方檔</td></tr>
</tbody></table></div>

<h2 id="back">回傳機具作業</h2>
<p>處方圖要「喂得進機具」才有用。流程是：雲端匯出處方檔 → 匯入地面站或機具 → 機具在飛行時依座標對應區塊、動態調整施藥或施肥量。對不上格式，圖就只是圖。</p>
<ul class="check">
  <li>確認平台匯出格式與你的機具地面站相容</li>
  <li>處方圖座標系統與航線定位一致（最好同為 RTK）</li>
  <li>首次導入先小區塊測試，確認對位與施量</li>
  <li>保留每次處方與施作紀錄，供後續比對</li>
</ul>
<div class="callout green"><span class="ct">務實提醒</span>資料流的價值在「接得上」。與其追求最完整的平台，不如先打通你現有機具與雲端的一條最短路：拍一次、處理一次、噴一次、再拍一次驗收。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>一定要用雲端嗎？自己電腦不能處理？</summary><div class="faq-a">技術上可以，但拼接與指數運算吃資源，且多人協作與行動存取不便。多數農用情境以雲端平台較順手，自處理適合進階使用者。</div></details>
  <details><summary>處方圖下載就能噴？</summary><div class="faq-a">還要確認格式相容、座標一致，並先小區測試對位。直接全田下場有重噴或漏噴風險。</div></details>
  <details><summary>田區資料上雲安全嗎？</summary><div class="faq-a">選擇具隱私政策的平台，了解資料歸屬與是否用於訓練。敏感田界或產銷資料，挑把關明確的服務。</div></details>
</div>""",
    ("tech-ai","AI 辨識病蟲與缺肥"), ("tech-autopilot","自動航線與任務規劃")),

  "tech-autopilot": (
    "自動航線與任務規劃：從手飛走向任務",
    "從「手飛」走向「任務」，航線、返航與斷航續飛。",
    ["自動飛行","航線","返航"], "lin",
    [("why","為什麼要用自動航線"),("param","航線規劃的關鍵參數"),("return","返航邏輯"),("resume","斷航續飛"),("faq","常見問答")],
    """<h2 id="why">為什麼要用自動航線</h2>
<p>手飛靠人眼與手感，小面積還行，面積一大就容易重複、漏區、疲勞。自動航線是把「飛哪、飛多高、飛多快、間距多少」事先規劃好，飛機照表操課。好處是一致、可重複、可記錄——每一塊田的每一條航線都能存檔、重飛。</p>
<div class="callout"><span class="ct">自動化的本質</span>不是把飛手變沒用，而是把人從「持續操控」解放出來，專注在監看異常與安全。規劃得好，新手也能飛出接近老手的均勻度。</div>

<h2 id="param">航線規劃的關鍵參數</h2>
<ul>
  <li><strong>作業邊界：</strong>先圈定實際田塊範圍，避開空地、水道與鄰田。</li>
  <li><strong>航線間距：</strong>依噴幅或拍攝重疊決定，太密浪費、太疏漏區。</li>
  <li><strong>飛行高度：</strong>噴藥顧霧滴落點、測繪顧解析度，目的不同高度不同。</li>
  <li><strong>飛行速度：</strong>影響單位面積施藥量或拍攝間隔，需與流量對應。</li>
  <li><strong>轉彎補償：</strong>轉角處的重疊與爬升，避免重噴或漏噴。</li>
</ul>
<div class="tablewrap"><table>
<caption>兩類任務的航線重點（依主流規格整理，實際以機型為準）</caption>
<thead><tr><th>參數</th><th>噴灑任務</th><th>測繪拍攝任務</th></tr></thead>
<tbody>
<tr><td>主要目標</td><td>均勻施作、控制用量</td><td>清晰拼接、解析度足</td></tr>
<tr><td>高度考量</td><td>霧滴落點與飄移</td><td>地面解析度</td></tr>
<tr><td>間距依據</td><td>有效噴幅</td><td>前後左右重疊率</td></tr>
<tr><td>速度影響</td><td>單位面積施藥量</td><td>相鄰照片間距</td></tr>
</tbody></table></div>

<h2 id="return">返航邏輯</h2>
<p>返航是安全的最後一道閘。常見觸發條件與邏輯要在地面站預先設好，而不是臨場反應：</p>
<ul>
  <li><strong>低電量返航：</strong>設剩餘電量或電壓門檻，一到就自動返航。</li>
  <li><strong>訊號失控返航：</strong>圖傳或遙控訊號中斷，按預設路徑與高度返航。</li>
  <li><strong>返航高度：</strong>預設高於沿途樹梢與電線，避免返程撞障礙。</li>
</ul>
<div class="callout"><span class="ct">返航高度要先想</span>很多人設定返航高度只顧「飛得起來」，卻沒考慮返程路上有沒有樹與電線。返航路線等於另一條航線，事前要規劃。</div>

<h2 id="resume">斷航續飛</h2>
<p>作業中途若因換電、低電量或手動暫停而中斷，「斷航續飛」讓飛機從上次沒飛完的地方接續，而不是從頭再飛一次。這對大面積噴藥尤其重要：換一次電就重飛整片，浪費藥也浪費時間。</p>
<ul class="check">
  <li>起飛前確認續飛功能與任務暫存設定</li>
  <li>換電後確認定位回到固定解再續飛</li>
  <li>續飛前目視確認起點附近無障礙與人</li>
  <li>記錄中斷點與續飛點，事後核對施作完整性</li>
</ul>
<div class="callout green"><span class="ct">務實提醒</span>自動航線把「操作」變「規劃」。與其急著飛大面積，不如先在小區塊把參數、返航與續飛都跑順一次，再放大到全田。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>自動飛行時飛手可以放著不管？</summary><div class="faq-a">不行。自動航線減輕操控，但飛手仍要全程監看電量、圖傳與環境，隨時準備接手緊急狀況。</div></details>
  <details><summary>斷航續飛每次都接得上？</summary><div class="faq-a">前提是定位穩定、任務有正確暫存。訊號飄移或中斷點記錄不清時，應人工確認後再續飛。</div></details>
  <details><summary>航線間距越密越均勻越好？</summary><div class="faq-a">太密會重噴、浪費且耗電。間距應對照有效噴幅或重疊需求，先小區試飛量出合適值。</div></details>
</div>""",
    ("tech-cloud","雲端資料處理"), ("tech-variable","變量施作與處方圖")),

  "tech-variable": (
    "變量施作與處方圖：哪裡有問題才處理哪裡",
    "依處方圖動態調整施藥施肥量，哪裡有問題才處理哪裡。",
    ["變量施作","處方圖","精準農業"], "lin",
    [("what","什麼是變量施作"),("why","為什麼要分區下藥"),("how","處方圖怎麼落地"),("limit","現實限制"),("faq","常見問答")],
    """<h2 id="what">什麼是變量施作</h2>
<p>傳統施作是「整塊田同一個量」，變量施作（Variable Rate Application）則是「依地圖分區給不同量」：長勢弱、疑似缺肥的區塊多給一點，長勢均勻、看起來健康的區塊少給或不給。核心觀念是——田本來就不均勻，藥肥也不該齊頭式分配。</p>
<div class="callout"><span class="ct">一句話理解</span>變量施作把「整片一樣」改成「對症下藥」。它省的不只是成本，更是把藥肥用在真正需要的地方。</div>

<h2 id="why">為什麼要分區下藥下肥</h2>
<ul>
  <li><strong>減少浪費：</strong>健康區塊不需要重複施作，省下藥與肥。</li>
  <li><strong>降低環境負擔：</strong>少噴不必要的藥，鄰田與殘留風險也隨之下降。</li>
  <li><strong>對症處理：</strong>問題區被標出來，可以針對性處理，而不是一概而論。</li>
</ul>
<div class="tablewrap"><table>
<caption>齊頭式與變量式施作比較（概念整理，實際效益依田況而異）</caption>
<thead><tr><th>面向</th><th>齊頭式（整田同量）</th><th>變量式（依圖分區）</th></tr></thead>
<tbody>
<tr><td>施作依據</td><td>經驗統一給量</td><td>處方圖分區給量</td></tr>
<tr><td>成本</td><td>用藥用肥固定</td><td>健康區可減量</td></tr>
<tr><td>均勻度</td><td>易重噴或漏區</td><td>對位準、可追溯</td></tr>
<tr><td>先決條件</td><td>低門檻</td><td>需影像、處方圖與相容機具</td></tr>
</tbody></table></div>

<h2 id="how">處方圖怎麼落地</h2>
<p>變量施作要成立，需要三個環節接起來：</p>
<ol>
  <li><strong>診斷：</strong>用多光譜或熱影像把田分成幾個管理等級。</li>
  <li><strong>成圖：</strong>在雲端或地面站把等級對應到施作量，匯出處方檔。</li>
  <li><strong>執行：</strong>機具依座標在不同區塊自動調整噴量或施肥量。</li>
</ol>
<p>關鍵在「對位」：處方圖的座標必須和飛機的 RTK 定位對得上，否則圖上說「這塊多噴」，飛機卻噴到隔壁去了。第一次導入一定要小區測試。</p>

<h2 id="limit">現實限制</h2>
<div class="procon">
  <div class="pc pro"><h4>適合變量施作的情境</h4><ul><li>大面積、長勢不均的田塊</li><li>已有影像監測與雲端處理</li><li>機具支援處方圖匯入</li></ul></div>
  <div class="pc con"><h4>要面對的門檻</h4><ul><li>前製成本：影像、平台、定位精度</li><li>機具相容性：格式與對位</li><li>判讀責任：仍需人工確認處置</li></ul></div>
</div>
<div class="callout green"><span class="ct">務實路徑</span>不必一次到位。可先從「把田分成兩三個等級、重點區加強處理」開始，累積影像與施作紀錄後，再逐步走向更細的變量施作。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>小農田值得做變量施作嗎？</summary><div class="faq-a">面積小時，前製成本相對高，可先從重點區監測與局部處理做起，或與合作社、服務隊共享平台。</div></details>
  <details><summary>處方圖一定能省藥？</summary><div class="faq-a">多數情境在健康區減量有助省藥，但前提是診斷與對位正確。先小區實證、量到實際節省，再擴大。</div></details>
  <details><summary>舊機能跑變量施作嗎？</summary><div class="faq-a">要看是否支援處方圖匯入與變量控制。機具不相容時，可考慮升級地面站或委由支援的服務隊施作。</div></details>
</div>""",
    ("tech-autopilot","自動航線與任務規劃"), ("tech-fleet","機隊與自動機巢")),

  "tech-fleet": (
    "機隊與自動機巢：多機協同與無人值守的下一步",
    "多機協同與自動機場，下一代省工農業的方向。",
    ["機隊","自動機場","協同"], "lin",
    [("now","多機調度現在哪"),("dock","自動機巢是什麼"),("collab","多機怎麼分工"),("gate","門檻與導入建議"),("faq","常見問答")],
    """<h2 id="now">多機調度現在哪</h2>
<p>單台機覆蓋面積有限，大型農場或專業飛防隊常同時出動多台機。所謂「機隊」不是買好幾台擺著，而是用一套調度平台把任務拆分給不同機：哪台負責哪一區、什麼時間飛、電池夠不夠，都在同一個後台排程。真正的難點不在飛，而在「分工與不重疊」。</p>
<div class="callout"><span class="ct">從單機到機隊的關鍵</span>不是硬體疊加，而是調度與資料自動化：多台機的航線、電池、任務進度要即時整合，才不會兩台飛同一块、或漏了某區。</div>

<h2 id="dock">自動機巢是什麼</h2>
<p>自動機巢（自動機場／Dock）是一個讓無人機自己「回家、充電、再出發」的小站。無人機完成任務降落後，機巢負責充電或換電、回收資料、依雲端排程再次起飛，中間不必人工搬電池。它把「巡田」從「人想到才飛」變成「固定每天自動飛」。</p>
<figure style="margin:18px 0"><img src="img/drone_team_collaboration.webp" alt="無人機團隊協作" style="width:100%;max-width:760px;margin:0 auto;border-radius:10px" loading="lazy"><figcaption style="margin-top:8px;font-size:14px;color:#667;text-align:center">多機協同與自動機巢的核心，是把起飛、換電、資料回傳串成一條自動化流程。</figcaption></figure>
<ul>
  <li><strong>自動充電／換電：</strong>解決人工換電的人力瓶頸。</li>
  <li><strong>資料自動回傳：</strong>影像上雲後再排下一次任務。</li>
  <li><strong>定時定點巡田：</strong>高頻監測變得可行，病蟲與缺水掌握更即時。</li>
</ul>

<h2 id="collab">多機怎麼分工</h2>
<p>常見的分工方式有兩種：一種是「同任務分區」，多台機一起把一大塊田切成數區同時噴，縮短當日作業時間；另一種是「異任務協同」，一台測繪、一台噴藥，資料在雲端接起來。無論哪種，都需要清楚的航線邊界與任務交接。</p>
<div class="tablewrap"><table>
<caption>多機協同常見模式（依主流做法整理，實際以平台為準）</caption>
<thead><tr><th>模式</th><th>做法</th><th>適合情境</th></tr></thead>
<tbody>
<tr><td>分區並行</td><td>大田切數區，多機同時作業</td><td>趕時效、大面積噴藥</td></tr>
<tr><td>異任務協同</td><td>測繪機與噴藥機分工</td><td>監測＋施作閉環</td></tr>
<tr><td>機巢輪飛</td><td>單機定時自動出勤</td><td>高頻小面積巡田</td></tr>
</tbody></table></div>

<h2 id="gate">門檻與導入建議</h2>
<p>自動機巢與機隊聽起來诱人，但導入門檻不低：</p>
<div class="procon">
  <div class="pc pro"><h4>價值點</h4><ul><li>省人力、監測更即時</li><li>資料自動化、決策更連續</li><li>大面積與果園高頻需求有感</li></ul></div>
  <div class="pc con"><h4>現實門檻</h4><ul><li>機巢與平台投資高</li><li>場地、供電、網路要建置</li><li>法規與維運成熟度仍在成長</li></ul></div>
</div>
<div class="callout green"><span class="ct">務實導入順序</span>對多數農友，先把「自動航線＋雲端資料＋斷航續飛」跑順，再評估要不要上機巢。小農不必獨自投資，可以透過合作社或服務隊共享機場，把成本攤開。</div>

<h2 id="faq">常見問答</h2>
<div class="faq">
  <details><summary>買好幾台機就是機隊了嗎？</summary><div class="faq-a">不是。沒有調度平台與任務拆分，多台機只是各自為政，容易重疊或漏區。機隊的核心是「協同排程」。</div></details>
  <details><summary>自動機巢現在成熟可用嗎？</summary><div class="faq-a">已有商用產品，但供電、網路、維運與法規仍在演進，導入前建議先實證一段時間，再規模化。</div></details>
  <details><summary>小農有機會用到機巢嗎？</summary><div class="faq-a">透過合作社、產銷班或服務隊共享機場，是讓小農也能用到高頻自動巡田、而不必獨自重投資的方式。</div></details>
</div>""",
    ("tech-variable","變量施作與處方圖"), ("tech","無人機技術")),
})

# ============================================================
# 法務與靜態頁
# ============================================================
def privacy_page():
    return static_legal("隱私政策","農翔誌隱私政策：本站蒐集哪些資訊、如何使用與保護。","privacy",[
     ("p","農翔誌（LipoSow）重視你的隱私。本政策說明我們在提供知識內容時，蒐集哪些資訊、如何使用，以及你的權利。本網站為示範知識庫（Example Domain）。"),
     ("h","我們蒐集什麼"),
     ("p","瀏覽本站時，伺服器與流量服務（如 CDN）可能記錄標準的存取紀錄，例如 IP、瀏覽器類型與瀏覽頁面，用於安全與效能。若你透過聯絡表單留下姓名與 Email，我們僅用於回覆你的諮詢，不會販售或轉交第三方。"),
     ("h","我們如何使用"),
     ("ul",["回覆你的聯絡與諮詢","維護網站安全與效能分析","持續改善內容品質"]),
     ("h","Cookie 與第三方"),
     ("p","本站主要為靜態內容，無廣告與追蹤系統。若採用第三方字型或分析服務，將以提供者之隱私政策為準。"),
     ("h","你的權利"),
     ("p","你可以要求查閱、更正或刪除你留下的個人資料。如需行使權利，請透過聯絡頁面與我們聯繫。"),
    ])

def disclaimer_page():
    return static_legal("免責聲明","農翔誌免責聲明：內容僅供參考，實際作業請遵循法規並諮詢專業。","disclaimer",[
     ("p","農翔誌（LipoSow）以繁體中文整理農業與無人機相關知識，目的在於資訊分享與教育。請你理解並同意以下聲明："),
     ("h","內容僅供參考"),
     ("p","本站內容（含法規、規格、流程與數據）基於可查證的公開資料與實務經驗整理，可能因時空、地區與個別情況而異。本站不提供個別農田診斷、購機推薦、報價或法律意見。"),
     ("h","以主管機關公告為準"),
     ("p","涉及法規、證照、飛行區域與農藥管理之資訊，請一律以交通部民用航空局及相關主管機關之現行公告為準。本站整理僅供參考，不構成合規保證。"),
     ("h","作業風險自負"),
     ("ul",["實際飛行之安全與合規責任由操作者自負","植保噴藥涉及藥劑與環境責任，請由具備資格的專業人員執行","本站不代購、不代飛、不承擔任何因使用本站內容所致之損害"]),
     ("h","外部連結"),
     ("p","本站可能引用外部資源與連結，對其內容與可用性不負責任。"),
    ])

def terms_page():
    return static_legal("使用條款","農翔誌使用條款：使用本站即表示同意本條款。","terms",[
     ("p","歡迎使用農翔誌（LipoSow）。使用本站即表示你同意以下使用條款。"),
     ("h","內容版權與使用"),
     ("p","本站內容受著作權保護，歡迎個人與非商業用途的引用與分享，引用時請註明出處。未經授權不得大量重製或作為商業內容出售。"),
     ("h","正確性與更新"),
     ("p","我們會持續更新與校正內容，但不保證內容完全無誤或即時。建議以主管機關與原始來源為最終依據。"),
     ("h","禁止事項"),
     ("ul",["不得將本站內容用於違法或不實宣稱","不得以程式大量抓取本站內容","不得在未標明來源的情況下主張為自創內容"]),
     ("h","條款變更"),
     ("p","本站得隨時調整本條款，變更後於本站公布即生效。若持續使用本站，視為同意變更後條款。"),
    ])

def main():
    # 首頁
    emit("index", full_page(TITLE["index"], HERO_TEXT[:120], "index", home_page()))
    # 支柱 Hub
    for p in PILLARS:
        emit(p["slug"], full_page(TITLE[p["slug"]], HUB_LEAD[p["slug"]], p["slug"], hub_page(p)))
    # 文章
    for slug in ART:
        emit(slug, full_page(TITLE[slug], ART[slug][1], slug, article_page(slug)))
    # 靜態
    emit("about", about_page())
    emit("contact", contact_page())
    emit("privacy", privacy_page())
    emit("disclaimer", disclaimer_page())
    emit("terms", terms_page())
    emit("sitemap", sitemap_page())
    print("DONE")

if __name__ == "__main__":
    main()




