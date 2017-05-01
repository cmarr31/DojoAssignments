using System;
using System.Collections.Generic;

namespace ConsoleApplication1
{
    public class Test
    {
        public void TestBinaryTree()
        {
            int[] values = new int[] { 1, 2, 3, 4, 5 };
            BinaryTree tree = new BinaryTree(values);
        }

        public void TestMovie()
        {
            var format = System.Globalization.CultureInfo.InvariantCulture.DateTimeFormat;
            Movie[] movies = new Movie[]
            {
            new Movie(DateTime.Parse("1/1/2015 20:00", format), DateTime.Parse("1/1/2015 21:30", format)),
            new Movie(DateTime.Parse("1/1/2015 21:30", format), DateTime.Parse("1/1/2015 23:00", format)),
            new Movie(DateTime.Parse("1/1/2015 23:10", format), DateTime.Parse("1/1/2015 23:30", format))
            };
            Console.WriteLine(MovieNight.CanViewAll(movies));
        }

        public void TestMatryoshkaDoll()
        {
            Console.WriteLine(new MatryoshkaDoll(new MatryoshkaDoll()).NumberOfSmallerDolls);
        }

        public void TestChickensOrBunnies()
        {
            int heads = 35;
            int legs = 94;
            int bunnies = 1;
            int chickens = 34;
            bool found = false;
            while (!found)
            {
                if (bunnies + chickens == heads && bunnies * 4 + chickens * 2 == legs)
                {
                    found = true;
                }
                else
                {
                    chickens--;
                    bunnies++;
                }
            }
            Console.WriteLine(bunnies);
            Console.WriteLine(bunnies);
        }

        public void TestReadBackwards()
        {
            string test = "Hello World!";
            char temp;
            string result = string.Empty;
            for (int i = test.Length; i > 0; i--)
            {
                temp = test.ToCharArray()[i - 1];
                Console.WriteLine(temp);
                result = result + temp;
            }
            Console.WriteLine(result);
        }

        public void TestVirtualVoids()
        {
            List<VirtualVoid> virtualVoids = new List<VirtualVoid>();
            virtualVoids.Add(new OverrideVirtualVoid());
            virtualVoids.Add(new NewVirtualVoid());
            virtualVoids.Add(new HideVirtualVoid());
            foreach (VirtualVoid virtualVoid in virtualVoids)
            {
                virtualVoid.Method();
            }
        }
        
        public void TestFindBiggestNumber()
        {
            Sample mySample = new Sample();
            mySample.FindBiggestNumber();
        }
        
        public void TestSortArray()
        {
            Sample mySample = new Sample();
            mySample.SortArray();
        }

        public void TestFactorial()
        {
            Sample mySample = new Sample();
            bool ExitLoop = false;
            int UsersNumber = 0;
            do
            {
                Console.Write("Enter a number to calculate it's factorial (or 0 to exit):");
                UsersNumber = Convert.ToInt16(Console.ReadLine());
                if (UsersNumber > 0)
                {
                    if (UsersNumber > 20)
                    {
                        Console.WriteLine("Numbers entered must be between 1 and 20 due to how big");
                        Console.WriteLine("these numbers get for higher values.");
                    }
                    else
                    {
                        //The recursion happens when the Factorial method is called.
                        Console.WriteLine("The Factorial of " + UsersNumber + " is " + mySample.Factorial(UsersNumber));
                    }
                }
                else
                {
                    if (UsersNumber == 0) ExitLoop = true;
                    Console.WriteLine("The number must not be negative.");
                }
            }
            while (!ExitLoop);
        }
    }
}