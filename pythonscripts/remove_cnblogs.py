"""
Mirror all web pages.

Useful if you are living down under.
"""
from mitmproxy import http
import re


def response(flow: http.HTTPFlow) -> None:
     flter = False
     if flow.request and flow.request.host:
          if 'cnblogs.com' in flow.request.host:
               flter = True

     if flter and flow.response and flow.response.content:
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

