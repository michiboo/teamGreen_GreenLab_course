"""
Mirror all web pages.

Useful if you are living down under.
"""
from mitmproxy import http
import re

def remove_speedtest(flow: http.HTTPFlow) -> None:
     if flow.response and flow.response.content:
          temp_content = flow.response.content
          temp_content = re.sub(b"<!-- IdentityHub Script begins here -->(.|\r|\n)*<!--IdentityHub Script ends here -->",
               b"", temp_content)
          temp_content = re.sub(b"<script.*src=\".*b.cdnst.net/javascript/amazon.js.*?\".*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script.*src=\".*ads/ad.js.*?\".*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<!-- Google Tag Manager -->(.|\r|\n)*<!-- End Google Tag Manager -->",
               b"", temp_content)
          temp_content = re.sub(b"<link rel=\"dns-prefetch\" href=\"//b.cdnst.net\" />",
               b"", temp_content)
          temp_content = re.sub(b"writeSource\(aaxEndpoint\);",
               b"", temp_content)
          temp_content = re.sub(b"\"ads\":true",
               b"\"ads\":false", temp_content)
          temp_content = re.sub(b"window.OOKLA.isBlocked = false;",
               b"window.OOKLA.isBlocked = true;", temp_content)
          flow.response.content = temp_content

def remove_science(flow: http.HTTPFlow) -> None:
     if flow.response and flow.response.content:
          temp_content = flow.response.content
          temp_content = re.sub(b"<script>(\n|\r|.).*try(\n|\r|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script src=\"//securepubads.g.doubleclick.net/tag/js/gpt.js\" async></script>",
               b"", temp_content)
          temp_content = re.sub(b"<meta name=\"baidu-site-verification\" content=\"code-asrYXzJgzI\" />",
               b"", temp_content)
          temp_content = re.sub(b"<meta name=\"facebook-domain-verification\" content=\"d7d83rddklmy6vh0uy6rrm9j4hptwp\" />",
               b"", temp_content)
          temp_content = re.sub(b"<script type=\"text/javascript\" src=\"https://weby.aaas.org/weby_bundle_header_v4.js\"></script>",
               b"", temp_content)
          temp_content = re.sub(b"<script type=\"text/javascript\" src=\"https://weby.aaas.org/weby_bundle_v4.js\"></script>",
               b"", temp_content)
          temp_content = re.sub(b"<script src=\"//weby.aaas.org/weby-lazyload-shim-console.js\" async></script>",
               b"", temp_content)
          temp_content = re.sub(b"<script defer.*</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script src=\"//assets.adobedtm.com/a48c09ba9d50/1e36ca10b673/launch-ea90f2ac46ad.min.js\" async></script>",
               b"", temp_content)
          temp_content = re.sub(b"<div data-widget-def=\"literatumAd\".*class=\"pb-ad(\n|\r|.)*?<h",
               b"<h", temp_content)
          temp_content = re.sub(b"<div.*class=\"grid-quote__ad(\n|\r|.)*?<div class=\"gr",
               b"<div class=\"gr", temp_content)
          temp_content = re.sub(b"<section class=\"my-2_5x\">(\n|\r|.)*?</section>",
               b"", temp_content)
          temp_content = re.sub(b"<div class=\"col-12 col-sm-5 col-xl-12 mb-2x mb-sm-0\"(\n|\r|.)*?<.div>(\n|\r|.)*?<.div>(\n|\r|.)*?<.div>(\n|\r|.)*?<.div>(\n|\r|.)*?<.div>",
               b"", temp_content)
          flow.response.content = temp_content

def remove_psychologytoday(flow: http.HTTPFlow) -> None:
     if flow.response and flow.response.content:
          temp_content = flow.response.content
          
          temp_content = re.sub(b"<!-- Google Tag Manager Data Layer -->(\r|\n|.)*?<!-- End Google Tag Manager Data Layer -->",
               b"", temp_content)
          temp_content = re.sub(b"<!-- Google Tag Manager -->(\r|\n|.)*?<!-- End Google Tag Manager -->",
               b"", temp_content)
          temp_content = re.sub(b"<script.*>(\r|\n).*<!--//-->(\r|\n).*<!\[CDATA\[//><!--(\r|\n).*if\(typeof googletag === 'undefined'\)(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script type=\"text/javascript\">((\r|\n).*){19}.*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"googletag.enableServices();",
               b"", temp_content)
          temp_content = re.sub(b"<div.*id=\"block-pt-ads-300x-right-www(\r|\n|.)*?<div.*class=\".*block-pt-user-meet-the-experts.*?>",
               b"", temp_content)
          temp_content = re.sub(b"<div id=\"block-pt-ads-300x305-voices-in-recovery(\r|\n|.)*?<div id=\"block-views-magazine-issues-block-2",
               b"<div id=\"block-views-magazine-issues-block-2", temp_content)
               
               
                 
          flow.response.content = temp_content

def remove_mirror(flow: http.HTTPFlow) -> None:
     if flow.response and flow.response.content:
          temp_content = flow.response.content
          temp_content = re.sub(b"<link.*href=\"https://www.google-analytics.com\".*?/>",
               b"", temp_content)
          temp_content = re.sub(b"<link.*href=\"https://www.googletagmanager.com\".*?/>",
               b"", temp_content)
          temp_content = re.sub(b"<link.*href=\"https://securepubads.g.doubleclick.net\".*?/>",
               b"", temp_content) 
          temp_content = re.sub(b"<link.*href=\"https://cdn.ampproject.org/v0.js\".*?/>",
               b"", temp_content)
          temp_content = re.sub(b"<link.*href=\"https://quantcast.mgr.consensu.org\".*?/>",
               b"", temp_content)
          temp_content = re.sub(b"<!-- Index Exchange start -->(.|\r|\n)*<!-- Index Exchange end -->",
               b"", temp_content)
          temp_content = re.sub(b"<!-- GPT Library preload - async -->(.|\r|\n)*<!-- GPT Library preload end -->",
               b"", temp_content)
          temp_content = re.sub(b"<!-- Amazon A9 APSTAG -->(.|\r|\n)*<!-- Amazon A9 APSTAG end-->",
               b"", temp_content)
          temp_content = re.sub(b"<!-- IAS -->(.|\r|\n)*<!-- Amazon A9 APSTAG end-->",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n|).*\(function\(w(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<meta name=\"google-site-verification\" content=\"lDCbJ-HOtMAaa6xwHzyQ4nnDZVp-J-BmBbQKbpNN3QI\">",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n|).*TMCONFIG = (\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script async src=\"https://static.chartbeat.com/js/chartbeat_mab.js\"></script>",
               b"", temp_content)
          temp_content = re.sub(b"<meta name='webgains-site-verification' content='pkwgvble' />",
               b"", temp_content)
          temp_content = re.sub(b"<script src=\"https://cdn.ampproject.org/v0.js\" async=\"async\"></script>",
               b"", temp_content)
          temp_content = re.sub(b"<iframe.*src=\"https://www.googletagmanager.com.*</iframe>",
               b"", temp_content)
          temp_content = re.sub(b"<reach-.*?>(\r|\n|.)*?</reach-.*?>",
               b"", temp_content)
          flow.response.content = temp_content

def remove_livejournal(flow: http.HTTPFlow) -> None:
     if flow.response and flow.response.content:
          temp_content = flow.response.content
          temp_content = re.sub(b"<link rel=\"preload\" href=\"//ssp.rambler.ru/capirs_async.js\" as=\"script\">",
               b"", temp_content)
          temp_content = re.sub(b"<script type=\"text/javascript\" src=\"//ssp.rambler.ru/capirs_async.js\" async></script>",
               b"", temp_content)
          temp_content = re.sub(b"<!-- Google Analytics -->(\r|\n|.)*?<!-- End Google Analytics -->",
               b"", temp_content)
          temp_content = re.sub(b"<script async src=\"https://vp.rambler.ru/player/sdk.js\"></script>",
               b"", temp_content)
          temp_content = re.sub(b"<!-- Begin comScore Tag -->(\r|\n|.)*?<!-- End comScore Tag -->",
               b"", temp_content)
          temp_content = re.sub(b"<!-- Google Tag Manager -->(\r|\n|.)*?<!-- End Google Tag Manager -->",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n).*\(function\(\).*(\r|\n).*Copyright(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<!-- tns-counter.ru -->(\r|\n|.)*?<!-- END RCM Counter -->",
               b"", temp_content)
          # temp_content = re.sub(b"<!-- RCM Counter -->(\r|\n|.)*?<!-- END RCM Counter -->",
          #      b"", temp_content)
          temp_content = re.sub(b"<!-- (C)2000-2021 Gemius.*(\r|\n|.)*?<!-- End Gemius -->",
               b"", temp_content)
          temp_content = re.sub(b"<!-- Google Tag Manager -->(\r|\n|.)*?<!-- End Google Tag Manager -->",
               b"", temp_content)

def remove_investing(flow: http.HTTPFlow) -> None:
     if flow.response and flow.response.content:
          temp_content = flow.response.content
          temp_content = re.sub(b"var disableAds = false;",
               b"var disableAds = true;", temp_content)
               
          temp_content = re.sub(b"<link.*securepubads.*\/>",
               b"", temp_content)
          temp_content = re.sub(b"<script.*securepubads.*?>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n).*Load(\r|\n|.)*?<\/script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n).*all(\r|\n|.)*?<\/script>",
               b"", temp_content) 
          temp_content = re.sub(b"<script.*>(\r|\n).*tag(\r|\n|.)*?<\/script>",
               b"", temp_content) 
          temp_content = re.sub(b"<div id=\"sln-hbanner\"(\r|\n|.)*?</div>(\r|\n|.)*?</div>(\r|\n|.)*?</div>",
               b"", temp_content) 
          temp_content = re.sub(b"<div id=\"hpAdVideo\"(\r|\n|.)*?</div>(\r|\n|.)*?</div>",
               b"", temp_content) 
          temp_content = re.sub(b"<div.*id=\"ad\d\"(\r|\n|.)*?</div>(\r|\n|.)*?</div>",
               b"", temp_content) 
          flow.response.content = temp_content

def remove_imbd(flow: http.HTTPFlow) -> None:
     if flow.response and flow.response.content:
          temp_content = flow.response.content
          
          temp_content = re.sub(b"<script>if\(typeof uet === 'function'\){ uet\('bb', 'LoadAds', {wb: 1}\); }</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n).*ads(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n).*!function.*(\r|\n).*(ads).*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script id=\"ads_tarnhelm\" src=\"https://m.media-amazon.com/images/S/sash/It-jnCbnFjUkpJt.js\"></script>",
               b"", temp_content)
          temp_content = re.sub(b"<script id=\"ads_doWithAds\">(\n|\r|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script id=\"ads_monitoring_setup\">(\n|\r|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script id=\"ads_safeframe_setup\">(\n|\r|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script id=\"ads_general_setup\">(\n|\r|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\n|\r).*doWithAds\(function\(\)(\n|\r|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>if(typeof uet === 'function'){ uet('be', 'LoadAds', {wb: 1}); }</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>if(typeof uex === 'function'){ uex('ld', 'LoadAds', {wb: 1}); }</script>",
               b"", temp_content)
               
          flow.response.content = temp_content

def remove_cnblogs(flow: http.HTTPFlow) -> None:
     if flow.response and flow.response.content:
          temp_content = flow.response.content
          temp_content = re.sub(b"<script async='async' src='https://www.googletagservices.com/tag/js/gpt.js'></script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(.|\r|\n)*var googletag(.|\r|\n)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(|\r|\n).*googletag.cmd.push(.|\r|\n)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script async src=\"https://www.googletagmanager.com/.*?\"></script>",
               b"", temp_content)
          flow.response.content = temp_content

def remove_bbc(flow: http.HTTPFlow) -> None:
     if flow.response and flow.response.content:
          temp_content = flow.response.content
          temp_content = re.sub(b"<script type=\"text/javascript\">(\r|\n)*.*analytics(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"document.head.appendChild\(script\);",
               b"", temp_content)
          temp_content = re.sub(b"bbcdotcom\.resetPage=function\(o\)(.|\r|\n)*?ads\.registerSlot\(d,n,c,t\)}\)},",
               b"", temp_content)
           
          flow.response.content = temp_content

def remove_accuweather(flow: http.HTTPFlow) -> None:
     if flow.response and flow.response.content:
          temp_content = flow.response.content
          temp_content = re.sub(b"<script.*src=\".*securepubads.g.doubleclick.net.*?\".*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script.*src=\".*googletagmanager.com.*?\".*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n)*.*\"https://s.go-mpulse.net/boomerang/\"(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n|)*.*mPulse: Could not parse configuration.*</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n|)*.*BOOMR_mq.*</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n).*getHitTimeStamp(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n)*.*window.dataLayer = window.d(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n)*.*globalAd(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n)*.*window.pbjs = window.pbjs(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n)*.*prebidTimeoutPromise(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n)*.*isPwaActive(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"var serverAdsOnPage =.*",
               b"", temp_content)
          temp_content = re.sub(b"<script>(\r|\n)*.*getCampaignLongevity(\r|\n|.)*?</script>",
               b"", temp_content)
          flow.response.content = temp_content
          
def response(flow: http.HTTPFlow) -> None:
     if flow.request and flow.request.host:
          if 'speedtest.net' in flow.request.host:
               remove_speedtest(flow)
          elif 'science.org' in flow.request.host:
               remove_science(flow)
          elif 'psychologytoday.com' in flow.request.host:
               remove_psychologytoday(flow)
          elif 'mirror.co.uk' in flow.request.host:
               remove_mirror(flow)
          elif 'livejournal.com' in flow.request.host:
               remove_livejournal(flow)
          elif 'investing.com' in flow.request.host:
               remove_investing(flow)
          elif 'imdb.com' in flow.request.host:
               remove_imbd(flow)
          elif 'cnblogs.com' in flow.request.host:
               remove_cnblogs(flow)
          elif 'bbc.com' in flow.request.host:
               remove_bbc(flow)
          elif 'accuweather.com' in flow.request.host:
               remove_accuweather(flow)

          

