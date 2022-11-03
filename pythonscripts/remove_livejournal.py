"""
Mirror all web pages.

Useful if you are living down under.
"""
from mitmproxy import http
import re


def response(flow: http.HTTPFlow) -> None:
     flter = False
     if flow.request and flow.request.host:
          if 'livejournal.com' in flow.request.host:
               flter = True

     if flter and flow.response and flow.response.content:
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



 


          flow.response.content = temp_content
          

