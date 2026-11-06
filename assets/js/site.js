/* ============================================================
   AgriSky 農翔誌 — 全站共用互動
   MegaMenu、行動版選單、文章目錄平滑捲動、年份、進度條
   ============================================================ */
(function(){
  'use strict';

  /* 頁尾年份 */
  var y = document.getElementById('yr');
  if(y) y.textContent = new Date().getFullYear();

  /* ---- Header MegaMenu：hover 預覽 + 點擊固定（點開後不因滑鼠移開而收合） ---- */
  var navItems = Array.prototype.slice.call(document.querySelectorAll('.nav-item'));
  var pinned = null; // 記錄「被點擊固定」的欄
  function closeOthers(exclude){
    navItems.forEach(function(x){ if(x !== exclude) x.classList.remove('open'); });
  }
  function closeAll(){ navItems.forEach(function(x){ x.classList.remove('open'); }); }
  navItems.forEach(function(it){
    var link = it.querySelector(':scope > a');
    // hover：僅作暫時預覽；若已有另一欄被「點擊固定」，不因 hover 切走
    it.addEventListener('mouseenter', function(){
      if(pinned && pinned !== it) return;
      closeOthers(it); it.classList.add('open');
    });
    it.addEventListener('mouseleave', function(){
      if(pinned === it) return; // 已固定：不隨滑鼠移開而收合
      it.classList.remove('open');
    });
    if(link){
      link.addEventListener('click', function(e){
        // 純錨點（無子選單）照常跳轉；有子選單則點擊切換並「固定」
        if(it.querySelector('.mega')){
          e.preventDefault();
          e.stopPropagation();
          var wasOpen = it.classList.contains('open') && pinned === it;
          closeOthers(it);
          if(wasOpen){
            it.classList.remove('open'); pinned = null; // 再點一次收起
          } else {
            it.classList.add('open'); pinned = it; // 點開並固定
          }
        }
      });
    }
  });
  // 點選單以外的任何地方：全部收合並解除固定
  document.addEventListener('click', function(e){
    if(!e.target.closest('.nav-item')){ closeAll(); pinned = null; }
  });
  // 按 Esc 也關閉
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape'){ closeAll(); pinned = null; }
  });

  /* ---- 行動版 Drawer ---- */
  var drawer = document.getElementById('drawer');
  var hamburger = document.getElementById('hamburger');
  if(drawer && hamburger){
    function setDrawer(open){
      drawer.classList.toggle('open', open);
      drawer.setAttribute('aria-hidden', open ? 'false' : 'true');
      hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
    }
    hamburger.addEventListener('click', function(e){
      e.stopPropagation();
      setDrawer(!drawer.classList.contains('open'));
    });
    drawer.querySelectorAll('[data-close]').forEach(function(el){
      el.addEventListener('click', function(){ setDrawer(false); });
    });
    drawer.querySelectorAll('.dl a').forEach(function(a){
      a.addEventListener('click', function(){ setDrawer(false); });
    });
  }

  /* ---- 文章內目錄：平滑捲動 + 閱讀進度高亮 ---- */
  var toc = document.querySelector('.toc ol');
  if(toc){
    var tocLinks = Array.prototype.slice.call(toc.querySelectorAll('a'));
    var secs = tocLinks.map(function(a){
      var id = a.getAttribute('href');
      return id ? document.getElementById(id.slice(1)) : null;
    });
    function highlight(){
      var pos = window.scrollY + 90;
      var current = -1;
      secs.forEach(function(s,i){
        if(s && s.offsetTop <= pos) current = i;
      });
      tocLinks.forEach(function(a,i){
        a.style.fontWeight = (i === current) ? '700' : '';
        a.style.color = (i === current) ? 'var(--green-700)' : '';
      });
    }
    window.addEventListener('scroll', highlight, {passive:true});
    highlight();
  }

  /* ---- 頂部閱讀進度條 ---- */
  var bar = document.getElementById('progress');
  if(bar){
    function upd(){
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var pct = h > 0 ? (window.scrollY / h) * 100 : 0;
      bar.style.width = pct + '%';
    }
    window.addEventListener('scroll', upd, {passive:true});
    upd();
  }

  /* ---- 平滑錨點捲動（不干擾一般連結） ---- */
  document.addEventListener('click', function(e){
    var a = e.target.closest('a[href^="#"]');
    if(!a) return;
    var id = a.getAttribute('href');
    if(id === '#' || id.length < 2) return;
    var el = document.getElementById(id.slice(1));
    if(el){
      e.preventDefault();
      var top = el.getBoundingClientRect().top + window.scrollY - (document.getElementById('siteHeader') ? 78 : 0);
      window.scrollTo({ top: top, behavior: 'smooth' });
      history.replaceState(null,'','#'+id.slice(1));
    }
  });

  /* ---- 聯絡表單（示範站：攔截送出並提示，不實際寄送） ---- */
  var cf = document.getElementById('contactForm');
  if(cf){
    cf.addEventListener('submit', function(e){
      e.preventDefault();
      var note = cf.querySelector('.form-note');
      if(note){
        note.textContent = '已收到你的諮詢。確認姓名與 Email 後，本站將於 2 個工作天內回覆。';
        note.style.color = 'var(--green-700)';
        note.style.fontWeight = '600';
      }
    });
  }



})();

(function(){
  var INDEX = [];
  fetch('/search-index.json', {cache:'force-cache'})
    .then(function(r){ return r.json(); })
    .then(function(d){ INDEX = d; })
    .catch(function(){});
  document.addEventListener('input', function(e){
    var inp = e.target;
    if(!inp || !inp.classList || !inp.classList.contains('search-input')) return;
    var wrap = inp.closest('.search-wrap');
    if(!wrap) return;
    var box = wrap.querySelector('.search-results');
    var q = inp.value.trim();
    if(!q || !INDEX.length){ box.hidden = true; return; }
    var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    var out = INDEX.filter(function(it){
      var hay = (it.title + ' ' + it.cat + ' ' + it.lead + ' ' + it.body).toLowerCase();
      return terms.every(function(t){ return hay.indexOf(t) >= 0; });
    }).slice(0, 8);
    if(!out.length){
      box.innerHTML = '<div class="sr-empty">找不到相符內容，試試更短關鍵字</div>';
      box.hidden = false;
      return;
    }
    var html = out.map(function(it){
      return '<a class="sr-item" href="' + it.url + '"><b></b></a>';
    }).join('');
    box.innerHTML = html;
    var items = box.querySelectorAll('.sr-item');
    out.forEach(function(it, i){
      items[i].querySelector('b').textContent = it.title;
      var sp = document.createElement('span');
      sp.textContent = it.cat + ' · ' + it.lead;
      items[i].appendChild(sp);
    });
    box.hidden = false;
  });
  document.addEventListener('click', function(e){
    if(e.target && e.target.closest && e.target.closest('.search-wrap')) return;
    var boxes = document.querySelectorAll('.search-results');
    for(var i=0;i<boxes.length;i++) boxes[i].hidden = true;
  });
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape'){
      var boxes = document.querySelectorAll('.search-results');
      for(var i=0;i<boxes.length;i++) boxes[i].hidden = true;
    }
  });
})();

(function(){
  // 手風琴只展開、不收起（再點一次仍保持展開）
  document.querySelectorAll('.acc').forEach(function(box){
    box.querySelectorAll('.acc-head').forEach(function(btn){
      btn.addEventListener('click', function(){
        var item = btn.closest('.acc-item');
        item.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
      });
    });
  });
  // 卡片式摺疊（details）同樣只展開不收起
  document.querySelectorAll('.bl-card').forEach(function(card){
    var sum = card.querySelector('summary');
    if(!sum) return;
    sum.addEventListener('click', function(e){
      if(card.open) e.preventDefault();
    });
  });
})();

(function(){
  function initBlogFilter(){
    var sel = document.getElementById('blogFilter');
    if(!sel || sel.getAttribute('data-bound') === '1') return;
    sel.setAttribute('data-bound', '1');
    sel.addEventListener('change', function(){
      var v = sel.value;
      document.querySelectorAll('#blogList .acc-item').forEach(function(it){
        it.style.display = (v === 'all' || it.getAttribute('data-cat') === v) ? '' : 'none';
      });
    });
  }
  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', initBlogFilter);
  } else {
    initBlogFilter();
  }
})();
