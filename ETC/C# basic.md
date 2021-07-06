## C#

#### C# 프로그래밍 언어

+ 모든 C# 프로그램은 Main() 이라는 시작 메서드를 갖는다.
+ Main()는 static으로 선언되며, 인자는 string[] 이다.
+ System.Console은 `.NET Framework` 클래스이며, WriteLine은 화면에 데이터를 출력하는 메서드이다.

```c#
namespace Intro_Ex1
{
    class Program
    {
        static void Main(string[] args)
        {
            System.Console.WriteLine("Hello World...");
        }
    }
}
```

> `.NET Framework` : 마이크로소프트사에서 제공하는 윈도우 프로그램 개발 및 실행환경으로, CLS를 따르는 모든 언어는 .NET Framework에서 실행가능 하며, CLR이라는 가상 기계 위에서 작동하기 때문에 플랫폼에 독립적인 특징이 있다.
>
> `CLS (Common Language Specification)` :  닷넷 호환 언어가 지켜야 할 최소한의 언어 사양
>
> `CLR (Common Language Runtime)` : 마이크로소프트에서 개발한 CLI를 따르는 가장 대표적인 VM



#### C# 데이터 타입

+ C#과 같은  `.NET 프로그래밍 언어`는 .NET의 Common Type System에 정의된 .NET 데이타 타입을 사용한다.

+ C#은 int, double, string 과 같은 C# 키워드로 데이타 타입을 표현할 수 있다.
+ 또한 `System.Int32`, `System.Double`, `System.String` 과 같은 .NET 데이타 클래스로 데이타 타입을 표현할 수도 있다. 내부적으로는 C# 컴파일러는 C# 키워드로 된 데이타 타입을 컴파일 후 .NET 데이타 타입으로 변경하게 된다.

| C# 데이터 타입 | .NET 데이터 타입 | 설명                                                 |
| :------------- | :--------------- | :--------------------------------------------------- |
| bool           | System.Boolean   | True or False                                        |
| byte           | System.Byte      | 8비트 unsigned integer                               |
| sbyte          | System.SByte     | 8비트 signed integer                                 |
| short          | System.Int16     | 16비트 signed integer                                |
| int            | System.Int32     | 32비트 signed integer                                |
| long           | System.Int64     | 64비트 signed integer                                |
| ushort         | System.UInt16    | 16비트 unsigned integer                              |
| uint           | System.UInt32    | 32비트 unsigned integer                              |
| ulong          | System.UInt64    | 64비트 unsigned integer                              |
| float          | System.Single    | 32비트 single precision 부동소수점 숫자              |
| double         | System.Double    | 64비트 double precision 부동소수점 숫자              |
| decimal        | System.Decimal   | 128비트 Decimal                                      |
| char           | System.Char      | 16비트 유니코드 문자                                 |
| string         | System.String    | 유니코드 문자열                                      |
|                | System.DateTime  | 날짜와 시간, 별도의 C# 키워드가 없음                 |
| object         | System.Object    | 모든 타입의 기본 클래스로 모든 유형을 포함할 수 있음 |

##### C# 리터럴 데이터

+ C# 코드에서 123, true, "ABC"와 같이 값을 직접 써줄 수 있는데, 이를 리터럴이라 한다.

+ C#에서 별도의 접미어(suffix)가 없이 리터럴 데이터를 사용하는 경우, C# 컴파일러는 기본적으로 데이터 타입에 그 값을 할당한다. 따라서 특정 데이터 타입을 지정하고 싶으면, 리터럴 데이터 뒤에 접미어를 추가해야 한다.

+ 접미어는 대소문자 구분을 하지 않는다.
+ **float** 데이터 타입은 숫자 뒤에 123.45F와 같이 **F**를 붙여 double이 아닌 float 타입임을 나타낸다.
+ **double** 데이터 타입은 숫자 뒤에 123.45D과 같이 **D**를 붙이거나 혹은 아무것도 붙이지 않음으로 해서 double 타입임을 나타낸다.
+ **decimal** 데이터 타입은 숫자 뒤에 123.45M과 같이 **M**를 붙여 decimal 타입임을 나타낸다.
+ **char** 데이터 타입은 작은따옴표 `'` (single quotation)을 사용하여 한 문자를 할당한다.
+ **string** 데이터 타입은 큰따옴표 `"` (double quotation)을 사용하여 문자열을 할당한다

```C#
// Bool
bool b = true;

// Numeric
short sh = -32768;   
int i = 2147483647;  
long l = 1234L;      // L suffix
uint ui = 1234U		 // U suffix
ulong ul = 1234UL	 // UL suffix
float f = 123.45F;   // F suffix
double d1 = 123.45; 
double d2 = 123.45D; // D suffix
decimal dm = 123.45M; // M suffix

// Char/String
char c = 'A';
string s = "Hello";

// DateTime  2011-10-30 12:35
DateTime dt = new DateTime(2011, 10, 30, 12, 35, 0);
```

##### 최대값, 최소값

+ 숫자형 데이터 타입의 최대값 혹은 최소값을 알아내기 위해서는 .NET 데이터 타입 클래스들의 MaxValue, MinValue 프로퍼티를 사용한다. C# 데이터 타입 키워드 뒤에서도 이러한 프로퍼티를 직접 호출할 수 있다.

+ 즉, int.MaxValue 혹은 Int32.MaxValue 처럼 사용할 수 있다.

```c#
int i = int.MaxVaule;
float f = float.MinValue
```

##### NULL

+ 어떤 변수가 메모리 상에 어떤 데이터도 가지고 있지 않다는 것을 의미하며, C#에서는 소문자 null 이라는 키워드를 사용한다.

+ 모든 데이터 타입이 null을 가질 수 있는 것은 아니며, null을 가질 수 있는 Reference 타입과 null을 가질 수 없는 value 타입으로 구분된다.

##### Nullable Type

+ 정수(int)나 날짜(DateTime)와 같은 value 타입은 일반적으로 null을 가질 수 없으나, C# 2.0에서부터 이러한 타입들에 null을 가질 수 있게 하였는데, 이를 Nullable Type이라 부른다.
+ int나 DateTime 타입명 뒤에 물음표 `?` 를 붙이면 Nullable Type이 된다.
+ Nullable Type을 다시 일반 value 타입으로 변경하기 위해서는 Nullable의 .Value 속성을 사용한다.

```c#
// Nullable 타입
int? i = null;
i = 101;
            
bool? b = null;

//int? 를 int로 할당
Nullable<int> j = null;
j = 10;
int k = j.Value;
```



#### C# 변수 및 상수

##### C# 변수

+ C# 변수는 메서드 안에서 로컬변수로 선언되거나, 클래스 안에서 멤버들이 사용하는 전역변수로 선언될 수 있다.
+ 로컬변수는 기본값을 할당받지 못하기 때문에 사용 전에 값을 할당해야 한다.
+ 전역변수는 값을 할당하지 않으면 기본값이 자동으로 할당된다.

```c#
using System;

namespace ConsoleApplication1
{
    class CSVar
    {
        //필드 (클래스 내에서 공통적으로 사용되는 전역 변수)
        int globalVar;
        const int MAX = 1024;

        public void Method1()
        {
            // 로컬변수
            int localVar;

            // 아래 할당이 없으면 에러 발생
            localVar = 100;

            Console.WriteLine(globalVar);	// int 타입의 기본값 0이 할당된다.
            Console.WriteLine(localVar);
        }
    }

    class Program
    {
        // 모든 프로그램에는 Main()이 있어야 함.
        static void Main(string[] args)
        {
            // 테스트
            CSVar obj = new CSVar();
            obj.Method1();
        }
    }
}
```

##### C# 상수

+ C# 상수는 C# 키워드 const를 사용하여 정의한다.
+ 상수는 초기에 정한 값은 중간에 변경할 수 없다.
+ const는 필드 선언부에서 사용되거나 메서드 내에서 사용될 수 있으며, 컴파일시 상수값이 결정된다.
+ readonly 키워드를 사용하여 읽기전용 (개념적으로 상수와 비슷한) 필드를 만들 수 있다. readonly는 필드 선언부나 클래스 생성자에서 그 값을 지정할 수 있고, 런타임 시 값이 결정된다)

```c#
using System;

namespace ConsoleApplication1
{
    class CSVar
    {
        // 상수
        const int MAX_VALUE = 1024;

        // readonly 필드 
        readonly int Max;
        public CSVar() 
        {
           Max = 1;
        }
        
        //...
    }
}
```



#### C# 배열

+ 배열은 일련의 동일한 데이터 타입 요소들로 구성된 데이터 집합으로서, 인덱스를 통하여 각각의 배열요소에 접근할 수 있다.
+ 배열의 요소는 대괄호 `[]` 안에 인덱스를 넣어 표시한다.
+ C#에서 배열은 1차 배열부터 최고 32차 배열을 가질 수 있다. 2차 이상의 다차원 배열은 각 차원별 요소 크기가 고정된 `Rectangular 배열`과 각 차원별 크기가 다른 `가변 배열`로 나뉠 수 있다.

```c#
// 1차 배열
string[] players = new string[10];
string[] Regions = { "서울", "경기", "부산" };

// 2차 배열 선언 및 초기화
string[,] Depts = {{"김과장", "경리부"},{"이과장", "총무부"}};

// 3차 배열 선언
string[,,] Cubes;
```

##### 가변 배열

다차원 배열에서 각 차원별 배열 요소 크기가 동일한 Recatangular 배열은 `[,]` 와 같이 괄호 안에 쉼표로 분리하여 표현한다. 하지만 각 차원별 배열 요소 크기가 가변적인 가변 배열의 경우에는 `[][]`와 같이 각 차원마다 괄호를 별도로 사용한다.

가변 배열은 배열의 배열이라 불리는데, 첫번째 차원의 크기는 컴파일 타임에 확정되어야 하고, 그 이상 차원은 런타임 시 동적으로 서로 다른 크기의 배열로 지정할 수 있다. 가변 배열은 각 차원별 배열 요소가 불규칙하여 Rectangular 배열처럼 고정된 크기를 사용하면 메모리의 낭비가 심한 경우에 사용하면 유용하다.

```c#
//Jagged Array (가변 배열)
//1차 배열 크기(3)는 명시해야
int[][] A = new int[3][];

//각 1차 배열 요소당 서로 다른 크기의 배열 할당 가능
A[0] = new int[2];
A[1] = new int[3] { 1, 2, 3 };
A[2] = new int[4] { 1, 2, 3, 4 };

A[0][0] = 1;
A[0][1] = 2;
```

##### C# 배열의 사용

C#의 모든 배열은 내부적으로 .NET Framework의 System.Array에서 파생된 것이다. 따라서 System.Array의 메서드, 프로퍼티를 사용할 수 있다.

```c#
static void Main(string[] args)
{
    int sum = 0;
    int[] scores = { 80, 78, 60, 90, 100 };		// 1차원 배열
    for (int i = 0; i < scores.Length; i++)		// 배열 요소들의 총합을 구하는 반복문
    {
        sum += scores[i];
    }
    Console.WriteLine(sum);        
}
```

##### C# 배열의 전달

C#에서 배열 전체를 전달하기 위해서는 보내는 쪽에서는 배열명을 사용하고, 받는 쪽에서 동일한 배열 타입의 배열을 받아들이면 된다.

배열은 레퍼런스 타입이기 때문에, 배열을 다른 객체나 메서드에 전달할 때, 직접 모든 배열 데이터를 복사하지 않고, 참조값만을 전달한다.

```c#
static void Main(string[] args)
{            
    int[] scores = { 80, 78, 60, 90, 100 };
    int sum = CalculateSum(scores); // 배열 전달: 배열명 사용
    Console.WriteLine(sum);        
}

static int CalculateSum(int[] scoresArray) // 배열 받는 쪽
{
    int sum = 0;
    for (int i = 0; i < scoresArray.Length; i++)
    {
        sum += scoresArray[i];
    }
    return sum;
}
```



#### C# 문자열

문자열은 프로그램에서 가장 많이 쓰이는 데이터 타입 중 하나이다. C#에서 문자열은 큰따옴표를 사용하여 표현되며, 단일 문자의 경우에는 작은따옴표를 사용하여 표현된다.

C#의 키워드 string은 .NET의 System.String 클래스와 동일하며, 따라서 System.String 클래스 내에 속한 메서드와 프로퍼티를 사용할 수 있다. 예를 들어 일정 문자열 부분만 뽑아내는 Substring() 메서드, 문자열의 길이를 구하는 Length 속성 등을 모두 사용할 수 있다.

C#의 문자열은 한 번 문자열이 설정되면, 다시 변경할 수 없는 Immutable이라는 특징을 가지고 있다. 예를 들어, 문자열 변수 s가 있을 때, `s="C#";` 이라고 한 후, 다시 `s="F#;` 이라고 실행하면, .NET 시스템은 새로운 string 객체를 생성하여 "F#"이라는 데이터로 초기화한 후 이를 변수명 s에 할당한다.

즉, 변수 s는 내부적으로는 전혀 다른 메모리를 갖는 객체를 가리키는 것이다.

```c#
using System;

namespace MySystem
{
   class Program
   {
      static void Main(string[] args)
      {         
         // 문자열(string) 변수
         string s1 = "C#";
         string s2 = "Programming";

         // 문자(char) 변수 
         char c1 = 'A';
         char c2 = 'B';

         // 문자열 결합
         string s3 = s1 + " " + s2;
         Console.WriteLine("String: {0}", s3);

         // 부분문자열 발췌
         string s3substring = s3.Substring(1, 5);
         Console.WriteLine("Substring: {0}", s3substring);
      }
   }
}
```

##### 문자열, 문자, 문자배열

문자열 (string)은 문자(character)의 집합체이다. 문자열 안에 있는 각 문자를 엑세스하고 싶으면, `[]`를 사용하여 문자 요소를 엑세스한다.

만약 문자열 변수 s가 "Hello"라는 값을 가지고 있을 때, s[0]은 첫번째 문자 H를 리턴하고, s[1]이라면 e를 리턴한다. 문자배열을 문자열로 변환하기 위해서는 new string을 사용한다.

하나의 문자는 상응하는 ASCII 코드 값을 가지기 때문에 문자에 숫자를 더하거나 빼면 다른 문자로 표현될 수 있다.

```c#
using System;

namespace MySystem
{
   class Program
   {
      static void Main(string[] args)
      {         
         string s = "C# Studies";

         // 문자열을 배열인덱스로 한문자 엑세스 
         for (int i = 0; i < s.Length; i++)
         {
            Console.WriteLine("{0}: {1}", i, s[i]);
         }

         // 문자열을 문자배열로 변환
         string str = "Hello";
         char[] charArray = str.ToCharArray();

         for (int i = 0; i < charArray.Length; i++)
         {
            Console.WriteLine(charArray[i]);
         }

         // 문자배열을 문자열로 변환
         char[] charArray2 = { 'A', 'B', 'C', 'D' };
         s = new string(charArray2);

         Console.WriteLine(s);

         // 문자 연산
         char c1 = 'A';
         char c2 = (char)(c1 + 3);
         Console.WriteLine(c2);  // D 출력
      }
   }
}
```

##### StringBuilder 클래스

문자열을 다루는데 중요한 클래스 중의 하나는 System.Text.StringBuilder 클래스이다. String 클래스는 위에서 설명한대로 Immutable이기 때문에, 문자열 갱신을 많이 하는 프로그램에는 적당하지 않다.

반면 Mutable 타입인 StringBuilder 클래스는 문자열 갱신이 많은 곳에서 자주 사용되는데 이는 이 클래스가 별도 메모리를 생성, 소멸하지 않고 일정한 버퍼를 갖고 문자열 갱신을 효율적으로 처리하기 때문이다.

특히 루프 안에서 계속 문자열을 추가 및 변경하는 코드에서는 string 대신 StringBuilder를 사용해야 한다.

```c#
using System;
using System.Text;

namespace MySystem
{
   class Program
   {
      static void Main(string[] args)
      {                  
         StringBuilder sb = new StringBuilder();
         for (int i = 1; i <= 26; i++)
         {
            sb.Append(i.ToString());
            sb.Append(System.Environment.NewLine);
         }
         string s = sb.ToString();

         Console.WriteLine(s);
      }
   }
}
```



#### C# enum(열거형)

+ C#의 키워드 enum은 열거형 상수를 표현하기 위한 것으로 이를 이용하면 상수 숫자들을 보다 의미있는 단어들로 표현할 수 있다. 그 덕분에 프로그램을 읽기 쉽게 해준다.
+ enum의 각 요소는 별도의 지정없이는 첫번째 요소가 0, 두번째 요소가 1, 세번째 요소가 2 등과 같이 1씩 증가된 값들을 할당받는다. 이는 개발자가 임의로 의미있는 번호를 지정해줄 수도 있다.
+ enum 문은 클래스 안이나 네임스페이스 내에서만 선언될 수 있다. 즉 메서드 안이나 속성 안에서는 선언되지 않는다.

```c#
public enum Category
{
   Cake,		// 숫자 0을 갖는다.
   IceCream,	// 숫자 1을 갖는다.
   Bread		// 숫자 2를 갖는다.
}
```

##### enum의 사용

+ enum 타입은 숫자형 타입과 호환이 가능하다. 만약 enum 타입의 변수를 int로 캐스팅하면 해당 enum 값의 숫자 값을 얻게 된다. 또한, enum 타입의 변수는 enum 리터럴값과 서로 비교할 수 있다.

```c#
class Program
{
    enum City
    {
        Seoul,		// 숫자 0을 갖는다. (자동)
        Daejun,  	// 숫자 1을 갖는다. (자동)
        Busan = 5,  // 숫자 5를 갖는다. (수동)
        Jeju = 10   // 숫자 10을 갖는다. (수동)
    }

    static void Main(string[] args)
    {
        City myCity;
        
        // enum 타입에 값을 대입하는 방법
        myCity = City.Seoul;

        // enum을 int로 변환(Casting)하는 방법. 
        // (int)를 앞에 지정.
        int cityValue = (int) myCity;		// int cityValue = 0

        if (myCity == City.Seoul) // enum 값을 비교하는 방법
        {
            Console.WriteLine("Welcome to Seoul");
        }
    }
}
```

##### Flag enum

+ enum의 각 멤버들은 각 비트별로 구분되는 값들(예 : 1, 2, 4, 8, ...)을 가질 수 있는데, 이렇게 enum 타입이 비트 필드를 갖는다는 것을 표시하기 위해 enum 선언문 바로 위에 [Flags] 라는 Attribute를 지정할 수 있다.

+ [Flags] 특성을 갖는 Flag enum은 **OR 연산자를 이용해서 한 enum 변수에 다중값을 가질 수 있으며, AND 연산자를 이용하여 enum 변수가 특정 멤버를 포함하고 있는지 체크할 수 있다.**

```c#
[Flags]
enum Border
{
    None = 0,
    Top = 1,
    Right = 2,
    Bottom = 4,
    Left = 8
}

static void Main(string[] args)
{
    // OR 연산자로 다중 플래그 할당
    Border b = Border.Top | Border.Bottom;	// Border b = 1 + 4

    // & 연산자로 플래그 체크
    if ((b & Border.Top) != 0)				// Border b에 1 값이 있는지 확인
    {
        //HasFlag()이용 플래그 체크
        if (b.HasFlag(Border.Bottom))		// Border b에 4 값이 있는지 확인
        {
            // "Top, Bottom" 출력
            Console.WriteLine(b.ToString());
        }
    }
}
```

https://www.csharpstudy.com/CSharp/CSharp-operator.aspx