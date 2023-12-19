using System;
using System.Collections.Generic;
using DotNet.Patterns;

namespace DotNet
{
    public static class Program
    {
        public static int x;
        public static int y;
        private static void Main(string[] args)
        {
            // Factory
            // var notificationServiceProvider = new NotificationServiceProvider();
            // var shippingService = new ShippingService(notificationServiceProvider);
            // shippingService.ShipItem();

            // Adapter
            // FileLogger<Program> logger = new FileLogger<Program>("Log.txt");
            // logger.LogDebug("New log message");

            // Observer
            // var reader = new ListReader();
            // var writer = new FileWriter();
            // reader.ListUpdated += (listItem) => Console.WriteLine(listItem);
            // reader.ListUpdated += writer.WriteToFile;
            // reader.ReadList();

            // Command
            List<ICommand> commandList = new List<ICommand>();

            while (true)
            {
                ConsoleKey key = Console.ReadKey(true).Key;
                if (key == ConsoleKey.UpArrow)
                {
                    commandList.Add(new UpCommand());
                }
                else if (key == ConsoleKey.DownArrow)
                {
                    commandList.Add(new DownCommand());
                }
                else if (key == ConsoleKey.LeftArrow)
                {
                    commandList.Add(new LeftCommand());
                }
                else if (key == ConsoleKey.RightArrow)
                {
                    commandList.Add(new RightCommand());
                }
                else if (key == ConsoleKey.Enter)
                {
                    Console.WriteLine();
                    commandList.ForEach(c => c.Invoke());
                    Console.WriteLine($": {x}, {y}");
                    commandList.Clear();
                }
            }
        }
    }
}
