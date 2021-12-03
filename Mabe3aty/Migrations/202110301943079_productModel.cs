namespace Mabe3aty.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class productModel : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.adminTables",
                c => new
                    {
                        id = c.Int(nullable: false, identity: true),
                        username = c.String(),
                        password = c.String(),
                        email = c.String(),
                        type = c.String(),
                    })
                .PrimaryKey(t => t.id);
            
            CreateTable(
                "dbo.prodcutModels",
                c => new
                    {
                        QR_code = c.Int(nullable: false, identity: true),
                        product_Name = c.String(),
                        product_Quantity = c.Int(nullable: false),
                        product_price = c.Single(nullable: false),
                    })
                .PrimaryKey(t => t.QR_code);
            
            CreateTable(
                "dbo.sales",
                c => new
                    {
                        sellID = c.Int(nullable: false, identity: true),
                        productID = c.Int(nullable: false),
                        TotalPrice = c.Single(nullable: false),
                        quantity = c.Int(nullable: false),
                        productName = c.String(),
                        sellType = c.String(),
                        sell_date = c.DateTime(nullable: false, storeType: "date"),
                    })
                .PrimaryKey(t => t.sellID);
            
        }
        
        public override void Down()
        {
            DropTable("dbo.sales");
            DropTable("dbo.prodcutModels");
            DropTable("dbo.adminTables");
        }
    }
}
