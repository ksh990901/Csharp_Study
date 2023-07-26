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
