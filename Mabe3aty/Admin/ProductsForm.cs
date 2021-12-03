using Mabe3aty.Models;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.Entity;
using System.Data.SqlClient;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Mabe3aty.Admin
{
    public  partial class ProductsForm : Form
    {
        string user;
        public ProductsForm(string user)
        {
            InitializeComponent();
            this.user = user;
            price_txt.ThousandsSeparator = true;

        }
        bool addnewProduct = false;
        private void add_btn_Click(object sender, EventArgs e)
        {
            try
            {
                if (!addnewProduct)
                {
                    productPanel.Enabled = true;
                    prodcutModelBindingSource.Add(new prodcutModel());
                    prodcutModelBindingSource.MoveLast();
                    product_name_txt.Focus();
                }
                else
                {
                    MessageBox.Show("برجاء حفظ البيانات اولا قبل اضافة جديد");
                }
            }
            catch (Exception)
            {

                MessageBox.Show("حدث خططا اثناء اجراء العملية \n برجاء اعادة تشغيل البرنامج", "خطأ", MessageBoxButtons.OK, MessageBoxIcon.Error);


            }


        }

        private void ProductsForm_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'tstss.adminTables' table. You can move, or remove it, as needed.
            from_date.CustomFormat = "dd / MM / yyyy";
            from_date.Format = DateTimePickerFormat.Custom;
            from_date.Value = DateTime.Now;
            to_date.CustomFormat = "dd / MM / yyyy";
            to_date.Format = DateTimePickerFormat.Custom;
            to_date.Value = DateTime.Now;
            using (ModelContext db = new ModelContext())
            {
                prodcutModelBindingSource.DataSource = db.productList.ToList();
                salesBindingSource.DataSource = db.salesList.ToList();
                adminTableBindingSource.DataSource = db.adminTable.ToList();
            }
            prodcutModel obj = prodcutModelBindingSource.Current as prodcutModel;
            sales obj2 = salesBindingSource.Current as sales;
            adminTable obj3 = adminTableBindingSource.Current as adminTable;

            DateTime from = new DateTime(from_date.Value.Year, from_date.Value.Month, from_date.Value.Day);
            DateTime to = new DateTime(to_date.Value.Year, to_date.Value.Month, to_date.Value.Day);
            get_totalPrice(from,to);
            if (obj != null)
            {

            }

        }
        public void get_totalPrice(DateTime from,DateTime to)
        {
            using (ModelContext db = new ModelContext())
            {
                var result = db.salesList
                    .Where(c => c.sell_date >= from)
                    .Where(c => c.sell_date <= to)
                    .GroupBy(o => o.sellType)
                    .Select(g => new { membername = g.Key, total = g.Sum(i => i.TotalPrice) });

                bool sell = false;
                bool ret= false;
                float sellTotal = 0f;
                float returnTotal = 0f;
                foreach (var group in result)
                {
                    if (group.membername.ToString() == "sell")
                    {
                        sales_lbl.Text = group.total.ToString() + "  جنيه  ";
                        sellTotal = group.total;
                        sell = true;
                    }
                    else
                    {
                        return_lbl.Text = group.total.ToString() + " جنيه ";
                        returnTotal = group.total;
                        ret = true;
                    }
                }
                if (!sell)
                    sales_lbl.Text = "0" + " جنيه ";
                if (!ret)
                    return_lbl.Text = "0" + " جنيه ";

                result_lbl.Text = (sellTotal - returnTotal).ToString() + "جنيه ";
            }
        }

        private void dataGridView1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Delete)
            {
                foreach (DataGridViewRow item in this.dataGridView1.SelectedRows)
                {
                    if (MessageBox.Show("هل انت متاكد تريد مسح "+ item.Cells[1].Value +" ?","تحذير", MessageBoxButtons.OKCancel, MessageBoxIcon.Warning) == DialogResult.OK)
                        dataGridView1.Rows.RemoveAt(item.Index);
                    
                }
            }
            
        }



        private void delete_btn_Click(object sender, EventArgs e)
        {
            if (!addnewProduct)
            {

                foreach (DataGridViewRow item in this.dataGridView1.SelectedRows)
                {
                    if (MessageBox.Show("هل انت متاكد تريد مسح " + item.Cells[1].Value + " ?", "تحذير", MessageBoxButtons.OKCancel, MessageBoxIcon.Warning) == DialogResult.OK)
                    {
                        using (ModelContext db =  new ModelContext())
                        {
                            prodcutModel obj = prodcutModelBindingSource.Current as prodcutModel;
                            if (obj != null)
                            {
                                if (db.Entry<prodcutModel>(obj).State == EntityState.Detached)
                                    db.Set<prodcutModel>().Attach(obj);
                                db.Entry<prodcutModel>(obj).State = EntityState.Deleted;
                                db.SaveChanges();
                                MessageBox.Show("تم مسح المحدد بنجاح","تم");
                                addnewProduct = false;
                                prodcutModelBindingSource.RemoveCurrent();
                            }
                        }
                    }
                }
            }
            else
            {
                MessageBox.Show("برجاء حفظ البيانات اولا قبل اضافة جديد");
            }
        }

        private void update_btn_Click(object sender, EventArgs e)
        {
            if (!addnewProduct)
            {
                productPanel.Enabled = true;
                product_name_txt.Focus();
                prodcutModel obj = prodcutModelBindingSource.Current as prodcutModel;
            }
            else
            {
                MessageBox.Show("برجاء حفظ البيانات اولا قبل اضافة جديد");
            }

            //editProduct();
        }

        private void toolStripTextBox1_TextChanged_1(object sender, EventArgs e)
        {
          //  this.productsBindingSource.Filter = "product_name like '%" + toolStripTextBox1.Text + "%'";
        }

        private void cancel_btn_Click(object sender, EventArgs e)
        {
            addnewProduct = false;
            productPanel.Enabled = false;
            prodcutModelBindingSource.ResetBindings(false);
            ProductsForm_Load(sender, e);
            
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            prodcutModel obj = prodcutModelBindingSource.Current as prodcutModel;
            if (obj != null)
            {

            }
        }

        private void save_btn_Click(object sender, EventArgs e)
        {
            try
            {
                using (ModelContext db = new ModelContext())
                {
                    prodcutModel obj = prodcutModelBindingSource.Current as prodcutModel;
                    if (obj != null)
                    {
                        if (db.Entry<prodcutModel>(obj).State == EntityState.Detached)
                        {
                            db.Set<prodcutModel>().Attach(obj);
                        }
                        if (obj.QR_code == 0)
                        {
                            db.Entry<prodcutModel>(obj).State = EntityState.Added;
                        }
                        else
                        {
                            db.Entry<prodcutModel>(obj).State = EntityState.Modified;
                        }
                        db.SaveChanges();
                        MessageBox.Show("تم حفظ البيانات بنجاح");
                        addnewProduct = false;
                        productPanel.Enabled = false;
                        dataGridView1.Refresh();
                    }
                    else
                    {
                        MessageBox.Show("برجاء تحديد الصف المراد حفظة اولا");
                    }
                }
            }
            catch (Exception)
            {

            }
            
        }

        public void generateReport(string type)
        {
        
            DateTime from = new DateTime(from_date.Value.Year, from_date.Value.Month, from_date.Value.Day);
            DateTime to = new DateTime(to_date.Value.Year, to_date.Value.Month, to_date.Value.Day);


            using (ModelContext db = new ModelContext())
            {
                salesBindingSource.DataSource =
                    db.salesList
                    .Where(c => c.sellType == type)
                    .Where(c => c.sell_date >= from)
                    .Where(c => c.sell_date <= to)
                    .ToList();
            }
            get_totalPrice(from, to);

        }
        private void sales_btn_Click(object sender, EventArgs e)
        {
            generateReport("sell");

        }

        private void return_btn_Click(object sender, EventArgs e)
        {
            generateReport("return");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            using(ModelContext db = new ModelContext())
            {
                if (MessageBox.Show(" هل انت متاكد تريد مسح جميع البيانات" + " ?", "تحذير", MessageBoxButtons.OKCancel, MessageBoxIcon.Warning) == DialogResult.OK)
                {
                    db.Database.ExecuteSqlCommand("TRUNCATE TABLE [sales]");
                    ProductsForm_Load(sender, e);
                }
            }
            
        }
        bool addNewUser = false;
        private void add_usr_btn_Click(object sender, EventArgs e)
        {
            try
            {
                if (!addNewUser)
                {
         
                    managePanel.Enabled = true;
                    adminTableBindingSource.Add(new adminTable());
                    adminTableBindingSource.MoveLast();
                    usename_txt.Focus();
                    addNewUser = true;
                }
                else
                    MessageBox.Show("برجاء حفظ البيانات اولا قبل اضافة جديد");
            }
            catch (Exception)
            {
                MessageBox.Show("حدث خططا اثناء اجراء العملية \n برجاء اعادة تشغيل البرنامج","خطأ",MessageBoxButtons.OK, MessageBoxIcon.Error);

            }
        }

        private void save_usr_btn_Click(object sender, EventArgs e)
        {
            try
            {

                if (usename_txt.Text != "" && password_txt.Text != "" && password_txt.Text == passwordConfirm_txt.Text)
                {

                    using (ModelContext db = new ModelContext())
                    {
                        adminTable obj = adminTableBindingSource.Current as adminTable;
                        if (obj != null)
                        {
                            if (db.Entry<adminTable>(obj).State == EntityState.Detached)
                            {
                                db.Set<adminTable>().Attach(obj);
                            }
                            if (obj.id == 0)
                            {
                                db.Entry<adminTable>(obj).State = EntityState.Added;
                            }
                            else
                            {
                                db.Entry<adminTable>(obj).State = EntityState.Modified;
                            }
                            db.SaveChanges();
                            addNewUser = false;
                            MessageBox.Show("تم حفظ البيانات بنجاح");
                            dataGridView1.Refresh();
                        
                        }
                        else
                        {
                            MessageBox.Show("برجاء تحديد الصف المراد حفظة اولا");
                        }
                    }
                }
                else
                {
                    if (passwordConfirm_txt.Text!=password_txt.Text)
                        MessageBox.Show("كلمة السر غير متطابقة");
                    else
                        MessageBox.Show("برجاء اداخل جميع البيانات بشكل صحيح");
                }
            }
            catch (Exception)
            {
                MessageBox.Show("حدث خططا اثناء اجراء العملية \n برجاء اعادة تشغيل البرنامج", "خطأ", MessageBoxButtons.OK, MessageBoxIcon.Error);

            }
        }

        private void edit_usr_btn_Click(object sender, EventArgs e)
        {
            if (!addNewUser)
            {
                managePanel.Enabled = true;
                adminTable obj = adminTableBindingSource.Current as adminTable;
                usename_txt.Focus();
            }
            else
            {
                MessageBox.Show("برجاء حفظ البيانات اولا قبل اضافة جديد");
            }
        }

        private void cancel_usr_btn_Click(object sender, EventArgs e)
        {
            addNewUser = false;
            managePanel.Enabled = false;
            adminTableBindingSource.ResetBindings(false);
            ProductsForm_Load(sender, e);
        }

        private void tabControl1_Click(object sender, EventArgs e)
        {
            //if (((TabControl)sender).SelectedTab.Name == managePanel.Name)
            //{
            //    using (ModelContext db = new ModelContext())
            //    {
            //        adminTableBindingSource.DataSource = db.adminTable.ToList();
            //    }
            //}

        }

        private void delete_usr_btn_Click(object sender, EventArgs e)
        {
            foreach (DataGridViewRow item in this.dataGridView3.SelectedRows)
            {
                if (MessageBox.Show("هل انت متاكد تريد مسح " + item.Cells[1].Value + " ?", "تحذير", MessageBoxButtons.OKCancel, MessageBoxIcon.Warning) == DialogResult.OK)
                {
                    using (ModelContext db = new ModelContext())
                    {
                        adminTable obj = adminTableBindingSource.Current as adminTable;
                        if (obj != null)
                        {
                            if (db.Entry<adminTable>(obj).State == EntityState.Detached)
                                db.Set<adminTable>().Attach(obj);
                            db.Entry<adminTable>(obj).State = EntityState.Deleted;
                            db.SaveChanges();
                            MessageBox.Show("تم مسح المحدد بنجاح");
                            adminTableBindingSource.RemoveCurrent();
                        }
                    }
                }
            }
        }
    }
}
