// Example: fetch data from your API and render chart
fetch(`${API_BASE_URL}/report/`)
    .then(response => response.json())
    .then(data => {
        const chartData = {
            labels: data.labels,
            datasets: [
                { label: ">=8", data: data.data_8, backgroundColor: "rgba(75, 192, 192, 0.6)" },
                { label: "6-7.99", data: data.data_6_8, backgroundColor: "rgba(255, 206, 86, 0.6)" },
                { label: "4-5.99", data: data.data_4_6, backgroundColor: "rgba(54, 162, 235, 0.6)" },
                { label: "<4", data: data.data_lt4, backgroundColor: "rgba(255, 99, 132, 0.6)" }
            ]
        };
        new Chart(document.getElementById("reportChart"), {
            type: "bar",
            data: chartData,
            options: {
                responsive: true,
                plugins: { legend: { position: "top" } },
                scales: { y: { beginAtZero: true } }
            }
        });
    });