namespace RingWorld
{
    using System;
    using System.Collections.Generic;
    using RingWorld.MapObject;

    class RingWorld
    {
        private static readonly Random rnd = new Random();

        public int size = 150;
        public int maxSpice = 4;

        public int cycles = 10;
        public int delay = 100;

        Map map;

        static void Main(string[] args)
        {
            // Create Spaces
            Dictionary<int, Space> spaces = new Dictionary<int, Space>();
            Space prevSpace = new Space(0);
            Space newSpace;
            for(int i = 1; i < this.size; i++)
            {
                newSpace = new Space(i);
                newSpace.AddAdjecentSpaces(prevSpace);
            }

            spaces[0].AddAdjecentSpaces(newSpace);

            // Create Map
            this.map = new Map(spaces);

            // Create Spice
            for(int i = 0; i < this.size; i++)
            {
                Spice spice = new Spice( this.maxSpice, 1, rnd.Next(ThreadStaticAttribute.maxSpice), i, this.map);
            }
            // Loop for cycles
                // Print
                // delay
                // Update
        }
    }
}