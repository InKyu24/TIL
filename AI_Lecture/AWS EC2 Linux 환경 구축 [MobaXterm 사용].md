# AWS EC2 Linux 환경 구축 [MobaXterm 사용]

## EC2 시간 변경

```bash
date

sudo rm /etc/localtimesudo ln -s -f  /usr/share/zoneinfo/Asia/Seoul /etc/localtime

date
```



## EC2 호스트명 변경

```bash
hostname

sudo vi /etc/cloud/cloud.cfg
	preserve_hostname: true

sudo vi /etc/hosts
	# host 변경

sudo vi /etc/hostname
	# hostname 변경

sudo reboot
```



## Docker 설치

```bash
sudo apt install docker.io
```



## Oracle 설치 [[참고]](https://hub.docker.com/r/deepdiver/docker-oracle-xe-11g)

```bash
mkdir -p ~/0cik/oracle_db

cd ~/0cik/oracle_db

sudo docker run -d --name oracle -p 40022:22 -p 41521:1521 -p 48080:8080 -v ~/0cik/oracle_db:/opt/oracle/oradata deepdiver/docker-oracle-xe-11g
```



## SQL Developer 를 이용한 데이터 구축

1. 새 접속

2. 접속 이름을 입력

3. 사용자 이름(system), 비밀번호(oracle)을 입력

4. 호스트 이름(IP 주소), 포트(41521)를 입력

5. 테스트 성공을 확인한 뒤, 저장하고 접속

   

6. 다른 사용자 카테고리에서 마우스 우클릭 후 사용자 생성

7. 사용자 이름 및 비밀번호 입력

8. 기본 테이블스페이스(USERS) 선택

9. 임시 테이블스페이스(TEMP) 선택

10. 부여된 롤 탭에서 롤 이름이 CONNECT와 RESOURCE인 행에 권한이 부여됨에 각각 체크

11. 할당량 탭에서 USERS에 할당량을 입력하고 단위(M) 입력

    

12. 새 접속

13. 접속 이름을 입력

14. 다른 사용자 카테고리에서 작성한 내용으로 사용자 이름과 비밀번호를 입력

15. 호스트 이름(IP 주소), 포트(41521)를 입력

16. 테스트 성공을 확인한 뒤, 저장하고 접속

    

17. SQL 워크시트에 질의 작성 및 실행으로 데이터 구축



## Spring boot 설정

1. application.properties에서 JDBC 설정 변경(url)

2. pom.xml에서 ojdbc 버전을 10으로 변경

   

3. Run as > Maven build 클릭

4. target 폴더에 배포파일 생성

5. Goals에 package 입력 및 Profile에 pom.xml 삭제 후 Run 버튼 클릭

6. target 폴더에 배포파일이 생성된 것을 확인

7. war 파일을 본 프로젝트 바로 하단으로 이동, 파일명을 project.war로 변경

8. 프로젝트 내에 new > file을 통해 Dockerfile 생성

   ```dockerfile
   FROM openjdk:11-jdk as builder
   ARG JAR_FILE=./project.war
   ENV TZ=Asia/Seoul
   COPY ${JAR_FILE} app.war
   ENTRYPOINT ["java","-jar","app.war"]
   ```

9. github에 저장소를 생성한 뒤, 프로젝트를 해당 저장소에 push & commit

   

## EC2 

1. git_registry 폴더 생성 및 해당 위치로 이동

   ```bash
   mkdir git_registry
   
   cd git_registry
   ```

2. 저장소에 올라가 있는 프로젝트 clone

   ```bash
   git clone [저장소 링크]
   ```

3. DockerHub에 프로젝트 올리기

   ```bash
   sudo docker build -t [DockerHub 아이디]/[프로젝트 이름] .  
   ```

4. EC2 내에서 프로젝트 실행

   ```bash
   sudo docker run -p 8090:8090 -p 9999:9999 [DockerHub 아이디]/[프로젝트 이름]
   ```

5. 웹 브라우저 주소창에 [ip주소:8090]으로 연결하면 프로젝트를 확인할 수 있다.











