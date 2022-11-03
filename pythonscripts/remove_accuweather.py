"""
Mirror all web pages.

Useful if you are living down under.
"""
from mitmproxy import http
import re


def response(flow: http.HTTPFlow) -> None:
     flter = False
     if flow.request and flow.request.host:
          if 'accuweather.com' in flow.request.host:
               flter = True

     if flter and flow.response and flow.response.content:
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
          # temp_content = re.sub(b"<script>(\r|\n)*.*gaAppConfig(\r|\n|.)*?</script>",
          #      b"", temp_content)
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
          
