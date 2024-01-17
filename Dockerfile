FROM python:3.9.2-slim-buster
RUN mkdir /app && chmod 777 /app
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git python3 python3-pip ffmpeg
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
# Or for Windows uncomment
# RUN apt-get update && apt-get install -y dos2unix
# RUN dos2unix bash.sh && pip3 install --no-cache-dir -r requirements.txt
CMD ["bash","bash.sh"]
