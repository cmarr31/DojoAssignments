using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    /// <summary>
    ///     1
    ///    / \
    ///   2   3
    ///  / \
    /// 4   5
    /// </summary>
    public class BinaryTree
    {
        int value;
        BinaryTree left;
        BinaryTree right;

        public BinaryTree(int[] values) : this(values, 0) { }

        public BinaryTree(int[] values, int index)
        {
            Load(this, values, index);
        }

        public void Load(BinaryTree tree, int[] values, int index)
        {
            this.value = values[index];
            if (index * 2 + 1 < values.Length)
            {
                this.left = new BinaryTree(values, index * 2 + 1);
            }
            if (index * 2 + 2 < values.Length)
            {
                this.right = new BinaryTree(values, index * 2 + 2);
            }
        }
    }
}
