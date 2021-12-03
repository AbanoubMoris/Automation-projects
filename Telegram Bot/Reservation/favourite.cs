using System;
using System.Collections.Generic;

namespace Reservation
{
    [Serializable]
    public class favourite
    {
        public Dictionary<string, List<string>> fav;

        public favourite(Dictionary<string, List<string>> fav)
        {
            this.fav = fav;

        }
    }
}
