"""
Mirror all web pages.

Useful if you are living down under.
"""
from mitmproxy import http
import re


def response(flow: http.HTTPFlow) -> None:
     # flter = False
     # if flow.request and flow.request.host:
     #      if 'mirror.co.uk' in flow.request.host:
     #           flter = True

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
          
