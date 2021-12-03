using Mabe3aty.Models;
using System;
using System.Data.Entity;
using System.Globalization;
using System.Linq;
using System.Windows.Forms;

namespace Mabe3aty.Users
{
    public partial class sell_form : Form
    {
        string user;
        public sell_form(string user)
        {
            InitializeComponent();
            this.user = user;
        }

        private void sell_form_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.Exit();
        }
        prodcutModel product;
        float total_price;
        private void getTotalprice()
        {
            if (code_txt.Text != "")
                using (ModelContext db = new ModelContext())
                {
                    try
                    {
                        product = db.productList.Find(Int32.Parse(code_txt.Text));
                        if (product != null)
                        {
                            name_txt.Text = product.product_Name;
                            total_price = (float.Parse(quantity_txt.Value.ToString()) * product.product_price);
                            total_price_txt.Text = total_price.ToString() + " جنيه ";

                        }
                        else
                        {
                            name_txt.Text = "من فضلك ادخل كود صحيح";
                        }
                    }
                    catch (Exception)
                    {
                        name_txt.Text = "من فضلك ادخل كود صحيح";
                    }
                   


                }
        }
        private void code_txt_TextChanged(object sender, System.EventArgs e)
        {
            getTotalprice();
        }

        private void quantity_txt_ValueChanged(object sender, EventArgs e)
        {
            getTotalprice();
        }
        public void sellORReturn(string type)
        {
            using (ModelContext db = new ModelContext())
            {
                sales obj = new sales()
                {
                    productID = Int32.Parse(code_txt.Text),
                    productName = name_txt.Text,
                    sell_date = DateTime.ParseExact(DateTime.Now.ToString("dd/MM/yyyy"), "dd/MM/yyyy", new CultureInfo("en-US"), DateTimeStyles.None),
                    sellType = type,
                    quantity = Int32.Parse(quantity_txt.Value.ToString()),
                    TotalPrice = total_price

                };
                if (obj != null)
                {
                    if (db.Entry<sales>(obj).State == EntityState.Detached)
                    {
                        db.Set<sales>().Attach(obj);
                    }
                    if (obj.sellID == 0)
                    {
                        db.Entry<prodcutModel>(product).State = EntityState.Modified;
                        db.Entry<sales>(obj).State = EntityState.Added;
                    }
                    db.SaveChanges();
                    MessageBox.Show("تم حفظ البيانات بنجاح");
                }
            }
        }
        private void sell_btn_Click(object sender, EventArgs e)
        {
            int user_quantity = Int32.Parse(quantity_txt.Value.ToString());
            if (product.product_Quantity-user_quantity<0)
            {
                MessageBox.Show("هذه الكمية اكثر من الموجودة لدينا\n من فضلك ادخل كمية اقل");
            }
            else
            {
                product.product_Quantity -= user_quantity;

                sellORReturn("sell");
            }
            
            
        }

        private void return_btn_Click(object sender, EventArgs e)
        {
            int user_quantity = Int32.Parse(quantity_txt.Value.ToString());
            product.product_Quantity += user_quantity;
            sellORReturn("return");
        }
    }
}
