# 🍽 METRiGS: 메뉴판 텍스트 번역 & 메뉴 이미지 생성 서비스
<br>

## 프로젝트 소개

- 사용자가 찍은 메뉴판 사진에 적힌 텍스트를 추출해 번역하고, 이를 바탕으로 메뉴 설명 및 이미지를 생성해 주는 웹 앱 서비스
- OCR 기능: Amazon Textract를 이용한 OCR 기술 적용해 텍스트 추출
- 번역 기능: DeepL API를 이용한 추출한 텍스트 번역
- 메뉴 설명 기능: ChatGPT를 이용한 AI 기반 메뉴 설명 생성
- 이미지 생성 기능: DALL-E를 이용한 AI 기반 메뉴 이미지 생성

<br>

## 페이지 소개

 - 메인 페이지
   - 사진 업로드 및 언어 선택
<br><br><span align="center"><img src="https://github.com/user-attachments/assets/2241b2ca-bdbc-4a0d-a226-8a2e262fc3c8"></span>
 - 결과 페이지
   - 번역 결과 및 메뉴 이미지 확인
<br><br><span align="center"><img src="https://github.com/user-attachments/assets/98ab4107-ca32-4126-b1be-dace7ad780b8"></span>

<br>


## 팀원 역할 분담

### 👩장유정 - 팀장

- **기획**
    - 프로젝트 구상 및 기획
    - 시스템 구성 설계
- **UI**
    - 결과 페이지
- **기능**
    - AWS Textract를 이용한 OCR 기능 개발
    - 추출한 텍스트를 바탕으로 DeePL API를 이용한 텍스트 번역 기능 개발
    - OpenAI의 ChatGPT를 이용한 메뉴 설명 생성 기능 개발
    - OpenAI의 DALL-E를 이용한 이미지 생성 기능 개발
    - 데이터베이스 설계 및 AWS RDS, S3를 이용한 DB 관리
    - Docker 환경 구축

<br>

### 👧김지현

- **UI**
    - CSS 및 EJS 총괄
    - 메인 페이지 구현
- **기능**
    - 메뉴 사진 업로드 기능 개발
    - 메뉴 이미지 데이터 관리 기능 개발
    - 데이터베이스 설계 및 AWS RDS, S3를 이용한 DB 관리
    - Docker 환경 구축
<br>
    

## 기술 스택

<h3 align="left">Frontend</h3>
<div>
	<img src="https://img.shields.io/badge/EJS-B4CA65?style=for-the-badge&logo=EJS&logoColor=black">
	<img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
	<img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
</div>

<h3 align="left">Backend</h3>
<div>
	<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
	<img src="https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/javascript-F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black">
	<img src="https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white">
</div>

<h3 align="left">DB</h3>
<div>
	<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
  <img src="https://img.shields.io/badge/Amazon RDS-527FFF?style=for-the-badge&logo=amazonrds&logoColor=white">
  <img src="https://img.shields.io/badge/Amazon S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white">
  
</div>

<h3 align="left">DevOps</h3>
<div>
	<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=Linux&logoColor=white">
	<img src="https://img.shields.io/badge/AWS EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=black">
	<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white">
</div>


<br>

## 개발 기간

- 전체 개발 기간 : 2024.05 ~ 2024.06

<br>
