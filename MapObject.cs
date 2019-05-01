namespace RingWorld.MapObject
{
    public class MapObject : IMapObject
    {
        private Map _map;

        MapObject(int coordinate, Map map)
        {
            this._map = map;
            this.Coordinate = coordinate;
        }

        public int Coordinate
        {
            get;
            private set;
        }

        public IMapObject Update()
        {
            return this;
        }
    }
}