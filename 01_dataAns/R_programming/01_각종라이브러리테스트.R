#install한 패키지는 추후엔 library 명령어만 넣으면 된다.

setwd("c:/iot1500") # 경로 설정, 큰따옴표 필요.
a = "선문대에서 가장 맛있는 점심은 짜장면이다."
extractNoun(a)
install.packages("KoNLP")

Koinstall = c('rJava', 'stringr', 'hash', 'tau', 
              'Sejong', 'RSQLite', 'devtools','vctrs')
install.packages(Koinstall)
library(rJava)
library(stringr)
library(KoNLP) #scala-library-2.11.8를 따로 다운 받아서 경로에 복사해줘야 한다.
useSejongDic() 
extractNoun('역시 요리는 맛있는 국밥 ') 

install.packages("multilinguer")
library(multilinguer)
multilinguer::install_jdk()
install.packages(c("hash", "tau", "Sejong", "RSQLite", "devtools", "bit", "rex", "lazyeval", "htmlwidgets", "crosstalk", "promises", "later", "sessioninfo", "xopen", "bit64", "blob", "DBI", "memoise", "plogr", "covr", "DT", "rcmdcheck", "rversions"), type = "binary")
# github 버전 설치
install.packages("remotes")
# 64bit 에서만 동작합니다.
# 이 부분에서 오류 나시는 분들은 다음 코드를 실행하세요.
remotes::install_github('haven-jeon/KoNLP', upgrade = "never", INSTALL_opts=c("--no-multiarch")) 
# 강제로 코드실행
devtools::install_github('haven-jeon/KoNLP',force=TRUE)

                   
                  l)

