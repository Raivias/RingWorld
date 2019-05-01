namespace RingWorld
{
    using System.Collections.Generic;

    public class Map
    {
        public Map(Dictionary<int, Space> spaces)
        {
            this._spaces = spaces;
        }

        private Dictionary<int, Space> _spaces;

        public int Size
        { 
            get {return this._spaces.Count;}
        }

        public Dictionary<int, Space> Spaces
        { 
            get {return _spaces;}
        }

        public Space GetSpace(int coordinates)
        {
            return this._spaces[coordinates];
        }
    }
}
