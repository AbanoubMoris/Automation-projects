using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mabe3aty.Models
{
    public class prodcutModel
    {
        [Key]
        public int QR_code { get; set; }

        public string product_Name { get; set; }

        public int product_Quantity { get; set; }

        public float product_price { get; set; }
    }
}
