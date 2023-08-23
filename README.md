# Csharp_Study
C#공부
[구조적인 프로그래밍]

1. 변수와 상수

2. 제어문 (if else, switch case)

3. 반복문(for, while, do while)

4. 메소드(함수)

5. 배열 [자료구조 -->Array, Stack, Queue, Tree, Graph ...]

[객체지향 프로그래밍]

1. 추상화(Abstract), 캡슐화(encapsulation)

2. 다형성(polymorphism)[Overloading, Overridding]

3. 상속(Inheritance)

4. 인터페이스(Interface)

5. 박싱,언박싱(Boxing, UnBoxing)

6. 래퍼 클래스(Wrapper Class)

7. 깊은복사(Deep Copy), 얕은복사(Shallow Copy)

File
C# 파일처리 프로그래밍

os, .net Core ==> C#을 사용할 수 있다.

클래스 사용

File 파일의 생성, 복사, 삭제, 이동 조회 등을 처리

FileInfo File 클래스와 하는 일이 동일하지만 정적 메소드 대신 

Instancec 메소드 제공

Directory 디렉터리 생성, 삭제, 이동, 조회 (정적 메소드)

DirectoryInfo Instance 메소드 제공

p623

파일의 기능     File              FileInfo       Directory                DirectoryInfo

생성              Create()        Create()       CreateDirectory()      Create()

복사              Copy()          CopyTo()      -                          -

삭제              Delete()        Delete()       Delete()                  Delete()

이동              Move()         MoveTo()     Move()                    MoveTo()


존재여부         Exists()        Exists          Exist()                     Exists

속성조회    GetAttributes()  Attributes     GetAttributes()          Attributes

하위 d조회          -              -             GetDirectories()      GetDirectories()   

하위 f조회           -              -             GetFiles()                 GetFiles()


1. 윈도우 메시지 (메시지 프로퍼티)
- Hwnd : 메시지를 받는 윈도의 핸들(Handle) 윈도우 객체를
            식별하고 관리하기 위해 O/S가 붙이는 번호
- Msg : 메시지 ID
- LParam : 메시지를 처리하는 정보(값)가 담겨 있습니다.
- WParam : 부가정보(조이스틱, 키보드, 마우스 값)
- Result : 메시지 처리에 대한 응답으로 O/S에 반환되는 값을 지정
            합니다.

2. 마우스 메시지 프로퍼티
   
-Button : 마우스의 방향(왼쪽, 오른쪽, 위, 아래)를 나타냄

-Clicks : 마우스 버튼의 클릭한 횟수를 나타냄, one 클릭, 더블클릭....

-Delta : 휠의 회전방향과 회전한 거리

-X : X좌표

-Y : Y좌표




임베디드 소프트웨어 프로그래밍

chip --> cpu + 메모리 + 보드 ---> mcu

8051, 8088 ---pic ---atmega128, 256

stm32(cortex- m , a, x arm)


-----------------------------
driver
리눅스 드라이버
kernel

----------------------------------------------
자료구조, 알고리즘


응용프로그램(논리 C#)
시스템 프로그래밍( O/S ---> Socker, Procss, Thread)

객체지향 프로그래밍(OOP--> 협업, 코드품질, 유지보수비용 절감...)
개발방법론(RUP, 애자일)

----------------------------------------------

C# Low Level 그리기 함수



1. DrawLine(Pen pen, Point pt1, Point pt2): 두 점을 연결하는 선을 그립니다.

2. DrawLines(Pen pen, Point[] points): 배열에 저장된 점들을 순서대로 연결하는 선을 그립니다.

3. DrawRectangle(Pen pen, Rectangle rect): 주어진 사각형을 그립니다.

4. DrawRectangles(Pen pen, Rectangle[] rects): 주어진 사각형 배열의 모든 사각형을 그립니다.

5. DrawEllipse(Pen pen, RectangleF rect): 주어진 사각형에 내접하는 타원을 그립니다.

6. DrawPolygon(Pen pen, Point[] points): 주어진 점들을 사용하여 다각형을 그립니다.

7. DrawPie(Pen pen, Rectangle rect, float startAngle, float sweepAngle): 주어진 사각형에 내접하는 원의 부분을 그립니다. 시작 각도와 스윕 각도를 기반으로 파이 조각을 그립니다.

8. DrawArc(Pen pen, RectangleF rect, float startAngle, float sweepAngle): 주어진 사각형에 내접하는 원호를 그립니다.



도형들을 채우는 함수 FillRectangle, FillPolygon, FillEllipse, FillPie 등의 메서드를 사용하면 도형 안을 색칠할 수 있습니다.

이러한 메서드들을 사용하려면 먼저 Pen 또는 Brush 객체를 생성해야 합니다. 이들 객체는 도형의 외곽선 색상, 선의 두께, 또는 도형의 내부 색상을 정의합니다.

----------------------------------------------

TCP Socket 프로그램으로 
1) 1:1 통신 구현
    1 -1) Server 구현 (단일처리 서버)
   
           1.서버소켓생성 & Client 연결 소켓 생성
   
           2.연결대기

           3.연결 성공시
   
           4. 데이터 교환(Read, Write)
   
           5. 리소스 반환 후 종료
   
    2 -1) Client 구현
   
           1. Client 소켓생성
   
           2. 연결
   
           3. 데이터 교환(Write, Read)
   
           4. 리소스 반환 후 종료
   



ViewBag

Passing Data From Controller To View In ASP.net Core 6

You can use the following objects to pass data between controller and view
ViewData
ViewBag
TempData
Strongly Typed View
ViewBag is also used to tansfer data from a controller a view
The general syntax of ViewBag is as follows: ViewBag. = ; where, Property: Is a String value that represents a property of ViewBag Value: Is the value of the property of ViewBag, Value may be a String, object, list, array or a different type, such as int, char, float, double, DateTime etc
ViewBag is a dynamic data type property of the base class of all the controllers, which is the ControllerBase class
ViewBag is a dynamic data type, which internally uses ViewData to store values.
ViewBag exists only for the current request and becomes null if the request is redirected.
ViewBag is a dynamic property based on the dynamic features introduced in C# 4.0
ViewBag does not require typecasting when you use complex data type.
Note: Viewbag does not provide compile time error checking For Example - if you mis-spell keys you wouldn't get any compile time errors. You get to know about the error only at runtime
TempData

It passes data form a controller to a view
TempData is used only for current or subsequent requests as it is a very short-lived instance.
Redirectiong is the only case when users can rely on TempData
When redirecting, current request is killed, and a new request is created on the server to serve the redirected view.
Sharing data between the controller actions are done through the ASP.NET MVC TempData dictionary
TempData is a Dictionary object derived form the TempDataDictionary class
TempData stores data as key-value pairs
TempData value must be type cast before use
TempData allows passing data form the current request to the subsequent request duing request redirection.
The general syntax of TempData is Follows:
TempData[Key] =
Key: is a string value to identify the object present in TempData
Value: Is the object present in TempData
TempData in ASP.net MVC can be used to store temporary data which can be used in the subsequent request
TempData will be cleared out after the completion of a subsequent request
Call TempData.Keep() to keep all the values of TempData in a third request
