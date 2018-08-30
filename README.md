# Python Crawling-Bot


### 개발 전
* Hearthstone 관련 데이터는 https://www.hearthstudy.com 에서 크롤링 합니다. 문제시 삭제

#### 1. 하스스톤 관련 데이터 수집
 - 정규전 덱 티어 및 순위
 - 덱 점유율
 - 덱 승률
 - 주요 덱 상성

#### 2. 데이터 처리
 - Hearthstone 디렉토리 아래 json 파일로 저장
 - 날짜별 정리 or 파일하나에 덮어쓰기 ( 현재 전자 선택 )
 ~~~
 {
    "date": "YYYY-MM-DD hh:mm:ss[.nnn]",
    "tiers": {
        "num_tier": [{"rank": "name"}],
    },
    "share": {
        "hero": [{"name": "share"}],
    },
    "distribution": {
        "name": "distribution",
    },
    "odds": {
        "name": "odds",
    },
    "counter": {
        "name": {
            "versus": "name",
            "odds": "odds",
            "entirely": "entirely",
        }
    }
 }
 ~~~

#### 3. 개발
 - 시간 날 때..
 - Tier -> share -> distribution -> odds -> counter 순서로 개발
 - 2018/08/30 Tier End
