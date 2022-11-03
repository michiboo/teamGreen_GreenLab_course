"""
Mirror all web pages.

Useful if you are living down under.
"""
from mitmproxy import http
import re


def response(flow: http.HTTPFlow) -> None:
     flter = False
     if flow.request and flow.request.host:
          if 'investing.com' in flow.request.host:
               flter = True

     if flter and flow.response and flow.response.content:
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
             