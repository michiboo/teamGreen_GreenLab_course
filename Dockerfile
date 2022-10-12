FROM mitmproxy/mitmproxy
COPY ./remove_mirror.py .
ENTRYPOINT ["mitmproxy", "-s", "remove_mirror.py"]

# docker run -it -v ~/.mitmproxy:/home/mitmproxy/.mitmproxy -p 8080:8080 $(docker build -q .)