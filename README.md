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



