import yfinance as yf
from datetime import datetime, timedelta
import pytz

def save_yesterday_stock_data():
    # 종목 리스트와 이름 매칭 (티커: 파일에 쓸 이름)
    stocks = {
        "069500.KS": "KODEX 200",
        "252670.KS": "KODEX 200선물인버스2X",
        "005930.KS": "삼성전자",
        "000660.KS": "SK하이닉스",
        "105560.KS": "KB금융",
        "005380.KS": "현대차",
        "068270.KS": "셀트리온",
        "055550.KS": "신한지주",
        "035420.KS": "NAVER",
        "000270.KS": "기아"
    }
    
    # 어제 날짜 계산
    yesterday = datetime.now() - timedelta(days=1)
    start_date = yesterday.strftime("%Y-%m-%d")
    end_date = (yesterday + timedelta(days=1)).strftime("%Y-%m-%d")
    
    # 한국 시간대 설정
    kst = pytz.timezone('Asia/Seoul')
    
    for ticker, name in stocks.items():
        # 데이터 다운로드 (어제 하루 분봉 데이터)
        stock_data = yf.download(ticker, start=start_date, end=end_date, interval="1m")
        
        # 데이터가 비어 있지 않으면 진행
        if not stock_data.empty:
            # 한국 시간으로 변환
            stock_data.index = stock_data.index.tz_convert(kst)
            
            # 어제 날짜에 해당하는 파일 이름 생성
            file_name = f"/저장폴더더/{yesterday.strftime('%Y-%m-%d')}_{name}.txt"
            
            # 텍스트 파일로 저장 (종목명 포함)
            with open(file_name, "w") as file:
                file.write(f"종목명: {name}\n")
                file.write(stock_data.to_string())
            
            print(f"File saved as {file_name}")
        else:
            print(f"No data available for {name} on {yesterday.strftime('%Y-%m-%d')}")

# 함수 실행
save_yesterday_stock_data()
