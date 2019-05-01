namespace RingWorld
{
    using System.Collections.Generic;
    using RingWorld.MapObject;

    class RingWorld
    {
        int size = 150;
        int maxSpice = 4;
        
        int cycles = 10;
        int delay = 100;

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

            // Create Food

            // Loop for cycles
                // Print
                // delay
                // Update
        }
    }
}