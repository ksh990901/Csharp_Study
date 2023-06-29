namespace SwitchCaseApp01
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //char num = 'A';

            //switch (num)
            //{
            //    case 'A':
            //        Console.WriteLine("A가 출력되었습니다");
            //        break;
            //        case 'B' :
            //        Console.WriteLine("B가 출력되었습니다");
            //        break;
            //    default:
            //        Console.WriteLine("기본값이 출력되었습니다");
            //        break;
            //}
            // 사용자에게 1 ~ 7사이의 숫자를 입력받고 숫자에 따라 요일을 출력하는 프로그램을 작성해주세요.
            //Console.WriteLine("숫자를 입력해주세요 :  ");

            //int num = Int32.Parse(Console.ReadLine());

            //switch (num)
            //{
            //    case 1:
            //        Console.WriteLine("월요일입니다.");
            //        break;
            //    case 2:
            //        Console.WriteLine("화요일입니다.");
            //        break;
            //    case 3:
            //        Console.WriteLine("수요일입니다.");
            //        break;
            //    case 4:
            //        Console.WriteLine("목요일입니다.");
            //        break;
            //    case 5:
            //        Console.WriteLine("금요일입니다.");
            //        break;
            //    case 6:
            //        Console.WriteLine("토요일입니다.");
            //        break;
            //    case 7:
            //        Console.WriteLine("일요일입니다.");
            //        break;


            //}
            //단을 입력하세요.

            Console.Write("단을 입력하세요 : ");
            int a = Int32.Parse(Console.ReadLine());

            switch (a) 
            {
                case 3:
                    for(int i = 1; i<= 9;  i++)
                        Console.WriteLine($"{a} * {i} = {a * i}");
                    break;
                    case 4:
                    for(int i = 1; i<= 9; i++)
                    Console.WriteLine($"{a} * {i} = {a * i}");    
                    break;
                    case 5:
                    for(int i = 1; i<= 9; i++)
                    Console.WriteLine($"{a} * {i} = {a * i}");
                    break;
                        case 6:
                    for(int i = 1; i<= 9; i++)
                    Console.WriteLine($"{a} * {i} = {a * i}");
                    break;
            }

        }     
    }
}
