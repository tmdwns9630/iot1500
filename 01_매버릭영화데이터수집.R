#22-10-24 월 1일차 // ctrl + Enter로 실행
  setwd("c:/iot1500") # 경로 설정, 큰따옴표 필요.
install.packages("rvest") #웹페이지 통째로 수집
install.packages("httr") #웹서버 접속
install.packages("stringr")
install.packages("wordcloud")
install.packages("RColorBrewer")
library(rvest) #라이브러리를 사용하겠다는 선언
library(httr)
library(stringr)
url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=81888&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='
allreviews = c() #댓글 모은 방// c(배열, 추가할 요소)

for(page in 1:100){
  urls = paste(url,page,sep="")
  htxt = read_html(url)
  comments = html_nodes(htxt,'div.score_result')
  reviews = html_text(comments)
  if(length(reviews)==0){break}
  
  allreviews = c(allreviews,reviews)
  print(page)
}
length(allreviews)
allreviews

write(allreviews,"movie.txt")
write.csv(allreviews,"영화평점수집.csv")


library(KoNLP)
library(wordcloud)
library(RColorBrewer) # 워드 클래스의 색 변경

data1 <- readLines("movie.txt") # 텍스트파일을 라인별로 불러냄.
data1
data2 <- sapply(data1,extractNoun,USE.NAMES=F) #data1에서 각 문장마다 명사를 추출하여 한 줄씩 만든다.
data2

data3 <- unlist(data2) #비순차적으로 정렬
movie_gsub <- str_replace_all(data3,"[^[:alpha:]]","") # 한글 영어 외는 삭제-> 특수문자 제거
gsub("\\d+","",movie_gsub) #gsub: 데이터의 전처리(정제) // 숫자 제거
gsub("\\.","",movie_gsub) #점(.) 제거

movie_gsub <- gsub(" ","",movie_gsub)#공백,비공,...을 공백으로 바꾼다.
movie_gsub <- gsub("비공","",movie_gsub) #데이터 정제는 가장 오래 시간이 걸리는 작업.
movie_gsub <- gsub("중간","",movie_gsub)#보통은 for문으로 돌린다.
movie_gsub <- gsub("영화","",movie_gsub)

movie_gsub <- Filter(function(x){nchar(x) >= 2},movie_gsub)#한글자짜리 문장을 삭제하는 필터링.
movie_gsub

write(unlist(movie_gsub),"Movie2.txt")#비순차적으로 정렬하여 텍스트파일에 저장.

#ㅁㅁㅁㅁㅁㅁㅁㅁㅁ(중요)ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ
data4 <- read.table("Movie2.txt") #공백을 제거하고, 라인별로 데이터를 불러온다.
#사용자가 직접 지울 필요 없다.
#테이블이라는 명칭을 쓰는 이유 : 사용하는 단어수를 카운팅해준다
#==> 많이 쓰는 단어를 간편하게 알 수 있다.
#ㅁㅁㅁㅁㅁㅁㅁㅁㅁ(중요)ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ

wordcount <- table(data4) #테이블 데이터의 개수를 변수에 할당.
head(sort(wordcount, decreasing=T),10) #디크리징:내림차순으로 정렬, 10개를 뽑아낸다.
palete <- brewer.pal(9,"Set3") #시간 관계상 패스. 색깔 관련

wordcloud(names(wordcount),freq=wordcount,scale=c(5,1),rot.per=0.25,min.freq=1,random.order=F,random.color=T,colors=palete)
#wordcloud : 구름 모양을 만든다.
#freq:빈도수, scale:글자크기(5:1), rot.per=세로비율이 25%, 
#min.freq=표시할 최소빈도수(2로 하면 한번 나온건 안나온다.),
#random.order:랜덤하게 나옴
#랜덤컬러:랜덤컬러.
#colors=색 지정, palete에서 가져옴(여기서 grey,red로 하면 회색, 빨간색만 나온다.)
#=====여기까지 워드 클라우드 만들기=====

#=====데이터 시각화======
#▶ 추천수가 많은 상위 10개 골라서 pie 그래프를 그리기.

top10 <- head(sort(wordcount, decreasing = T),10) #상위 10개를 내림차순 정렬로 top10에 저장.
pie(top10, main="영화평점댓글 TOP 10") #그래프를 만든다(사용할데이터,타이틀명)
pie(top10,col=rainbow(10),radius=1,main="영화평점댓글 TOP 10")
#(사용할데이터,항목마다 쓸 색깔,반지름 길이,타이틀명)
top10
pct <- round(top10/sum(top10)*100,1) #항목별로 백분율을 구해서 pct에 저장.  
pct
names(top10) #Object에 이름 부여. ???

lab <- paste(names(top10),"\n",pct,"%") #합친다?
#lab
pie(top10, main="영화평점댓글 TOP 10",col=rainbow(10),cex=0.8,labels=lab)

bchart <- head(sort(wordcount, decreasing = T),10)
bchart
bp <- barplot(bchart, main="영화평점댓글 TOP 10",col=rainbow(10),cex.names=0.9,las=1,ylim=c(0,3000))
#막대 그래프를 만든다.
#cex.name : 가로의 이름 크기 설정
#las : 1=가로로 쓰기, 2=세로로 쓰기
#ylim:그래프의 y축 좌표축 값 범위(최소값, 최대값)
pct <- round(bchart/sum(bchart)*100,1)
pct

text(x=bp, y=bchart*1.05, labels=paste("(",pct,"%",")"),col="black",cex=0.7)
text(x=bp, y=bchart*0.95, labels=paste(bchart,"건"),col="black",cex=0.7)
#text() : plot region에 문자를 입력하는 함수.
#(x좌표,y좌표,출력할문자열,색깔,문자크기)

barplot(bchart,main="영화평점댓글 TOP 10",col="grey",xlim=c(0,1000),cex.name=0.7,las=1,horiz=T)
#xlim:그래프의 x축 좌표축 값 범위(최소값, 최대값)
#horiz:TRUE를 지정하면 막대를 옆으로 눕혀서 그린다. 
text(x=bchart*0.9, y=bp, labels=paste(bchart,"건"),col="black",cex=0.7)
text(x=bchart*1.8, y=bp, labels=paste("(",pct,"%",")"),col="black",cex=0.7)


