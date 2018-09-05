# Hearthstone Meta Crawling Bot


### 개발 전
* Hearthstone 관련 데이터는 https://www.hearthstudy.com 에서 크롤링 합니다. 문제시 삭제

#### 1. 하스스톤 관련 데이터 수집
 - 정규전 덱 티어 및 순위
 - 덱 분포도
 - 덱 승률
 - ~~주요 덱 상성~~
 - ~~직업 별 상성~~
 - 직업별 승률

#### 2. 데이터 처리
 - Hearthstone 디렉토리 아래 json 파일로 저장
 - 날짜별 정리
 ~~~
 {
    "date": "YYYY-MM-DD hh:mm:ss[.nnn]",
    "tiers": {
        "num_tier": [{"rank": "name"}],
    },
    "frequency": {
        "name": "frequency",
    },
    "win_rates": {
        "name": "win_rates",
    },
    "matchup": {
        "main": {
            "name": {
                "versus": "name",
                "win_rates": "win_rates",
                "entirely": "entirely",
            }
        },
        "class": {
            "name": {
                "versus": "name",
                "win_rates": "win_rates",
                "entirely": "entirely",
            }
        }
    }
 }
 ~~~

#### 3. 개발
 - sprumin123@gmail.com
 - Parser, Crawler, 크롤러
 - 시간 날 때..
 - Tiers -> Frequency -> Win_Rates -> Matchup 순서로 개발
 - 2018/08/30 Tiers End
 - 2018/08/30 Frequency End 
 - 2018/08/31 win_rates End
 - 개발 완료후 Django를 사용하여 Data를 확인할 수 있는 웹 페이지 제작
 - 2018/09/05 Matchup에서 막혔다. requests로 받아오는데 500뜸 계속.. 삽질
   Matchup은 크롤링을 좀더 공부한 후에 완성해야겠다. 
 - 2018/09/05 Matchup Pending -> Classrates Add 