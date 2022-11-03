"""
Mirror all web pages.

Useful if you are living down under.
"""
from mitmproxy import http
import re


def response(flow: http.HTTPFlow) -> None:
     flter = False
     if flow.request and flow.request.host:
          if 'bbc.com' in flow.request.host:
               flter = True

     if flter and flow.response and flow.response.content:
          temp_content = flow.response.content
          temp_content = re.sub(b"<script type=\"text/javascript\">(\r|\n)*.*analytics(\r|\n|.)*?</script>",
               b"", temp_content)
          temp_content = re.sub(b"document.head.appendChild\(script\);",
               b"", temp_content)
          temp_content = re.sub(b"bbcdotcom\.resetPage=function\(o\)(.|\r|\n)*?ads\.registerSlot\(d,n,c,t\)}\)},",
               b"", temp_content)
           
          flow.response.content = temp_content
          

