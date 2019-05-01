namespace RingWorld.MapObject
{
    using System;

    public class Spice : MapObject
    {
        private static readonly Random rnd = new Random();

        Spice(int max, int initial, int coordinate, Map map) : base(coordinate, map)
        {
            this.Max = max;
            this.Amount = initial;
        }

        public int Amount
        {
            get;
            set;
        }

        public int Max
        {
            get;
            private set;
        }

        public void Generate()
        {
            this.Amount += rnd.Next(this.Max);
        }

        new public IMapObject Update()
        {
            newSpice.Generate();
            return this;
        }
    }
}