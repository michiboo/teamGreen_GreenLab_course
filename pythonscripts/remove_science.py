"""
Mirror all web pages.

Useful if you are living down under.
"""
from mitmproxy import http
import re


def response(flow: http.HTTPFlow) -> None:
     flter = False
     if flow.request and flow.request.host:
          if 'science.org' in flow.request.host:
               flter = True

     if flter and flow.response and flow.response.content:
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
