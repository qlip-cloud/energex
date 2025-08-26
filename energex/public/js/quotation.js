frappe.ui.form.on("Quotation", {
    transaction_date: function(frm, cdt, cdn){
        
        let selling_default_valid_till = cint(frappe.boot.selling_default_valid_till);

        let d = new Date( moment(frm.doc.transaction_date).format('MM-DD-YYYY'));

		d.setDate(d.getDate()+ parseInt(selling_default_valid_till));
        
        frm.doc.valid_till = d

        frm.refresh_fields()
    }
});