using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class VirtualVoid
    {
        public virtual void Method()
        {
            Console.WriteLine("virtual");
        }
    }

    class OverrideVirtualVoid : VirtualVoid
    {
        public override void Method()
        {
            Console.WriteLine("override");
        }
    }

    class NewVirtualVoid : VirtualVoid
    {
        public new void Method()
        {
            Console.WriteLine("new");
        }
    }

    class HideVirtualVoid : VirtualVoid
    {
        public void Method()
        {
            Console.WriteLine("hide");
        }
    }
}
