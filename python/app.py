from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
import logging
import uuid
import json
import io
import boto3
 
# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

# .env 파일의 경로를 지정하여 환경 변수 로드
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# 환경 변수에서 RDS 설정 로드
RDS_HOST = os.getenv('host')
RDS_PORT = int(os.getenv('port'))
RDS_USER = os.getenv('user')
RDS_PASSWORD = os.getenv('password')
RDS_DB = os.getenv('database')

def savetomysql(table, data):
    try:
        connection = mysql.connector.connect(
            host=RDS_HOST,
            port=RDS_PORT,
            user=RDS_USER,
            password=RDS_PASSWORD,
            database=RDS_DB
        )
        cursor = connection.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, list(data.values()))
        connection.commit()
        cursor.close()
        connection.close()
    except Error as err:
        print(f"Error: {err}")
        return False
    return True

@app.post("/uploadImage")
async def upload_file(file: UploadFile = File(...), exifData: str = Form(...)):
    table_name = "OriginalMenus"
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    
    try:
        # 파일 내용을 읽어서 Blob 데이터로 저장
        logger.info("Reading file content...")
        file_content = await file.read()
        logger.info("File content read successfully")

        # EXIF 데이터에서 GPS 정보 추출
        logger.info("Extracting EXIF data...")
        exif_data = json.loads(exifData)
        lat, lon = extract_gps_info(exif_data)
        logger.info(f"Extracted GPS info: Latitude = {lat}, Longitude = {lon}")

        data = {
            "filename": unique_filename,
            "file_blob": file_content,
            "latitude": lat,
            "longitude": lon
        }

        if savetomysql(table_name, data):
            return {"message": "File uploaded successfully", "file_name": unique_filename, "latitude": lat, "longitude": lon}
        else:
            return JSONResponse(content={"message": "Failed to save metadata to database"}, status_code=500)
    except Error as db_err:
        logger.error(f"Database error: {db_err}")
        return JSONResponse(content={"message": f"Database error: {db_err}"}, status_code=500)
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        return JSONResponse(content={"message": str(e)}, status_code=500)

# 이미지 가져오는 엔드포인트
@app.get("/get_image")
def get_image(filename):
    try:
        connection = mysql.connector.connect(
            host=RDS_HOST,
            port=RDS_PORT,
            user=RDS_USER,
            password=RDS_PASSWORD,
            database=RDS_DB
        )
        cursor = connection.cursor(dictionary=True)
        
        # 이미지 데이터 가져오기 쿼리 실행
        query = "SELECT file_blob FROM OriginalMenus WHERE filename = %s"
        cursor.execute(query, (filename,))
        result = cursor.fetchone()
        
        if result and 'file_blob' in result:
            image_data = result['file_blob']
            return StreamingResponse(io.BytesIO(image_data), media_type="image/jpeg")
        else:
            return {"error": "Image not found"}
    except Error as e:
        return {"error": str(e)}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def convert_to_degrees(value):
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

def extract_gps_info(exif_data):
    gps_info = {}
    if exif_data:
        for tag, value in exif_data.items():
            if tag.startswith('GPS'):
                gps_info[tag] = value

    lat = lon = None
    if 'GPSLatitude' in gps_info and 'GPSLongitude' in gps_info:
        lat = convert_to_degrees(gps_info['GPSLatitude'])
        lon = convert_to_degrees(gps_info['GPSLongitude'])
        lat_ref = gps_info.get('GPSLatitudeRef', 'N')
        lon_ref = gps_info.get('GPSLongitudeRef', 'E')

        if lat_ref != "N":
            lat = -lat
        if lon_ref != "E":
            lon = -lon

    return lat, lon