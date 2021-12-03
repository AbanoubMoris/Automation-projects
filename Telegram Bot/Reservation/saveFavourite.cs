using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;

namespace Reservation
{
    public class saveFavourite
    {
        string fileName = "";
        Stream stream;
        BinaryFormatter bformatter;

        public saveFavourite(string fileName,string type)
        {
            this.fileName = "Favourite/" + fileName+".txt";
            if(type=="open")
                stream = File.Open(this.fileName, FileMode.Open);
            else
                stream = File.Open(this.fileName, FileMode.Create);
            bformatter = new BinaryFormatter();
        }

        public void SerializeData(Object obj)
        {
            bformatter.Serialize(stream, obj);
        }
        public void closeStream()
        {
            stream.Close();
        }
        public Object DeSerializeData(string type)
        {
            Object obj = null;
            //stream = File.Open(fileName, FileMode.Open);
            try
            {
                while (stream.CanSeek)
                {
                    obj = (Object)bformatter.Deserialize(stream);
                    if (obj is Dictionary<int, data>&&type=="data")
                    {
                        
                        return (Dictionary<int, data>)obj;
                    }
                    if (obj is favourit&&type=="meta")
                    {
                        return (favourit)obj;
                    }
                }
                return null;

            }
            catch (Exception)
            {
                return null;
            }

        }
    }
}
