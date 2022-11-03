"""
Mirror all web pages.

Useful if you are living down under.
"""
from mitmproxy import http
import re


def response(flow: http.HTTPFlow) -> None:
     flter = False
     if flow.request and flow.request.host:
          if 'speedtest.net' in flow.request.host:
               flter = True

     if flter and flow.response and flow.response.content:
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
          

