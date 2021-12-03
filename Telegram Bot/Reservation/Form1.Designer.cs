
namespace Reservation
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
            this.listItems = new System.Windows.Forms.ComboBox();
            this.disabilty = new System.Windows.Forms.Panel();
            this.panel1 = new System.Windows.Forms.Panel();
            this.update = new System.Windows.Forms.Button();
            this.create = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.panel3 = new System.Windows.Forms.Panel();
            this.filename_txt = new System.Windows.Forms.TextBox();
            this.chat_id_txt = new System.Windows.Forms.TextBox();
            this.botId_txt = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.choose_fv_btn = new System.Windows.Forms.Button();
            this.fav_combo = new System.Windows.Forms.ComboBox();
            this.save_btn = new System.Windows.Forms.Button();
            this.logn_pnl = new System.Windows.Forms.Panel();
            this.login_btn = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.login_txt = new System.Windows.Forms.TextBox();
            this.panel2 = new System.Windows.Forms.Panel();
            this.panel1.SuspendLayout();
            this.panel3.SuspendLayout();
            this.logn_pnl.SuspendLayout();
            this.panel2.SuspendLayout();
            this.SuspendLayout();
            // 
            // backgroundWorker1
            // 
            this.backgroundWorker1.DoWork += new System.ComponentModel.DoWorkEventHandler(this.backgroundWorker1_DoWork);
            this.backgroundWorker1.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.backgroundWorker1_RunWorkerCompleted);
            // 
            // listItems
            // 
            this.listItems.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.listItems.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold);
            this.listItems.FormattingEnabled = true;
            this.listItems.Location = new System.Drawing.Point(160, 57);
            this.listItems.Name = "listItems";
            this.listItems.Size = new System.Drawing.Size(121, 29);
            this.listItems.TabIndex = 0;
            this.listItems.SelectedIndexChanged += new System.EventHandler(this.listItems_SelectedIndexChanged);
            // 
            // disabilty
            // 
            this.disabilty.Location = new System.Drawing.Point(3, 57);
            this.disabilty.Name = "disabilty";
            this.disabilty.Size = new System.Drawing.Size(141, 231);
            this.disabilty.TabIndex = 1;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.update);
            this.panel1.Controls.Add(this.create);
            this.panel1.Controls.Add(this.button1);
            this.panel1.Controls.Add(this.panel3);
            this.panel1.Controls.Add(this.choose_fv_btn);
            this.panel1.Controls.Add(this.fav_combo);
            this.panel1.Controls.Add(this.save_btn);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Left;
            this.panel1.Enabled = false;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(362, 424);
            this.panel1.TabIndex = 2;
            // 
            // update
            // 
            this.update.Font = new System.Drawing.Font("Segoe UI", 11.25F, System.Drawing.FontStyle.Bold);
            this.update.Location = new System.Drawing.Point(26, 311);
            this.update.Name = "update";
            this.update.Size = new System.Drawing.Size(156, 45);
            this.update.TabIndex = 11;
            this.update.Text = "تعديل مفضلة";
            this.update.UseVisualStyleBackColor = true;
            this.update.Click += new System.EventHandler(this.update_Click);
            // 
            // create
            // 
            this.create.Font = new System.Drawing.Font("Segoe UI", 11.25F, System.Drawing.FontStyle.Bold);
            this.create.Location = new System.Drawing.Point(188, 311);
            this.create.Name = "create";
            this.create.Size = new System.Drawing.Size(156, 45);
            this.create.TabIndex = 8;
            this.create.Text = "انشاء مفضلة";
            this.create.UseVisualStyleBackColor = true;
            this.create.Click += new System.EventHandler(this.create_Click);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("Segoe UI", 11.25F, System.Drawing.FontStyle.Bold);
            this.button1.Location = new System.Drawing.Point(112, 376);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(138, 45);
            this.button1.TabIndex = 2;
            this.button1.Text = "ابدأ البرنامج";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // panel3
            // 
            this.panel3.Controls.Add(this.filename_txt);
            this.panel3.Controls.Add(this.chat_id_txt);
            this.panel3.Controls.Add(this.botId_txt);
            this.panel3.Controls.Add(this.label1);
            this.panel3.Controls.Add(this.label2);
            this.panel3.Controls.Add(this.label3);
            this.panel3.Enabled = false;
            this.panel3.Location = new System.Drawing.Point(25, 12);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(301, 207);
            this.panel3.TabIndex = 9;
            // 
            // filename_txt
            // 
            this.filename_txt.AccessibleName = "اسم المفضلة";
            this.filename_txt.Font = new System.Drawing.Font("Segoe UI", 11F);
            this.filename_txt.Location = new System.Drawing.Point(28, 28);
            this.filename_txt.Name = "filename_txt";
            this.filename_txt.Size = new System.Drawing.Size(248, 27);
            this.filename_txt.TabIndex = 3;
            // 
            // chat_id_txt
            // 
            this.chat_id_txt.AccessibleName = "معرف القناة";
            this.chat_id_txt.Font = new System.Drawing.Font("Segoe UI", 11F);
            this.chat_id_txt.Location = new System.Drawing.Point(29, 82);
            this.chat_id_txt.Name = "chat_id_txt";
            this.chat_id_txt.Size = new System.Drawing.Size(248, 27);
            this.chat_id_txt.TabIndex = 4;
            // 
            // botId_txt
            // 
            this.botId_txt.AccessibleName = "معرف البوت";
            this.botId_txt.Font = new System.Drawing.Font("Segoe UI", 11F);
            this.botId_txt.Location = new System.Drawing.Point(29, 142);
            this.botId_txt.Multiline = true;
            this.botId_txt.Name = "botId_txt";
            this.botId_txt.Size = new System.Drawing.Size(248, 56);
            this.botId_txt.TabIndex = 5;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Segoe UI", 12F);
            this.label1.Location = new System.Drawing.Point(105, 4);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(95, 21);
            this.label1.TabIndex = 1;
            this.label1.Text = "اسم المفضلة";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Segoe UI", 12F);
            this.label2.Location = new System.Drawing.Point(113, 58);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(88, 21);
            this.label2.TabIndex = 3;
            this.label2.Text = "معرف القناة";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Segoe UI", 12F);
            this.label3.Location = new System.Drawing.Point(107, 115);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(91, 21);
            this.label3.TabIndex = 5;
            this.label3.Text = "معرف البوت";
            // 
            // choose_fv_btn
            // 
            this.choose_fv_btn.Font = new System.Drawing.Font("Segoe UI", 11.25F, System.Drawing.FontStyle.Bold);
            this.choose_fv_btn.Location = new System.Drawing.Point(188, 260);
            this.choose_fv_btn.Name = "choose_fv_btn";
            this.choose_fv_btn.Size = new System.Drawing.Size(156, 45);
            this.choose_fv_btn.TabIndex = 7;
            this.choose_fv_btn.Text = "اختيار مفضلة";
            this.choose_fv_btn.UseVisualStyleBackColor = true;
            this.choose_fv_btn.Click += new System.EventHandler(this.choose_fv_btn_Click);
            // 
            // fav_combo
            // 
            this.fav_combo.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.fav_combo.Enabled = false;
            this.fav_combo.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold);
            this.fav_combo.FormattingEnabled = true;
            this.fav_combo.Location = new System.Drawing.Point(58, 225);
            this.fav_combo.Name = "fav_combo";
            this.fav_combo.Size = new System.Drawing.Size(243, 29);
            this.fav_combo.TabIndex = 6;
            this.fav_combo.SelectedIndexChanged += new System.EventHandler(this.fav_combo_SelectedIndexChanged);
            // 
            // save_btn
            // 
            this.save_btn.Font = new System.Drawing.Font("Segoe UI", 11.25F, System.Drawing.FontStyle.Bold);
            this.save_btn.Location = new System.Drawing.Point(25, 260);
            this.save_btn.Name = "save_btn";
            this.save_btn.Size = new System.Drawing.Size(157, 45);
            this.save_btn.TabIndex = 10;
            this.save_btn.Text = "حفظ المفضلة";
            this.save_btn.UseVisualStyleBackColor = true;
            this.save_btn.Click += new System.EventHandler(this.save_btn_Click);
            // 
            // logn_pnl
            // 
            this.logn_pnl.BackColor = System.Drawing.Color.LightSlateGray;
            this.logn_pnl.Controls.Add(this.login_btn);
            this.logn_pnl.Controls.Add(this.label4);
            this.logn_pnl.Controls.Add(this.login_txt);
            this.logn_pnl.Location = new System.Drawing.Point(-3, 0);
            this.logn_pnl.Name = "logn_pnl";
            this.logn_pnl.Size = new System.Drawing.Size(662, 424);
            this.logn_pnl.TabIndex = 6;
            // 
            // login_btn
            // 
            this.login_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.login_btn.ForeColor = System.Drawing.Color.Sienna;
            this.login_btn.Location = new System.Drawing.Point(202, 215);
            this.login_btn.Name = "login_btn";
            this.login_btn.Size = new System.Drawing.Size(256, 45);
            this.login_btn.TabIndex = 2;
            this.login_btn.Text = "تسجيل الدخول";
            this.login_btn.UseVisualStyleBackColor = true;
            this.login_btn.Click += new System.EventHandler(this.login_btn_Click);
            // 
            // label4
            // 
            this.label4.AccessibleName = "كلمة المرور";
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.ForeColor = System.Drawing.Color.OldLace;
            this.label4.Location = new System.Drawing.Point(382, 146);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(74, 16);
            this.label4.TabIndex = 1;
            this.label4.Text = "كلمة المرور";
            // 
            // login_txt
            // 
            this.login_txt.AccessibleName = "كلمة المرور";
            this.login_txt.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold);
            this.login_txt.Location = new System.Drawing.Point(202, 170);
            this.login_txt.Name = "login_txt";
            this.login_txt.PasswordChar = '*';
            this.login_txt.Size = new System.Drawing.Size(255, 29);
            this.login_txt.TabIndex = 0;
            this.login_txt.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.login_txt_KeyPress);
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.listItems);
            this.panel2.Controls.Add(this.disabilty);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Right;
            this.panel2.Enabled = false;
            this.panel2.Location = new System.Drawing.Point(368, 0);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(284, 424);
            this.panel2.TabIndex = 3;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(652, 424);
            this.Controls.Add(this.logn_pnl);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.panel1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Telegram Bot";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.panel1.ResumeLayout(false);
            this.panel3.ResumeLayout(false);
            this.panel3.PerformLayout();
            this.logn_pnl.ResumeLayout(false);
            this.logn_pnl.PerformLayout();
            this.panel2.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.ComponentModel.BackgroundWorker backgroundWorker1;
        private System.Windows.Forms.ComboBox listItems;
        private System.Windows.Forms.Panel disabilty;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.ComboBox fav_combo;
        private System.Windows.Forms.Button save_btn;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox botId_txt;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox chat_id_txt;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox filename_txt;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button choose_fv_btn;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.Button update;
        private System.Windows.Forms.Button create;
        private System.Windows.Forms.Panel logn_pnl;
        private System.Windows.Forms.Button login_btn;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox login_txt;
    }
}

