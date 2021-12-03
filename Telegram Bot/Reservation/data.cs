using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Reservation
{
    [Serializable]
    class dates
    {
        public string date;
        public string place;
        public dates(string place,string date)
        {
            this.place = place;
            this.date = date;
        }
    }
    [Serializable]
    class disabls
    {
        public string disName;
        public Dictionary<int, List<dates>> places; //places code,list dates
        public disabls(string disName)
        {
            this.disName = disName;
            places = new Dictionary<int, List<dates>>();
        }
    }
    [Serializable]
    class data
    {
        public string govName;
        public Dictionary<int, disabls> disDic; //disability code,disabls
        public data(string govName)
        {
            this.govName = govName;
            disDic = new Dictionary<int, disabls>();
        }

    }
    [Serializable]
    public class favourit
    {
        public string filename;
        public string chat_id;
        public string bot_id;

        public favourit(string filename, string chat_id, string bot_id)
        {
            this.filename = filename;
            this.chat_id = chat_id;
            this.bot_id = bot_id;
        }
    }

}
