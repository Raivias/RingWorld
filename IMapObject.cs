namespace RingWorld.MapObject
{
    public interface IMapObject
    {
        int Coordinate
        {
            get;
        }

        IMapObject Update();
    }
}