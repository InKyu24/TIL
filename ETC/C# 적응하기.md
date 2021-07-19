#### C# console 살펴보기

```c#
// java의 import
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// java의 package와 같은 역할을 하는 namespace [java처럼 path가 길어지지 않는다]
namespace CSharpStudy
{
    class Program
    {
        static void Main(string[] args)
        {
            // System.out.println
            Console.WriteLine("안녕 C#!");
            // System.out.print
            Console.Write("Hello c#");
        } 
    }
}
```

#### C# 변수 선언

```c#
static void Main(string[] args)
{
    short shortNum = 0;
    int intNum = 0;
    double doubleNum = 0;
    float floatNum = 0;

    // java와 달리 s가 소문자, 큰 따옴표 사용
    string stringText = "";
    // 작은 따옴표 사용
    char charText = 'a';
    // java와 달리 boolean이 아닌 bool
    bool boolVal = true;

    // .NET Framework 변수 선언 [Ctrl + . 을 누르게 되면 vs에서 제공하는 제안을 볼 수 있다.]
    Int16 dotNetShort = 0;
    Int32 dotNetInt = 0;
    Int64 dotNetDouble = 0;
    String dotNetString = "";

    // dynamic 타입 선언 [var에 커서를 대보면 자동으로 지정된 타입을 확인할 수 있다.]
    var dynamicType = 0;
} 
```

#### C# if

```c#
static void Main(string[] args)
{
    var num = 1;
    Console.Write("0~9 사이의 값을 입력:");

    var input = Console.ReadLine();

    if (num.ToString() == input)
    {
        Console.WriteLine("같은 값을 입력");
    }
    else
    {
        Console.WriteLine("다른 값을 입력");
    }
} 
```

#### C# while

```c#
static void Main(string[] args)
{
    Console.WriteLine("3의 배수가 아닌 수를 출력한다.");
    var num = 0;
    while (true)
    {
        num++;
        if (num % 3 == 0)
        {
            continue;
        }
        Console.WriteLine(num);
        if (num == 100)
        {
            break;
        }
    }
} 
```

#### C# do while

```c#
static void Main(string[] args)
{   
	Console.WriteLine("1~10 출력");
    var num = 1;
    do
    {
        Console.WriteLine(num++);
    } while (num <= 10);
}
```

#### C# for

```c#
static void Main(string[] args)
{
    for (var i = 0; i<=10; i++)
    {
        Console.WriteLine(i);
    }
} 
```

```c#
static void Main(string[] args)
{
    var num = 0;
    for (; num<=10; num++)
    {
        Console.WriteLine(num);
    }
} 
```

#### C# foreach

```c#
// for문을 이용한 경우
static void Main(string[] args)
        {
            List<int> numberList = new List<int>();

            numberList.Add(1);
            numberList.Add(2);
            numberList.Add(3);
            numberList.Add(4);
            numberList.Add(5);

            for (var index = 0; index < numberList.Count; index++)
            {
                Console.WriteLine(numberList[index]);
            }
        }
```

```c#
// foreach문을 이용한 경우
static void Main(string[] args)
{
    List<int> numberList = new List<int>();

    numberList.Add(1);
    numberList.Add(2);
    numberList.Add(3);
    numberList.Add(4);
    numberList.Add(5);

    foreach (var num in numberList)
    {
        Console.WriteLine(num);
    }
}
```

#### C# Generic List

```c#
static void Main(string[] args)
{
    // Generic List 생성방법 1
    List<int> numberList = new List<int>();
    numberList.Add(1);
    numberList.Add(2);
    numberList.Add(3);

    // Generic List 생성방법 2
    var stringList = new List<string>();
    stringList.Add("text1");
    stringList.Add("text2");
    stringList.Add("text3");

    // Generic List 생성방법 3
    var doubleList = new List<double>()
    {
        1.0,
        2.0,
        3.0
    };
}
```

#### C# 사용자 정의 타입

```java
// java에서 쓰는 방식 
class User {
    private int no;
    private String name;

    public void setNo (int no) {
        no = no;
    }
    public int getNo (int no) {
        return no;
    }
    public void setName (String name) {
        name = name;
    }
    public String getName (String name) {
        return name;
    }
}
```

```c#
class User
    {
        // prop 작성 후 tab 키
        public int No { get; set; }
        public string Name { get; set; }
        public int Age { get; set; }
        public string Phone { get; set; }
    }
```

```c#
class Program
{
    static void Main(string[] args)
    {
        // 번호 이름 나이 연락처
        // 1 최인규 30 010-7193-1234
        // 2 최경석 24 010-3745-1234

        var user1 = new User()
            user1.No = 1;
        user1.Name = "최인규";
        user1.Age = 30;
        user1.Phone = "010-7193-1234";

        var user2 = new User();
        user2.No = 2;
        user2.Name = "최경석";
        user2.Age = 24;
        user2.Phone = "010-3745-1234";

        var list = new List<User>
        {
            user1,
            user2
        };

        foreach(var user in list)
        {
            Console.WriteLine("번호:" + user.No + " 이름:" + user.Name + " 나이:" + user.Age + " 전화번호:" + user.Phone);
        }
    }
}
```

```c#
// 위의 Program 클래스 코드 더 간략하게 정리 가능
class Program
{
    static void Main(string[] args)
    {
        // 번호 이름 나이 연락처
        // 1 최인규 30 010-7193-1234
        // 2 최경석 24 010-3745-1234

        // ctrl + space 를 활용
        var list = new List<User>
        {
            new User()
            {
                No = 1,
                Name = "최인규",
                Age = 30,
                Phone = "010-7193-8445"
            },
            new User()
            {
                No = 2,
                Name = "최경석",
                Age = 24,
                Phone = "010-3745-1234"
            }
        };

        foreach(var user in list)
        {
            Console.WriteLine("번호:" + user.No + " 이름:" + user.Name + " 나이:" + user.Age + " 전화번호:" + user.Phone);
        }
    }
}
```

#### C# Class, method, 클래스 라이브러리

```java
// java에서의 메소드 선언
public void howToMakeJavaMethod() {
}
```

```c#
// c#에서의 메서드 선언
public void HowToMakeCSharpMethod()
{
    
}
```

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using FristLibrary;

namespace CSharpStudy
{
    class Program
    {
        static void Main(string[] args)
        {
            // 같은 솔루션, 같은 프로젝트 내 다른 클래스 [접근제한자 public]
            Calc calc = new Calc();
            calc.Hello1();
			
            // 같은 솔루션, 다른 프로젝트 내 클래스 [using]
            FirstClass first = new FirstClass();
            first.FirstClassPrint();
        }
    }
}
```

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpStudy
{
    class Program
    {
        static void Main(string[] args)
        {
            FirstClass first = new FirstClass();
            first.FirstClassPrint();
        }
    }
}
```

#### C# DB connection

* Java에서의 DB 연결
  1. JDBC
  2. JDBC ibatis, mybatis
  3. JDBC Hibernate [ORM]
* C#에서의 DB 연결
  1. ADO.NET
  2. Enterprise Library
  3. EntityFramework [ORM]

#### ASP.NET

1. Web Form

   웹 페이지 내에 소스 코드 존재할 수 있다. -> 유지보수가 굉장히 어려움

2. ASP.NET MVC

   Web Form의 유지보수 단점 해소

3. SignalR (ex. 실시간 채팅)

4. Web API

   DB에서 나온 정보를 XML, JSON 형식으로 송출해주는 서비스



#### C# Controller에서 View로 데이터 전달하기

##### * 방법 1

```c#
// Controller
public IActionResult Index()
{
    var hongUser = new User
    {
        UserNo = 1,
        UserName = "홍길동"
    };
    return View(hongUser);
}
```

```html
<!-- Viewer -->
<h2> 사용자 번호 : @Model.userNo </h2>
<h2> 사용자 이름 : @Model.userName </h2>
```

##### * 방법 2

```c#
// Controller
public IActionResult Index()
{
    var hongUser = new User
    {
        UserNo = 1,
        UserName = "홍길동"
    };
    ViewBag.Hong = hongUser;
    return View();
}
```

```html
<!-- Viewer -->
<h2> 사용자 번호 : @ViewBag.Hong.userNo </h2>
<h2> 사용자 이름 : @ViewBag.Hong.userName </h2>
```

##### * 방법 3

```c#
// Controller
public IActionResult Index()
{
    var hongUser = new User
    {
        UserNo = 1,
        UserName = "홍길동"
    };
	ViewData["HongNo"] = hongUser.UserNo;
    ViewData["HongName"] = hongUser.UserName;
    return View();
}
```

```html
<!-- Viewer -->
<h2> 사용자 번호 : @ViewData["HongNo"] </h2>
<h2> 사용자 이름 : @ViewData["HongName"] </h2>
```
