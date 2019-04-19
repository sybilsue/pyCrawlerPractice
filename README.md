<p>downloadPhotoFromwin4000.py</p>
<p>从<a href = "http://www.win4000.com/">美桌网</a>下载指定壁纸集的壁纸，壁纸将按照数字顺序存放在同文件夹中。</p>
<p>通过修改</p>
<div class="highlight highlight-source-shell">
    <pre>
    url = 'http://www.win4000.com/wallpaper_detail_155712.html'
</pre>
</div>
<p>切换下载地址，要求该url为壁纸集的第一张壁纸。</p>
<p> </p>
<p> </p>
<p>getWallpaperFrom5857.py</p>
<p>从<a href = "http://www.5857.com/">5857壁纸站</a>下载指定壁纸集的壁纸，壁纸将按照数字顺序存放在同文件夹中。</p>
<p>通过修改</p>
<div class="highlight highlight-source-shell">
    <pre>
   url = 'http://www.5857.com/pcbz/82865.html'
</pre>
</div>
<p>切换下载地址，要求该url为壁纸集的第一张壁纸。</p>
<p> </p>
<p> </p>
<p>getArticleNumFromOA.py</p>
<p>从oxford academic旗下各期刊门户网站统计某期刊某一年的所有卷 期 文章数。</p>
<p>通过修改</p>
<div class="highlight highlight-source-shell">
    <pre>
    url = 'https://academic.oup.com/abbs/issue-archive'
</pre>
</div>
<p>修改所统计的期刊，要求该url为期刊的issue-archive页。</p>
<p>通过修改</p>
<div class="highlight highlight-source-shell">
    <pre>
if '2018' in years:
</pre>
</div>
<p>修改年份，要求年份为字符串</p>
