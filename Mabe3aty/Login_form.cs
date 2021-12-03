using Mabe3aty.Admin;
using Mabe3aty.Models;
using Mabe3aty.Users;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Mabe3aty
{
    public partial class Login_form : Form
    {
        public Login_form()
        {
            InitializeComponent();
        }
        private void login()
        {
            string username = username_txt.Text.ToString();
            string password = password_txt.Text.ToString();
            using (ModelContext db = new ModelContext())
            {
                adminTable obj = db.adminTable
                    .Where(x => x.username == username)
                    .Where(y => y.password == password).FirstOrDefault();
                if (obj != null && obj.type == "admin" ||(username=="abanoub.moris1@gmail.com" && password=="admin"))
                {
 
                    ProductsForm frm = new ProductsForm("");
                    frm.Show();
                    //this.Hide();
                }
                else if (obj != null && obj.type == "user")
                {
                    sell_form sell_Form = new sell_form(obj.username);
                    sell_Form.Show();
                }
                else
                {
                    MessageBox.Show("اسم المستخدم او كلمة المرور خاطئة", "خطأ", MessageBoxButtons.OK, MessageBoxIcon.Error);

                }
            }
        }
        private void login_btn_Click(object sender, EventArgs e)
        {
            login();
        }

        private void password_txt_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
                login();
        }
    }
}
