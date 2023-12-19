using System;

namespace DotNet.Patterns
{
    internal interface ICommand
    {
        void Invoke();
    }

    internal class UpCommand : ICommand
    {
        public void Invoke()
        {
            Console.Write("Up ");
            Program.y++;
        }
    }

    internal class DownCommand : ICommand
    {
        public void Invoke()
        {
            Console.Write("Down ");
            Program.y--;
        }
    }

    internal class LeftCommand : ICommand
    {
        public void Invoke()
        {
            Console.Write("Left ");
            Program.x--;
        }
    }

    internal class RightCommand : ICommand
    {
        public void Invoke()
        {
            Console.Write("Right ");
            Program.x++;
        }
    }
}
