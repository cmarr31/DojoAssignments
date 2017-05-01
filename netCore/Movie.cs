using System;

namespace ConsoleApplication1
{
    public class Movie
    {
        public DateTime Start { get; private set; }
        public DateTime End { get; private set; }

        public Movie(DateTime start, DateTime end)
        {
            this.Start = start;
            this.End = end;
        }
    }
}
