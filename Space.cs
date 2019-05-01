namespace RingWorld
{
    using RingWorld.MapObject;
    using System.Collections.Generic;

    public class Space
    {
        Space(int coordinate)
        {
            this.coordinate = coordinate;
        }

        public int coordinate = -1;

        private IList<Space> adjecentSpaces = new List<Space>();

        public IList<IMapObjects> objectsInSpace = new List<IMapObjects>();

        public AddAdjecentSpaces(Space space)
        {
            this.adjecentSpaces.Add(space);
        }
    }
}