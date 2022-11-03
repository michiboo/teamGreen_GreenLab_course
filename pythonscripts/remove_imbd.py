"""
Mirror all web pages.

Useful if you are living down under.
"""
from mitmproxy import http
import re


def response(flow: http.HTTPFlow) -> None:
     flter = False
     if flow.request and flow.request.host:
          if 'imdb.com' in flow.request.host:
               flter = True

     if flter and flow.response and flow.response.content:
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


