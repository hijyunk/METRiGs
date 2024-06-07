# 베이스 이미지로 Node.js 사용
FROM node:16.20.2

# step 2 : Package Install
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# 작업 디렉토리 설정
WORKDIR '/root'

# 의존성 설치
RUN git clone https://github.com/hijyunk/METRiGs METRiGs2
WORKDIR '/root/METRiGs2/node'
RUN npm install
RUN npm install -g nodemon

# 의존성 설치
RUN git clone https://github.com/malangzo/METRiGs METRiGs1
WORKDIR '/root/METRiGs1/node'
RUN npm install
RUN npm install -g nodemon

# 애플리케이션이 실행될 포트 설정
EXPOSE 8000 8500

# 애플리케이션 시작 명령어
CMD nodemon /root/METRiGs1/node/app.js & nodemon /root/METRiGs2/node/app.js