function renderStudent(student) {
    return `
        <table style="margin-top:10px; border-collapse: collapse; width:100%; max-width:500px;">
            <tr>
                <th style="text-align:left; padding:6px 12px; width:220px;">Registration Number (SBD):</th>
                <td style="padding:6px 12px; text-align:center;">${student.sbd}</td>
            </tr>
            <tr><td style="padding:6px 12px; width:220px;">Toán</td><td style="padding:6px 12px; text-align:center;">${student.toan ?? 'None'}</td></tr>
            <tr><td style="padding:6px 12px;">Ngữ Văn</td><td style="padding:6px 12px; text-align:center;">${student.ngu_van ?? 'None'}</td></tr>
            <tr><td style="padding:6px 12px;">Ngoại Ngữ</td><td style="padding:6px 12px; text-align:center;">${student.ngoai_ngu ?? 'None'}</td></tr>
            <tr><td style="padding:6px 12px;">Vật Lý</td><td style="padding:6px 12px; text-align:center;">${student.vat_li ?? 'None'}</td></tr>
            <tr><td style="padding:6px 12px;">Hóa Học</td><td style="padding:6px 12px; text-align:center;">${student.hoa_hoc ?? 'None'}</td></tr>
            <tr><td style="padding:6px 12px;">Sinh Học</td><td style="padding:6px 12px; text-align:center;">${student.sinh_hoc ?? 'None'}</td></tr>
            <tr><td style="padding:6px 12px;">Lịch Sử</td><td style="padding:6px 12px; text-align:center;">${student.lich_su ?? 'None'}</td></tr>
            <tr><td style="padding:6px 12px;">Địa Lý</td><td style="padding:6px 12px; text-align:center;">${student.dia_li ?? 'None'}</td></tr>
            <tr><td style="padding:6px 12px;">GDCD</td><td style="padding:6px 12px; text-align:center;">${student.gdcd ?? 'None'}</td></tr>
            <tr><td style="padding:6px 12px;">Mã Ngoại Ngữ</td><td style="padding:6px 12px; text-align:center;">${student.ma_ngoai_ngu ?? ''}</td></tr>
        </table>
    `;
}

document.getElementById('scoreForm').onsubmit = function(e) {
    e.preventDefault();
    const sbd = document.getElementById('sbd').value;
    fetch(`${API_BASE_URL}/check-score/?sbd=${encodeURIComponent(sbd)}`)
        .then(res => res.json())
        .then(data => {
            if (data.error) {
                document.getElementById('result').innerHTML = `<p style="color:red;">${data.error}</p>`;
            } else {
                document.getElementById('result').innerHTML = renderStudent(data);
            }
        });
};