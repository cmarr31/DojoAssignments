using System;
using System.Linq;

namespace ConsoleApplication1
{
    class Sample
    {
        private int[] numbers = { 3, 9, 5, 10 };

        public void FindBiggestNumber()
        {
            int max = 0;// numbers.Max();
            for (int i = 0; i < numbers.Count(); i++)
            {
                Console.WriteLine(numbers[i]);
                if (max < numbers[i])
                {
                    max = numbers[i];
                }
            }
            Console.Write("Biggest number = ");
            Console.WriteLine(max);
            Console.WriteLine();
        }

        public void SortArray()
        {
            bool ready = false;
            while (!ready)
            {
                ready = true;
                int temp = numbers[0];
                for (int i = 0; i < numbers.Count(); i++)
                {
                    if (numbers[i] < temp)
                    {
                        ready = false;
                        numbers[i - 1] = numbers[i];
                        numbers[i] = temp;
                        temp = numbers[i];
                    }
                    else
                    {
                        temp = numbers[i];
                    }
                }
            }

            //test
            Console.WriteLine("Sorted");
            for (int i = 0; i < numbers.Count(); i++)
            {
                Console.WriteLine(numbers[i]);
            }
        }

        public int Factorial(int number)
        {
            int temp = 0;
            if (number == 1)
            {
                temp = 1;
            }
            else
            {
                temp = Factorial(number-1) * number;
            }
            return temp;
        }
    }
}