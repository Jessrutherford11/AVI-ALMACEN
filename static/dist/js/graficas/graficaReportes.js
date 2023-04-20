// datos
const data = {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], //Etiquetas que aparecen en la barritas
    datasets: [{ //valores
        label: 'Weekly Sales', //nombre de la barrita de arriba
        data: [18, 12, 6, 9, 12, 3, 9], //Porcentaje de la barrita
        backgroundColor: [
            'rgba(144, 238, 144, 0.5)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(0, 0, 205, 0.3)',
            'rgba(105, 105, 105, 0.5)',
            'rgba(153, 102, 255, 0.5)',
            'rgba(240, 230, 140, 0.9)',
         
        ],
        borderColor: [
            'rgba(144, 238, 144, 3)',
            'rgba(54, 162, 235, 1)',
            'rgba(0, 0, 205, 1)',
            'rgba(105, 105, 105, 8)',
            'rgba(153, 102, 255, 1)',
            'rgba(240, 230, 140, 6)',
           
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