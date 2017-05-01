using System;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            Test test = new Test();
            Console.WriteLine("1 Test Movie");
            Console.WriteLine("2 Test Matryoshka Doll");
            Console.WriteLine("3 Test Chickens Or Bunnies");
            Console.WriteLine("4 Test ReadBackwards");
            Console.WriteLine("5 Test Virtual Voids");
            Console.WriteLine("6 Test Binary Tree");
            Console.WriteLine("7 Test FindBiggestNumber");
            Console.WriteLine("8 Test SortArray");
            Console.WriteLine("9 Test Factorial");
            // density dispersion
            // binary search
            // mirror
            string value = Console.ReadLine();
            switch (value)
            {
                case "1": test.TestMovie(); break;
                case "2": test.TestMatryoshkaDoll(); break;
                case "3": test.TestChickensOrBunnies(); break;
                case "4": test.TestReadBackwards(); break;
                case "5": test.TestVirtualVoids(); break;
                case "6": test.TestBinaryTree(); break;
                case "7": test.TestFindBiggestNumber(); break;
                case "8": test.TestSortArray(); break;
                case "9": test.TestFactorial(); break;
            }
            Console.ReadLine();
        }
    }
}