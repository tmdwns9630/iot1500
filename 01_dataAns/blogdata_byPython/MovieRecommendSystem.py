from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

urls = 'C:\\Users\\user\\Documents' # 코드 결과 저장 경로
if(1):
    driver = webdriver.Chrome('c:/iot1500/chromedriver.exe') # 드라이버 잡기
    #노트북
    #movieURL = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=38899&type=after&onlyActualPointYn=Y&onlySpoilerPointYn=N&order=sympathyScore'

    #스파이더맨:노 웨이 홈
    movieURL = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=208077&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false'
    driver.get(movieURL)
    #웹드라이버로 가져올 영화 평점 주소

    # 네이버 무비 노트북 평점 항목
    #/html/body/div/div/div[5]/ul/li[7]/div[2]/dl/dt/em[1]/a/span
    driver.find_element("xpath",'//*[@id="actualYnLable"]').click() # 관람객 평점으로 클릭

    driver.implicitly_wait(1) # 1초 대기
    total_lst = []
    f = open(urls+'/Spidy_movieList_beforeFilter.txt','w')
    f.write(str(total_lst))
    f.close()
    print("파일 저장")

# 테스트용 리스트
# if(1):
#     total_lst = [['미드웨이', '킨: 더 비기닝', '업그레이드', '나의 사랑, 그리스', '잭애스 프레젠트: 배드 그랜파', '덕혜옹주', '나의 소녀시대', '코블러', '스파이', '내 인생을 훔친 사랑스러운 도둑녀'], ['존 윅 3: 파라벨룸', '토르: 라그나로크', '인터스텔라', '아수라', '투모로우랜드', '수어사이드 스쿼드', '더 건맨: 테이큰 감독 뉴프로젝트', '터미네이터 제니시스', '겨울왕국', '분노의 질주: 더 세븐'], ['노트북', '다크 나이트', '클레멘타인', '이퀼리브리엄', '울트라바이올렛'], ['부산행', '맨 인 더 다크', '노트북', '아수라'], ['어우동: 주인 없는 꽃', '주디', '찍히면 죽는다', '히말라야', '판의 미로 - 오필리아와 세 개의 열쇠', '버닝', '복수는 나의 것', '악인은 살아 있다', '포드 V 페라리', '백두산'], ['에놀라 홈즈', '레베카', '쇼생크 탈출', '삼진그룹 영어토익반', '맨 오브 스틸', '82년생 김지영', '스켈리톤 키', '사랑에 빠지는 아주 특별한 법칙', '쏘우', '의궤, 8일간의 축제 3D'], ['알리타: 배틀 엔젤', '부라더', '범죄도시', '남한산성', '뫼비우스', '청년경찰', '덩케르크', '박열', '임금님의 사건수첩', '특별시민'], ['라푼젤', '노트북'], ['헤이트풀8', '명량', '노트북', '코쿠리코 언덕에서', '광해, 왕이 된 남자', '2012'], ['군함도', '너의 이름은.', '봄날은 간다', '제이슨 본', '내부자들', '인턴', '연평해전', '퓨리', '바람', '여인의 향기'], ['도굴', '폴라', '사라진 탄환', '인비저블맨', '콜', '국제수사', '도희야', '반도', '#살아있다', '은하'], ['세계일주', '양자물리학', '사바하', '그것만이 내 세상', '오션스8', '배반의 장미', '타이타닉', '그날의 분위기', '포화 속으로', '슬로우 비디오'], ['연인', '겟 아웃', '프리 윌리', '미녀와 야수', '코요테 어글리', '메이즈 러너: 스코치 트라이얼', '라이온 킹', '베스트 오브 미', '도둑들', '기생수 파트1'], ['언플랜드', '출국', '링컨', '남한산성', '위플래쉬', '군함도', '왕과 나', '사랑: 세 도시 이야기', '북 오브 러브', '어벤져스: 에이지 오브 울트론'], ['신의 한 수', '구타유발자들', '세븐 데이즈', '노트북', '드라이브', '변호인', '어바웃 타임', '웜 바디스', '월드워Z', '램페이지 : 더 테러리스트'], ['블레이드 러너 2049', '나의 사촌 레이첼', '하우 아이 리브: 내가 사는 이유', '007 스펙터', '구스범스', '아메리칸 울트라', '007 퀀텀 오브 솔러스', '암살', '엑소더스: 신들과 왕들', '나이트 크롤러'], ['노인과 바다', '노트북', '마이 블루베리 나이츠'], ['블랙', '노트북', '위대한 비밀', '웜 바디스', '향수 - 어느 살인자의 이야기', '더 코브: 슬픈 돌고래의 진실', '카핑 베토벤', '피아니스트', '아나스타샤'], ['26년', '아이티 거리의 아이들', '공범', '애프터 어스', '조선명탐정: 각시투구꽃의 비밀', '노트북', '태극기 휘날리며', '케이트 앤 레오폴드', '블랙 쉽', '다빈치 코드'], ['밀리언 달러 베이비', '미드웨이', '미이라 2', '터미네이터 2:오리지널', '라이온 킹', '킹콩', '변호인', '쥬라기 공원 2 - 잃어버린 세계', '콩: 스컬 아일랜드', '진주만'], ['당신, 거기 있어줄래요', '노트북', '밀정', '도리를 찾아서', '미 비포 유', '비포 선라이즈', '캐롤', '히말라야', '명탐정 코난: 이차원의 저격수', '검은 사제들'], ['사바하', '덩케르크', '플립', '미이라', '서서평, 천천히 평온하게', '보스 베이비', '겟 아웃', '대립군', '캐리비안의 해적: 죽은 자는 말이 없다', '노무현입니다'], ['다운사이징', '비밀은 없다', '나를 잊지 말아요', '트래쉬', '장수상회', '인터스텔라', '엑소더스: 신들과 왕들', '워터 디바이너', '나이트 크롤러', '개를 훔치는 완벽한 방법'], ['용서받지 못한 자', '고사 두 번째 이야기: 교생실습', '메이즈 러너: 스코치 트라이얼', '해바라기', '겨울왕국 2', '82년생 김지영', '알라딘', '자전차왕 엄복동', '토이 스토리 4', '그린 랜턴: 반지의 선택'], ['전국노래자랑', '장고:분노의 추적자', '턱시도', '비커밍 제인', '연애의 온도', '남자사용설명서', '마이 시스터즈 키퍼', '노트북', '내 깡패 같은 애인', '박수건달'], ['삼진그룹 영어토익반', '신의 한 수', '쇼생크 탈출', '엣지 오브 투모로우', '500일의 썸머', '끝까지 간다', '다세포 소녀', '노트북'], ['작은 아씨들', '기생충', '쥬라기 월드: 폴른 킹덤', '분노', '아주 긴 변명', '라라랜드', '너의 이름은.', '노트북', '립반윙클의 신부', '태풍이 지나가고'], ['상어', '노트북'], ['이스케이프 플랜', '쓰리데이즈 투 킬', '행복을 찾아서', '이상한 나라의 앨리스', '쿵푸 팬더 2', '할로우 맨', '테이큰 2', '논스톱', '익스펜더블 2', '터미네이터 2:오리지널'], ['항거:유관순 이야기', '나를 찾아줘', '약장수', '암수살인', '인랑', '게이트', '풍운', '다운사이징', '에이리언: 커버넌트', '툼디:부러진 검의 전설'], ['클레멘타인', '연평해전', '검객', '강철비2: 정상회담', '밤쉘: 세상을 바꾼 폭탄선언', '화려한 휴가', '주디', '타오르는 여인의 초상', '두 교황', '1917'], ['록키 4', '지금, 만나러 갑니다', '이프 온리', '웨딩 싱어', '워킹걸', '노트북', '어바웃 타임', '월-E'], ['오션스8', '목소리의 형태', '뷰티 인사이드', '노트북', '소원', '라스트 에어벤더', '어벤져스'], ['가장 보통의 연애', '극한직업', '스윙키즈', '노트북', '브리짓 존스의 베이비', '싱 스트리트', '캡틴 아메리카: 시빌 워', '주토피아', '러브레터', '검사외전'], ['먼 훗날 우리', '밀리언 달러 베이비', '너의 이름은.', '노트북'], ['어바웃 타임', '노트북', '월터의 상상은 현실이 된다'], ['허삼관', '앵두야, 연애하자', '노트북', '신세계', '남영동1985', '회사원', '나쁜 피', '조조- 황제의 반란 ', '피에타', '간첩'], ['혼숨', '노트북', '아가씨'], ['플립', '주토피아', '겟썸 3', '고지전', '탐정 홍길동: 사라진 마을', '혹성탈출: 반격의 서막', '메이즈 러너: 스코치 트라이얼', '아가씨', '김복남 살인사건의 전말', '업사이드 다운'], ['판의 미로 - 오필리아와 세 개의 열쇠', '판도라', '어바웃 타임', '노트북'], ['뉴 뮤턴트', '걸캅스', '캡틴 마블', '나는 내일, 어제의 너와 만난다', '로건', '닥터 스트레인지', '노트북', '라라랜드'], ['런', '다만 악에서 구하소서', '오케이 마담', '위대한 쇼맨', '온워드: 단 하루의 기적', '반도', '신의 한 수: 귀수편', '원스', '조커', '원스 어폰 어 타임... 인 할리우드'], ['러스트 앤 본', '안녕, 나의 소울메이트', '오멘 2', '신과함께-죄와 벌', '그것만이 내 세상', '내 이름은 칸', '약장수', '내가 널 사랑할 수 없는 10가지 이유', '기억의 밤', '미옥'], ['노트북']]



for v in range(5):
    for i in range(10):
        time.sleep(.4)
        # 관람객을 클릭했을때 나타나는 영화리스트
        watcher = driver.find_element("xpath",'/html/body/div/div/div[5]/ul/li[{num}]/div[2]/dl/dt/em[1]/a/span'.format(num=i+1))
        
        watcher.click() #Clicks the element.
        time.sleep(0.4)
        page = driver.page_source
        driver.back() #Goes one step backward in the browser history.
        info = bs(page,'lxml')
        td_list = info.find_all('td','title')
        lst = []
        for i in range(len(td_list)):
            lst.append(td_list[i].a.string)
            total_lst.append(lst)
            time.sleep(0.4)
            
    time.sleep(.4)
    next_page = driver.find_element("xpath",'//*[@id="pagerTagAnchor{num2}"]/span'.format(num2 = v+2))
    time.sleep(.4)
    next_page.click()
print(total_lst)
print("토탈 리스트 완료")
print("전체 길이 :")
print(len(total_lst))
print(total_lst.count(total_lst[0]))
# ['부산행', '맨 인 더 다크', '노트북', '아수라']
x = 0;
#%% 영화 댓글을 쓴 횟수가 1 이상이어서 두번 이상 반복되는 자료는 삭제함.
# 42로 하면 된다
# 범위만 다시 잘 잡으면 될 듯?
print("for문 시작 전 len(total_lst) : %d" % len(total_lst))
for i in range(len(total_lst)):
    print("2차 for문 i : %d" % i)
    print("전체 len : %d" % len(total_lst))

    if(len(total_lst) == i):
        print("ㅁㅁㅁㅁㅁlen(total_lst) == iㅁㅁㅁㅁㅁ")
        break;
    
    if total_lst.count(total_lst[i]) != 1:
        try:
            while(total_lst.count(total_lst[i]) != 1):
                total_lst.remove(total_lst[i])
        except:
            continue
    print("---------------------------")
#%%
print(total_lst)
print("반복 요소 제거 완료")
#외부 파일에 저장

f = open(urls+'/Spidy_movieList.txt','w')
#f = open('Spidy_movieList.txt','w')
f.write(str(total_lst))
f.close()
print("2차 파일 저장")