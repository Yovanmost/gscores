fetch(`${API_BASE_URL}/top-group-a/`)
    .then(res => res.json())
    .then(students => {
        const tbody = document.querySelector('#topGroupATable tbody');
        tbody.innerHTML = students.map((student, i) => `
            <tr>
                <td style="text-align:center;">${i+1}</td>
                <td style="text-align:center;">${student.sbd}</td>
                <td style="text-align:center;">${student.toan}</td>
                <td style="text-align:center;">${student.vat_li}</td>
                <td style="text-align:center;">${student.hoa_hoc}</td>
                <td style="text-align:center; font-weight:bold;">${student.total_group_a}</td>
            </tr>
        `).join('');
    });