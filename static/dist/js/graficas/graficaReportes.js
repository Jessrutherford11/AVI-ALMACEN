// datos
const data = {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], //Etiquetas que aparecen en la barritas
    datasets: [{ //valores
        label: 'Weekly Sales', //nombre de la barrita de arriba
        data: [18, 12, 6, 9, 12, 3, 9], //Porcentaje de la barrita
        backgroundColor: [
            'rgba(255, 26, 104, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(0, 0, 0, 0.2)'
        ],
        borderColor: [
            'rgba(255, 26, 104, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)',
            'rgba(0, 0, 0, 1)'
        ],
        borderWidth: 1
    }]
};

// config 
const config = {
    type: 'bar',
    data,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};

// render init block
const myChart = new Chart(
    document.getElementById('reportes'), //Aqui se pone el nobre que se puso en el id del html 
    config
);