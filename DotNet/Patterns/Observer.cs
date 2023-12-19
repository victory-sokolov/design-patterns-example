using System;
using System.IO;

namespace DotNet.Patterns
{
    class ListReader
    {
        public delegate void NewListItem(string listItem);

        public event NewListItem ListUpdated;

        public void ReadList()
        {
            while (true)
            {
                var listItem = Console.ReadLine();
                ListUpdated?.Invoke(listItem);
            }
        }
    }

    public class FileWriter
    {
        public string filename = DateTime.Now.ToFileTime().ToString();
        public void WriteToFile(string line) =>
            File.AppendAllText(filename, line + Environment.NewLine);
    }
}
