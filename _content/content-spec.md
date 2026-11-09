# AgriSky 農翔誌 — 新增條目撰寫規格（凍結模式，所有子代理必須遵循）

工作目錄（唯一落點）：`D:\_325_cloudflarepage_site\liposow.com\agrisky-pro\`
**禁止觸碰**：`build.py`、任何 `.html`、`assets\`、`_shots\`、其他目錄。你只負責**建立一個**輸出檔 `_content\part_<你的tag>.py`。

## 1. 生成機制（必讀，已由主代理驗證）

網站由 `build.py` 生成全部頁面。文章資料在 dict `ART`（鍵=slug），每條為 **8 元組**：
```
("標題", "摘要lead", ["標籤1","標籤2","標籤3"], 作者鍵,
 [("目錄id","目錄名"), ...], 正文HTML,
 ("上一篇slug","上一篇標題"), ("下一篇slug","下一篇標題"))
```
同時必須在 `TITLE` dict 補上「slug:標題」，兩者標題文字必須完全一致。
作者鍵限四種：`lin`(林政宇, 農業技術主編)、`chen`(陳映筑, 法規與安全編輯)、`xu`(許哲銘, 生活應用編輯)、`team`(農翔誌編輯群)。

正文 HTML 支援（**只准用這些**）：
- `<h2 id="xxx">` 段落標題（id 必須與 toc 清單一致，toc 的 id 即 h2 的 id）
- `<p>`、`<ul>`/`<ol>`（`<li><strong>…</strong>…</li>` 帶粗體起頭）
- `<div class="tablewrap"><table><caption>…</caption><thead>…</thead><tbody>…</tbody></table></div>`
- `<div class="callout"><span class="ct">…</span>…</div>` 或 `<div class="callout green">`
- `<div class="procon"><div class="pc pro"><h4>…</h4><ul>…</ul></div><div class="pc con">…</div></div>`
- `<ul class="check"><li>…</li></ul>`（勾選清單）
- `<div class="faq"><details><summary>…</summary><div class="faq-a">…</div></details></div>`
- 圖片（僅指定的篇目）：見下方「圖片配置」的 figure 片段

## 2. 內容品質紅線（宣告式，不是步驟）

每篇都要做到：
- **正文至少 4 個 H2 段落**，每個 H2 內含實質內容（≥1 段文字 + 清單/表格等）
- **至少 1 種** table 或 procon 或 check 清單（禁止整篇只有文字段落）
- **建議含 FAQ**（2–4 題 details），題目要像真實讀者會問的
- 繁體中文、**台灣實務導向**；語氣專業、實用、詳盡，避免空泛口號
- **不編造具體數據／法條**：凡涉法規、規格、費用、數據，一律用「以主管機關現行公告為準」「依主流規格整理」「示意」「視行情而定」等限定語，**禁止**出現假精確數字（如具體金額、具體罰款、具體規格數值）
- 標題可自訂長標題，但必須包含任務指定的短名主詞；`ART` 標題與 `TITLE[slug]` 完全一致
- 摘要 lead 直接用任務指定的 lead 文字（可小幅潤飾，不要改義）
- 作者鍵嚴格照任務指定

## 3. 輸出檔格式（唯一交付物）

`D:\_325_cloudflarepage_site\liposow.com\agrisky-pro\_content\part_<tag>.py`，UTF-8，格式：
```python
# -*- coding: utf-8 -*-
# <支柱> 支柱新增條目（<tag>）
TITLE.update({
  "slug-1": "標題",
  ...
})
ART.update({
  "slug-1": (
    "標題",
    "摘要lead",
    ["標籤1", "標籤2", "標籤3"],
    "作者鍵",
    [("h2-id-1", "目錄名1"), ("h2-id-2", "目錄名2"), ("h2-id-3", "目錄名3"), ("h2-id-4", "目錄名4"), ("h2-id-5", "目錄名5")],
    """<h2 id="h2-id-1">…</h2>
<p>…</p>
…""",
    ("上一篇slug", "上一篇標題"),
    ("下一篇slug", "下一篇標題"),
  ),
  ...
})
```

## 4. 交稿前自檢（全部通過才算完成）

1. `python -m py_compile "D:\_325_cloudflarepage_site\liposow.com\agrisky-pro\_content\part_<tag>.py"` 通過
2. 你的 slug 清單與任務指定**完全一致**，不多不少；TITLE 與 ART 都涵蓋全部
3. prev/next 兩個元組**逐字照抄**任務表格（slugs 與標題都一樣）
4. 每篇正文 ≥4 個 H2；id 與 toc 一一對應；每篇 ≥1 種 table/procon/check
5. 無假精確數字／法條
6. 確認 `assets\img\` 內有你要用的 webp 檔（若任務指定圖片）

## 5. 回報格式

回報：輸出檔絕對路徑、撰寫的 slug 清單、自檢結果摘要（py_compile 通過、鏈結核對）、圖片用了哪幾張（若有）。
