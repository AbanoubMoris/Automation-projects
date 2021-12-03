using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mabe3aty.Models
{
    public class sales
    {
        [Key]
        public int sellID { get; set; }
        public int productID { get; set; }
        public float TotalPrice { get; set; }
        public int quantity { get; set; }
        public string productName { get; set; }
        public string sellType { get; set; }
        [Column(TypeName = "Date")]
        public DateTime sell_date { get; set; }

    }
}
