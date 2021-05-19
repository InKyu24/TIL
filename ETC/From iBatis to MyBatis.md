### iBatis와 MyBatis 간 차이

| iBatis                       | MyBatis             | 비고             |
| ---------------------------- | ------------------- | ---------------- |
| com.ibatis.*                 | org.apache.ibatis.* | 패키지 구조 변경 |
| SqlMapConfig                 | Configration        | 용어변경         |
| sqlMap                       | mapper              | 용어변경         |
| sqlMapClient                 | sqlSession          | 구문대체         |
| rowHandler                   | resultHandler       | 구문대체         |
| resultHandler                | SqlSessionFactory   | 구문대체         |
| parameterMap, parameterClass | parameterType       | 속성 통합        |
| resultClass                  | resultType          | 용어변경         |
| #var#                        | #{var}              | 구문대체         |
| $var$                        | ${var}              | 구문대체         |
| <isEqual> , <isNull>         | <if>                | 구문대체         |



### MyBatis 차별점

#### annotation 도입

- annotation 을 적극 도입하여 DAO 에 대해서 행하던 sqlMapClient DI 설정을 안해도 된다.
- spring 2.5 대 부터 annotation 이 도입되어서 설정이 매우 간편해진 것 처럼 무척 간편해졌다.
- bean id sqlSessionFactory, sqlSessionTemplate 만 지정하면 된다.

#### rowHandler 대체

- xml 및 대량 데이터 처리를 위해 사용하였던 rowHandler가 삭제되었다.
- sqlMapClient 가 없어지고 sqlSession 으로 대체 되었는데, sqlSession 의 API 를 살펴보니 large data 처리용 method 를 제공한다.
- rowHandler 가 resultHandler 로 바뀌었다.
- 큰 변화중 하나는 자바 애노테이션을 사용해서 xml을 사용하지 않고 모든것을 자바로만 할 수 있게 되었다. 물론 Configration.xml 도 자바에서 직접 DataSource, Environment 등을 선언해서 클래스화 시킬수 있다.
- 주의할점은 xml로 Configure를 만들고 환경변수와 property를 클래스로도 만들었다면, 클래스쪽이 나중에 읽어지게 되서 xml로 되어있는 세팅이 자바 클래스에서 선언해놓은것으로 덮어써지게 된다. 혼란을 줄수 있으니 한가지 방법만으로 프로젝트를 구성하는것이 좋을것이다.
- Configuration configuration = new Con…. 형식으로 선언을 하고 나서는 mapper도 xml이 아니고 configuration.addMapper(UserMapper.class) 형식으로 추가 해야 하기 때문에 어느쪽으로 할것인지 확실하게 결정을 하고 나서 진행해야 한다.

#### 네임스페이스 방식 변경

- sqlMap 파일별로 줄여놓은 이름을 사용했다면 이제 풀경로로 사용하게 된다.

  (혼란을 줄이고 어떤것이 호출되는지 정확하게 알 수 있다)

| iBatis                    | MyBatis                                        |
| ------------------------- | ---------------------------------------------- |
| <sqlMap namespace="User"> | <mapper namespace="myBatis.mapper.UserMapper"> |



### iBatis에서 MyBatis로 전환 [단계별]

1. pom.xml에서 mybatis dependency 추가

2. dispatcher-servlet.xml에서

   ```xml
   기존 ibatis
   
   <beans:bean id="sqlMapClient" class="org.springframework.orm.ibatis.SqlMapClientFactoryBean">
     <beans:property name="configLocations" value="classpath:/sqlmap/SqlMapConfig.xml" />
         <beans:property name="dataSource" ref="dataSource" />
         <beans:property name="mappingLocations">
          <beans:list>
           <beans:value>classpath:/sqlmap/**/*.xml</beans:value>
          </beans:list>
         </beans:property>
     </beans:bean>
   
   <beans:bean id="sqlMapClientTemplate" class="org.springframework.orm.ibatis.SqlMapClientTemplate">
      <beans:property name="sqlMapClient" ref="sqlMapClient" />
     </beans:bean>
   
   신규 mybatis
   
   <beans:bean id="sqlSessionFactoryBean" class="org.mybatis.spring.SqlSessionFactoryBean">
      <beans:property name="dataSource" ref="dataSource" />
      <beans:property name="configLocation" value="classpath:/mybatis-config.xml" />
      <beans:property name="mapperLocations">
       <beans:array>
        <beans:value>classpath*:/sqlmap/**/*.xml</beans:value>
       </beans:array>
      </beans:property>
     </beans:bean>
    
    <beans:bean id="SqlSession" class="org.mybatis.spring.SqlSessionTemplate">
     <beans:constructor-arg index="0" ref="sqlSessionFactoryBean" />
    </beans:bean>
   
   transactionManager 도 동일하게 사용한다.
   ```

3. sqlMapConfig를 Configration으로 변경

   ```xml
   기존 ibatis
   <?xml version="1.0" encoding="UTF-8" ?>
   <!DOCTYPE sqlMapConfig      
       PUBLIC "-//ibatis.apache.org//DTD SQL Map Config 2.0//EN"      
       "http://ibatis.apache.org/dtd/sql-map-config-2.dtd">
   
   <sqlMapConfig>
   	<settings useStatementNamespaces="true"	/>	
   	<sqlMap resource="kr/co/openeg/lab/member/dao/member.xml" />
   	<sqlMap resource="kr/co/openeg/lab/board/dao/board.xml" />
   	<sqlMap resource="kr/co/openeg/lab/login/dao/login.xml" />
   </sqlMapConfig>
   
   
   신규 mybatis
   
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE configuration
       PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
       "http://mybatis.org/dtd/mybatis-3-config.dtd">
   
   <configuration>
   
   	<typeAliases>
   		<typeAlias type="kr.co.openeg.lab.login.model.LoginHistory" alias="LoginHistory"/>
   		<typeAlias type="kr.co.openeg.lab.login.model.LoginSessionModel" alias="LoginModel"/>
   		<typeAlias type="kr.co.openeg.lab.board.model.BoardCommentModel" alias="BoardCommentModel"/>
   		<typeAlias type="kr.co.openeg.lab.board.model.BoardModel" alias="BoardModel"/>
   		<typeAlias type="kr.co.openeg.lab.member.model.MemberModel" alias="MemberModel"/>
   		<typeAlias type="kr.co.openeg.lab.member.model.MemberSecurity" alias="MemberSecurity"/>
   	</typeAliases>
   </configuration>
   ```

