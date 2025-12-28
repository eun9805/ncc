# 1. 베이스 이미지 설정 (Python 3.11 슬림 버전 사용으로 용량 최적화)
FROM python:3.11-slim-bookworm

# 2. 필수 패키지 및 Firefox 설치
# Selenium 구동에 필요한 라이브러리들과 Firefox를 설치합니다.
RUN apt-get update && apt-get install -y --no-install-recommends \
    firefox-esr \
    wget \
    bzip2 \
    curl \
    libnss3 \
    libdbus-glib-1-2 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# 3. Geckodriver 설치 (ARM64 아키텍처용 v0.35.0)
# 사용자가 제공한 경로(/usr/bin/geckodriver)에 맞게 설정합니다.
ENV GECKODRIVER_PATH=/usr/bin/geckodriver
RUN curl -LO https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux-aarch64.tar.gz \
    && tar -xzf geckodriver-v0.35.0-linux-aarch64.tar.gz -C /usr/bin/ \
    && rm geckodriver-v0.35.0-linux-aarch64.tar.gz \
    && chmod +x /usr/bin/geckodriver

# 4. 작업 디렉토리 설정
WORKDIR /app

# 5. 종속성 설치
# requirements.txt를 먼저 복사하여 캐시 효율을 높입니다.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. 소스 코드 복사
COPY . .

# 7. 실행 권한 부여
RUN chmod +x run_firefox.py

# 8. 환경 변수 설정 (기본값)
ENV NAVER_ACCOUNTS='{}'
ENV DELAY_HOURS=48
ENV MIN_DWELL_TIME=6

# 9. 스크립트 실행
CMD ["python", "run_firefox.py"]