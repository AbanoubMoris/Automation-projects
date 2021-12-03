using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.IO;
using System.Media;
using System.Net;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using System.Xml;

namespace Reservation
{

    public partial class Form1 : Form
    {
        saveFavourite FavouriteObj;
        favourit favouritMeta;
        SoundPlayer sound = new SoundPlayer("sound.wav");

        public Form1()
        {
            InitializeComponent();
            
        }
        WebClient webclient = new WebClient();

        int i = 0;
        List<string> messages = new List<string>();
        HashSet<string> sent = new HashSet<string>();
        string current_fav = "Test_favourite";
        private void Form1_Load(object sender, EventArgs e)
        {
            dataStruct = new Dictionary<int, data>();
            try
            {
                string active = "https://abanoubmoris.github.io/";
                string expire = webclient.DownloadString(active);
                if (expire.Contains("11"))
                {
                    disabilty.Enabled = false;
                    panel1.Enabled = false;
                    button1.Enabled = false;
                    logn_pnl.Enabled = false;
                    login_btn.Text = "انتهت صلاحية البرنامج";
                    MessageBox.Show("انتهت صلاحية البرنامج");
                    return;
                }
            }
            catch (Exception)
            {

                return;
            }

            string url = "http://pod.mohp.gov.eg/apps/lookups/lk_governments.php?dhxr1637706488519=1";
            var govs = webclient.DownloadString(url);
            read("http://pod.mohp.gov.eg/apps/lookups/lk_governments.php?dhxr1637706488519=1", this.panel2, "", 0, 0, 0);
            read("http://pod.mohp.gov.eg/apps/lookups/major_dismed.php?dhxr1637706488522=1", disabilty, "", 0, 0, 0);

            LoadFavourite();
        }
        
        private void LoadFavourite()
        {
            fav_combo.Items.Clear();
            string[] txTFiles = GetFileNames("Favourite", "*.txt");
            int idx = -1;
            foreach (var item in txTFiles)
            {
   
                fav_combo.Items.Add(item.Replace(".txt", ""));
                if (item.Contains(current_fav)&& !item.Contains("empty"))
                {
                    idx = fav_combo.Items.Count - 1;
                }
            }
            if (txTFiles.Length > 0 && current_fav=="")
                fav_combo.SelectedIndex = 0;
            else if (txTFiles.Length > 0 && idx > -1)
            {
                fav_combo.SelectedIndex = idx;
            }
        }

        string currentPlaceName = "";
        Dictionary<string, int> govDic = new Dictionary<string, int>();
        Dictionary<string, int> disDic = new Dictionary<string, int>();
        private void read(string url, Panel panel, string typeOfRead, int govCode, int disCode, int placeCode)
        {
            
            XmlDocument doc1 = new XmlDocument();
            doc1.Load(url);
            XmlElement root = doc1.DocumentElement;
            XmlNodeList nodes = root.SelectNodes("/data/item");
            int i = 0;
            foreach (XmlNode node in nodes)
            {
                if (i == 0)
                {
                    i++;
                    continue;
                }
                else
                {
                    string value = node.Attributes[1].InnerText;
                    string code = node.Attributes[0].InnerText;
                    if (panel != null)
                    {

                        if (panel.Name == "panel2")
                        {
                            govDic.Add(value, Int32.Parse(code));
                            listItems.Items.Add(value);
                            listItems.SelectedIndex = 0;
                        }
                        else
                        {
                            CheckBox checkBox = new CheckBox();
                            checkBox.Text = value.Replace("ﺍﻹﻋﺎﻗﺔ", "");
                            checkBox.CheckedChanged += checkBox_changed;
                            checkBox.Location = new Point(10, 1 + i * 22);
                            checkBox.Name = "disabilty" + "|" + code;
                            disDic.Add(checkBox.Text, Int32.Parse(code));
                            checkBox.Font = new Font("Segoe UI", 9, FontStyle.Bold);
                            panel.Controls.Add(checkBox);

                        }

                    }
                    else
                    {

                        if (typeOfRead == "places")
                        {

                            dataStruct[govCode].disDic[disCode].places.Add(Int32.Parse(code), new List<dates>());

                            currentPlaceName = value;

                        }
                        else//Read Dates of each place
                        {
                            dataStruct[govCode].disDic[disCode].places[placeCode].Add(new dates(currentPlaceName, value));
                        }
                    }
                }
                i++;

            }
        }
        Dictionary<int, data> dataStruct;
        int CurrentGovCode = 0;
        bool checkboxChangedByCode = false;


        private void checkBox_changed(object sender, EventArgs e)
        {
            if (!checkboxChangedByCode)
            {
                CheckBox checkBox = ((CheckBox)(sender));
                int code = Int32.Parse(checkBox.Name.Split('|')[1]);
                string name = checkBox.Text;
                CurrentGovCode = govDic[listItems.SelectedItem.ToString()];

                if (checkBox.Checked)
                {
                    if (dataStruct == null)
                    {
                        dataStruct = new Dictionary<int, data>();
                        dataStruct.Add(CurrentGovCode, new data(listItems.SelectedItem.ToString()));
          
                    }
                    if (!dataStruct.ContainsKey(CurrentGovCode))
                    {
                        dataStruct[CurrentGovCode].disDic.Add(code, new disabls(name));
                    }
                    else
                    {
                        dataStruct[CurrentGovCode].disDic.Add(code, new disabls(name));
                    }
                }
                if (!checkBox.Checked)
                {
                    dataStruct[CurrentGovCode].disDic.Remove(code);
                }
                checkboxChangedByCode = false;
            }
        }

        private void removeDisChecks(bool IsJustView, bool value, int code)
        {
            checkboxChangedByCode = false;
            if (!IsJustView)
            {
                foreach (CheckBox box in disabilty.Controls)
                {
                    checkboxChangedByCode = true;
                    box.Checked = false;
                }
            }
            else
            {
                foreach (CheckBox box in disabilty.Controls)
                {
                    checkboxChangedByCode = true;
                    
                    if (disDic[box.Text]==code)
                    {
                        box.Checked = value;
                        break;
                    }
                }
            }
            checkboxChangedByCode = false;
        }

        public string TelegramSendMessage(string apilToken, string destID, string text)
        {
            string urlString = $"https://api.telegram.org/bot{apilToken}/sendMessage?chat_id={destID}&text={text}";

            WebClient webclient = new WebClient();
  
            return webclient.DownloadString(urlString);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            disabilty.Enabled = false;
            panel1.Enabled = false;
            button1.Enabled = false;

            backgroundWorker1.RunWorkerAsync();

        }

        private void checkNew()
        {
            StringBuilder s = new StringBuilder();
            foreach (var gov in dataStruct)
            {

                foreach (var dis in gov.Value.disDic)
                {
                    dataStruct[gov.Key].disDic[dis.Key].places = new Dictionary<int, List<dates>>();

                    read($"http://pod.mohp.gov.eg/apps/lookups/centers.php?lk_governments={gov.Key}&major_dismed={dis.Key}&dhxr1637706713073=1", null, "places", gov.Key, dis.Key, 0);
                    foreach (var place in dis.Value.places)
                    {
                        read($"http://pod.mohp.gov.eg/apps/lookups/centers_visit.php?fk_center_id={place.Key}&major_dismed={dis.Key}&dhxr1635635374790=1", null, "", gov.Key, dis.Key, place.Key);

                    }
                    foreach (var dates in dis.Value.places.Values)
                    {
                        s.Append(gov.Value.govName).Append("\n");
                        s.Append(dis.Value.disName).Append(" - ");
                        int cnt = 0;
                        foreach (var date in dates)
                        {
                            s.Append(date.place + " - " + date.date.Replace('-', '/') + "\n");
                            cnt++;
                        }
                        if (!sent.Contains("تم بدء البرنامج بنجاح"))
                            messages.Add("تم بدء البرنامج بنجاح");
                        if (!sent.Contains(s.ToString()))
                        {
                            messages.Add(s.ToString());
                        }
                        s.Clear();
                    }

                }
            }
        }

        private void save_btn_Click(object sender, EventArgs e)
        {
            if (listItems.SelectedIndex == 0)
            {
     
                CurrentGovCode = govDic[listItems.Items[0].ToString()];
                if (dataStruct == null)
                {
                    dataStruct = new Dictionary<int, data>();
                }
                if (!dataStruct.ContainsKey(CurrentGovCode))
                {
                    dataStruct.Add(CurrentGovCode, new data(listItems.Items[0].ToString()));
                }
     
            }
            panel3.Enabled = true;
            panel2.Enabled = true;
            if (filename_txt.Text == "" || chat_id_txt.Text == "" || botId_txt.Text == "")
            {
                MessageBox.Show(
                    "من فضلك ادخل جميع البيانات",
                    "خطأ",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
                return;
            }
            saveFavourite saveFavourite;
            string filename = filename_txt.Text;
            string botid = botId_txt.Text;
            string chatid = chat_id_txt.Text;

            if (!fav_combo.Items.Contains(filename_txt.Text))
            {
                saveFavourite = new saveFavourite(filename, "");
                
            }
            else
                saveFavourite = new saveFavourite(filename, "open");
            try
            {
                
                favouritMeta = new favourit(filename, chatid, botid);
                saveFavourite.SerializeData(favouritMeta);
                saveFavourite.SerializeData(dataStruct);
                saveFavourite.closeStream();
                fav_combo.Items.Add(filename_txt.Text);
                current_fav = filename;
                MessageBox.Show("تم الحفظ");
            }
            catch (Exception)
            {

                
            }
            panel3.Enabled = false;
            panel2.Enabled = false;
            LoadFavourite();
        }

        private static string[] GetFileNames(string path, string filter)
        {
            string[] files = Directory.GetFiles(path, filter);
            for (int i = 0; i < files.Length; i++)
                files[i] = Path.GetFileName(files[i]);
            return files;
        }

        

        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            BackgroundWorker worker = (BackgroundWorker)sender;
            checkNew();
            bool firstMessageSent = false;

            foreach (string m in messages)
            {
                if (!sent.Contains(m))
                {
                    if(!firstMessageSent)
                        TelegramSendMessage(botId_txt.Text, chat_id_txt.Text, " تم ايجاد عدد"+" "+ messages.Count +" " +" ميعاد ");
                    firstMessageSent = true;
                    Thread.Sleep(70);
                    var x = TelegramSendMessage(botId_txt.Text, chat_id_txt.Text, m);
                    sent.Add(m);
                    sound.Play();
                }
            }
            Thread.Sleep(1000);
            messages.Clear();
            worker.ReportProgress(0, messages);
            i++;



        }

        private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            messages.Clear();
            backgroundWorker1.RunWorkerAsync();
        }

        private void choose_fv_btn_Click(object sender, EventArgs e)
        {
            
            fav_combo.Enabled = true;
            try
            {
                current_fav = fav_combo.SelectedItem.ToString();
                FavouriteObj = new saveFavourite(current_fav, "open");
                favouritMeta = (favourit)FavouriteObj.DeSerializeData("meta");
                dataStruct = (Dictionary<int, data>)FavouriteObj.DeSerializeData("data");
                filename_txt.Text = favouritMeta.filename;
                botId_txt.Text = favouritMeta.bot_id;
                chat_id_txt.Text = favouritMeta.chat_id;
                FavouriteObj.closeStream();
                CurrentGovCode = govDic[listItems.Items[0].ToString()];
                foreach (var dis in dataStruct[CurrentGovCode].disDic)
                {
                    removeDisChecks(true, true, dis.Key);
                }


            }
            catch (Exception)
            {
                MessageBox.Show("حدث خطأ اثناء تحميل المفضلة");

            }
            fav_combo.Focus();
            panel2.Enabled = false;

        }

        private void listItems_SelectedIndexChanged(object sender, EventArgs e)
        {
            ComboBox box = (ComboBox)sender;
            string name = box.Text;
            if (govDic.Count > 2)
            {
                CurrentGovCode = govDic[name];
                if (box.SelectedIndex >= 0)
                {
                    if (dataStruct == null)
                    {
                        dataStruct = new Dictionary<int, data>();
                    }
                    if (!dataStruct.ContainsKey(CurrentGovCode))
                    {
                        removeDisChecks(false, false, 0);
                        dataStruct.Add(CurrentGovCode, new data(name));


                    }
                    removeDisChecks(false, false, 0);
                    foreach (var dis in dataStruct[CurrentGovCode].disDic)
                    {
                        removeDisChecks(true, true, dis.Key);

                    }
                }
            }
        }

        private void create_Click(object sender, EventArgs e)
        {
            panel3.Enabled = true;
            panel2.Enabled = true;
            dataStruct = null;
            current_fav = "empty";
            saveFavourite x = new saveFavourite(current_fav, "");
            removeDisChecks(false, false, 0);
            x.closeStream();
            LoadFavourite();
            fav_combo.Items.Add(current_fav);
            filename_txt.Text = "";
            botId_txt.Text = "";
            chat_id_txt.Text = "";
            filename_txt.Focus();

        }

        private void update_Click(object sender, EventArgs e)
        {
            panel3.Enabled = true;
            panel2.Enabled = true;

            filename_txt.Focus();

        }

        private void fav_combo_SelectedIndexChanged(object sender, EventArgs e)
        {

            ComboBox box = (ComboBox)sender;
            string name = box.Text.ToString();
            this.Text=name;
            current_fav = name;

            FavouriteObj = new saveFavourite(current_fav, "open");
             
            favouritMeta = (favourit)FavouriteObj.DeSerializeData("meta");
            dataStruct = (Dictionary<int, data>)FavouriteObj.DeSerializeData("data");
            if (favouritMeta == null)
            {
                filename_txt.Text = "";
                chat_id_txt.Text = "";
                botId_txt.Text = "";
            }

            if (favouritMeta != null)
            {
                filename_txt.Text = favouritMeta.filename;
                chat_id_txt.Text = favouritMeta.chat_id;
                botId_txt.Text = favouritMeta.bot_id;

            }

            if (current_fav != "empty")
            {
                CurrentGovCode = govDic[listItems.SelectedItem.ToString()];
                
                removeDisChecks(false, false, 0);
                //dataStruct[CurrentGovCode].disDic = new Dictionary<int, disabls>();
                foreach (var dis in dataStruct[CurrentGovCode].disDic)
                {
                    removeDisChecks(true, true, dis.Key);
                }
            }
            else
            {
                removeDisChecks(false, false, 0);
            }
                
        FavouriteObj.closeStream();

        }

        private void login_btn_Click(object sender, EventArgs e)
        {
            if (login_txt.Text.ToLower() == "654321m")
            {
                MessageBox.Show("تم تسجيل الدخول بنجاح");
                panel1.Enabled = true;
                logn_pnl.Visible = false;
            }
            else
            {
                MessageBox.Show("كلمة المرور خاطئة من فضلك حاول مرة اخري");
            }
        }

        private void login_txt_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (char)13)
            {
                if (login_txt.Text.ToLower() == "654321m")
                {
                    MessageBox.Show("تم تسجيل الدخول بنجاح");
                    panel1.Enabled = true;
                    logn_pnl.Visible = false;
                }
                else
                {
                    MessageBox.Show("كلمة المرور خاطئة من فضلك حاول مرة اخري");
                }
            }
        }
    }
}
