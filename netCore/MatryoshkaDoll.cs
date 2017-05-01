namespace ConsoleApplication1
{
    public class MatryoshkaDoll
    {
        private readonly MatryoshkaDoll containedDoll;

        public MatryoshkaDoll() { }

        public MatryoshkaDoll(MatryoshkaDoll containedDoll)
        {
            this.containedDoll = containedDoll;
        }

        public int NumberOfSmallerDolls
        {
            get
            {                
                if (this.containedDoll == null)
                {
                    return 1;
                }
                else
                {
                    return containedDoll.NumberOfSmallerDolls + 1;
                }
            }
        }
    }
}