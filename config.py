"""
네이버 포인트 스크래퍼 설정 파일
"""
import os
import json

# ==================== 네이버 계정 정보 ====================
# 환경변수 NAVER_ACCOUNTS를 JSON 문자열로 받음 
# 예: '{"id1":"pw1", "id2":"pw2"}'
naver_accounts_env = os.getenv('NAVER_ACCOUNTS', '{}')
try:
    naver_login_info = json.loads(naver_accounts_env)
except json.JSONDecodeError:
    naver_login_info = {}

# ==================== 기본 설정 ====================
# Docker 내부 경로에 맞춰 기본값 설정
GECKODRIVER_PATH = os.getenv('GECKODRIVER_PATH', '/usr/bin/geckodriver')
DELAY_HOURS = int(os.getenv('DELAY_HOURS', '48'))
MIN_DWELL_TIME = int(os.getenv('MIN_DWELL_TIME', '6'))

# ==================== User Agent 설정 ====================
REQUEST_USER_AGENT = os.getenv('REQUEST_USER_AGENT', "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0")
FIREFOX_USER_AGENT = os.getenv('FIREFOX_USER_AGENT', "Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0.1 Mobile/15E148 Safari/604.1")

# ==================== 스크래핑 대상 사이트 설정 ====================
SCRAPING_SITES = {
    "https://damoang.net/economy": {"tag": "div", "class": "flex-grow-1 overflow-hidden", "domain": "damoang.net"},
    "https://www.clien.net/service/board/jirum": {"tag": "span", "class": "list_subject", "domain": "clien.net"},
    "https://bbs.ruliweb.com/market/board/1020": {"tag": "td", "class": "subject", "domain": "ruliweb.com"},
    "https://www.ppomppu.co.kr/zboard/zboard.php?id=coupon": {"tag": "td", "class": "baseList-space", "domain": "ppomppu.co.kr"},
    "https://www.dogdrip.net/hotdeal": {"tag": "h5", "class": "ed title margin-remove", "domain": "dogdrip.net"},
}