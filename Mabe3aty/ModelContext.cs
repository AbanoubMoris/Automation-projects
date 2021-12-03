using Mabe3aty.Models;
using System.Data.Entity;

namespace Mabe3aty
{
    public class ModelContext : DbContext 
    {
        //public ModelContext() : base("name=Mabe3aty.Properties.Settings.conn2") { }
        public ModelContext() : base("name=Mabe3aty.Properties.Settings.MyDatabaseConn") { }
        public DbSet<prodcutModel> productList { get; set; }
        public DbSet<sales> salesList { get; set; }
        public DbSet<adminTable> adminTable { get; set; }

    }
}