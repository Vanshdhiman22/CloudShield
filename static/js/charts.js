const ctx = document.getElementById('attackChart').getContext('2d');
const attackChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['IAM Abuse', 'Brute Force', 'S3 Access', 'API Abuse'],
        datasets: [{
            label: 'Detected Threats',
            data: [5, 2, 3, 1], // Placeholder data
            backgroundColor: ['#f00', '#0f0', '#00f', '#ffa500']
        }]
    }
});
