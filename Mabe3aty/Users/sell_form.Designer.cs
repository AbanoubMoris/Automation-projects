
namespace Mabe3aty.Users
{
    partial class sell_form
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(sell_form));
            this.quantity_txt = new System.Windows.Forms.NumericUpDown();
            this.code_txt = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.total_price_txt = new System.Windows.Forms.Label();
            this.name_txt = new System.Windows.Forms.Label();
            this.sell_btn = new System.Windows.Forms.Button();
            this.return_btn = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.quantity_txt)).BeginInit();
            this.SuspendLayout();
            // 
            // quantity_txt
            // 
            this.quantity_txt.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F);
            this.quantity_txt.Location = new System.Drawing.Point(91, 177);
            this.quantity_txt.Maximum = new decimal(new int[] {
            10000,
            0,
            0,
            0});
            this.quantity_txt.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.quantity_txt.Name = "quantity_txt";
            this.quantity_txt.Size = new System.Drawing.Size(175, 26);
            this.quantity_txt.TabIndex = 1;
            this.quantity_txt.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.quantity_txt.ValueChanged += new System.EventHandler(this.quantity_txt_ValueChanged);
            // 
            // code_txt
            // 
            this.code_txt.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.code_txt.Location = new System.Drawing.Point(91, 129);
            this.code_txt.Name = "code_txt";
            this.code_txt.Size = new System.Drawing.Size(175, 26);
            this.code_txt.TabIndex = 15;
            this.code_txt.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.code_txt.TextChanged += new System.EventHandler(this.code_txt_TextChanged);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Times New Roman", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(29, 133);
            this.label4.Name = "label4";
            this.label4.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
            this.label4.Size = new System.Drawing.Size(37, 20);
            this.label4.TabIndex = 14;
            this.label4.Text = "الكود";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Times New Roman", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.Brown;
            this.label1.Location = new System.Drawing.Point(200, 26);
            this.label1.Name = "label1";
            this.label1.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
            this.label1.Size = new System.Drawing.Size(122, 36);
            this.label1.TabIndex = 16;
            this.label1.Text = "سنتر مريم";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Times New Roman", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(28, 182);
            this.label2.Name = "label2";
            this.label2.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
            this.label2.Size = new System.Drawing.Size(42, 20);
            this.label2.TabIndex = 17;
            this.label2.Text = "الكمية";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Times New Roman", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(29, 254);
            this.label3.Name = "label3";
            this.label3.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
            this.label3.Size = new System.Drawing.Size(52, 20);
            this.label3.TabIndex = 18;
            this.label3.Text = "القيمة :";
            // 
            // total_price_txt
            // 
            this.total_price_txt.AutoSize = true;
            this.total_price_txt.Font = new System.Drawing.Font("Times New Roman", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.total_price_txt.Location = new System.Drawing.Point(87, 254);
            this.total_price_txt.Name = "total_price_txt";
            this.total_price_txt.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
            this.total_price_txt.Size = new System.Drawing.Size(58, 20);
            this.total_price_txt.TabIndex = 19;
            this.total_price_txt.Text = "10 جنيه";
            // 
            // name_txt
            // 
            this.name_txt.AutoSize = true;
            this.name_txt.Font = new System.Drawing.Font("Times New Roman", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.name_txt.Location = new System.Drawing.Point(281, 133);
            this.name_txt.Name = "name_txt";
            this.name_txt.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
            this.name_txt.Size = new System.Drawing.Size(146, 19);
            this.name_txt.TabIndex = 20;
            this.name_txt.Text = "من فضلك ادخل كود صحيح";
            // 
            // sell_btn
            // 
            this.sell_btn.BackColor = System.Drawing.SystemColors.MenuHighlight;
            this.sell_btn.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.sell_btn.Font = new System.Drawing.Font("Times New Roman", 13F, System.Drawing.FontStyle.Bold);
            this.sell_btn.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.sell_btn.Location = new System.Drawing.Point(91, 329);
            this.sell_btn.Name = "sell_btn";
            this.sell_btn.Size = new System.Drawing.Size(127, 31);
            this.sell_btn.TabIndex = 21;
            this.sell_btn.Text = "اتمام عملية البيع";
            this.sell_btn.UseVisualStyleBackColor = false;
            this.sell_btn.Click += new System.EventHandler(this.sell_btn_Click);
            // 
            // return_btn
            // 
            this.return_btn.BackColor = System.Drawing.SystemColors.ControlDark;
            this.return_btn.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.return_btn.Font = new System.Drawing.Font("Times New Roman", 13F, System.Drawing.FontStyle.Bold);
            this.return_btn.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.return_btn.Location = new System.Drawing.Point(314, 329);
            this.return_btn.Name = "return_btn";
            this.return_btn.Size = new System.Drawing.Size(127, 31);
            this.return_btn.TabIndex = 22;
            this.return_btn.Text = "مرتجع";
            this.return_btn.UseVisualStyleBackColor = false;
            this.return_btn.Click += new System.EventHandler(this.return_btn_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(363, 435);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(157, 13);
            this.label5.TabIndex = 23;
            this.label5.Text = "Developed By  : Abanoub Moris\r\n";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(1, 435);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(166, 26);
            this.label6.TabIndex = 24;
            this.label6.Text = "For maintainance :  01274198513\r\n\r\n";
            // 
            // sell_form
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(519, 450);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.return_btn);
            this.Controls.Add(this.sell_btn);
            this.Controls.Add(this.name_txt);
            this.Controls.Add(this.total_price_txt);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.code_txt);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.quantity_txt);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "sell_form";
            this.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
            this.RightToLeftLayout = true;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "المبيعات";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.sell_form_FormClosing);
            ((System.ComponentModel.ISupportInitialize)(this.quantity_txt)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.NumericUpDown quantity_txt;
        private System.Windows.Forms.TextBox code_txt;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label total_price_txt;
        private System.Windows.Forms.Label name_txt;
        private System.Windows.Forms.Button sell_btn;
        private System.Windows.Forms.Button return_btn;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
    }
}