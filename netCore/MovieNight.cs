using System.Linq;

namespace ConsoleApplication1
{
    public static class MovieNight
    {
        public static bool CanViewAll(Movie[] movies)
        {
            bool value = true;
            
            for (int i = 0; i < movies.Count<Movie>()-1;i++)
            {
                if (movies[i].End > movies[i + 1].Start)
                { value = false; }
            }
            return value;
        }        
    }
}
