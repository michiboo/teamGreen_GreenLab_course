"""
Mirror all web pages.

Useful if you are living down under.
"""
from mitmproxy import http
import re


def response(flow: http.HTTPFlow) -> None:
     flter = False
     if flow.request and flow.request.host:
          if 'psychologytoday.com' in flow.request.host:
               flter = True

     if flter and flow.response and flow.response.content:
          temp_content = flow.response.content
          
          temp_content = re.sub(b"<!-- Google Tag Manager Data Layer -->(\r|\n|.)*?<!-- End Google Tag Manager Data Layer -->",
               b"", temp_content)
          temp_content = re.sub(b"<!-- Google Tag Manager -->(\r|\n|.)*?<!-- End Google Tag Manager -->",
               b"", temp_content)
          temp_content = re.sub(b"<script.*>(\r|\n).*<!--//-->(\r|\n).*<!\[CDATA\[//><!--(\r|\n).*if\(typeof googletag === 'undefined'\)(\r|\n|.)*?</script>",
               b"", temp_content)
          # temp_content = re.sub(b"<script.*>(\r|\n).*<!--//-->(\r|\n).*<!\[CDATA\[//><!--(\r|\n).*googletag.cmd.push\(function\(\)(\r|\n|.)*?</script>",
          #      b"", temp_content)
          temp_content = re.sub(b"<script type=\"text/javascript\">((\r|\n).*){19}.*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"googletag.enableServices();",
               b"", temp_content)
          temp_content = re.sub(b"<div.*id=\"block-pt-ads-300x-right-www(\r|\n|.)*?<div.*class=\".*block-pt-user-meet-the-experts.*?>",
               b"", temp_content)
          temp_content = re.sub(b"<div id=\"block-pt-ads-300x305-voices-in-recovery(\r|\n|.)*?<div id=\"block-views-magazine-issues-block-2",
               b"<div id=\"block-views-magazine-issues-block-2", temp_content)
               
               
                 
          flow.response.content = temp_content


